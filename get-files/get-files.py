#!/usr/bin/env python3

import os


def main():
    folder_path = os.getcwd()
    recursive = input("Do you want to include subdirectories? (y/n): ").strip().lower()
    output_content = []

    if recursive == "y":
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                collect_file_content(file_path, file_name, output_content)
    else:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                collect_file_content(file_path, file_name, output_content)

    output_file = os.path.join(folder_path, "output.txt")
    with open(output_file, "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(output_content))

    print(f"File content saved in {output_file}")


def collect_file_content(file_path, file_name, output_content):
    output_content.append(f"// {file_name}")
    output_content.append("```")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            output_content.append(file.read())
    except UnicodeDecodeError:
        output_content.append("[Error: Could not read file due to encoding issues]")
    output_content.append("```\n")


if __name__ == "__main__":
    main()
