import argparse
import sys
import os
import subprocess

def list_python_files(path, ignore_folders=None):
    if ignore_folders is None:
        ignore_folders = ["env", ".vs"]

    python_files = []

    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ignore_folders]  # Exclude the ignored folders

        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))

    return python_files


def analyze_code_with_pylint(python_files):
    pylint_reports = {}

    for file in python_files:
        python_executable = sys.executable
        cmd = [python_executable, "-m", "pylint", file, "--output-format=text"]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        pylint_output = result.stdout

        if pylint_output:
            pylint_reports[file] = pylint_output

    return pylint_reports


def main(project_path):
    # Find all Python files in the project folder
    python_files = list_python_files(project_path)

    # Analyze the Python files using Pylint
    pylint_reports = analyze_code_with_pylint(python_files)

    # Print the Pylint reports
    for file, report in pylint_reports.items():
        print(f"File: {file}\n{report}\n")


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Analyze a Python project with Pylint.")
    # parser.add_argument("-p", "--path", required=True, help="Path to the project folder.")
    # args = parser.parse_args()

    # project_path = args.path
    project_path = "C:/Eurofiber/visio2excel"

    main(project_path)
