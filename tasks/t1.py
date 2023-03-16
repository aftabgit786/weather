from weather.utils.reader import read_file

file_values = read_file()

for file_value in file_values:
    date = file_value[0]
    max_temp = float(file_value[1])
    min_temp = float(file_value[3])
    diffrent_max_with_min = max_temp - min_temp

    print(f"{date}, Maximum-Temp is {max_temp} AND Minimum-Temp is {min_temp} Diffrance, {diffrent_max_with_min}")

