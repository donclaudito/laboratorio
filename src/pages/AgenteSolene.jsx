import React from "react";
import { Sparkles } from "lucide-react";
import SoleneConversation from "@/components/agents/SoleneConversation";

export default function AgenteSolene() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-emerald-50 to-teal-50 p-4 sm:p-6">
      <div className="max-w-7xl mx-auto">
        <div className="bg-gradient-to-r from-emerald-500 to-teal-600 rounded-t-2xl p-6 text-white shadow-lg">
          <div className="flex items-center justify-center gap-3 mb-2">
            <Sparkles className="w-7 h-7" />
            <h1 className="text-2xl font-extrabold tracking-tight">Solene — Assistente de Solicitações</h1>
          </div>
          <p className="text-center text-sm opacity-90">
            Converse com a Solene para montar solicitações de exames, gerenciar pacientes e modelos.
          </p>
        </div>
        <div className="bg-white rounded-b-2xl shadow-lg p-3">
          <SoleneConversation />
        </div>
      </div>
    </div>
  );
}