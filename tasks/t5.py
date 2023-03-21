from weather.utils.reader import read_files

file_values = read_files("/home/aftab/Desktop/Data/ISDP/weather/files/f2.csv")

for file_value in file_values:
    date = file_value[1]
    events = file_value[-2]
    if events in ["Rain",  "Snow",  "Rain-Snow"]:
        print(f"{events} of the date {date}")
