import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Checkbox } from "@/components/ui/checkbox";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
} from "@/components/ui/dialog";
import { Badge } from "@/components/ui/badge";
import {
  FileText,
  Copy,
  Trash2,
  CheckCircle,
  ClipboardList,
  Heart,
  Wind,
  Stethoscope,
  Pill,
} from "lucide-react";

const MOTIVOS_GRUPOS = [
  {
    grupo: "Hérnias da Parede Abdominal",
    opcoes: [
      "Hérnia Inguinal Direita",
      "Hérnia Inguinal Esquerda",
      "Hérnia Inguinal Bilateral",
      "Hérnia Inguinal Direita Recidivada",
      "Hérnia Inguinal Esquerda Recidivada",
      "Hérnia Inguinal Bilateral Recidivada",
      "Hérnia Crural Direita",
      "Hérnia Crural Esquerda",
      "Hérnia Crural Bilateral",
      "Hérnia Umbilical",
      "Hérnia Umbilical Recidivada",
      "Hérnia Epigástrica",
      "Hérnia Epigástrica Recidivada",
      "Hérnia Incisional",
      "Hérnia Incisional Recidivada",
      "Hérnia de Spiegel",
      "Hérnia Lombar",
      "Hérnia Obturadora",
      "Hérnia Paraesofágica / Hiatal",
      "Diástase dos Retos Abdominais",
    ],
  },
  {
    grupo: "Vesícula e Vias Biliares",
    opcoes: [
      "Colelitíase / Colecistite Crônica Calculosa",
      "Colecistite Aguda (eletiva após resolução)",
      "Coledocolitíase",
      "Pólipo de Vesícula Biliar",
      "Colangite Crônica",
    ],
  },
  {
    grupo: "Esôfago e Estômago",
    opcoes: [
      "Doença do Refluxo Gastroesofágico (DRGE) — Fundoplicatura",
      "Hérnia Hiatal Mista / Paraesofágica",
      "Acalasia de Esôfago",
      "Divertículo de Zenker",
      "Divertículo Esofágico de Tração",
      "Úlcera Péptica Gástrica Refratária",
      "Úlcera Péptica Duodenal Refratária",
      "Tumor Benigno Gástrico (GIST / Leiomioma)",
      "Estenose Pilórica do Adulto",
    ],
  },
  {
    grupo: "Intestino Delgado",
    opcoes: [
      "Aderências / Bridas Intestinais (cirurgia eletiva)",
      "Tumor Benigno de Intestino Delgado",
      "Doença de Crohn — Ressecção Eletiva",
      "Divertículo de Meckel Sintomático",
      "Fístula Enterocutânea",
    ],
  },
  {
    grupo: "Cólon e Reto",
    opcoes: [
      "Doença Diverticular do Cólon Sintomática",
      "Pólipo Colônico de Grande Volume (não ressecável por colonoscopia)",
      "Megacólon Chagásico",
      "Constipação Crônica de Causa Colônica",
      "Colite Ulcerativa — Cirurgia Eletiva",
      "Doença de Crohn Colônica — Cirurgia Eletiva",
      "Prolapso Retal",
      "Retocele Sintomática",
      "Estenose Retal Benigna",
    ],
  },
  {
    grupo: "Região Anorretal e Períneo",
    opcoes: [
      "Hemorróidas Grau III / IV",
      "Fissura Anal Crônica",
      "Fístula Perianal (transesfincteriana / supraesfincteriana)",
      "Fístula Perianal Baixa (interesfincteriana / submucosa)",
      "Abscesso Anorretal Recorrente",
      "Cisto Pilonidal / Seio Pilonidal",
      "Condiloma Acuminado Perianal (extenso)",
      "Incontinência Fecal — Esfincteroplastia Eletiva",
      "Hidradenite Supurativa Perianal",
    ],
  },
  {
    grupo: "Fígado, Pâncreas e Baço",
    opcoes: [
      "Cisto Hepático Simples Sintomático",
      "Cisto Hidático Hepático",
      "Hepatolitíase",
      "Hemangioma Hepático Sintomático",
      "Adenoma Hepático",
      "Hipertensão Portal — Shunt Cirúrgico Eletivo",
      "Pancreatite Crônica — Cirurgia Eletiva (Frey / Puestow / Beger)",
      "Pseudocisto Pancreático Sintomático",
      "Cistoadenoma Seroso / Mucinoso do Pâncreas",
      "Esplenomegalia — Esplenectomia Eletiva",
      "Cisto Esplênico Sintomático",
    ],
  },
  {
    grupo: "Tireoide e Paratireoide",
    opcoes: [
      "Bócio Nodular — Tireoidectomia Parcial / Total",
      "Nódulo de Tireoide Indeterminado (Bethesda III / IV)",
      "Hipertireoidismo Refratário ao Tratamento Clínico",
      "Hiperparatireoidismo Primário — Paratireoidectomia",
      "Adenoma de Paratireoide",
    ],
  },
  {
    grupo: "Parede Torácica e Mediastino (Cirurgia Geral)",
    opcoes: [
      "Empiema Pleural Crônico (decorticação eletiva)",
      "Cisto Mediastinal Benigno",
      "Tumor de Parede Torácica Benigno",
    ],
  },
  {
    grupo: "Mama (Cirurgia Geral)",
    opcoes: [
      "Fibroadenoma de Mama",
      "Tumor Filodes Benigno de Mama",
      "Ginecomastia",
      "Abscesso Mamário Recorrente / Fístula de Ducto",
      "Cisto Mamário Volumoso / Recorrente",
    ],
  },
  {
    grupo: "Partes Moles e Dermatologia",
    opcoes: [
      "Cisto Sebáceo / Epidérmico",
      "Lipoma",
      "Fibroma / Dermatofibroma",
      "Nevo Melanocítico — Exérese Eletiva",
      "Queratose Seborreica Complicada",
      "Granuloma Piogênico",
      "Carcinoma Basocelular / Espinocelular (ressecção eletiva)",
      "Cirurgia Ambulatorial Dermatológica Geral",
    ],
  },
  {
    grupo: "Outros",
    opcoes: [
      "Outro (especificar no campo personalizado)",
    ],
  },
];

