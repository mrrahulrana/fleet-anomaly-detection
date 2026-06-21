import mlflow
import mlflow.sklearn


EXPERIMENT_NAME = (
    "fleet-anomaly-detection"
)


def setup_mlflow():

    mlflow.set_tracking_uri(
        "sqlite:///mlflow.db"
    )

    mlflow.set_experiment(
        EXPERIMENT_NAME
    )


def start_run(run_name):

    return mlflow.start_run(
        run_name=run_name
    )


def log_params(params):

    mlflow.log_params(
        params
    )


def log_metrics(metrics):

    mlflow.log_metrics(
        metrics
    )


def log_model(model):

    mlflow.sklearn.log_model(
        model,
        "model"
    )