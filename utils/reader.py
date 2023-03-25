def get_file_contents(file_path):
    """ take 1 argument from file and get content """
    file_contents = []

    with open(file_path) as file_reader:
        file_content = file_reader.read()

        for line in file_content.split("\n")[1:-1]:
            column = line.split(",")
            file_contents.append(column)

        file_reader.close()

    return file_contents