// Lista plana para compatibilidade com o campo de texto gerado
const MOTIVOS = MOTIVOS_GRUPOS.flatMap((g) => g.opcoes);

const COMORBIDADES = [
  { id: "has", label: "Hipertensão Arterial Sistêmica (HAS)" },
  { id: "dm", label: "Diabetes Mellitus (DM)" },
  { id: "cardiopatia", label: "Cardiopatia" },
  { id: "pneumopatia", label: "Pneumopatia" },
  { id: "nefropatia", label: "Nefropatia" },
  { id: "obesidade", label: "Obesidade" },
  { id: "alergia", label: "Alergia a Medicamentos" },
  { id: "drogas", label: "Uso de Drogas Ilícitas" },
  { id: "tabagismo", label: "Tabagismo" },
  { id: "etilismo", label: "Etilismo" },
  { id: "sem_comorbidades", label: "Sem Comorbidades Conhecidas" },
];

const MEDICAMENTOS_POR_COMORBIDADE = {
  has: {
    titulo: "Hipertensão Arterial (HAS)",
    grupos: [
      {
        grupo: "IECA / BRA",
        medicamentos: [
          "Enalapril 5mg 1x/dia",
          "Enalapril 10mg 2x/dia",
          "Losartana 50mg 1x/dia",
          "Losartana 100mg 1x/dia",
          "Ramipril 5mg 1x/dia",
          "Valsartana 80mg 1x/dia",
        ],
      },
      {
        grupo: "Bloqueadores do Canal de Cálcio",
        medicamentos: [
          "Anlodipino 5mg 1x/dia",
          "Anlodipino 10mg 1x/dia",
          "Nifedipino retard 20mg 2x/dia",
        ],
      },
      {
        grupo: "Betabloqueadores",
        medicamentos: [
          "Atenolol 25mg 1x/dia",
          "Atenolol 50mg 1x/dia",
          "Metoprolol 50mg 2x/dia",
          "Carvedilol 6,25mg 2x/dia",
          "Carvedilol 12,5mg 2x/dia",
        ],
      },
      {
        grupo: "Diuréticos",
        medicamentos: [
          "Hidroclorotiazida 25mg 1x/dia",
          "Clortalidona 25mg 1x/dia",
          "Furosemida 40mg 1x/dia",
          "Espironolactona 25mg 1x/dia",
        ],
      },
    ],
  },
  dm: {
    titulo: "Diabetes Mellitus (DM)",
    grupos: [
      {
        grupo: "Biguanidas",
        medicamentos: [
          "Metformina 500mg 2x/dia",
          "Metformina 850mg 2x/dia",
          "Metformina 1g 2x/dia",
        ],
      },
      {
        grupo: "Sulfonilureias",
        medicamentos: [
          "Glibenclamida 5mg 1x/dia",
          "Glicazida 30mg 1x/dia",
          "Glipizida 5mg 1x/dia",
        ],
      },
      {
        grupo: "Inibidores de DPP-4 / GLP-1",
        medicamentos: [
          "Sitagliptina 100mg 1x/dia",
          "Vildagliptina 50mg 2x/dia",
          "Liraglutida 1,2mg SC 1x/dia",
          "Semaglutida 0,5mg SC 1x/semana",
        ],
      },
      {
        grupo: "Inibidores de SGLT-2",
        medicamentos: [
          "Empagliflozina 10mg 1x/dia",
          "Dapagliflozina 10mg 1x/dia",
        ],
      },
      {
        grupo: "Insulinas",
        medicamentos: [
          "Insulina NPH 10UI SC 2x/dia",
          "Insulina Regular conforme glicemia",
          "Insulina Glargina 10UI SC 1x/dia",
          "Insulina Detemir SC 1x/dia",
        ],
      },
    ],
  },
  cardiopatia: {
    titulo: "Cardiopatia",
    grupos: [
      {
        grupo: "Antiagregantes / Anticoagulantes",
        medicamentos: [
          "AAS 100mg 1x/dia",
          "Clopidogrel 75mg 1x/dia",
          "Warfarina (dose variável — INR alvo 2–3)",
          "Rivaroxabana 20mg 1x/dia",
          "Apixabana 5mg 2x/dia",
          "Dabigatrana 150mg 2x/dia",
        ],
      },
      {
        grupo: "Hipolipemiantes",
        medicamentos: [
          "Atorvastatina 20mg 1x/dia",
          "Atorvastatina 40mg 1x/dia",
          "Atorvastatina 80mg 1x/dia",
          "Rosuvastatina 10mg 1x/dia",
          "Rosuvastatina 20mg 1x/dia",
        ],
      },
      {
        grupo: "Betabloqueadores / Antiarrítmicos",
        medicamentos: [
          "Metoprolol 50mg 2x/dia",
          "Carvedilol 6,25mg 2x/dia",
          "Bisoprolol 5mg 1x/dia",
          "Amiodarona 200mg 1x/dia",
          "Digoxina 0,25mg 1x/dia",
        ],
      },
      {
        grupo: "Para IC / Vasodilatadores",
        medicamentos: [
          "Sacubitril/Valsartana 49/51mg 2x/dia",
          "Ivabradina 5mg 2x/dia",
          "Isossorbida 20mg 3x/dia",
          "Furosemida 40mg 1x/dia",
          "Espironolactona 25mg 1x/dia",
        ],
      },
    ],
  },
  pneumopatia: {
    titulo: "Pneumopatia",
    grupos: [
      {
        grupo: "Broncodilatadores de Curta Ação (SABA)",
        medicamentos: [
          "Salbutamol 100mcg inalatório (2 jatos SOS)",
          "Fenoterol 100mcg inalatório (2 jatos SOS)",
        ],
      },
      {
        grupo: "Broncodilatadores de Longa Ação (LABA/LAMA)",
        medicamentos: [
          "Formoterol 12mcg inalatório 2x/dia",
          "Salmeterol 50mcg inalatório 2x/dia",
          "Tiotrópio 18mcg inalatório 1x/dia",
          "Umeclidínio 62,5mcg inalatório 1x/dia",
        ],
      },
      {
        grupo: "Corticosteroides Inalatórios",
        medicamentos: [
          "Budesonida 200mcg inalatório 2x/dia",
          "Budesonida 400mcg inalatório 2x/dia",
          "Fluticasona 250mcg inalatório 2x/dia",
          "Beclometasona 200mcg inalatório 2x/dia",
        ],
      },
      {
        grupo: "Corticosteroides Sistêmicos / Outros",
        medicamentos: [
          "Prednisona 20mg 1x/dia (exacerbação)",
          "Montelucaste 10mg 1x/dia",
          "Teofilina 200mg 2x/dia",
        ],
      },
    ],
  },
  nefropatia: {
    titulo: "Nefropatia",
    grupos: [
      {
        grupo: "Protetores Renais",
        medicamentos: [
          "Losartana 50mg 1x/dia",
          "Enalapril 10mg 1x/dia",
          "Dapagliflozina 10mg 1x/dia",
        ],
      },
      {
        grupo: "Anemia / Osso",
        medicamentos: [
          "Eritropoetina 4.000UI SC 3x/semana",
          "Ferro sacarato IV (conforme protocolo)",
          "Carbonato de cálcio 500mg 3x/dia",
          "Calcitriol 0,25mcg 1x/dia",
        ],
      },
      {
        grupo: "Diuréticos / Equilíbrio",
        medicamentos: [
          "Furosemida 40mg 1x/dia",
          "Furosemida 80mg 2x/dia",
          "Bicarbonato de sódio 840mg 3x/dia",
        ],
      },
      {
        grupo: "Quelantes de Fósforo",
        medicamentos: [
          "Sevelâmer 800mg 3x/dia (com refeições)",
          "Carbonato de cálcio como quelante 3x/dia",
        ],
      },
    ],
  },
  obesidade: {
    titulo: "Obesidade",
    grupos: [
      {
        grupo: "Antiobesidade",
        medicamentos: [
          "Orlistate 120mg 3x/dia (com refeições)",
          "Sibutramina 10mg 1x/dia",
          "Liraglutida 3mg SC 1x/dia",
          "Semaglutida 2,4mg SC 1x/semana",
          "Naltrexona/Bupropiona 8/90mg 2x/dia",
        ],
      },
      {
        grupo: "Adjuvantes Metabólicos",
        medicamentos: [
          "Metformina 850mg 2x/dia",
          "Topiramato 25mg 1x/dia",
        ],
      },
    ],
  },
  tabagismo: {
    titulo: "Tabagismo",
    grupos: [
      {
        grupo: "Terapia de Reposição de Nicotina",
        medicamentos: [
          "Adesivo de nicotina 21mg/24h (fase 1)",
          "Adesivo de nicotina 14mg/24h (fase 2)",
          "Goma de nicotina 2mg SOS",
          "Pastilha de nicotina 2mg SOS",
        ],
      },
      {
        grupo: "Farmacoterapia",
        medicamentos: [
          "Vareniclina 0,5mg 1x/dia (1ª semana) → 1mg 2x/dia",
          "Bupropiona 150mg 1x/dia → 2x/dia",
        ],
      },
    ],
  },
  etilismo: {
    titulo: "Etilismo",
    grupos: [
      {
        grupo: "Redução do Craving / Abstinência",
        medicamentos: [
          "Naltrexona 50mg 1x/dia",
          "Acamprosato 666mg 3x/dia",
          "Dissulfiram 250mg 1x/dia (uso supervisionado)",
        ],
      },
      {
        grupo: "Suplementação",
        medicamentos: [
          "Tiamina (Vitamina B1) 300mg/dia VO",
          "Complexo B 1 comprimido 2x/dia",
          "Ácido fólico 5mg 1x/dia",
        ],
      },
      {
        grupo: "Controle de Abstinência Aguda",
        medicamentos: [
          "Diazepam 10mg VO (protocolo CIWA)",
          "Lorazepam 2mg VO (protocolo CIWA)",
        ],
      },
    ],
  },
  drogas: {
    titulo: "Uso de Drogas Ilícitas",
    grupos: [
      {
        grupo: "Opioides (Redução de Danos / TAO)",
        medicamentos: [
          "Metadona (dose conforme protocolo TAO)",
          "Buprenorfina/Naloxona 8/2mg sublingual",
        ],
      },
      {
        grupo: "Suporte Psiquiátrico",
        medicamentos: [
          "Quetiapina 25mg à noite (agitação/insônia)",
          "Haloperidol 5mg IM (crise aguda)",
          "Diazepam 10mg VO (abstinência)",
        ],
      },
    ],
  },
};

