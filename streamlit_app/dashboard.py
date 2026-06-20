import streamlit as st

from dashboard_service import (

    load_predictions,

    load_alerts
)

from dashboard_utils import (

    anomaly_pie_chart,

    speed_distribution,

    temperature_distribution,

    alert_severity_chart
)

st.set_page_config(

    page_title="Fleet Operations Dashboard",

    layout="wide"
)

st.title(
    "🚚 Fleet Anomaly Detection Dashboard"
)

predictions = load_predictions()

alerts = load_alerts()

# KPIs

total_predictions = len(
    predictions
)

total_anomalies = (

    predictions["anomaly"]

    .sum()
)

total_alerts = len(
    alerts
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Predictions",
    total_predictions
)

col2.metric(
    "Anomalies",
    total_anomalies
)

col3.metric(
    "Alerts",
    total_alerts
)

st.divider()

# Charts

st.plotly_chart(

    anomaly_pie_chart(
        predictions
    ),

    use_container_width=True
)

st.plotly_chart(

    speed_distribution(
        predictions
    ),

    use_container_width=True
)

st.plotly_chart(

    temperature_distribution(
        predictions
    ),

    use_container_width=True
)

if not alerts.empty:

    st.plotly_chart(

        alert_severity_chart(
            alerts
        ),

        use_container_width=True
    )

st.divider()

st.subheader(
    "Recent Predictions"
)

st.dataframe(

    predictions.head(20),

    use_container_width=True
)

st.subheader(
    "Recent Alerts"
)

st.dataframe(

    alerts.head(20),

    use_container_width=True
)