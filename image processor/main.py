from test import convert_image_to_string
from file_to_dict import dict_of_all_expenses


def clean_file(url: str) -> None:
    file = open(url, "w+")
    file.write("")
    file.close()


def running():

    # Read Text from screenshots into a file
    convert_image_to_string("pictures/statements.png")
    convert_image_to_string("pictures/statements3.png")
    convert_image_to_string("pictures/BOA statements.png")

    # Organize this text into a dictionary
    expenses_dict = dict_of_all_expenses("recognized.txt")

    for key, value in expenses_dict.items():
        print(key, value)

    # Clean the file
    # clean_file("recognized.txt")


if __name__ == "__main__":
    running()

