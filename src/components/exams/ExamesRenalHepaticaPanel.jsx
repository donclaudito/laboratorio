import { Checkbox } from "@/components/ui/checkbox";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const examGroups = [
  {
    id: "renal",
    group: "🫘 Função Renal",
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
    group: "🫀 Função Hepática",
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
    group: "🔬 Pancreática & Outros",
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
            <CardTitle className="text-sm font-semibold text-gray-700 tracking-wide">
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