import { Brain } from "lucide-react";

export default function Topbar() {
  return (
    <header className="h-16 border-b bg-white flex items-center justify-between px-6">

      <div className="flex items-center gap-2">

        <Brain className="text-blue-600"/>

        <h1 className="text-xl font-bold">
          MedIntel
        </h1>

      </div>

    </header>
  );
}