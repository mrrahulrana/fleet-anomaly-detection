import random
from datetime import datetime, timedelta

import pandas as pd

NUM_VEHICLES = 50
RECORDS_PER_VEHICLE = 1000

OUTPUT_FILE = "data/raw/telemetry_data.csv"


def generate_vehicle_record(
        vehicle_id,
        timestamp
):

    # Normal fleet behavior

    speed = round(
        max(
            0,
            random.gauss(
                70,
                15
            )
        ),
        2
    )

    rpm = round(
        max(
            700,
            random.gauss(
                2200,
                400
            )
        ),
        2
    )

    fuel_level = round(
        random.uniform(
            5,
            100
        ),
        2
    )

    engine_temp = round(
        max(
            70,
            random.gauss(
                90,
                5
            )
        ),
        2
    )

    gps_lat = round(
        random.uniform(
            47.0,
            55.0
        ),
        6
    )

    gps_lon = round(
        random.uniform(
            6.0,
            15.0
        ),
        6
    )

    ignition_status = random.choice(
        [0, 1]
    )

    anomaly = 0

    # Inject anomalies (~2%)

    if random.random() < 0.02:

        anomaly = 1

        speed = round(
            random.uniform(
                150,
                220
            ),
            2
        )

        rpm = round(
            random.uniform(
                4500,
                7000
            ),
            2
        )

        engine_temp = round(
            random.uniform(
                120,
                150
            ),
            2
        )

    return {

        "vehicle_id": vehicle_id,

        "timestamp": timestamp,

        "speed": speed,

        "rpm": rpm,

        "fuel_level": fuel_level,

        "engine_temp": engine_temp,

        "gps_lat": gps_lat,

        "gps_lon": gps_lon,

        "ignition_status": ignition_status,

        "is_anomaly": anomaly
    }


def generate_dataset():

    records = []

    start_time = (
        datetime.now()
        - timedelta(days=7)
    )

    for vehicle in range(
            1,
            NUM_VEHICLES + 1
    ):

        vehicle_id = (
            f"V{vehicle:03d}"
        )

        current_time = start_time

        for _ in range(
                RECORDS_PER_VEHICLE
        ):

            records.append(

                generate_vehicle_record(

                    vehicle_id,

                    current_time
                )
            )

            current_time += timedelta(
                minutes=5
            )

    return pd.DataFrame(
        records
    )


def save_dataset(df):

    df.to_csv(

        OUTPUT_FILE,

        index=False
    )

    print(
        f"\nSaved {len(df)} records "
        f"to {OUTPUT_FILE}"
    )


def print_statistics(df):

    print("\nDataset Shape:")
    print(df.shape)

    print("\nSample Records:")
    print(df.head())

    print("\nTelemetry Statistics:")
    print(
        df[
            [
                "speed",
                "rpm",
                "fuel_level",
                "engine_temp"
            ]
        ].describe()
    )

    print("\nAnomaly Distribution:")
    print(
        df["is_anomaly"]
        .value_counts()
    )


if __name__ == "__main__":

    print(
        "\nGenerating telemetry dataset..."
    )

    dataframe = generate_dataset()

    save_dataset(
        dataframe
    )

    print_statistics(
        dataframe
    )