function ModalMedicamentos({ comorbidade, open, onClose, onConfirmar }) {
  const [selecionados, setSelecionados] = useState([]);
  const dados = MEDICAMENTOS_POR_COMORBIDADE[comorbidade?.id];

  const toggle = (med) =>
    setSelecionados((prev) =>
      prev.includes(med) ? prev.filter((m) => m !== med) : [...prev, med]
    );

  const handleConfirmar = () => {
    onConfirmar(selecionados);
    setSelecionados([]);
    onClose();
  };

  const handleClose = () => {
    setSelecionados([]);
    onClose();
  };

  if (!dados) return null;

  return (
    <Dialog open={open} onOpenChange={(v) => !v && handleClose()}>
      <DialogContent className="max-w-lg max-h-[80vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2 text-teal-700">
            <Pill className="w-5 h-5" />
            Medicamentos — {dados.titulo}
          </DialogTitle>
          <p className="text-sm text-gray-500 pt-1">
            Selecione os medicamentos que o paciente usa para adicionar ao campo de medicações.
          </p>
        </DialogHeader>

        <div className="space-y-4 py-2">
          {dados.grupos.map((g) => (
            <div key={g.grupo}>
              <Badge variant="secondary" className="mb-2 text-xs font-semibold">
                {g.grupo}
              </Badge>
              <div className="space-y-1 pl-1">
                {g.medicamentos.map((med) => (
                  <div key={med} className="flex items-center gap-2">
                    <Checkbox
                      id={`med-${med}`}
                      checked={selecionados.includes(med)}
                      onCheckedChange={() => toggle(med)}
                    />
                    <label
                      htmlFor={`med-${med}`}
                      className="text-sm text-gray-700 cursor-pointer select-none"
                    >
                      {med}
                    </label>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>

        <DialogFooter className="gap-2">
          <Button variant="outline" onClick={handleClose}>
            Fechar
          </Button>
          <Button
            onClick={handleConfirmar}
            disabled={selecionados.length === 0}
            className="bg-teal-600 hover:bg-teal-700 text-white"
          >
            Adicionar {selecionados.length > 0 ? `(${selecionados.length})` : ""} ao formulário
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

function CopyButton({ text, label }) {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <Button
      onClick={handleCopy}
      size="sm"
      className={`transition-all duration-300 ${
        copied
          ? "bg-gray-500 hover:bg-gray-600"
          : "bg-teal-600 hover:bg-teal-700"
      } text-white`}
    >
      {copied ? (
        <>
          <CheckCircle className="w-4 h-4 mr-1" />
          Copiado!
        </>
      ) : (
        <>
          <Copy className="w-4 h-4 mr-1" />
          {label || "Copiar"}
        </>
      )}
    </Button>
  );
}

function OutputCard({ icon: Icon, title, content, iconColor }) {
  if (!content) return null;
  return (
    <Card className="border border-gray-200 shadow-sm">
      <CardHeader className="pb-2 pt-4 px-4">
        <CardTitle className="text-base font-semibold flex items-center gap-2 text-gray-700">
          <Icon className={`w-5 h-5 ${iconColor}`} />
          {title}
        </CardTitle>
      </CardHeader>
      <CardContent className="px-4 pb-4">
        <Textarea
          value={content}
          readOnly
          rows={8}
          className="w-full font-mono text-sm bg-gray-50 resize-y"
        />
        <div className="mt-2 flex justify-end">
          <CopyButton text={content} />
        </div>
      </CardContent>
    </Card>
  );
}

export default function GeradorLaudo() {
  const hoje = new Date().toLocaleDateString("pt-BR");

  const [form, setForm] = useState({
    motivoPrincipal: "",
    motivoPersonalizado: "",
    motivoAssociado: "",
    procedimento: "",
    anamnese: "",
    exame: "",
    alergias: "",
    medicacoes: "",
    conduta: "",
    comorbidades: {},
  });

  const [outputs, setOutputs] = useState(null);
  const [modalComorbidade, setModalComorbidade] = useState(null);

  const set = (key, val) => setForm((prev) => ({ ...prev, [key]: val }));

  const toggleComorbidade = (id) => {
    const jaMarcada = !!form.comorbidades[id];

    setForm((prev) => {
      const next = { ...prev.comorbidades };
      if (id === "sem_comorbidades") {
        if (next[id]) {
          delete next[id];
        } else {
          return { ...prev, comorbidades: { sem_comorbidades: true } };
        }
      } else {
        if (next[id]) {
          delete next[id];
        } else {
          delete next["sem_comorbidades"];
          next[id] = true;
        }
      }
      return { ...prev, comorbidades: next };
    });

    // Abre modal ao marcar (não ao desmarcar), se houver medicamentos para essa comorbidade
    if (!jaMarcada && id !== "sem_comorbidades" && MEDICAMENTOS_POR_COMORBIDADE[id]) {
      setModalComorbidade(COMORBIDADES.find((c) => c.id === id));
    }
  };

  const adicionarMedicamentos = (lista) => {
    if (lista.length === 0) return;
    setForm((prev) => {
      const atual = prev.medicacoes.trim();
      const novo = lista.join("\n");
      return { ...prev, medicacoes: atual ? `${atual}\n${novo}` : novo };
    });
  };

  const comorbidadesText = () => {
    const selecionadas = COMORBIDADES.filter((c) => form.comorbidades[c.id]).map((c) => c.label);
    return selecionadas.length > 0 ? selecionadas.join(", ") : "Sem comorbidades conhecidas";
  };

  const motivoPrincipalText = () =>
    form.motivoPersonalizado || form.motivoPrincipal || "[motivo não informado]";

  const gerarLaudo = () => {
    const motivo = motivoPrincipalText();
    const associado = (form.motivoAssociado && form.motivoAssociado !== "none") ? `\nMotivo Associado: ${form.motivoAssociado}` : "";
    const procedimento = form.procedimento || "[procedimento não informado]";
    const anamnese = form.anamnese || "[anamnese não informada]";
    const exame = form.exame || "[exame físico não informado]";
    const comorbidades = comorbidadesText();
    const alergias = form.alergias || "Nega";
    const medicacoes = form.medicacoes || "Nega uso de medicações";
    const conduta = form.conduta || "[conduta não informada]";

    const laudo = `LAUDO DE CONSULTA CIRÚRGICA
Data: ${hoje}
Médico: Dr. Claudio M Orenstein — CRM-SP 58120

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MOTIVO DO ENCAMINHAMENTO
${motivo}${associado}

PROCEDIMENTO PROPOSTO
${procedimento}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANAMNESE / QUEIXA PRINCIPAL
${anamnese}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANTECEDENTES E COMORBIDADES
${comorbidades}

Alergias: ${alergias}
Medicações em uso: ${medicacoes}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXAME FÍSICO
${exame}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONDUTA / RECOMENDAÇÕES
${conduta}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dr. Claudio M Orenstein
CRM-SP 58120`;

    const preAnestesica = `SOLICITAÇÃO DE AVALIAÇÃO PRÉ-ANESTÉSICA
Data: ${hoje}

Encaminho paciente para avaliação pré-anestésica visando cirurgia eletiva.

Diagnóstico / Motivo: ${motivo}${associado ? `\n${associado}` : ""}
Procedimento Proposto: ${procedimento}

Comorbidades: ${comorbidades}
Alergias: ${alergias}
Medicações em uso: ${medicacoes}

${anamnese ? `Histórico Resumido:\n${anamnese}` : ""}

Solicito avaliação quanto ao risco anestésico-cirúrgico e liberação para o procedimento.

Dr. Claudio M Orenstein — CRM-SP 58120`;

    const cardiologia = `SOLICITAÇÃO DE AVALIAÇÃO CARDIOLÓGICA PRÉ-OPERATÓRIA
Data: ${hoje}

Encaminho paciente para avaliação cardiológica pré-operatória.

Diagnóstico: ${motivo}
Procedimento Proposto: ${procedimento}

Comorbidades: ${comorbidades}
Alergias: ${alergias}
Medicações em uso: ${medicacoes}

Solicito avaliação do risco cardiovascular e liberação para cirurgia eletiva.

Dr. Claudio M Orenstein — CRM-SP 58120`;

    const pneumologia = `SOLICITAÇÃO DE AVALIAÇÃO PNEUMOLÓGICA PRÉ-OPERATÓRIA
Data: ${hoje}

Encaminho paciente para avaliação pneumológica pré-operatória.

Diagnóstico: ${motivo}
Procedimento Proposto: ${procedimento}

Comorbidades: ${comorbidades}
Alergias: ${alergias}
Medicações em uso: ${medicacoes}

Solicito avaliação do risco respiratório e liberação para cirurgia eletiva.

Dr. Claudio M Orenstein — CRM-SP 58120`;

    const aih = `DADOS PARA AIH — Autorização de Internação Hospitalar
Data: ${hoje}

Diagnóstico Principal: ${motivo}${associado ? `\nDiagnóstico Secundário: ${associado}` : ""}
Procedimento Proposto: ${procedimento}

Comorbidades: ${comorbidades}
Medicações: ${medicacoes}
Alergias: ${alergias}

Conduta: ${conduta}

Médico Solicitante: Dr. Claudio M Orenstein
CRM-SP 58120`;

    setOutputs({ laudo, preAnestesica, cardiologia, pneumologia, aih });

    setTimeout(() => {
      document.getElementById("outputs-section")?.scrollIntoView({ behavior: "smooth" });
    }, 100);
  };

  const limpar = () => {
    setForm({
      motivoPrincipal: "",
      motivoPersonalizado: "",
      motivoAssociado: "",
      procedimento: "",
      anamnese: "",
      exame: "",
      alergias: "",
      medicacoes: "",
      conduta: "",
      comorbidades: {},
    });
    setOutputs(null);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 p-4 sm:p-8">
      <div className="max-w-4xl mx-auto space-y-6">
        {/* Header */}
        <div className="bg-gradient-to-r from-teal-600 to-cyan-700 rounded-2xl p-6 text-white shadow-lg">
          <div className="flex items-center justify-center gap-3 mb-2">
            <Stethoscope className="w-8 h-8" />
            <h1 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
              Gerador de Laudos — Cirurgia Eletiva
            </h1>
          </div>
          <p className="text-center text-sm opacity-90">
            Preencha os dados do paciente e gere laudos, avaliações e AIH automaticamente.
          </p>
        </div>

        {/* Formulário */}
        <Card className="shadow-xl">
          <CardHeader className="border-b pb-4">
            <CardTitle className="text-lg text-gray-800 flex items-center gap-2">
              <ClipboardList className="w-5 h-5 text-teal-600" />
              Dados do Encaminhamento
            </CardTitle>
          </CardHeader>
          <CardContent className="pt-6 space-y-6">
            {/* Motivo Principal */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="space-y-1">
                <Label>Motivo do Encaminhamento Principal *</Label>
                <Select
                  value={form.motivoPrincipal}
                  onValueChange={(v) => set("motivoPrincipal", v)}
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Selecione..." />
                  </SelectTrigger>
                  <SelectContent className="max-h-72">
                    {MOTIVOS_GRUPOS.map((g) => (
                      <SelectGroup key={g.grupo}>
                        <SelectLabel className="text-xs font-bold text-teal-700 bg-teal-50 px-2 py-1">
                          {g.grupo}
                        </SelectLabel>
                        {g.opcoes.map((m) => (
                          <SelectItem key={m} value={m}>
                            {m}
                          </SelectItem>
                        ))}
                      </SelectGroup>
                    ))}
                  </SelectContent>
                </Select>
              </div>
              <div className="space-y-1">
                <Label>Motivo Personalizado (sobrescreve o campo acima)</Label>
                <Input
                  placeholder="Ex: Hérnia de Spiegel direita..."
                  value={form.motivoPersonalizado}
                  onChange={(e) => set("motivoPersonalizado", e.target.value)}
                />
              </div>
            </div>

            {/* Motivo Associado */}
            <div className="space-y-1">
              <Label>Motivo Associado (Opcional)</Label>
              <Select
                value={form.motivoAssociado}
                onValueChange={(v) => set("motivoAssociado", v)}
              >
                <SelectTrigger>
                  <SelectValue placeholder="Selecione diagnóstico secundário..." />
                </SelectTrigger>
                <SelectContent className="max-h-72">
                  <SelectItem value="none">Nenhum</SelectItem>
                  {MOTIVOS_GRUPOS.map((g) => (
                    <SelectGroup key={g.grupo}>
                      <SelectLabel className="text-xs font-bold text-teal-700 bg-teal-50 px-2 py-1">
                        {g.grupo}
                      </SelectLabel>
                      {g.opcoes.map((m) => (
                        <SelectItem key={m} value={m}>
                          {m}
                        </SelectItem>
                      ))}
                    </SelectGroup>
                  ))}
                </SelectContent>
              </Select>
            </div>

            {/* Procedimento */}
            <div className="space-y-1">
              <Label>Procedimento Proposto</Label>
              <Input
                placeholder="Ex: Herniorrafia inguinal direita com tela (técnica de Lichtenstein)"
                value={form.procedimento}
                onChange={(e) => set("procedimento", e.target.value)}
              />
            </div>

            {/* Anamnese */}
            <div className="space-y-1">
              <Label>Anamnese / Queixa Principal</Label>
              <Textarea
                placeholder="Descreva a queixa principal e histórico clínico..."
                rows={4}
                value={form.anamnese}
                onChange={(e) => set("anamnese", e.target.value)}
              />
            </div>

            {/* Comorbidades */}
            <div className="space-y-2">
              <Label className="text-base font-semibold">Comorbidades</Label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 border rounded-lg p-4 bg-gray-50">
                {COMORBIDADES.map((c) => (
                  <div key={c.id} className="flex items-center gap-2">
                    <Checkbox
                      id={c.id}
                      checked={!!form.comorbidades[c.id]}
                      onCheckedChange={() => toggleComorbidade(c.id)}
                    />
                    <label
                      htmlFor={c.id}
                      className="text-sm text-gray-700 cursor-pointer select-none"
                    >
                      {c.label}
                    </label>
                  </div>
                ))}
              </div>
            </div>

            {/* Alergias + Medicações */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="space-y-1">
                <Label>Alergias Medicamentosas</Label>
                <Input
                  placeholder="Ex: Dipirona, Penicilina..."
                  value={form.alergias}
                  onChange={(e) => set("alergias", e.target.value)}
                />
              </div>
              <div className="space-y-1">
                <Label>Medicações em Uso</Label>
                <Textarea
                  placeholder="Ex: Losartana 50mg 1x/dia, Metformina 500mg 2x/dia..."
                  rows={3}
                  value={form.medicacoes}
                  onChange={(e) => set("medicacoes", e.target.value)}
                />
              </div>
            </div>

            {/* Exame Físico */}
            <div className="space-y-1">
              <Label>Exame Físico</Label>
              <Textarea
                placeholder="Descreva os achados do exame físico..."
                rows={4}
                value={form.exame}
                onChange={(e) => set("exame", e.target.value)}
              />
            </div>

            {/* Conduta */}
            <div className="space-y-1">
              <Label>Conduta / Recomendações</Label>
              <Textarea
                placeholder="Descreva a conduta proposta e orientações..."
                rows={3}
                value={form.conduta}
                onChange={(e) => set("conduta", e.target.value)}
              />
            </div>

            {/* Ações */}
            <div className="flex flex-wrap gap-3 pt-4 border-t">
              <Button
                onClick={gerarLaudo}
                className="bg-teal-600 hover:bg-teal-700 text-white font-bold px-6 py-3 shadow-md transition-all duration-300 hover:scale-105"
              >
                <FileText className="w-5 h-5 mr-2" />
                Gerar Laudo
              </Button>
              <Button
                onClick={limpar}
                variant="destructive"
                className="px-6 py-3 font-bold shadow-md"
              >
                <Trash2 className="w-5 h-5 mr-2" />
                Limpar Formulário
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* Outputs */}
        {outputs && (
          <div id="outputs-section" className="space-y-4">
            <h2 className="text-xl font-bold text-gray-800 border-b pb-2">
              Documentos Gerados
            </h2>

            <OutputCard
              icon={FileText}
              iconColor="text-teal-600"
              title="Laudo de Consulta Cirúrgica"
              content={outputs.laudo}
            />
            <OutputCard
              icon={Stethoscope}
              iconColor="text-purple-600"
              title="Solicitação Pré-Anestésica"
              content={outputs.preAnestesica}
            />
            <OutputCard
              icon={Heart}
              iconColor="text-red-500"
              title="Avaliação Cardiológica Pré-Operatória"
              content={outputs.cardiologia}
            />
            <OutputCard
              icon={Wind}
              iconColor="text-blue-500"
              title="Avaliação Pneumológica Pré-Operatória"
              content={outputs.pneumologia}
            />
            <OutputCard
              icon={ClipboardList}
              iconColor="text-amber-600"
              title="Dados para AIH"
              content={outputs.aih}
            />
          </div>
        )}
      </div>

      <ModalMedicamentos
        comorbidade={modalComorbidade}
        open={!!modalComorbidade}
        onClose={() => setModalComorbidade(null)}
        onConfirmar={adicionarMedicamentos}
      />
    </div>
  );
}
