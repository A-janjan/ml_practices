import pickle
import sqlite3
import numpy as np
import os


# import HashingVectorizer from local dir
from vectorizer import vect

class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == 'sklearn.linear_model.stochastic_gradient' and name == 'SGDClassifier':
            module = 'sklearn.linear_model._stochastic_gradient'
        elif module == 'sklearn.linear_model.sgd_fast':
            module = 'sklearn.linear_model._sgd_fast'
        return super().find_class(module, name)
    
# Preparing the Classifier
cur_dir = os.path.dirname(__file__)
pickle_file_path = os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl')

with open(pickle_file_path, 'rb') as f:
        clf = CustomUnpickler(f).load()


def update_model(db_path, model, batch_size=10000):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT * from review_db')
    results = c.fetchmany(batch_size)
    
    while results:
        data = np.array(results)
        X = data[:, 0]
        y = data[:, 1].astype(int)
        classes = np.array([0, 1])
        X_train = vect.transform(X)
        model.partial_fit(X_train, y, classes = classes)
        results = c.fetchmany(batch_size)
        
    conn.close()
    return model


cur_dir = os.path.dirname(__file__)

db = os.path.join(cur_dir, 'reviews.sqlite')

clf = update_model(db_path=db, model=clf, batch_size=10000)

# update my classifier.pkl file
pickle.dump(clf, open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'), 'wb'), protocol=4)