import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Send } from "lucide-react";

type ChatInputProps = {
    input: string;
    setInput: React.Dispatch<React.SetStateAction<string>>;
    handleSend: () => void;
    loading: boolean;
};

export default function ChatInput({
    input,
    setInput,
    handleSend,
    loading,
}: ChatInputProps) {

    return (

        <div className="border-t bg-white p-4 flex gap-4">

            <Input
                placeholder="Ask MedIntel..."
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => {
                    if (e.key === "Enter") {
                        handleSend();
                    }
                }}
            />

            <Button
                onClick={handleSend}
                disabled={loading}
            >
                <Send size={18} />
            </Button>

        </div>

    );

}