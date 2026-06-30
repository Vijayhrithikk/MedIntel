type Message = {
    role: "user" | "assistant";
    content: string;
};

type ChatWindowProps = {
    messages: Message[];
};

export default function ChatWindow({ messages }: ChatWindowProps) {

    return (

        <div className="flex-1 overflow-auto p-8 space-y-6">

            {messages.map((message, index) => (

                <div
                    key={index}
                    className={`flex ${
                        message.role === "user"
                            ? "justify-end"
                            : "justify-start"
                    }`}
                >

                    <div
                        className={`rounded-xl px-5 py-3 max-w-2xl ${
                            message.role === "user"
                                ? "bg-blue-600 text-white"
                                : "bg-white border"
                        }`}
                    >

                        {message.content}

                    </div>

                </div>

            ))}

        </div>

    );

}