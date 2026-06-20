import plotly.express as px


def anomaly_pie_chart(df):

    counts = (

        df["anomaly"]

        .value_counts()

        .reset_index()
    )

    counts.columns = [

        "anomaly",

        "count"
    ]

    return px.pie(

        counts,

        values="count",

        names="anomaly",

        title="Anomaly Distribution"
    )


def speed_distribution(df):

    return px.histogram(

        df,

        x="speed",

        nbins=30,

        title="Vehicle Speed Distribution"
    )


def temperature_distribution(df):

    return px.histogram(

        df,

        x="engine_temp",

        nbins=30,

        title="Engine Temperature Distribution"
    )


def alert_severity_chart(df):

    grouped = (

        df.groupby(
            "severity"
        )

        .size()

        .reset_index(
            name="count"
        )
    )

    return px.bar(

        grouped,

        x="severity",

        y="count",

        title="Alerts by Severity"
    )