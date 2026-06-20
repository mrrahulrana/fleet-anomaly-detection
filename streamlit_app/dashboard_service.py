import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd

from sqlalchemy import text

from app.database.db import engine


def load_predictions():

    query = """

    SELECT *

    FROM anomaly_predictions

    ORDER BY created_at DESC

    """

    return pd.read_sql(
        text(query),
        engine
    )


def load_alerts():

    query = """

    SELECT *

    FROM alert_events

    ORDER BY created_at DESC

    """

    return pd.read_sql(
        text(query),
        engine
    )