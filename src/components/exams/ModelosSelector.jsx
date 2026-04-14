import React, { useState, useEffect } from "react";
import { base44 } from "@/api/base44Client";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card } from "@/components/ui/card";
import { BookOpen, Save, Trash2, ChevronDown, ChevronUp, CheckCircle } from "lucide-react";

export default function ModelosSelector({ selectedExams, onCarregarModelo }) {
  const [modelos, setModelos] = useState([]);
  const [showList, setShowList] = useState(false);
  const [showSaveForm, setShowSaveForm] = useState(false);
  const [nomeModelo, setNomeModelo] = useState("");
  const [descricaoModelo, setDescricaoModelo] = useState("");
  const [savedFeedback, setSavedFeedback] = useState(false);

  const carregar = async () => {
    const lista = await base44.entities.ModeloSolicitacao.list("-created_date", 50);
    setModelos(lista);
  };

  useEffect(() => { carregar(); }, []);

  const salvarModelo = async () => {
    if (!nomeModelo.trim()) return;
    const totalExames = Object.values(selectedExams).reduce((acc, section) => {
      return acc + Object.values(section).filter(Boolean).length;
    }, 0);
    if (totalExames === 0) return;

    await base44.entities.ModeloSolicitacao.create({
      nome: nomeModelo.trim(),
      descricao: descricaoModelo.trim() || undefined,
      exames: selectedExams
    });
    setNomeModelo("");
    setDescricaoModelo("");
    setShowSaveForm(false);
    setSavedFeedback(true);
    setTimeout(() => setSavedFeedback(false), 2000);
    await carregar();
  };

  const excluir = async (id, e) => {
    e.stopPropagation();
    await base44.entities.ModeloSolicitacao.delete(id);
    await carregar();
  };

  const contarExames = (exames) => {
    return Object.values(exames || {}).reduce((acc, section) => {
      return acc + Object.values(section).filter(Boolean).length;
    }, 0);
  };

  return (
    <div className="mb-6 border border-emerald-200 rounded-xl p-4 bg-emerald-50/30">
      <div className="flex items-center justify-between mb-2">
        <h2 className="text-lg font-bold text-gray-800 flex items-center gap-2">
          <BookOpen className="w-5 h-5 text-emerald-500" />
          Modelos de Solicitação
        </h2>
        <div className="flex gap-2">
          <Button
            size="sm"
            variant="outline"
            onClick={() => { setShowList(!showList); setShowSaveForm(false); }}
            className="text-xs border-emerald-400 text-emerald-600 hover:bg-emerald-50"
          >
            {showList ? <ChevronUp className="w-4 h-4 mr-1" /> : <ChevronDown className="w-4 h-4 mr-1" />}
            Carregar Modelo
          </Button>
          <Button
            size="sm"
            variant="outline"
            onClick={() => { setShowSaveForm(!showSaveForm); setShowList(false); }}
            className="text-xs border-emerald-400 text-emerald-600 hover:bg-emerald-50"
          >
            {savedFeedback ? (
              <><CheckCircle className="w-4 h-4 mr-1 text-green-500" /> Salvo!</>
            ) : (
              <><Save className="w-4 h-4 mr-1" /> Salvar Atual</>
            )}
          </Button>
        </div>
      </div>

      {/* Formulário de salvar */}
      {showSaveForm && (
        <Card className="p-4 mt-3 border-emerald-200 bg-white">
          <p className="text-xs text-gray-500 mb-3">
            Salva os exames atualmente selecionados como um modelo reutilizável.
          </p>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-3">
            <div>
              <Label className="text-xs text-gray-600 mb-1 block">Nome do modelo *</Label>
              <Input
                value={nomeModelo}
                onChange={e => setNomeModelo(e.target.value)}
                placeholder="Ex: Check-up Geral, Cardiológico..."
                className="text-sm"
              />
            </div>
            <div>
              <Label className="text-xs text-gray-600 mb-1 block">Descrição (opcional)</Label>
              <Input
                value={descricaoModelo}
                onChange={e => setDescricaoModelo(e.target.value)}
                placeholder="Ex: Rotina anual completa"
                className="text-sm"
              />
            </div>
          </div>
          <div className="flex gap-2">
            <Button size="sm" onClick={salvarModelo} className="bg-emerald-500 hover:bg-emerald-600 text-white">
              <Save className="w-4 h-4 mr-1" /> Salvar Modelo
            </Button>
            <Button size="sm" variant="outline" onClick={() => setShowSaveForm(false)}>Cancelar</Button>
          </div>
        </Card>
      )}

      {/* Lista de modelos */}
      {showList && (
        <Card className="mt-3 border-emerald-200 overflow-hidden">
          {modelos.length === 0 ? (
            <p className="text-sm text-gray-500 text-center py-4">Nenhum modelo salvo ainda.</p>
          ) : (
            <ul className="divide-y divide-gray-100 max-h-56 overflow-y-auto">
              {modelos.map(m => (
                <li
                  key={m.id}
                  onClick={() => { onCarregarModelo(m.exames); setShowList(false); }}
                  className="flex items-center justify-between px-4 py-3 cursor-pointer hover:bg-emerald-50 transition-colors"
                >
                  <div>
                    <p className="text-sm font-semibold text-gray-800">{m.nome}</p>
                    <p className="text-xs text-gray-400">
                      {m.descricao ? `${m.descricao} · ` : ""}
                      {contarExames(m.exames)} exame{contarExames(m.exames) !== 1 ? "s" : ""}
                    </p>
                  </div>
                  <button
                    onClick={(e) => excluir(m.id, e)}
                    className="text-gray-300 hover:text-red-400 transition-colors ml-3 shrink-0"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </li>
              ))}
            </ul>
          )}
        </Card>
      )}
    </div>
  );
}