import mlflow


MODEL_NAME = (
    "fleet-anomaly-model"
)


def register_model(run_id):

    model_uri = (

        f"runs:/{run_id}/model"
    )

    result = mlflow.register_model(

        model_uri=model_uri,

        name=MODEL_NAME
    )

    return result