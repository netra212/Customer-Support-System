from utils.config_loader import load_config

config = load_config()

collection_name = config["astra_db"]["collection_name"]
embedding_model_name = config["embedding_model"]["model_name"]
top_k = config["retriever"]["top_k"]

print("Collection Name: ", collection_name, "| Emedding model: ",embedding_model_name, "| Top k: ",top_k)