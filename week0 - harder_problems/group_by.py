def group_by(func, seq):
    result = {}
    for item in seq:
        key = func(item)
        if key in result:
            result[key].append(item)
        else:
            result[key] = [item]

    return result


def main():
    print(group_by(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
    print(group_by(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
    print(group_by(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))
if __name__ == "__main__":
    main()
