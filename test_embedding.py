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