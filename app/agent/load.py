import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings

load_dotenv(verbose=True, override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")
activeloop_token = os.getenv("ACTIVELOOP_TOKEN")
activeloop_dataset = os.getenv("ACTIVELOOP_DATASET")
development_folder = os.getenv("DEVELOPMENT_FOLDER")

embeddings = OpenAIEmbeddings()

from langchain.document_loaders import TextLoader

root_dir = development_folder
docs = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        try: 
            loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
            docs.extend(loader.load_and_split())
        except Exception as e: 
            pass

from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(docs)

from langchain.vectorstores import DeepLake

db = DeepLake.from_documents(texts, embeddings, dataset_path=activeloop_dataset)