import { Upload, FileText } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function Sidebar() {

    const papers = [
        "WHO.pdf",
        "CDC.pdf",
        "JAMA.pdf"
    ];

    return (

        <aside className="w-72 border-r bg-white p-4">

            <Button className="w-full mb-6">

                <Upload className="mr-2 h-4 w-4"/>

                Upload Paper

            </Button>

            <h2 className="font-semibold mb-4">
                Papers
            </h2>

            <div className="space-y-2">

                {papers.map((paper)=>(
                    <div
                        key={paper}
                        className="flex items-center gap-2 rounded-lg border p-3 hover:bg-slate-100 cursor-pointer"
                    >
                        <FileText size={18}/>

                        {paper}

                    </div>
                ))}

            </div>

        </aside>

    )

}