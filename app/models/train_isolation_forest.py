import pandas as pd

from sklearn.ensemble import IsolationForest

from app.models.model_utils import save_model

from app.mlops.mlflow_manager import (
    setup_mlflow,
    start_run,
    log_params,
    log_metrics,
    log_model
)

INPUT_FILE = "data/processed/features.csv"

MODEL_FILE = "models/isolation_forest.pkl"

PREDICTIONS_FILE = "data/anomalies/anomaly_predictions.csv"

ANOMALIES_FILE = "data/anomalies/only_anomalies.csv"


FEATURE_COLUMNS = [

    "speed",

    "rpm",

    "fuel_level",

    "engine_temp",

    "avg_speed_5",

    "speed_variance_5",

    "rpm_variance_5",

    "temp_change_rate",

    "speed_change_rate",

    "rpm_change_rate",

    "is_idle",

    "high_temp",

    "overspeed"
]


def load_features():

    return pd.read_csv(
        INPUT_FILE
    )


def prepare_training_data(df):

    return df[
        FEATURE_COLUMNS
    ]


def train_model(X):

    model = IsolationForest(

        contamination=0.02,

        n_estimators=100,

        random_state=42,

        n_jobs=-1
    )

    model.fit(X)

    return model


def score_anomalies(
        model,
        X,
        df
):

    predictions = model.predict(X)

    scores = model.decision_function(X)

    df["predicted_anomaly"] = predictions

    df["anomaly_score"] = scores

    # Convert
    # -1 = anomaly
    #  1 = normal

    df["predicted_anomaly"] = (

        df["predicted_anomaly"]

        .apply(
            lambda x:
            1 if x == -1 else 0
        )
    )

    return df


def save_predictions(df):

    df.to_csv(

        PREDICTIONS_FILE,

        index=False
    )

    print(
        f"\nSaved predictions to "
        f"{PREDICTIONS_FILE}"
    )


def save_only_anomalies(df):

    anomalies = df[
        df["predicted_anomaly"] == 1
    ]

    anomalies.to_csv(

        ANOMALIES_FILE,

        index=False
    )

    print(
        f"\nSaved {len(anomalies)} anomalies "
        f"to {ANOMALIES_FILE}"
    )

    return anomalies


def print_summary(
        df,
        anomalies
):

    anomaly_count = len(
        anomalies
    )

    anomaly_ratio = round(

        anomaly_count
        /
        len(df)
        * 100,

        2
    )

    print(
        "\n========== MODEL SUMMARY =========="
    )

    print(
        f"\nTotal Records: {len(df)}"
    )

    print(
        f"Detected Anomalies: {anomaly_count}"
    )

    print(
        f"Anomaly Ratio: {anomaly_ratio}%"
    )

    print(
        "\nTop 10 Anomalies:"
    )

    print(

        anomalies

        .sort_values(
            "anomaly_score"
        )

        .head(10)

        [
            [
                "vehicle_id",

                "speed",

                "rpm",

                "engine_temp",

                "anomaly_score"
            ]
        ]
    )


def main():

    setup_mlflow()

    with start_run(
        "isolation-forest-v1"
    ) as run:

        print(
            "\nLoading features..."
        )

        dataframe = load_features()

        X = prepare_training_data(
            dataframe
        )

        print(
            "\nTraining model..."
        )

        model = train_model(X)

        save_model(
            model,
            MODEL_FILE
        )

        dataframe = score_anomalies(

            model,

            X,

            dataframe
        )

        save_predictions(
            dataframe
        )

        anomalies = save_only_anomalies(
            dataframe
        )

        anomaly_count = len(
            anomalies
        )

        anomaly_ratio = (

            anomaly_count
            /
            len(dataframe)
        )

        log_params({

            "algorithm":
            "IsolationForest",

            "contamination":
            0.02,

            "n_estimators":
            100
        })

        log_metrics({

            "anomaly_count":
            anomaly_count,

            "anomaly_ratio":
            anomaly_ratio
        })

        log_model(
            model
        )

        print_summary(

            dataframe,

            anomalies
        )

        print(
            f"\nMLflow Run ID:"
            f" {run.info.run_id}"
        )


if __name__ == "__main__":

    main()