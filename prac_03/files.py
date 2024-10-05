"""Files Exercise"""


def main():
    question_1()
    question_2()
    question_3()
    question_4()


def question_1():
    name = input("What is your name? ")
    out_file = open('name.txt', 'w')
    print(name, file=out_file)
    out_file.close()


def question_2():
    in_file = open('name.txt', 'r')
    name = in_file.read().strip()
    in_file.close()
    print(f"Hi {name}!")


def question_3():
    pass


def question_4():
    pass


main()
