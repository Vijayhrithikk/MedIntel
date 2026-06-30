from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from core.config import GOOGLE_API_KEY, MODEL_NAME
from rag.vectorstore import vectorstore

llm = ChatGoogleGenerativeAI(model=MODEL_NAME,google_api_key=GOOGLE_API_KEY,temperature=0)

prompt = ChatPromptTemplate.from_template(
"""
You are MedIntel.

Answer ONLY from the provided context.

If the answer is not present, say:
"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}
"""
)

def ask_question(question: str):

    docs = vectorstore.similarity_search(question, k=5)

    context = "\n\n".join(doc.page_content for doc in docs)

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return {
        "answer": response.content,
        "sources": docs
    }