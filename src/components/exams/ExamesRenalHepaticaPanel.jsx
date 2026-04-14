import { Checkbox } from "@/components/ui/checkbox";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Filter, Beaker, FlaskConical } from "lucide-react";

const examGroups = [
  {
    id: "renal",
    group: "Função Renal",
    icon: <Filter className="w-4 h-4" />,
    iconBg: "bg-blue-100 text-blue-600",
    items: [
      "Ureia",
      "Creatinina",
      "Cistatina C",
      "Albumina",
      "Proteínas Totais e Frações",
      "LDH (Desidrogenase Láctica)",
    ],
  },
  {
    id: "hepatica",
    group: "Função Hepática",
    icon: <Beaker className="w-4 h-4" />,
    iconBg: "bg-green-100 text-green-600",
    items: [
      "TGO (AST)",
      "TGP (ALT)",
      "GGT (Gama-Glutamil Transferase)",
      "Bilirrubinas (Total e Frações)",
      "Fosfatase Alcalina",
      "TAP (Tempo de Protrombina) / RNI",
    ],
  },
  {
    id: "pancreatica_outros",
    group: "Pancreática & Outros",
    icon: <FlaskConical className="w-4 h-4" />,
    iconBg: "bg-purple-100 text-purple-600",
    items: [
      "Amilase",
      "Lipase",
      "Ferritina",
      "Alfa-1-Antitripsina",
      "Cobre Sérico",
      "Ceruloplasmina",
    ],
  },
];

export default function ExamesRenalHepaticaPanel({ selectedExams = {}, onExamChange }) {
  const sectionId = "renal_hepatica";

  const handleToggle = (examName) => {
    onExamChange(sectionId, examName, !selectedExams[examName]);
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      {examGroups.map((group) => (
        <Card key={group.id} className="border border-gray-200 shadow-sm">
          <CardHeader className="pb-2 pt-4 px-4">
            <CardTitle className="flex items-center gap-2 text-sm font-semibold text-gray-700 tracking-wide">
              <span className={`p-1.5 rounded-md ${group.iconBg}`}>{group.icon}</span>
              {group.group}
            </CardTitle>
          </CardHeader>
          <CardContent className="px-4 pb-4 space-y-2">
            {group.items.map((exam) => (
              <div key={exam} className="flex items-start gap-2">
                <Checkbox
                  id={`renal_hepatica-${exam}`}
                  checked={!!selectedExams[exam]}
                  onCheckedChange={() => handleToggle(exam)}
                  className="mt-0.5"
                />
                <Label
                  htmlFor={`renal_hepatica-${exam}`}
                  className="text-sm text-gray-600 leading-tight cursor-pointer"
                >
                  {exam}
                </Label>
              </div>
            ))}
          </CardContent>
        </Card>
      ))}
    </div>
  );
}