def __init__(self, filepath):
        self.filepath = filepath

    def print_map(self):
        my_file = open(self.filepath, 'r')
        content = my_file.read()
        content = content.split('\n')
        for line in content:
            print(line)
        my_file.close()