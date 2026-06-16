import pandas as pd

INPUT_FILE = "data/raw/telemetry_data.csv"

OUTPUT_FILE = (
    "data/processed/features.csv"
)


def load_data():

    df = pd.read_csv(
        INPUT_FILE
    )

    df["timestamp"] = pd.to_datetime(
        df["timestamp"]
    )

    return df


def create_features(df):

    df = df.sort_values(
        [
            "vehicle_id",
            "timestamp"
        ]
    )

    # Rolling Average Speed

    df["avg_speed_5"] = (

        df.groupby(
            "vehicle_id"
        )["speed"]

        .transform(

            lambda x:

            x.rolling(
                window=5,
                min_periods=1
            ).mean()
        )
    )

    # Rolling Speed Variance

    df["speed_variance_5"] = (

        df.groupby(
            "vehicle_id"
        )["speed"]

        .transform(

            lambda x:

            x.rolling(
                window=5,
                min_periods=1
            ).var()
        )
    )

    # Rolling RPM Variance

    df["rpm_variance_5"] = (

        df.groupby(
            "vehicle_id"
        )["rpm"]

        .transform(

            lambda x:

            x.rolling(
                window=5,
                min_periods=1
            ).var()
        )
    )

    # Temperature Change Rate

    df["temp_change_rate"] = (

        df.groupby(
            "vehicle_id"
        )["engine_temp"]

        .diff()

        .fillna(0)
    )

    # Speed Change Rate

    df["speed_change_rate"] = (

        df.groupby(
            "vehicle_id"
        )["speed"]

        .diff()

        .fillna(0)
    )

    # RPM Change Rate

    df["rpm_change_rate"] = (

        df.groupby(
            "vehicle_id"
        )["rpm"]

        .diff()

        .fillna(0)
    )

    # Idle Indicator

    df["is_idle"] = (

        (
            df["speed"] < 5
        )

        &

        (
            df["ignition_status"] == 1
        )

    ).astype(int)

    # High Temperature Indicator

    df["high_temp"] = (

        df["engine_temp"] > 110

    ).astype(int)

    # Overspeed Indicator

    df["overspeed"] = (

        df["speed"] > 120

    ).astype(int)

    # Missing values from rolling variance

    df = df.fillna(0)

    return df


def save_features(df):

    df.to_csv(

        OUTPUT_FILE,

        index=False
    )

    print(
        f"\nSaved engineered features "
        f"to {OUTPUT_FILE}"
    )


def print_summary(df):

    print("\nFeature Dataset Shape:")

    print(df.shape)

    print("\nEngineered Columns:")

    engineered_columns = [

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

    print(engineered_columns)

    print("\nSample Records:")

    print(

        df[
            engineered_columns
        ].head()
    )


if __name__ == "__main__":

    print(
        "\nLoading telemetry data..."
    )

    dataframe = load_data()

    print(
        "\nCreating features..."
    )

    dataframe = create_features(
        dataframe
    )

    save_features(
        dataframe
    )

    print_summary(
        dataframe
    )