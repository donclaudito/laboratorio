import { Checkbox } from "@/components/ui/checkbox";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { TestTube, Microscope, FlaskConical } from "lucide-react";

const examGroups = [
  {
    id: "urina",
    group: "Urina",
    icon: <TestTube className="w-4 h-4" />,
    iconBg: "bg-yellow-100 text-yellow-600",
    items: [
      "Urina Tipo I (EAS)",
      "Microalbuminúria (Amostra isolada ou 24h)",
      "Creatinina Urinária",
      "Relação Albumina/Creatinina Urinária (RAC)",
      "Citologia Urinária (se indicado por hematúria)",
    ],
  },
  {
    id: "fezes_basico",
    group: "Fezes – Básico",
    icon: <Microscope className="w-4 h-4" />,
    iconBg: "bg-orange-100 text-orange-600",
    items: [
      "Protoparasitológico de Fezes (PPF)",
      "Sangue Oculto nas Fezes (Pesquisa imunocromatográfica)",
      "Coprocultura",
      "Pesquisa de Leucócitos nas Fezes",
      "pH e Substâncias Redutoras nas Fezes",
    ],
  },
  {
    id: "fezes_avancado",
    group: "Fezes – Avançado",
    icon: <FlaskConical className="w-4 h-4" />,
    iconBg: "bg-lime-100 text-lime-600",
    items: [
      "Calprotectina Fecal",
      "Elastase Pancreática Fecal",
      "Gordura Fecal (Sudan III ou Esteatócrito)",
      "Pesquisa de Clostridioides difficile (Toxinas A e B)",
    ],
  },
];

const SECTION_ID = "urina_fezes";

export default function ExamesUrinaFezesPanel({ selectedExams = {}, onExamChange }) {
  const handleToggle = (examName) => {
    onExamChange(SECTION_ID, examName, !selectedExams[examName]);
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
                  id={`${SECTION_ID}-${exam}`}
                  checked={!!selectedExams[exam]}
                  onCheckedChange={() => handleToggle(exam)}
                  className="mt-0.5"
                />
                <Label
                  htmlFor={`${SECTION_ID}-${exam}`}
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