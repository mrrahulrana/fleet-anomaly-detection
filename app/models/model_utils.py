import joblib


def save_model(model, model_path):

    joblib.dump(
        model,
        model_path
    )

    print(
        f"\nModel saved to {model_path}"
    )


def load_model(model_path):

    return joblib.load(
        model_path
    )