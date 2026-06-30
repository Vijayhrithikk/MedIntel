from langchain_google_genai import GoogleGenerativeAIEmbeddings

from core.config import GOOGLE_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",api_key=GOOGLE_API_KEY)