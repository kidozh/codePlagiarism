# A simple code plagiarism checker for C/C++/Text


use AST and winnowing to check the plagiarism

I have not finished yet. So sorry for that.


## file structure

you should specify a directory which may contains subdirectory which should be a container of all different code files.

then program will traverse all specified code file in every subdirectory,then check them one by one

## dependency

+ pycparse (it may gennerate AST for C)
+ winnow

## how to run by console

`python check.py -d <your_directory> -l <c/c++ | char>`
