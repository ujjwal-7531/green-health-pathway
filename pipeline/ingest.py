import pathway as pw

CSV_PATH = "data/simulated_stream/environment_stream.csv"

# Define schema correctly
schema = pw.schema_from_types(
    timestamp=str,
    area_id=str,
    aqi=float,
    temperature=float,
    wind_speed=float,
)

# Read CSV in streaming mode
environment_stream = pw.io.csv.read(
    CSV_PATH,
    schema=schema,
    mode="streaming",
)

# ✅ Correct way to print live data
pw.debug.compute_and_print(environment_stream)

# Run the Pathway pipeline
pw.run()
