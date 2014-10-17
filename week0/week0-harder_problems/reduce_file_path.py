def reduce_file_path(path):

    path = path.split("/")
    reduced_path = []

    for element in path:
        if element == "..":
            if reduced_path:
                reduced_path.pop()
        elif element != "." and element != "/":
            reduced_path.append(element)

    reduced_path = list(filter(None, reduced_path))
    return "/" + "/".join(reduced_path)



