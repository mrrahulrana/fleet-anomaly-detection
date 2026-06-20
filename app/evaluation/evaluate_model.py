import json

import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from app.mlops.mlflow_manager import (
    setup_mlflow,
    start_run,
    log_metrics
)


INPUT_FILE = (
    "data/anomalies/anomaly_predictions.csv"
)

REPORT_FILE = (
    "reports/classification_report.txt"
)

CONFUSION_FILE = (
    "reports/confusion_matrix.csv"
)

METRICS_FILE = (
    "reports/metrics.json"
)


def load_predictions():

    return pd.read_csv(
        INPUT_FILE
    )


def evaluate(df):

    y_true = df["is_anomaly"]

    y_pred = df["predicted_anomaly"]

    accuracy = accuracy_score(
        y_true,
        y_pred
    )

    precision = precision_score(
        y_true,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_true,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_true,
        y_pred,
        zero_division=0
    )

    cm = confusion_matrix(
        y_true,
        y_pred
    )

    report = classification_report(
        y_true,
        y_pred,
        zero_division=0
    )

    return {

        "accuracy": round(
            accuracy,
            4
        ),

        "precision": round(
            precision,
            4
        ),

        "recall": round(
            recall,
            4
        ),

        "f1_score": round(
            f1,
            4
        ),

        "confusion_matrix": cm,

        "classification_report": report
    }


def save_results(results):

    # Save classification report

    with open(
        REPORT_FILE,
        "w"
    ) as file:

        file.write(
            results[
                "classification_report"
            ]
        )

    # Save confusion matrix

    cm_df = pd.DataFrame(

        results[
            "confusion_matrix"
        ],

        columns=[
            "Predicted_Normal",
            "Predicted_Anomaly"
        ],

        index=[
            "Actual_Normal",
            "Actual_Anomaly"
        ]
    )

    cm_df.to_csv(
        CONFUSION_FILE
    )

    # Save metrics JSON

    metrics = {

        "accuracy":
        results["accuracy"],

        "precision":
        results["precision"],

        "recall":
        results["recall"],

        "f1_score":
        results["f1_score"]
    }

    with open(
        METRICS_FILE,
        "w"
    ) as file:

        json.dump(
            metrics,
            file,
            indent=4
        )


def print_results(results):

    print(
        "\n========== MODEL EVALUATION =========="
    )

    print(
        f"\nAccuracy: "
        f"{results['accuracy']}"
    )

    print(
        f"Precision: "
        f"{results['precision']}"
    )

    print(
        f"Recall: "
        f"{results['recall']}"
    )

    print(
        f"F1 Score: "
        f"{results['f1_score']}"
    )

    print(
        "\nConfusion Matrix:"
    )

    print(
        results[
            "confusion_matrix"
        ]
    )

    print(
        "\nClassification Report:\n"
    )

    print(
        results[
            "classification_report"
        ]
    )


def main():

    print(
        "\nLoading prediction results..."
    )

    df = load_predictions()

    setup_mlflow()

    with start_run(
        "model-evaluation"
    ):

        results = evaluate(
            df
        )

        log_metrics({

            "accuracy":
            results["accuracy"],

            "precision":
            results["precision"],

            "recall":
            results["recall"],

            "f1_score":
            results["f1_score"]
        })

        save_results(
            results
        )

        print_results(
            results
        )

    print(
        "\nEvaluation completed successfully."
    )

    print(
        "\nReports saved under reports/"
    )


if __name__ == "__main__":

    main()