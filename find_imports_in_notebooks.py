#!/usr/bin/env python3

# https://realpython.com/command-line-interfaces-python-argparse/
import argparse  # https://docs.python.org/3.3/library/argparse.html

# find files
# https://docs.python.org/3/library/glob.html
import glob

# https://docs.python.org/3/library/json.html
import json

# which version of Python is running?
import sys
#print(sys.version)

# test imports without importing
# https://docs.python.org/3/library/importlib.html
import importlib

# docstrings should conform to
# https://google.github.io/styleguide/pyguide.html



def extract_json_from_notebook(notebook_filepath: str):
    """
    Args:
        notebook_filepath: full path to ipynb file

    Returns:
        JSON content
    """
    with open(notebook_filepath,'r') as file_handle:
        file_content = json.load(file_handle)

    return file_content

def find_import_in_json(notebook_json) -> list:
    """
    Args:
        notebook_json: JSON of Jupyter notebook

    Returns:
        list of source code lines that contain "import "
    """

    list_of_lines_with_import = []

    #print(notebook_json.keys())
    #print(notebook_json['cells'])
    for this_cell in notebook_json['cells']:
        if this_cell['cell_type']=='code':
            for this_line in this_cell['source']:
                if "import " in this_line:
                    #print(this_line.strip())
                    list_of_lines_with_import.append(this_line.strip())

    return list_of_lines_with_import

def does_import_work(module_name: str) -> bool:
    """

    Args:
        module_name: name of module to evaluate, e.g., "datetime"

    Returns:
        boolean
    """
    # https://stackoverflow.com/a/14050282/1164295
    if sys.version_info[0]==3 and sys.version_info[1]<4:
        module_loader = importlib.find_loader(module_name)

    elif sys.version_info[0]==3 and sys.version_info[1]>=4:
        import importlib.util
        module_loader = importlib.util.find_spec(module_name)

    if module_loader is None:
        return False
    else:
        return True



if __name__ == "__main__":

    theparser = argparse.ArgumentParser(
        description="find imported modules in Jupyter notebooks", allow_abbrev=False
    )

    # optional argument
    theparser.add_argument(
        "--directory",
        metavar="dir",
        type=str,
        default=".",
        help="directory in which to look for .ipynb files",
    )

    args = theparser.parse_args()

    notebook_filepaths_list = glob.glob(args.directory+"/**/*.ipynb", recursive=True)

    for this_notebook_filepath in notebook_filepaths_list:
        notebook_json = extract_json_from_notebook(this_notebook_filepath)
        print("\n    "+this_notebook_filepath)
        list_of_lines_with_import = find_import_in_json(notebook_json)
        for this_line in list_of_lines_with_import:
            #print(this_line)
            if this_line.startswith("import "):
                line_as_list = this_line.split(" ")
                #print(line_as_list[1])
                if does_import_work(line_as_list[1]):
                    print("            works: "+this_line)
                else:
                    print(this_line)
            else: # line does not start with import, e.g. "from x import y"
                print(this_line)

#EOF
