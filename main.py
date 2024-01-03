from image_processing import convert_image_to_string
from text_processing import dict_of_all_expenses
import os
import ipdb


def exec_program(path_to_data, path_to_text, tesseract_exec_path, del_bank_statements):

    data_paths = list_files_in_folder(path_to_data)

    if path_to_data[-1] != "/":
        path_to_data = path_to_data + "/"

    if path_to_text[-1] != "/":
        path_to_text = path_to_text + "/"

    for path in data_paths:
        file_name = path_to_text + path.split("/")[-1].split(".")[0] + ".txt"
        if file_name in list_files_in_folder(path_to_text):
            file_name = path.split("/")[-1]
            print(f"Text already generated for Image: {file_name}")
            continue
        else:
            convert_image_to_string(path, path_to_text, tesseract_exec_path)

    for text_path in list_files_in_folder(path_to_text):
        expenses = dict_of_all_expenses(text_path)
        expenses_dict = {"name": text_path.split("/")[-1].split(".")[0], "data": expenses}
        print(expenses_dict)
        # TODO: SEND TO DATABASE

    if del_bank_statements:
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

    # CHANGE THESE VARIABLES DEPENDING ON YOUR LOCAL MACHINE'S ENVIRONMENT
    path_to_data = "/Users/rushil/Downloads/Finance-Visualizer/data", 
    path_to_text = "/Users/rushil/Downloads/Finance-Visualizer/text",
    tesseract_exec_path = "/usr/local/bin/tesseract",
    del_bank_statements = True

    exec_program(path_to_data, path_to_text, tesseract_exec_path, del_bank_statements)

