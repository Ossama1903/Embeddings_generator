import argparse
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.openai import OpenAIEmbeddings
import chromadb
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

os.environ["OPENAI_API_KEY"] = "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"

# # Set up command line argument parser
# parser = argparse.ArgumentParser(description='Process text files and create embeddings.')
# parser.add_argument('directory_path', type=str, help='Path to the directory containing text files')

# # Parse command line arguments
# args = parser.parse_args()

# # Specify the directory containing the text files
# directory_path = args.directory_path

# print(f"Processing directory {directory_path}")

# # Iterate through all files in the directory
# for filename in os.listdir(directory_path):
#     if filename.endswith(".txt"):
#         file_path = os.path.join(directory_path, filename)
#         try:
#             print(f"Creating embeddings for {filename}")

#             # Similar code as before, with minor modifications
#             loader = TextLoader(file_path, encoding="utf-8")
#             documents = loader.load()

#             text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=0)
#             docs = text_splitter.split_documents(documents)

#             embeddings = OpenAIEmbeddings()
#             new_client = chromadb.EphemeralClient()

#             #Vector DB
#             openai_lc_client = Chroma.from_documents(
#                 docs, embeddings, persist_directory = f"{directory_path}-embeddings"
#             )

#             openai_lc_client.persist()

#         except Exception as e:
#             print(f"Error processing {filename}: {e}")

vectordb = None
embedding = OpenAIEmbeddings()
vectordb = Chroma(
    persist_directory="2018-G11-Biology-E-embeddings", embedding_function=embedding
)

query = "Photosynthesis"
docs = vectordb.similarity_search(query)

for i in range(len(docs)):
    print(docs[i].page_content)
    print("\n\n")

# print(docs[0].page_content)
