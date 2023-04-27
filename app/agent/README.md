# Getting Started with agent

## Primary Commands

In the Python Environments window, or in a shell (e.g. Powershell or command prompt) you can create a new virtual environment.

### Python Environments -> Add Environment or run `py -m venv .venv`

Use this command to create the virtual environment, which is an isolated environment with dependencies used only for this project, that is, not global.

### Run `.venv\Scripts\Activate` in Powershell or `.venv\Scripts\activate.bat` in command prompt

Use this command to activate the virtual environment and to run the following commands inside the created virtual environment.

### Python Environments -> Add Environment (check Install packages from file: requirements.txt) or `pip install -r requirements.txt`

Use this command to install the requirements for your project when creating the virtual environment.

### Start ingest.py script or run `py ingest.py` (or `py app\agent\ingest.py` at root)

Use this command to ingest the agent's memory with the development project's files.

### Start agent.py script or run `py agent.py` (or `py app\agent\agent.py` at root)

Use this command to test the AI model with questions about the codebase.

## Helpful Commands

### Python Environments -> env -> Generate requirements.txt or `py -m pip freeze > requirements.txt`

Use this command regularly to generate the list of requirements for your project.

### Python Environments -> env -> Manage Python Packages or run `pip install package_name`

Use this command to manage and install new packages in the virtual environment.

### Run `pip install -U langchain deeplake openai tiktoken`

Use this command to update the main packages of the project.

### Run `pip uninstall -r requirements.txt -y`

Use this command to uninstall packages found at requirements.txt, especially in case of errors. Combine with command to create the requirements list `py -m pip freeze > requirements.txt` and you can re-install all packages in case of errors.

### Run `pip uninstall package_name` and `pip install package_name==1.2.3`

Use these commands to downgrade a package, in case of related errors.

### (Optional) Run `pip install pip-review`

Use this command to install pip-review which is able to automatically install available package updates.

### (Dangerous) Run `pip-review --local --auto`

Use this command to install available local package updates. It's dangerous as it can create mismatches between dependencies.

## Learn More

You can learn more in the [Python in Visual Studio](https://learn.microsoft.com/en-gb/visualstudio/python/tutorial-working-with-python-in-visual-studio-step-01-create-project?view=vs-2022) article.