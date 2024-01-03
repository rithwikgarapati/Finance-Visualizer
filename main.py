from image_processing import convert_image_to_string
from text_processing import dict_of_all_expenses
import os
import ipdb


def exec_program(path_to_data="/Users/rushil/Downloads/Finance-Visualizer/data", 
                 path_to_text="/Users/rushil/Downloads/Finance-Visualizer/text"):

    data_paths = list_files_in_folder(path_to_data)

    for path in data_paths:

        if os.path.exists("/text/" + path.split("/")[-1]):
            continue
        else:
            convert_image_to_string(path)

    for text_path in list_files_in_folder(path_to_text):
        expenses = dict_of_all_expenses(text_path)
        # TODO: SEND TO DATABASE


    for del_path in list_files_in_folder(path_to_text):
        clean_file(del_path)


def list_files_in_folder(folder_path):
    file_paths = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths


def clean_file(url):
    try:
        os.remove(url)
        print(f"File '{url}' successfully deleted.")
    except FileNotFoundError:
        print(f"File '{url}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    exec_program()

