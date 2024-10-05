"""Files Exercise"""


def main():
    """Answers for each question"""
    question_1()
    question_2()
    question_3()
    question_4()


def question_1():
    """Answer for question 1"""
    name = input("What is your name? ")
    out_file = open('name.txt', 'w')
    print(name, file=out_file)
    out_file.close()


def question_2():
    """Answer for question 2"""
    in_file = open('name.txt', 'r')
    name = in_file.read().strip()
    in_file.close()
    print(f"Hi {name}!")


def question_3():
    """Answer for question 3"""
    with open("numbers.txt", "r") as in_file:
        total = float(in_file.readline()) + float(in_file.readline())
        print(f"Total: {total}")


def question_4():
    """Answer for question 4"""
    with open("numbers.txt", "r") as in_file:
        total = 0
        for line in in_file:
            total += float(line)
        print(f"Total: {total}")


main()
