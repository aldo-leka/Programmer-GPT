# Programmer-GPT

The inspiration for this project came from the necessity to provide context continuously to Chat-GPT about code that I wanted to get help with. What if Chat-GPT already had access to all my codebase?

Programmer-GPT is an AI agent that uses OpenAI API and the GPT models to analyse your codebase and solve your programming tasks.

## Getting Started

Currently only the `agent` Python project is functional and it provides two Python scripts which are useful: `ingest.py` and `agent.py`.

In order for these scripts to work you need to create a new file named `.env` at subfolder `\app\agent\` that contains the following data:

1. DEVELOPMENT_FOLDER=C:/Projects/my-project
2. OPENAI_API_KEY=your-openai-api-key
3. ACTIVELOOP_TOKEN=your-activeloop-token
4. ACTIVELOOP_DATASET=hub://username/dataset-name

You can get the token and set your username for Activeloop's Deep Lake at `app.activeloop.ai`.
Dataset name can be whatever you want to name your dataset, e.g. the dev project's name.

To use the scripts:

1. Run `py app\agent\ingest.py` to ingest your codebase into the memory of Chat-GPT. Keep in mind that in order to speed up the process and reduce waste, `ingest.py` won't upload the folder and files that follow the patterns that are specified in the `.gitignore` files found in the development folder.

2. Run `py app\agent\agent.py` to have Chat-GPT give you implementations for new features or simply provide answers for your questions.

Demo
![alt text](https://github.com/lekisti/Programmer-GPT/blob/main/img/demo.png?raw=true)