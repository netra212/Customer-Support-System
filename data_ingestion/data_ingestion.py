from langchain_astradb import AstraDBGraphVectorStore
from dotenv import load_dotenv
import os
import pandas as pd
from data_ingestion.data_transform import data_converter

load_dotenv()

ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# OPENAI_API_KEY = "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"


class ingest_data:
    def __init__(self):
        print("Data Ingestion Class Initialized...!")

    def data_ingestion(self):
        pass

if __name__ == "__main__":
    d_in = ingest_data()
