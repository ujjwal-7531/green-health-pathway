import pathway as pw

CSV_PATH = "data/simulated_stream/environment_stream.csv"

schema = pw.schema_from_types(
    timestamp=str,
    area_id=str,
    aqi=float,
    temperature=float,
    wind_speed=float,
)

stream = pw.io.csv.read(
    CSV_PATH,
    schema=schema,
    mode="streaming",
)

alerts = stream.with_columns(
    health_risk=pw.if_else(
        (pw.this.aqi > 170)
        & (pw.this.temperature > 34)
        & (pw.this.wind_speed < 1.5),
        "HIGH",
        pw.if_else(
            pw.this.aqi > 130,
            "MEDIUM",
            "LOW",
        ),
    )
).filter(
    pw.this.health_risk != "LOW"
)

# ✅ Output structured data only (NO string casting)
alerts_out = alerts.select(
    pw.this.timestamp,
    pw.this.area_id,
    pw.this.aqi,
    pw.this.temperature,
    pw.this.wind_speed,
    pw.this.health_risk,
)

pw.debug.compute_and_print(alerts_out)
pw.run()
