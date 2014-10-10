def prepare_meal(number):
    answer = ""
    if number % 5 == 0:
        answer += "and eggs"

    while number % 3 == 0:
        return "spam" + answer
        number // 3


def main():

    print(prepare_meal(5))
    print(prepare_meal(3))
    print(prepare_meal(27))
    print(prepare_meal(15))
    print(prepare_meal(45))
    print(prepare_meal(7))
    
if __name__ == "__main__":
    main()
