from rag.rag import ask_question


def qa_tool(question: str):

    return ask_question(question)


def summary_tool(question: str):

    return ask_question(
        f"Summarize the uploaded document.\n\nQuestion: {question}"
    )


def compare_tool(question: str):

    return ask_question(
        f"Compare the uploaded documents.\n\nQuestion: {question}"
    )