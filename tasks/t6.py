from weather.utils.reader import read_and_get_file_contents
from weather.utils.constent import MappingForT5AndT6
from datetime import datetime

file_contents = read_and_get_file_contents("/home/aftab/Desktop/Data/ISDP/weather/files/f2.csv")

for file_content in file_contents:
    date = file_content[MappingForT5AndT6.DATE]
    events = file_content[MappingForT5AndT6.EVENTS]

    if events == "Thunderstorm":

        date_str = str(date)

        date_to_names = datetime.strptime(date_str, "%Y-%m-%d")
        day_name = date_to_names.strftime("%A")

        print(f"{date_str} of wather is Thunderstorm and day is {day_name}")
