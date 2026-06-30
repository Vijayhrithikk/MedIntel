from rag.rag import ask_question
from agents.graph import graph


class ChatService:

    def ask(self, question: str):

        result = graph.invoke({
            "question": question
        })

        return {
            "answer": result["answer"],
            "steps": [
                "Graph Started",
                "RAG Executed",
                "Graph Finished"
            ],
        }