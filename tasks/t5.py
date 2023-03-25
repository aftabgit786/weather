from weather.utils.reader import get_file_contents
from weather.utils.constent import MappingIndexF2

file_path = "/home/aftab/Desktop/Data/ISDP/weather/files/f2.csv"
file_contents = get_file_contents(file_path)

for file_content in file_contents:
    date = file_content[MappingIndexF2.DATE]
    events = file_content[MappingIndexF2.EVENTS]

    if events in ["Rain",  "Snow",  "Rain-Snow"]:

        print(f"{events} of the date {date}")
