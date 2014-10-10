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


def main():

    print(reduce_file_path("/"))
    print(reduce_file_path("/srv/../"))
    print(reduce_file_path("/srv/www/htdocs/wtf/"))
    print(reduce_file_path("/srv/www/htdocs/wtf"))
    print(reduce_file_path("/srv/./././././"))
    print(reduce_file_path("/etc//wtf/"))
    print(reduce_file_path("/etc/../etc/../etc/../"))
    print(reduce_file_path("/etc//wtf/"))
    print(reduce_file_path("/etc/../etc/../etc/../"))
    print(reduce_file_path("//////////////"))
    print(reduce_file_path("/../"))


if __name__ == '__main__':
    main()
