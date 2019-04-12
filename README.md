# PythonProgramming
1. For python, system packages are stored in a child directory of the path stored in sys.prefix.
    - import sys
    - sys.prefix
2. Third party packages installed using easy_install or pip are typically placed in one of the directories pointed to by site.getsitepackages().
    - import site
    - site.getsitepackages()
3. For two projects to use different version of same third party depedencies, python uses virtual environments.
   - To create a new Virtual environment, use  python3 -m venv env
   - this command creates a directory called env, which contains a directory structure.
   - In order to use this environment’s packages/resources in isolation, you need to “activate” it. To do this, just run the                                         following: $ source env/bin/activate

