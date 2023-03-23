from weather.utils.reader import read_and_get_file_contents
from weather.utils.constent import MappingForT5AndT6

file_contents = read_and_get_file_contents("/home/aftab/Desktop/Data/ISDP/weather/files/f2.csv")

for file_content in file_contents:
    date = file_content[MappingForT5AndT6.DATE]
    events = file_content[MappingForT5AndT6.EVENTS]

    if events in ["Rain",  "Snow",  "Rain-Snow"]:

        print(f"{events} of the date {date}")
