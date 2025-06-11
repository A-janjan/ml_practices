for adding to DVC:

dvc stage add -n train_model \
  -d src/train.py \
  -d data/california_housing.csv \
  -o models/model.pkl \
  -M metrics.json \
  -p model_params \
  python main.py


---


for runing:

$ dvc repro