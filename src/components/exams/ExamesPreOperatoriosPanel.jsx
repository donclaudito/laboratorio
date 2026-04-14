import { Checkbox } from "@/components/ui/checkbox";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Droplets, FlaskConical, Shield } from "lucide-react";

const examGroups = [
  {
    id: "coagulacao_sangue",
    group: "Sangue e Coagulação",
    icon: <Droplets className="w-4 h-4" />,
    iconBg: "bg-red-100 text-red-600",
    items: [
      "Hemograma Completo",
      "Coagulograma Completo (TAP, RNI, TTPA e Tempo de Sangramento)",
      "Contagem de Plaquetas",
      "Tipagem Sanguínea (ABO) e Fator Rh",
      "Pesquisa de Anticorpos Irregulares (Screening)",
      "Beta-HCG (para pacientes em idade fértil)",
    ],
  },
  {
    id: "bioquimica",
    group: "Bioquímica",
    icon: <FlaskConical className="w-4 h-4" />,
    iconBg: "bg-blue-100 text-blue-600",
    items: [
      "Glicemia em Jejum",
      "Creatinina",
      "Ureia",
      "Eletrólitos (Sódio, Potássio, Cálcio Iônico e Magnésio)",
      "TGO (AST) e TGP (ALT)",
      "Bilirrubinas (Total e Frações)",
      "Proteínas Totais e Frações",
      "Proteína C Reativa (PCR)",
    ],
  },
  {
    id: "infeccioso_urina",
    group: "Infeccioso e Urina",
    icon: <Shield className="w-4 h-4" />,
    iconBg: "bg-emerald-100 text-emerald-600",
    items: [
      "Urina Tipo I (EAS)",
      "Marcadores de Hepatites (HBsAg e Anti-HCV)",
      "HIV 1 e 2",
      "VDRL",
    ],
  },
];

const SECTION_ID = "pre_operatorios";

export default function ExamesPreOperatoriosPanel({ selectedExams = {}, onExamChange }) {
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