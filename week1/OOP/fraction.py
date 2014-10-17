class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def get_float(self):
        return self.nominator / self.denominator

    def __eq__(self, other):
        return other.get_float() == self.get_float()

    def __lt__(self, other):
        return other.get_float() > self.get_float()

    def __gt__(self, other):
        return other.get_float() < self.get_float()

    def __add__(self, other):
        
        return Fraction(nom, denom)


    def __sub__(self, other):


def main():
    a = Fraction(1, 2)
    b = Fraction(1, 2)
    c = Fraction(3, 10)

    print(a == b)
    print(a < c)
    print(a > c)
    print(a + b)


if __name__ == '__main__':
    main()