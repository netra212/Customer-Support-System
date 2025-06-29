from langchain_astradb import AstraDBGraphVectorStore
from dotenv import load_dotenv
import os
import pandas as pd
from data_transform import data_converter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings

load_dotenv()

ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["GOOGLE_API_KEY "] = GOOGLE_API_KEY
os.environ["ASTRA_DB_API_ENDPOINT"] = ASTRA_DB_API_ENDPOINT
os.environ["ASTRA_DB_APPLICATION_TOKEN"] = ASTRA_DB_APPLICATION_TOKEN
os.environ["ASTRA_DB_KEYSPACE"] = ASTRA_DB_KEYSPACE

# Custom SentenceTransformer wrapper class
# class SentenceTransformerEmbedding(Embedding):
#     def __init__(self, model_name = "paraphrase-MiniLM-L6-v2"):
#         self.model = SentenceTransformer(model_name)
    
#     # For a single query. 
#     def embed_query(self, text, **kwargs):
#         embeddings = self.model.encode([text], **kwargs)
#         return embeddings[0]  # Return the first embedding for the query
    
#     # For a whole documents query. 
#     def embed_documents(self, texts, **kwargs):
#         embeddings = self.model.encode(texts, **kwargs)
#         return embeddings
    
class ingest_data:
    def __init__(self):

        '''
        # OpenAI API key Limit Cross So....!
        self.embedding = OpenAIEmbeddings(
            model = "text-embedding-3-small"
        )

        # GoogleAPIKEY.
        # self.embedding = GoogleGenerativeAIEmbeddings(model = "models/text-embedding-004")

        '''

        # Using the SentenceTransformer for embedding generation
        # self.embedding = SentenceTransformerEmbeddings('paraphrase-MiniLM-L6-v2')  # Pre-trained model
        self.embedding = GoogleGenerativeAIEmbeddings(model = "models/text-embedding-004")
        self.data_converter = data_converter()

    def data_ingestion(self, status):
        print("Initiating Data Ingestion with Astra DB Graph Vector store.")
        vstore = AstraDBGraphVectorStore(
            embedding = self.embedding,
            collection_name = "chatbotecom", 
            api_endpoint = ASTRA_DB_API_ENDPOINT, 
            token = ASTRA_DB_APPLICATION_TOKEN, 
            namespace = ASTRA_DB_KEYSPACE
        )
        storage = status

        if storage == None:
            docs = self.data_converter.data_transformation()
            inserted_ids = vstore.add_documents(docs)
            print(inserted_ids)
        else:
            return vstore

        return vstore, inserted_ids


if __name__ == "__main__":
    d_in = ingest_data()
    vstore, inserted_ids = d_in.data_ingestion(None) # None mean we haven't stored the data yet. 
    print(f"\nInserted {len(inserted_ids)} documents.")
    # results = vstore.similarity_search(
    #     "Can you tell me the low budget headphone ?"
    # ) 
    # for res in results:
    #     print(f"{res.page_content} [{res.metadata}]")
