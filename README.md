# digital archeology

tools for assessing software

## find classes and functions in Python scripts

```bash
./find_classes_in_python_scripts.sh 
    ./afolder/more_folder/cool.py:class imim(ASDF_DF, SDfma):
    ./afolder/somefi.py:class ASDF_FSDFM():
```

```bash
./find_functions_in_python_scripts.sh 
    ./afolder/more_folder/cool.py:def mimmigmiasdf(m, miamdfa):
    ./afolder/more_folder/cool.py:def mim(adf, imaisdf):
    ./afolder/more_folder/cool.py:    def here_ime():
    ./afolder/somefi.py:def mycool(miafd):
    ./afolder/somefi.py:def masdfi(mim):
    ./find_imports_in_notebooks.py:def extract_json_from_notebook(notebook_filepath: str):
    ./find_imports_in_notebooks.py:def find_import_in_json(notebook_json) -> list:
    ./find_imports_in_notebooks.py:def does_import_work(module_name: str) -> bool:
```

## find imports in notebooks 

```bash
./find_imports_in_notebooks.py --help
usage: find_imports_in_notebooks.py [-h] [--directory dir]

find imported modules in Jupyter notebooks

optional arguments:
  -h, --help       show this help message and exit
  --directory dir  directory in which to look for .ipynb files
```

Example use:
```bash
./find_imports_in_notebooks.py 

    ./afolder/toplevel.ipynb
import thisfunc

    ./afolder/more_folder/great.ipynb
from bob.another.this import func as hello
import thiscell as cool

    ./afolder/more_folder/herebe/thisone.ipynb
import helpold
            works: import time
            works: import datetime
import amimf
from eas.imig.ima import fimasdf
```
