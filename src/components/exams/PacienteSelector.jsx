import React, { useState, useEffect } from "react";
import { base44 } from "@/api/base44Client";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card } from "@/components/ui/card";
import { UserPlus, User, Trash2, ChevronDown, ChevronUp } from "lucide-react";

export default function PacienteSelector({ pacienteSelecionado, onSelecionarPaciente }) {
  const [pacientes, setPacientes] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [showList, setShowList] = useState(false);
  const [form, setForm] = useState({ nome: "", idade: "", paciente_id: "" });

  const carregar = async () => {
    const lista = await base44.entities.Paciente.list("-created_date", 100);
    setPacientes(lista);
  };

  useEffect(() => { carregar(); }, []);

  const salvar = async () => {
    if (!form.nome.trim()) return;
    const novo = await base44.entities.Paciente.create({
      nome: form.nome.trim(),
      idade: form.idade ? Number(form.idade) : undefined,
      paciente_id: form.paciente_id.trim() || undefined
    });
    setForm({ nome: "", idade: "", paciente_id: "" });
    setShowForm(false);
    await carregar();
    onSelecionarPaciente(novo);
  };

  const excluir = async (id, e) => {
    e.stopPropagation();
    await base44.entities.Paciente.delete(id);
    if (pacienteSelecionado?.id === id) onSelecionarPaciente(null);
    await carregar();
  };

  return (
    <div className="mb-6">
      <div className="flex items-center justify-between mb-2">
        <h2 className="text-lg font-bold text-gray-800 flex items-center gap-2">
          <User className="w-5 h-5 text-emerald-500" />
          Paciente
        </h2>
        <div className="flex gap-2">
          <Button
            size="sm"
            variant="outline"
            onClick={() => { setShowList(!showList); setShowForm(false); }}
            className="text-xs border-emerald-400 text-emerald-600 hover:bg-emerald-50"
          >
            {showList ? <ChevronUp className="w-4 h-4 mr-1" /> : <ChevronDown className="w-4 h-4 mr-1" />}
            Selecionar
          </Button>
          <Button
            size="sm"
            variant="outline"
            onClick={() => { setShowForm(!showForm); setShowList(false); }}
            className="text-xs border-emerald-400 text-emerald-600 hover:bg-emerald-50"
          >
            <UserPlus className="w-4 h-4 mr-1" />
            Novo
          </Button>
        </div>
      </div>

      {/* Paciente selecionado */}
      {pacienteSelecionado && (
        <div className="flex items-center gap-3 bg-emerald-50 border border-emerald-300 rounded-lg px-4 py-2 text-sm text-emerald-800">
          <User className="w-4 h-4 shrink-0" />
          <span className="font-semibold">{pacienteSelecionado.nome}</span>
          {pacienteSelecionado.idade && <span className="text-emerald-600">• {pacienteSelecionado.idade} anos</span>}
          {pacienteSelecionado.paciente_id && <span className="text-emerald-600">• ID: {pacienteSelecionado.paciente_id}</span>}
          <button onClick={() => onSelecionarPaciente(null)} className="ml-auto text-emerald-400 hover:text-red-400 transition-colors">✕</button>
        </div>
      )}

      {/* Formulário de novo paciente */}
      {showForm && (
        <Card className="p-4 mt-3 border-emerald-200 bg-emerald-50/40">
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-3">
            <div>
              <Label className="text-xs text-gray-600 mb-1 block">Nome *</Label>
              <Input
                value={form.nome}
                onChange={e => setForm({ ...form, nome: e.target.value })}
                placeholder="Nome completo"
                className="text-sm"
              />
            </div>
            <div>
              <Label className="text-xs text-gray-600 mb-1 block">Idade</Label>
              <Input
                type="number"
                value={form.idade}
                onChange={e => setForm({ ...form, idade: e.target.value })}
                placeholder="Ex: 45"
                className="text-sm"
              />
            </div>
            <div>
              <Label className="text-xs text-gray-600 mb-1 block">ID / Prontuário</Label>
              <Input
                value={form.paciente_id}
                onChange={e => setForm({ ...form, paciente_id: e.target.value })}
                placeholder="Ex: 00123"
                className="text-sm"
              />
            </div>
          </div>
          <div className="flex gap-2">
            <Button size="sm" onClick={salvar} className="bg-emerald-500 hover:bg-emerald-600 text-white">
              Salvar e Selecionar
            </Button>
            <Button size="sm" variant="outline" onClick={() => setShowForm(false)}>Cancelar</Button>
          </div>
        </Card>
      )}

      {/* Lista de pacientes */}
      {showList && (
        <Card className="mt-3 border-emerald-200 overflow-hidden">
          {pacientes.length === 0 ? (
            <p className="text-sm text-gray-500 text-center py-4">Nenhum paciente cadastrado.</p>
          ) : (
            <ul className="divide-y divide-gray-100 max-h-52 overflow-y-auto">
              {pacientes.map(p => (
                <li
                  key={p.id}
                  onClick={() => { onSelecionarPaciente(p); setShowList(false); }}
                  className={`flex items-center justify-between px-4 py-2.5 cursor-pointer hover:bg-emerald-50 transition-colors text-sm ${pacienteSelecionado?.id === p.id ? "bg-emerald-100 font-semibold" : ""}`}
                >
                  <div className="flex items-center gap-2">
                    <User className="w-4 h-4 text-emerald-400 shrink-0" />
                    <span>{p.nome}</span>
                    {p.idade && <span className="text-gray-400 text-xs">• {p.idade} anos</span>}
                    {p.paciente_id && <span className="text-gray-400 text-xs">• ID: {p.paciente_id}</span>}
                  </div>
                  <button
                    onClick={(e) => excluir(p.id, e)}
                    className="text-gray-300 hover:text-red-400 transition-colors ml-3"
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