import os

from dotenv import load_dotenv
from igittigitt import IgnoreParser
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import DeepLake

load_dotenv(verbose=True, override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")
activeloop_token = os.getenv("ACTIVELOOP_TOKEN")
activeloop_dataset = os.getenv("ACTIVELOOP_DATASET")
development_folder = os.getenv("DEVELOPMENT_FOLDER")


def process_directory(dirpath, filenames, docs):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        try:
            loader = TextLoader(file_path, encoding="utf-8")
            docs.extend(loader.load_and_split())
        except Exception as e:
            pass


def abspath(path, *paths):
    return os.path.abspath(os.path.join(path, *paths))


gitignore_parser = IgnoreParser()
gitignore_parser.parse_rule_files(development_folder)
gitignore_parser.add_rule(".env", development_folder)
gitignore_parser.add_rule(".venv", development_folder)
gitignore_parser.add_rule("env/", development_folder)
gitignore_parser.add_rule("venv/", development_folder)
gitignore_parser.add_rule("ENV/", development_folder)

docs = []

for dirpath, dirnames, filenames in os.walk(os.path.normpath(development_folder)):
    # filter out ignored directories
    dirnames = [
        dirname
        for dirname in dirnames
        if not gitignore_parser.match(os.path.abspath(os.path.join(dirpath, dirname)))
    ]

    # filter out ignored files
    filenames = [
        file
        for file in filenames
        if not gitignore_parser.match(os.path.abspath(os.path.join(dirpath, file)))
    ]

    process_directory(dirpath, filenames, docs)

embeddings = OpenAIEmbeddings()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(docs)

db = DeepLake.from_documents(
    texts, embeddings, dataset_path=activeloop_dataset)

# TODO Implement local redis cache for legally safer (not cloud) memory usage
