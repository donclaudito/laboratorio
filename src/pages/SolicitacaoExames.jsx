import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { FileText, Copy, Trash2, CheckCircle, Download, Printer } from "lucide-react";
import ExamSection from "../components/exams/ExamSection";
import ExamesMetabolicosPanel from "../components/exams/ExamesMetabolicosPanel";
import ExamesRenalHepaticaPanel from "../components/exams/ExamesRenalHepaticaPanel";
import ExamesGeralHormonalPanel from "../components/exams/ExamesGeralHormonalPanel";
import ExamesUrinaFezesPanel from "../components/exams/ExamesUrinaFezesPanel";
import ExamesPreOperatoriosPanel from "../components/exams/ExamesPreOperatoriosPanel";
import PacienteSelector from "../components/exams/PacienteSelector";
import ModelosSelector from "../components/exams/ModelosSelector";
import { gerarPDF, imprimirPDF } from "../components/exams/PdfGenerator";

export default function SolicitacaoExames() {
  const [selectedExams, setSelectedExams] = useState({});
  const [resultado, setResultado] = useState("");
  const [showResult, setShowResult] = useState(false);
  const [copySuccess, setCopySuccess] = useState(false);
  const [pacienteSelecionado, setPacienteSelecionado] = useState(null);

  // Dados das seções de exames (seções 1-4 tratadas como painéis separados)
  const examSections = [
    {
      id: "exames_complementares",
      title: "6. Exames Complementares (Imagiológicos e Gráficos)",
      exams: [
        "Eletrocardiograma (ECG)",
        "Raio-X de Tórax (se indicado)"
      ]
    },
    {
      id: "ultrassom",
      title: "7. Ultrassom (Imagiologia)",
      exams: [
        "Ultrassom Abdominal Total",
        "Ultrassom de Vias Urinárias",
        "Ultrassom de Tireoide",
        "Ultrassom Transvaginal (Feminino)",
        "Ultrassom de Próstata (Masculino)",
        "Ultrassom de Mamas",
        "USG com Doppler Venoso de Membros Inferiores",
        "USG com Doppler Arterial de Membros Inferiores",
        "Ultrassom de Parede Abdominal (Hérnia)",
        "Ultrassom de Partes Moles (Região Específica)",
        "Ultrassom de Bolsa Escrotal/Testicular",
        "Ultrassom Transretal",
        "Ultrassom com Doppler de Carótidas e Vertebrais",
        "Ultrassom para Mapeamento de Hérnia Inguinal",
        "Ultrassom para Mapeamento de Hérnia Umbilical",
        "Ultrassom para Mapeamento de Hérnia Incisional",
        "Ultrassom para Mapeamento de Hérnia Epigástrica",
        "Ultrassom de Hérnia de Spigel",
        "Ultrassom de Hérnia Obturadora",
        "Ultrassom Dinâmico de Parede Abdominal (Manobra de Valsalva)"
      ]
    },
    {
      id: "tomografia",
      title: "8. Tomografia Computadorizada (TC) - Protocolos",
      radioGroups: [
        {
          name: "tc_cranio",
          label: "TC de Crânio:",
          options: [
            "TC de Crânio (Sem Contraste)",
            "TC de Crânio (Com Contraste)"
          ]
        },
        {
          name: "tc_torax",
          label: "TC de Tórax:",
          options: [
            "TC de Tórax (Sem Contraste)",
            "TC de Tórax (Com Contraste)"
          ]
        },
        {
          name: "tc_abdomen",
          label: "TC de Abdômen:",
          options: [
            "TC de Abdômen (Sem Contraste)",
            "TC de Abdômen (Com Contraste)",
            "TC de Abdômen e Pelve (Com Contraste)"
          ]
        },
        {
          name: "tc_coluna",
          label: "TC de Coluna:",
          options: [
            "TC de Coluna (Segmento Específico - Sem Contraste)",
            "TC de Coluna (Segmento Específico - Com Contraste)"
          ]
        }
      ],
      exams: [
        "Angiotomografia de Artérias Pulmonares (Angio-TC de Tórax)",
        "Angiotomografia de Aorta (Abdominal ou Torácica)"
      ]
    },
    {
      id: "ressonancia",
      title: "9. Ressonância Magnética (RM) - Protocolos",
      radioGroups: [
        {
          name: "rm_cranio",
          label: "RM de Crânio (Encéfalo):",
          options: [
            "RM de Crânio (Sem Contraste)",
            "RM de Crânio (Com Contraste)"
          ]
        },
        {
          name: "rm_abdomen",
          label: "RM de Abdômen:",
          options: [
            "RM de Abdômen Superior (Sem Contraste)",
            "RM de Abdômen Superior (Com Contraste)",
            "Colangiorressonância (RM de Vias Biliares)",
            "RM de Pelve/Retal (Com Contraste e Protocolo para Fístula/Endometriose)"
          ]
        },
        {
          name: "rm_coluna",
          label: "RM de Coluna:",
          options: [
            "RM de Coluna (Segmento Específico - Sem Contraste)",
            "RM de Coluna (Segmento Específico - Com Contraste)"
          ]
        }
      ]
    },
    {
      id: "endoscopia_colonoscopia",
      title: "10. Endoscopia e Colonoscopia",
      exams: [
        "Endoscopia Digestiva Alta (EDA)",
        "Endoscopia Digestiva Alta com Biópsia e/ou Teste de Urease",
        "Colonoscopia",
        "Colonoscopia com Polipectomia (Se necessário)",
        "Retossigmoidoscopia Flexível",
        "Cápsula Endoscópica (Investigação de Intestino Delgado)",
        "CPRE (Colangiopancreatografia Retrógrada Endoscópica)",
        "Ecoendoscopia (USG Endoscópico) - Alta",
        "Ecoendoscopia (USG Endoscópico) - Baixa/Retal",
        "PHmetria Esofágica de 24h"
      ]
    }
  ];

  const handleExamChange = (sectionId, examName, checked) => {
    setSelectedExams(prev => ({
      ...prev,
      [sectionId]: {
        ...prev[sectionId],
        [examName]: checked
      }
    }));
  };

  const handleSectionToggle = (sectionId, exams, radioGroups) => {
    const currentSection = selectedExams[sectionId] || {};
    const allChecked = exams?.every(exam => currentSection[exam]) && 
                       (!radioGroups || radioGroups.every(group => 
                         group.options.some(opt => currentSection[opt])
                       ));
    
    const newState = {};
    exams?.forEach(exam => {
      newState[exam] = !allChecked;
    });

    setSelectedExams(prev => ({
      ...prev,
      [sectionId]: newState
    }));
  };

  const gerarSolicitacao = () => {
    const hoje = new Date().toLocaleDateString('pt-BR');
    let pacienteInfo = pacienteSelecionado ? `\n**Paciente:** ${pacienteSelecionado.nome}${pacienteSelecionado.idade ? ` | ${pacienteSelecionado.idade} anos` : ""}${pacienteSelecionado.paciente_id ? ` | ID: ${pacienteSelecionado.paciente_id}` : ""}` : "";
    let resultado = `# SOLICITAÇÃO DE EXAMES\n\n**Médico Solicitante:** Dr Claudio M Orenstein CREMSP 58120\n**Data da Solicitação:** ${hoje}${pacienteInfo}\n\n---\n`;
    
    let examesSelecionados = 0;

    const stripPrefix = (name) => {
      const match = name.match(/^(\d+\.\s)(.*)/);
      return match ? match[2] : name;
    };

    // Seções dos painéis de colunas (1-5)
    const painelSections = [
      { id: "metabolica", title: "1. Avaliação Metabólica e Cardiovascular (Sangue)" },
      { id: "renal_hepatica", title: "2. Função Renal, Hepática e Pancreática (Sangue)" },
      { id: "geral_hormonal", title: "3. Avaliação Geral, Hemato e Hormonal (Sangue)" },
      { id: "urina_fezes", title: "4. Urina e Fezes" },
      { id: "pre_operatorios", title: "5. Pré-Operatórios (Laboratoriais)" },
    ];

    // Todas as seções em ordem
    const todasSecoes = [
      ...painelSections,
      ...examSections.map(s => ({ id: s.id, title: s.title }))
    ];

    todasSecoes.forEach(section => {
      const sectionExams = selectedExams[section.id] || {};
      const examsForSection = Object.entries(sectionExams).filter(([_, checked]) => checked);

      if (examsForSection.length > 0) {
        examesSelecionados += examsForSection.length;
        resultado += "\n";
        const cleanSectionName = stripPrefix(section.title);
        resultado += `### ${cleanSectionName}\n`;

        examsForSection.forEach(([examName]) => {
          resultado += `- [x] ${examName}\n`;
        });
      }
    });

    if (examesSelecionados === 0) {
      resultado += "Nenhum exame foi selecionado.\n";
    } else {
      resultado += `\n---\n\n## ORIENTAÇÕES IMPORTANTES\n\n* **Preparo:** Consultar o laboratório sobre jejum e demais preparos específicos.\n* **TC/RM com Contraste:** Para exames com contraste, é obrigatório apresentar exames de função renal (Creatinina) recentes.\n* **Exames de Imagem:** Para exames de imagem, o paciente deve levar exames anteriores relevantes.\n`;
    }

    setResultado(resultado);
    setShowResult(true);
    setTimeout(() => {
      document.getElementById('resultado-area')?.scrollIntoView({ behavior: 'smooth' });
    }, 100);
  };

  const copiarResultado = () => {
    navigator.clipboard.writeText(resultado);
    setCopySuccess(true);
    setTimeout(() => setCopySuccess(false), 2000);
  };

  const limparSelecao = () => {
    setSelectedExams({});
    setResultado("");
    setShowResult(false);
    setCopySuccess(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 p-4 sm:p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="bg-gradient-to-r from-emerald-500 to-teal-600 rounded-t-2xl p-6 text-white shadow-lg mb-0">
          <div className="flex items-center justify-center gap-3 mb-2">
            <FileText className="w-8 h-8" />
            <h1 className="text-3xl font-extrabold tracking-tight">
              Gerador de Solicitação de Exames
            </h1>
          </div>
          <p className="text-center text-sm opacity-90">
            Selecione os exames e gere o documento final em Markdown.
          </p>
        </div>

        {/* Formulário */}
        <Card className="shadow-xl rounded-t-none rounded-b-2xl p-6 sm:p-8">
          <PacienteSelector
            pacienteSelecionado={pacienteSelecionado}
            onSelecionarPaciente={setPacienteSelecionado}
          />

          <ModelosSelector
            selectedExams={selectedExams}
            onCarregarModelo={setSelectedExams}
          />

          <h2 className="text-xl font-bold mb-4 text-gray-800 border-b pb-2">
            Selecione os Exames
          </h2>

          <div className="space-y-6">
            {/* Seção Metabólica em 3 colunas */}
            <div>
              <h3 className="text-base font-semibold text-gray-700 mb-3">
                1. Avaliação Metabólica e Cardiovascular (Sangue)
              </h3>
              <ExamesMetabolicosPanel
                selectedExams={selectedExams["metabolica"] || {}}
                onExamChange={handleExamChange}
              />
            </div>

            {/* Seção Renal/Hepática em 3 colunas */}
            <div>
              <h3 className="text-base font-semibold text-gray-700 mb-3">
                2. Função Renal, Hepática e Pancreática (Sangue)
              </h3>
              <ExamesRenalHepaticaPanel
                selectedExams={selectedExams["renal_hepatica"] || {}}
                onExamChange={handleExamChange}
              />
            </div>

            {/* Seção Geral/Hemato/Hormonal em 3 colunas */}
            <div>
              <h3 className="text-base font-semibold text-gray-700 mb-3">
                3. Avaliação Geral, Hemato e Hormonal (Sangue)
              </h3>
              <ExamesGeralHormonalPanel
                selectedExams={selectedExams["geral_hormonal"] || {}}
                onExamChange={handleExamChange}
              />
            </div>

            {/* Seção Urina e Fezes em 3 colunas */}
            <div>
              <h3 className="text-base font-semibold text-gray-700 mb-3">
                4. Urina e Fezes
              </h3>
              <ExamesUrinaFezesPanel
                selectedExams={selectedExams["urina_fezes"] || {}}
                onExamChange={handleExamChange}
              />
            </div>

            {/* Seção Pré-Operatórios em 3 colunas */}
            <div>
              <h3 className="text-base font-semibold text-gray-700 mb-3">
                5. Pré-Operatórios (Laboratoriais)
              </h3>
              <ExamesPreOperatoriosPanel
                selectedExams={selectedExams["pre_operatorios"] || {}}
                onExamChange={handleExamChange}
              />
            </div>

            {examSections.map(section => (
              <ExamSection
                key={section.id}
                section={section}
                selectedExams={selectedExams[section.id] || {}}
                onExamChange={handleExamChange}
                onSectionToggle={handleSectionToggle}
              />
            ))}
          </div>

          {/* Botões de Ação */}
          <div className="flex flex-wrap gap-4 pt-6 border-t border-gray-200 mt-6">
            <Button
              onClick={gerarSolicitacao}
              className="bg-emerald-500 hover:bg-emerald-600 text-white font-bold px-6 py-3 shadow-md transition-all duration-300 hover:scale-105"
            >
              <FileText className="w-5 h-5 mr-2" />
              Gerar Solicitação
            </Button>
            <Button
              onClick={limparSelecao}
              variant="destructive"
              className="px-6 py-3 font-bold shadow-md transition-all duration-300"
            >
              <Trash2 className="w-5 h-5 mr-2" />
              Limpar Seleção
            </Button>
          </div>

          {/* Área de Resultado */}
          {showResult && (
            <div className="mt-8" id="resultado-area">
              <h2 className="text-xl font-bold mb-4 text-gray-800 border-b pb-2">
                Resultado da Solicitação (Markdown)
              </h2>
              <Textarea
                value={resultado}
                readOnly
                rows={15}
                className="w-full p-4 border border-gray-300 rounded-lg bg-gray-50 text-gray-800 font-mono text-sm shadow-inner"
              />
              <div className="flex flex-wrap gap-3 mt-4">
                <Button
                  onClick={copiarResultado}
                  className={`px-6 py-3 font-bold shadow-md transition-all duration-300 ${
                    copySuccess
                      ? "bg-gray-500 hover:bg-gray-600"
                      : "bg-emerald-500 hover:bg-emerald-600"
                  }`}
                >
                  {copySuccess ? (
                    <>
                      <CheckCircle className="w-5 h-5 mr-2" />
                      Copiado!
                    </>
                  ) : (
                    <>
                      <Copy className="w-5 h-5 mr-2" />
                      Copiar Resultado
                    </>
                  )}
                </Button>
                <Button
                  onClick={() => gerarPDF(resultado, pacienteSelecionado)}
                  className="bg-teal-600 hover:bg-teal-700 text-white px-6 py-3 font-bold shadow-md transition-all duration-300 hover:scale-105"
                >
                  <Download className="w-5 h-5 mr-2" />
                  Exportar PDF
                </Button>
                <Button
                  onClick={() => imprimirPDF(resultado, pacienteSelecionado)}
                  className="bg-gray-700 hover:bg-gray-800 text-white px-6 py-3 font-bold shadow-md transition-all duration-300 hover:scale-105"
                >
                  <Printer className="w-5 h-5 mr-2" />
                  Imprimir
                </Button>
              </div>
            </div>
          )}
        </Card>
      </div>
    </div>
  );
}