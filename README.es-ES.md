

# Programmer-GPT

Programmer-GPT es un asistente de código impulsado por IA que se integra con los modelos GPT de OpenAI para analizar tu base de código y asistirte en tareas de programación. Inspirado por la necesidad de proporcionar continuamente contexto a ChatGPT, esta herramienta automatiza el proceso, permitiendo a la IA comprender e interactuar con tu proyecto completo.

## ✨ Características
- 📂 **Ingesta de Base de Código** – Analiza automáticamente los archivos de tu proyecto respetando las reglas de `.gitignore`.
- 💡 **Asistencia Impulsada por IA** – Genera implementaciones, refactoriza código u obtén explicaciones para lógica compleja.
- 🔍 **Almacenamiento de Datos Personalizable** – Almacena los datos analizados localmente o en la nube utilizando Deep Lake de Activeloop.
- 🛠 **Flujo de Trabajo Automatizado** – No es necesario copiar y pegar código en ChatGPT, simplemente consulta tu proyecto.

## 🚀 Cómo Empezar

### **Prerrequisitos**
- Python 3.8+
- Clave API de OpenAI
- (Opcional) Cuenta de Activeloop para almacenamiento en la nube

### **Instrucciones de Configuración**
1. **Clona el repositorio**  
   ```sh
   git clone https://github.com/aldo-leka/Programmer-GPT.git
   cd Programmer-GPT
   ```
2. **Crea un archivo `.env`** con los siguientes valores:
   ```ini
   DEVELOPMENT_FOLDER=C:/Projects/my-project
   OPENAI_API_KEY=your-openai-api-key
   ACTIVELOOP_TOKEN=your-activeloop-token
   ACTIVELOOP_DATASET=hub://username/dataset-name
   ```
   - Para almacenar el conjunto de datos localmente, usa `./my_deeplake/` en lugar de una URL de Activeloop.
   - Si lo almacenas localmente, puedes dejar `ACTIVELOOP_TOKEN` vacío.

3. **Instala las dependencias**  
   ```sh
   pip install -r requirements.txt
   ```

### **Uso**

1. **Ingestiona tu base de código**  
   ```sh
   python agent/ingest.py
   ```
   - Este script analiza tu base de código y la prepara para el análisis de IA.
   - Los archivos ignorados por `.gitignore` se excluyen automáticamente.

2. **Consulta tu proyecto con IA**  
   ```sh
   python agent/agent.py
   ```
   - Usa este script para hacerle preguntas a GPT sobre tu código, solicitar implementaciones de funciones u obtener ayuda con la depuración.

## 🎥 Demostración
![Programmer-GPT Demo](https://github.com/aldo-leka/Programmer-GPT/blob/main/img/demo.png?raw=true)

---

## 📁 Estructura del Proyecto
```
Programmer-GPT/
│── agent/                 # Scripts de procesamiento de IA
│   ├── ingest.py          # Analiza e ingiere archivos del proyecto
│   ├── agent.py           # Asistente de programación impulsado por IA
│── img/                   # Imágenes de demostración
│── .env.example           # Ejemplo de variables de entorno
│── requirements.txt       # Dependencias de Python
```

---

## 🤝 Contribuir
¿Quieres mejorar Programmer-GPT? ¡Siéntete libre de bifurcar el repositorio y enviar una pull request!

---

## 📜 Licencia
Este proyecto está licenciado bajo la **Licencia MIT**.

---

## 📬 Contacto
Para errores, preguntas o solicitudes de funciones, comunícate a través de **GitHub Issues**.
