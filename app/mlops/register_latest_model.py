import mlflow

from app.mlops.model_registry import (
    register_model
)

client = mlflow.tracking.MlflowClient()

experiment = client.get_experiment_by_name(
    "fleet-anomaly-detection"
)

runs = client.search_runs(
    experiment.experiment_id
)

latest_run = runs[0]

register_model(
    latest_run.info.run_id
)

print(
    "Model registered."
)