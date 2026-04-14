import { Checkbox } from "@/components/ui/checkbox";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Microscope, Activity, Zap } from "lucide-react";

const examGroups = [
  {
    id: "hemato_ferro",
    group: "Hematologia & Ferro",
    icon: <Microscope className="w-4 h-4" />,
    iconBg: "bg-red-100 text-red-600",
    items: [
      "Hemograma Completo",
      "Ferritina",
      "Ferro Sérico",
      "Capacidade Total de Ligação do Ferro (TIBC)",
      "Saturação de Transferrina",
      "Vitamina B12",
      "Folato Sérico",
      "Magnésio Eritrocitário",
    ],
  },
  {
    id: "tireoide_vitaminas",
    group: "Tireoide & Vitaminas",
    icon: <Activity className="w-4 h-4" />,
    iconBg: "bg-teal-100 text-teal-600",
    items: [
      "TSH (Hormônio Estimulante da Tireoide)",
      "T4 Livre",
      "T3 Livre",
      "T3 Reverso (RT3)",
      "Anticorpos Anti-TPO",
      "Anticorpos Anti-Tireoglobulina",
      "Vitamina D (25-OH Vitamina D)",
      "Proteína C Reativa Ultrassensível (PCR-us)",
    ],
  },
  {
    id: "hormonal",
    group: "Hormônios & Minerais",
    icon: <Zap className="w-4 h-4" />,
    iconBg: "bg-violet-100 text-violet-600",
    items: [
      "Zinco Sérico",
      "Selênio Sérico",
      "Cortisol Basal (8h)",
      "DHEA (Deidroepiandrosterona)",
      "Sulfato de DHEA (S-DHEA)",
      "Testosterona Total e Livre",
      "SHBG (Globulina Transportadora de Hormônios Sexuais)",
      "Estradiol",
    ],
  },
];

const SECTION_ID = "geral_hormonal";

export default function ExamesGeralHormonalPanel({ selectedExams = {}, onExamChange }) {
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