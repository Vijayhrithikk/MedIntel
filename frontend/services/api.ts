export async function askQuestion(question: string) {
    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({question})
    });
    return response.json();
}