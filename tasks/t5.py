from weather.utils.reader import read_files
file1_path = "/home/aftab/Desktop/Data/ISDP/weather/files/f1.csv"
file2_path = "/home/aftab/Desktop/Data/ISDP/weather/files/f2.csv"

file1_values, file2_values = read_files(file1_path, file2_path)
for file_value in file2_values:
    date = file_value[1]
    events = file_value[-2]
    if events == "Rain" or events == "Snow" or events == "Rain-Snow":
        print(f"{events} of the date {date}")
