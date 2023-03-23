from weather.utils.reader import read_and_get_file_contents  # import function from other file
from datetime import datetime


file_values = read_and_get_file_contents("/home/aftab/Desktop/Data/ISDP/weather/files/f2.csv")  # function take 1 Perimeter

for file_value in file_values:
    date = file_value[1]  # get date and store in variable
    events = file_value[-2]    # get events from file and store in variable
    if events == "Thunderstorm":  # condition get 1 event from all events
        date_str = str(date)  # convert date into string
        date_to_names = datetime.strptime(date_str, "%Y-%m-%d")  # compare & get names of days, months, years using datetime
        day_name = date_to_names.strftime("%A")  # get days name
        print(f"{date_str} of wather is Thunderstorm and day is {day_name}")
