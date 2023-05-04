import os

from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake

load_dotenv()

embeddings = OpenAIEmbeddings(disallowed_special=())


activeloop_dataset = os.getenv("ACTIVELOOP_DATASET")
development_folder = os.getenv("DEVELOPMENT_FOLDER")

# Question Answering on Auto-GPT algorithm codebase
db = DeepLake(dataset_path=activeloop_dataset,
              read_only=True, embedding_function=embeddings)

retriever = db.as_retriever()
retriever.search_kwargs['distance_metric'] = 'cos'
retriever.search_kwargs['fetch_k'] = 100
retriever.search_kwargs['maximal_marginal_relevance'] = True
retriever.search_kwargs['k'] = 10


model = ChatOpenAI(model='gpt-4', temperature=0,
                   request_timeout=120)  # gpt-3.5-turbo
qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)

chat_history = []
project_name = development_folder.split('/')[-1]

# prompt for user input
print(
    f"Welcome to the {project_name} chatbot. Ask any questions or type 'exit' to quit.")
while True:
    user_input = input(">> ")
    if user_input == "exit":
        break
    question = user_input
    result = qa({"question": question, "chat_history": chat_history})
    chat_history.append((question, result['answer']))
    print(f"**Answer**: {result['answer']} \n")
