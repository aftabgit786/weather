from weather.utils.reader import get_file_contents
from weather.utils.constant import MappingIndexF1

file_path = "/home/aftab/Desktop/Data/ISDP/weather/files/f1.csv"
file_contents = get_file_contents(file_path)

for file_content in file_contents:
    date = file_content[MappingIndexF1.DATE]
    max_temperature = float(file_content[MappingIndexF1.MAXIMUM_TEMPERATURE])
    min_temperature = float(file_content[MappingIndexF1.MINIMUM_TEMPERATURE])

    average = (max_temperature - min_temperature) / 2

    print(f"{date}, Maximum-Temp is {max_temperature} AND Minimum-Temp is {min_temperature} of Average is: {average}")
