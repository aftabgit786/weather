from weather.utils.reader import read_and_get_file_contents
from weather.utils.constent import MappingForT1AndT2

file_contents = read_and_get_file_contents("/home/aftab/Desktop/Data/ISDP/weather/files/f1.csv")

for file_content in file_contents:
    date = file_content[MappingForT1AndT2.DATE]
    max_temperature = float(file_content[MappingForT1AndT2.MAXIMUM_TEMPERATURE])
    min_temperature = float(file_content[MappingForT1AndT2.MINIMUM_TEMPERATURE])

    calculate_difference = max_temperature - min_temperature

    print(f"{date}, Maximum-Temp is {max_temperature} AND Minimum-Temp is {min_temperature} Diffrance, {calculate_difference}")
