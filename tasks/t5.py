from weather.utils.reader import read_and_get_file_contents  # import function from other file


file_values = read_and_get_file_contents("/home/aftab/Desktop/Data/ISDP/weather/files/f2.csv")  # function take 1 Perimeter

for file_value in file_values:
    date = file_value[1]  # get date and store in variable
    events = file_value[-2]  # get events from file and store in variable
    if events in ["Rain",  "Snow",  "Rain-Snow"]:  # condition get 3 events from all events
        print(f"{events} of the date {date}")
