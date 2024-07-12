import pandas as pd
import numpy as np


data = {
    'Value': [0,1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 10, 20, 30, 100]
}

df = pd.DataFrame(data)


# define the bins and labels

bins = [0, 5, 10, 20, 50, np.inf]
labels = ['0-5', '5-10', '10-20', '20-50', '+50']

df['Binned'] = pd.cut(df['Value'], bins=bins, labels=labels, right=False)


print(df)