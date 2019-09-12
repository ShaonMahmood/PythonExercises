import argparse
import numpy as np
import pandas as pd

def csv_processing(csv_data_url):
    # read the csv from url and load into dataframe
    df = pd.read_csv(csv_data_url, encoding='utf-8')

    # convert into datetime object
    df.pickup_time = pd.to_datetime(df.pickup_time)
    df.set_index(pd.DatetimeIndex(df.pickup_time),inplace=True)

    # pick only the morning trips using pandas between_time
    morning_trips = df.between_time('6:00AM','12:00PM')

    # group by source_station_name and then sorted according to size
    sorted_stations_by_size = morning_trips.groupby(['source_station_name','source_station_code']).\
                size().to_frame('size').reset_index().\
                sort_values(['size'],ascending=False)

    # select top 5 using head method
    top5_docking_stations = sorted_stations_by_size.head()

    print('Top five source stations:\n')
    for index,row in top5_docking_stations.iterrows():
        print('{0} (code: {1}): {2} trips'.format(row['source_station_name'], row['source_station_code'], row['size']))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_data_url", type=str,
                        help="input url for fetching csv data")

    args = parser.parse_args()
    csv_processing(csv_data_url=args.csv_data_url)