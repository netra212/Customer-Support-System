from dotenv import load_dotenv
from utils.config_loader import load_config
import os
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

class ModelLoader:
    """
    A utility class to load embedding models and LLM models."""
    
    def __init__(self):
        load_dotenv()
        # self.__validate_env()
        self.config = load_config()
    
    # def _validate_env(self):
    #     """
    #     Validate necessary environment variables
    #     """
    #     required_vars = ["GOOGLE_API_KEY"] 
    #     missing_vars = [var for var in required_vars if not os.getenv(var)]
    #     if missing_vars:
    #         raise EnvironmentError(f"Missing environment variables: {missing_vars}")
        
    def load_embedding(self):
        """
        Load and return the embedding model. 
        """
        print("Loading Embedding models.")
        model_name = self.config["embedding_model"]["model_name"]
        return SentenceTransformerEmbeddings(model_name=model_name)

    def load_llm(self):
        """
        Load and return the LLM model. 
        """
        print("LLM Loading....!")
        model_name = self.config["llm"]["model_name"]
        gemini_model = ChatGoogleGenerativeAI(
            model = model_name
        )