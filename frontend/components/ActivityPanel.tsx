import { Brain } from "lucide-react";

export default function ActivityPanel(){

    const steps = [
        "Intent Detected",
        "Retrieved 5 Chunks",
        "Generated Answer"
    ];

    return(

        <div className="h-24 border-t bg-white px-6 py-3">

            <div className="flex items-center gap-2 mb-2">

                <Brain size={18}/>

                <span className="font-semibold">

                    Agent Activity

                </span>

            </div>

            <div className="flex gap-3">

                {steps.map((step)=>(

                    <div
                        key={step}
                        className="rounded-full bg-green-100 text-green-700 px-4 py-1 text-sm"
                    >
                        ✓ {step}
                    </div>

                ))}

            </div>

        </div>

    )

}