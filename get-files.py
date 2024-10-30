#!/usr/bin/env python3

import os


def main():
    # Automatically use the current directory as the folder path
    folder_path = os.getcwd()

    # Ask if the user wants to include subdirectories
    recursive = input("Do you want to include subdirectories? (y/n): ").strip().lower()

    # Set the output file to be in the current working directory
    output_file = os.path.join(folder_path, "output.txt")

    with open(output_file, "w", encoding="utf-8") as f_out:
        if recursive == "y":
            for root, _, files in os.walk(folder_path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    write_file_content(file_path, file_name, f_out)
        else:
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    write_file_content(file_path, file_name, f_out)

    print(f"File content saved in {output_file}")


def write_file_content(file_path, file_name, f_out):
    f_out.write(f"// {file_name}\n")
    f_out.write("```\n")
    with open(file_path, "r", encoding="utf-8") as file:
        f_out.write(file.read())
    f_out.write("\n```\n\n")


if __name__ == "__main__":
    main()
