from datetime import datetime
from dotenv import load_dotenv

import matplotlib.dates as mdates
import matplotlib.pyplot as pl
import os
import json



def readData():

    buf_date_time = []
    buf_val = []

    load_dotenv()

    with open(os.environ["DATA_PATH"]) as f:
        d = json.load(f)

        # Parsing the Date

        for entry in d:
            buf_date_time.append(
                datetime.combine(
                    datetime.strptime(entry['date'], '%d.%m.%Y'),
                    datetime.time(datetime.strptime(entry['time'], '%H:%M'))
                )
            )
            buf_val.append(float(str(entry['temp_adj']).replace(",", ".")))

    return buf_date_time, buf_val


def main():
    timestamps, values = readData()

    pl.axhline(39, color="r", linestyle="--")
    pl.axhline(36.7, color="r", linestyle="--")
    pl.plot(timestamps, values)
    pl.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d.%m. %H:%M"))
    pl.gcf().autofmt_xdate()
    pl.ylim(33, 42)
    pl.show()

if __name__ == "__main__":
    main()