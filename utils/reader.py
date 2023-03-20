def read_file():
    file_values = []
    with open("/home/aftab/Desktop/Data/ISDP/weather/files/f1.csv") as file_reader:
        file_content = file_reader.read()
        for row in file_content.split("\n")[1:-1]:
            file_values.append(row.split(","))
        file_reader.close()

        return file_values

def read_file_for_events():
    file_values = []
    with open("/home/aftab/Desktop/Data/ISDP/weather/files/f2.csv") as file_reader:
        file_content = file_reader.read()
        for row in file_content.split("\n")[1:-1]:
            file_values.append(row.split(","))
        file_reader.close()

        return file_values

