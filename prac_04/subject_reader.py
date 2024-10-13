"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    max_lecturer_length = max(len(record[1]) for record in data)
    max_number_of_students_length = max(len(str(record[2])) for record in data)
    for record in data:
        subject, lecturer, number_of_students = record
        print(
            f"{subject} is taught by {lecturer:<{max_lecturer_length}} and has "
            f"{number_of_students:>{max_number_of_students_length}} students")


main()
