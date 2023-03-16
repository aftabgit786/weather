def get_content_of_files(file_content):
    file_values = []
    for row in file_content.split("\n")[1:]:
        file_values.append(row.split(","))
        return file_values


def read_file():
    file_values = []
    with open("/home/aftab/Desktop/Data/ISDP/weather/files/f1.csv") as file_reader:
        file_content = file_reader.read()
        file_values += get_content_of_files(file_content)
        file_reader.close()

        return file_values

file_values = read_file()
for file_value in file_values:
    print(file_value)
