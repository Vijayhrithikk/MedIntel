from langchain_chroma import Chroma

from rag.embeddings import embeddings

vectorstore = Chroma(collection_name="medical_documents", embedding_function=embeddings, persist_directory="./chroma_db")