from weather.utils.reader import read_file_for_events

file_values = read_file_for_events()

for file_value in file_values:

    date = file_value[1]

    events = file_value[-2]

    if events == "Rain" or events == "Snow" or events == "Rain-Snow":
        print(f"{events} of the date {date}")
