from weather.utils.reader import read_and_get_file_contents  # import function from other file


file_values = read_and_get_file_contents("/home/aftab/Desktop/Data/ISDP/weather/files/f1.csv")  # function take 1 Perimeter

for file_value in file_values:
    date = file_value[0]  # get date and store in variable
    max_temp = float(file_value[1])  # get maximum temperature in variable and convert in float
    min_temp = float(file_value[3])  # get minimum temperature in variable and convert in float
    diffrent_max_temp_with_min_temp = max_temp - min_temp  # calculate difference between maximum temperature & minimum temperature

    print(f"{date}, Maximum-Temp is {max_temp} AND Minimum-Temp is {min_temp} Diffrance, {diffrent_max_temp_with_min_temp}")
