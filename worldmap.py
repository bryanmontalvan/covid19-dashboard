import pandas as pd
from influxdb import InfluxDBClient

client= InfluxDBClient(host="localhost", port=8086)
client.switch_database("covid")

df = pd.read_csv("self-made-covid19.csv")
df.dropna(inplace=True)
print(df.shape)

for row_ind, row in df.iloc[1:].iterrows():
    json_body=[{
        "measurement":"CovidMap",
        "fields":{
        "name":row[0],
        "latitude":float(row[2]),
        "longitude":float(row[3]),
        "metric":row[4]
        }
        }]
    client.write_points(json_body)
print("Done")

