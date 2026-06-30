"use client"
import Sidebar from "@/components/Sidebar";
import Topbar from "@/components/Topbar";
import ChatWindow from "@/components/ChatWindow";
import ChatInput from "@/components/ChatInput";
import ActivityPanel from "@/components/ActivityPanel";
import { useState } from "react";
import { askQuestion } from "@/services/api";

export default function Home() {

  const [messages, setMessages] = useState([
  {
    role: "assistant",
    content: "Hello! Ask me about your uploaded documents."
  }
]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {

    if (!input.trim()) return;

    const userMessage = {
        role: "user",
        content: input,
    };

    setMessages(prev => [...prev, userMessage]);

    setLoading(true);

    const result = await askQuestion(input);

    const assistantMessage = {
        role: "assistant",
        content: result.answer,
    };

    setMessages(prev => [...prev, assistantMessage]);

    setLoading(false);

    setInput("");

};

  return (
    <main className="h-screen flex flex-col bg-slate-50">

      <Topbar />

      <div className="flex flex-1 overflow-hidden">

        <Sidebar />

        <div className="flex flex-1 flex-col">

          <ChatWindow messages={messages} />

          <ChatInput input={input}
    setInput={setInput}
    handleSend={handleSend}
    loading={loading}/>

        </div>

      </div>

      <ActivityPanel />

    </main>
  );
}