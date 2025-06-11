import yaml
from src.train import train_and_save_model

if __name__ == "__main__":
    # Load parameters from params.yaml
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)

    model_params = params["model_params"]

    # Call training function with loaded params
    train_and_save_model(
        model_path="models/model.pkl",
        **model_params
    )
