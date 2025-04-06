# miniconda setup. for windows run commands in command prompt or bash
conda create -p ./myenv python=3.12 -c conda-forge
conda activate ./myenv
conda deactivate


# first time activate the environment powershell
conda init powershell
Then restart the terminal (close it and open again) or restart PyCharm entirely.
conda activate ./myenv
where python

# first time activate the environment bash
conda init cmd.exe
conda activate .\myenv
where python


# fast api 
pip install "fastapi[standard]"


The command pip install "fastapi[standard]" installs FastAPI along with additional optional dependencies that are commonly used in FastAPI projects. These additional dependencies include packages for features like data validation, serialization, and asynchronous support.  Here is a brief explanation of what happens when you run this command:  
fastapi: The core FastAPI framework.
[standard]: A set of optional dependencies that enhance FastAPI's functionality.
By installing fastapi[standard], you ensure that you have all the necessary tools and libraries to fully utilize FastAPI's features.


# create separate env for fast api & other projects. Remove root virtual env