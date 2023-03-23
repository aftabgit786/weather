def read_and_get_file_contents(file_path):
    file_values = []  # Initialize empty list
    with open(file_path) as file_reader:
        file_content = file_reader.read()  # get content in file
        for row in file_content.split("\n")[1:-1]:
            file_values.append(row.split(","))
        file_reader.close()  # close file

    return file_values
