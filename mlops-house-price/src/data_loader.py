from sklearn.datasets import fetch_california_housing
import pandas as pd

def load_california_housing():
    """
    Load the California housing dataset and return it as a pandas DataFrame.
    
    Returns:
        pd.DataFrame: A DataFrame containing the California housing data.
    """
    data = fetch_california_housing(as_frame=True)
    df = data.frame # type: ignore
    df.columns = [col.replace(' ', '_') for col in df.columns]  # Replace spaces with underscores
    return df