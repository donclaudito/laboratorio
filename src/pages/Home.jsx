import React from "react";
import { Link } from "react-router-dom";
import { FileText } from "lucide-react";

export default function Home() {
  return (
    <div className="min-h-screen relative flex items-center justify-center">
      {/* Background image */}
      <div
        className="absolute inset-0 bg-cover bg-center bg-no-repeat"
        style={{
          backgroundImage: `url('https://media.base44.com/images/public/6911e9012f392441cc52fdec/5527ed94b_Gemini_Generated_Image_9bkksa9bkksa9bkk.png')`
        }}
      />
      {/* Overlay */}
      <div className="absolute inset-0 bg-white/50 backdrop-blur-[2px]" />

      {/* Content */}
      <div className="relative z-10 text-center px-6">
        <div className="mb-6 flex justify-center">
          <div className="bg-emerald-500 p-4 rounded-full shadow-xl">
            <FileText className="w-12 h-12 text-white" />
          </div>
        </div>
        <h1 className="text-4xl sm:text-5xl font-extrabold text-gray-800 mb-3 tracking-tight drop-shadow">
          Dr. Claudio M Orenstein
        </h1>
        <p className="text-lg text-gray-600 mb-2 font-medium">CRM-SP 58120</p>
        <p className="text-gray-500 mb-10 max-w-md mx-auto">
          Sistema de geração de solicitações de exames médicos
        </p>
        <Link
          to="/SolicitacaoExames"
          className="inline-flex items-center gap-3 bg-emerald-500 hover:bg-emerald-600 text-white font-bold px-8 py-4 rounded-xl shadow-lg text-lg transition-all duration-300 hover:scale-105"
        >
          <FileText className="w-6 h-6" />
          Gerar Solicitação de Exames
        </Link>
      </div>
    </div>
  );
}