from weather.utils.reader import read_files
from datetime import datetime


file_values = read_files("/home/aftab/Desktop/Data/ISDP/weather/files/f2.csv")
for file_value in file_values:
    date = file_value[1]
    events = file_value[-2]
    if events == "Thunderstorm":
        date_str = str(date)
        date_to_names = datetime.strptime(date_str, "%Y-%m-%d")
        day_name = date_to_names.strftime("%A")
        print(f"{date_str} of wather is Thunderstorm and day is {day_name}")
