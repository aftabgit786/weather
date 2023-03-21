from weather.utils.reader import read_files
file_values = read_files("/home/aftab/Desktop/Data/ISDP/weather/files/f1.csv")
for file_value in file_values:
    date = file_value[0]
    max_temp = float(file_value[1])
    min_temp = float(file_value[3])
    average_of_max_with_min = (max_temp - min_temp) / 2
    print(f"{date}, Maximum-Temp is {max_temp} AND Minimum-Temp is {min_temp} of Average is: {average_of_max_with_min}")
