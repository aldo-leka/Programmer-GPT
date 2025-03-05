# Programmer-GPT

Programmer-GPT is an AI-powered code assistant that integrates with OpenAI's GPT models to analyze your codebase and assist with programming tasks. Inspired by the need to continuously provide context to ChatGPT, this tool automates the process, allowing AI to understand and interact with your entire project.

## ✨ Features
- 📂 **Codebase Ingestion** – Automatically parses your project files while respecting `.gitignore` rules.
- 💡 **AI-Powered Assistance** – Generate implementations, refactor code, or get explanations for complex logic.
- 🔍 **Customizable Data Storage** – Store analyzed data locally or in the cloud using Activeloop’s Deep Lake.
- 🛠 **Automated Workflow** – No need to copy-paste code into ChatGPT—simply query your project.

## 🚀 Getting Started

### **Prerequisites**
- Python 3.8+
- OpenAI API Key
- (Optional) Activeloop Account for cloud storage

### **Setup Instructions**
1. **Clone the repository**  
   ```sh
   git clone https://github.com/aldo-leka/Programmer-GPT.git
   cd Programmer-GPT
   ```
2. **Create a `.env` file** with the following values:
   ```ini
   DEVELOPMENT_FOLDER=C:/Projects/my-project
   OPENAI_API_KEY=your-openai-api-key
   ACTIVELOOP_TOKEN=your-activeloop-token
   ACTIVELOOP_DATASET=hub://username/dataset-name
   ```
   - To store the dataset locally, use `./my_deeplake/` instead of an Activeloop URL.
   - If storing locally, you can leave `ACTIVELOOP_TOKEN` empty.

3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

### **Usage**

1. **Ingest your codebase**  
   ```sh
   python agent/ingest.py
   ```
   - This script scans your codebase and prepares it for AI analysis.
   - Files ignored by `.gitignore` are automatically excluded.

2. **Query your project with AI**  
   ```sh
   python agent/agent.py
   ```
   - Use this script to ask GPT about your code, request feature implementations, or get debugging help.

## 🎥 Demo
![Programmer-GPT Demo](https://github.com/aldo-leka/Programmer-GPT/blob/main/img/demo.png?raw=true)

---

## 📁 Project Structure
```
Programmer-GPT/
│── agent/                 # AI processing scripts
│   ├── ingest.py          # Scans and ingests project files
│   ├── agent.py           # AI-powered programming assistant
│── img/                   # Demo images
│── .env.example           # Example environment variables
│── requirements.txt       # Python dependencies
```

---

## 🤝 Contributing
Want to enhance Programmer-GPT? Feel free to fork the repo and submit a pull request!

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📬 Contact
For issues, questions, or feature requests, reach out via **GitHub Issues**.

