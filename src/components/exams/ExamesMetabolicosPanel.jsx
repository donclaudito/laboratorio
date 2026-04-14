import { Checkbox } from "@/components/ui/checkbox";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Droplets, Heart, FlaskConical } from "lucide-react";

const examGroups = [
  {
    id: "glicidico",
    group: "Metabolismo Glicídico",
    icon: <Droplets className="w-4 h-4" />,
    iconBg: "bg-red-100 text-red-600",
    items: [
      "Glicemia em Jejum",
      "Hemoglobina Glicada (HbA1c)",
      "Insulina de Jejum",
      "Peptídeo C",
      "Frutosamina",
      "Relação Albumina/Creatinina Urinária",
    ],
  },
  {
    id: "lipidico",
    group: "Perfil Lipídico & Risco CV",
    icon: <Heart className="w-4 h-4" />,
    iconBg: "bg-rose-100 text-rose-600",
    items: [
      "Colesterol Total e Frações (LDL, HDL, VLDL)",
      "Triglicerídeos",
      "Apolipoproteína A1 (Apo A1)",
      "Apolipoproteína B (Apo B)",
      "Lipoproteína (a) [Lp(a)]",
      "Lp-PLA2 (Fosfolipase A2)",
      "Homocisteína",
    ],
  },
  {
    id: "inflamacao",
    group: "Inflamação, Nutrição & Outros",
    icon: <FlaskConical className="w-4 h-4" />,
    iconBg: "bg-amber-100 text-amber-600",
    items: [
      "PCR-ultrassensível (PCR-us)",
      "Fibrinogênio",
      "Ácido Úrico",
      "Gama-GT (GGT)",
      "Ferritina",
      "Vitamina B12",
      "Folato Sérico",
      "25-Hidroxivitamina D",
      "Magnésio Eritrocitário",
    ],
  },
];

export default function ExamesMetabolicosPanel({ selectedExams = {}, onExamChange }) {
  const sectionId = "metabolica";

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
                  id={`metabolica-${exam}`}
                  checked={!!selectedExams[exam]}
                  onCheckedChange={() => handleToggle(exam)}
                  className="mt-0.5"
                />
                <Label
                  htmlFor={`metabolica-${exam}`}
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