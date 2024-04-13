# digital archeology

tools for assessing software

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
