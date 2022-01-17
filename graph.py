import pandas as pd
from influxdb import InfluxDBClient
import datetime
client= InfluxDBClient(host="localhost", port=8086)
client.switch_database("covid19")

df = pd.read_csv("covid_19_data.csv")
df.dropna(inplace=True)
print(df.shape)

for row_ind, row in df.iloc[1:].iterrows():
    json_body=[{
        "measurement":"CovidMetric",
        "tags":{"Country":row[3], "State":row[2]},
        "fields":{
        "Confirmed":row[5],
        "Deaths":row[6],
        "Recovered":row[7]
        },
        "time": datetime.datetime.utcnow().strptime(row[1], "%m/%d/%Y")
        }]
    client.write_points(json_body)
print("Done")


