# Getting Started with agent

## Helpful Commands

In the Python Environments window, or in a shell (e.g. Powershell or command prompt) you can create a new virtual environment.

### Python Environments -> Add Environment or `py -m venv env`

Use this command in the /agents project folder to create the virtual environment, which is an isolated environment with dependencies only for this project, aka not global.

### `env\Scripts\Activate` in Powershell or `env\Scripts\activate.bat` in command prompt

Use this command to activate the virtual environment and run the following commands inside the created virtual environment.

### Python Environments -> env -> Manage Python Packages or `pip install package_name`

Use this command to manage and install new packages in the virtual environment.

### (Optional) Python Environments -> env -> Generate requirements.txt or `py -m pip freeze > requirements.txt`

Use this command regularly to generate the list of requirements for your project.

### (Optional) Python Environments -> Add Environment (check Install packages from file: requirements.txt) or `pip install -r requirements.txt`

Use this command to install the requirements for your project when creating the virtual environment.

## Learn More

You can learn more in the [Python in Visual Studio](https://learn.microsoft.com/en-gb/visualstudio/python/tutorial-working-with-python-in-visual-studio-step-01-create-project?view=vs-2022) article.