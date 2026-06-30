from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from core.config import GOOGLE_API_KEY, MODEL_NAME


llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GOOGLE_API_KEY,
    temperature=0,
)

planner_prompt = ChatPromptTemplate.from_template("""
You are an intent classifier.

Classify the user's question into exactly one of these labels.

QA
SUMMARY
COMPARE

Return ONLY the label.

Question:
{question}
""")

planner_chain = planner_prompt | llm


def detect_intent(question: str) -> str:
    response = planner_chain.invoke({
        "question": question
    })

    return response.content.strip().upper()