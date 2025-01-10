import pickle
import os

class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == 'sklearn.linear_model.stochastic_gradient' and name == 'SGDClassifier':
            module = 'sklearn.linear_model._stochastic_gradient'
        elif module == 'sklearn.linear_model.sgd_fast':
            module = 'sklearn.linear_model._sgd_fast'
        return super().find_class(module, name)


def load_pickle():
    # Path to your pickle file
    pickle_file_path = os.path.join(os.getcwd(), 'movieclassifier/pkl_objects/classifier.pkl')

    # Load the model using the custom unpickler
    with open(pickle_file_path, 'rb') as f:
        clf = CustomUnpickler(f).load()
        
    return clf