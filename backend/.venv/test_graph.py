from agents.graph import graph

result = graph.invoke({
    "question":"Summarize the uploaded paper."
})

print(result)