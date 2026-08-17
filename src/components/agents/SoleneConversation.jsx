import React, { useState, useEffect, useRef } from "react";
import { base44 } from "@/api/base44Client";
import { Send, Sparkles, Trash2, Loader2, Pencil, Check, X } from "lucide-react";
import MessageBubble from "./MessageBubble";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Copy, CheckCircle, Download, Printer } from "lucide-react";
import { gerarPDF, imprimirPDF } from "@/components/exams/PdfGenerator";

export default function SoleneConversation() {
  const [conversations, setConversations] = useState([]);
  const [currentConversation, setCurrentConversation] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [loadingConvs, setLoadingConvs] = useState(true);
  const [copySuccess, setCopySuccess] = useState(false);
  const messagesEndRef = useRef(null);
  const AGENT_NAME = "solene";
  const RENAMES_KEY = "solene_renames";
  const [editingId, setEditingId] = useState(null);
  const [editingName, setEditingName] = useState("");
  const editInputRef = useRef(null);

  const [renames, setRenames] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem(RENAMES_KEY) || "{}");
    } catch {
      return {};
    }
  });

  const persistRenames = (next) => {
    setRenames(next);
    try {
      localStorage.setItem(RENAMES_KEY, JSON.stringify(next));
    } catch {}
  };

  const displayName = (conv) => renames[conv.id] || conv.metadata?.name || "Conversa";

  useEffect(() => {
    loadConversations();
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const loadConversations = async () => {
    try {
      const convs = await base44.agents.listConversations({ agent_name: AGENT_NAME });
      setConversations(convs || []);
    } catch (e) {
      setConversations([]);
    } finally {
      setLoadingConvs(false);
    }
  };

  const startNewConversation = async () => {
    setLoading(true);
    try {
      const conv = await base44.agents.createConversation({
        agent_name: AGENT_NAME,
        metadata: { name: "Nova conversa", description: "Conversa com a Solene" },
      });
      setCurrentConversation(conv);
      setMessages(conv.messages || []);
      setConversations((prev) => [conv, ...prev]);
    } finally {
      setLoading(false);
    }
  };

  const selectConversation = async (conv) => {
    const full = await base44.agents.getConversation(conv.id);
    setCurrentConversation(full);
    setMessages(full.messages || []);
  };

  const sendMessage = async () => {
    if (!input.trim() || !currentConversation) return;
    const content = input.trim();
    setInput("");
    setMessages((prev) => [...prev, { role: "user", content }]);
    setLoading(true);
    try {
      await base44.agents.addMessage(currentConversation, { role: "user", content });
    } catch (e) {
      setMessages((prev) => [...prev, { role: "assistant", content: "Erro ao enviar mensagem." }]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (!currentConversation) return;
    const unsubscribe = base44.agents.subscribeToConversation(currentConversation.id, (data) => {
      setMessages(data.messages || []);
    });
    return () => unsubscribe();
  }, [currentConversation]);

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const deleteConversation = async (convId, e) => {
    e.stopPropagation();
    try {
      await base44.agents.deleteConversation?.(convId);
      setConversations((prev) => prev.filter((c) => c.id !== convId));
      if (currentConversation?.id === convId) {
        setCurrentConversation(null);
        setMessages([]);
      }
    } catch (e) {}
  };

  const startRename = (conv, e) => {
    e.stopPropagation();
    setEditingId(conv.id);
    setEditingName(displayName(conv));
    setTimeout(() => editInputRef.current?.select(), 0);
  };

  const cancelRename = () => {
    setEditingId(null);
    setEditingName("");
  };

  const commitRename = (conv) => {
    const nome = editingName.trim();
    setEditingId(null);
    setEditingName("");
    if (!nome || nome === displayName(conv)) return;
    persistRenames({ ...renames, [conv.id]: nome });
    setConversations((prev) => prev.map((c) => c.id === conv.id ? { ...c, metadata: { ...c.metadata, name: nome } } : c));
    if (currentConversation?.id === conv.id) {
      setCurrentConversation((prev) => prev ? { ...prev, metadata: { ...prev.metadata, name: nome } } : prev);
    }
  };

  const lastAssistantMarkdown = [...messages].reverse().find((m) => m.role === "assistant" && m.content)?.content || "";

  const copiarUltimo = () => {
    navigator.clipboard.writeText(lastAssistantMarkdown);
    setCopySuccess(true);
    setTimeout(() => setCopySuccess(false), 2000);
  };

  const extractSolicitacao = () => {
    if (!lastAssistantMarkdown) return "";
    const start = lastAssistantMarkdown.indexOf("# SOLICITAÇÃO");
    if (start === -1) return lastAssistantMarkdown;
    const end = lastAssistantMarkdown.indexOf("---", start + 5);
    return lastAssistantMarkdown.slice(start);
  };

  const solicitacaoDoc = extractSolicitacao();

  return (
    <div className="grid grid-cols-1 lg:grid-cols-[280px_1fr] gap-4 h-[calc(100vh-3rem)]">
      {/* Sidebar: conversations */}
      <div className="bg-white border rounded-xl shadow-sm p-3 flex flex-col">
        <Button
          onClick={startNewConversation}
          disabled={loading}
          className="w-full bg-emerald-500 hover:bg-emerald-600 text-white mb-3"
        >
          <Sparkles className="w-4 h-4 mr-2" />
          Nova conversa
        </Button>
        <div className="flex-1 overflow-y-auto space-y-1">
          {loadingConvs ? (
            <div className="flex justify-center py-6">
              <Loader2 className="w-5 h-5 animate-spin text-muted-foreground" />
            </div>
          ) : conversations.length === 0 ? (
            <p className="text-xs text-muted-foreground text-center py-6">
              Nenhuma conversa ainda.
            </p>
          ) : (
            conversations.map((conv) => (
              <div
                key={conv.id}
                onClick={() => selectConversation(conv)}
                className={`group flex items-center justify-between px-3 py-2 rounded-lg cursor-pointer text-sm hover:bg-muted/60 transition-colors ${
                  currentConversation?.id === conv.id ? "bg-emerald-50 border border-emerald-200" : ""
                }`}
              >
                {editingId === conv.id ? (
                  <div className="flex items-center gap-1 w-full">
                    <input
                      ref={editInputRef}
                      value={editingName}
                      onChange={(e) => setEditingName(e.target.value)}
                      onClick={(e) => e.stopPropagation()}
                      onKeyDown={(e) => {
                        if (e.key === "Enter") { e.preventDefault(); commitRename(conv); }
                        if (e.key === "Escape") { e.preventDefault(); cancelRename(); }
                      }}
                      className="flex-1 min-w-0 text-sm px-1.5 py-0.5 rounded border border-emerald-300 focus:outline-none focus:ring-1 focus:ring-emerald-400"
                      placeholder="Nome da conversa"
                    />
                    <button
                      onClick={(e) => { e.stopPropagation(); commitRename(conv); }}
                      className="text-emerald-600 hover:text-emerald-700"
                      title="Salvar"
                    >
                      <Check className="w-3.5 h-3.5" />
                    </button>
                    <button
                      onClick={(e) => { e.stopPropagation(); cancelRename(); }}
                      className="text-gray-400 hover:text-gray-600"
                      title="Cancelar"
                    >
                      <X className="w-3.5 h-3.5" />
                    </button>
                  </div>
                ) : (
                  <>
                    <span className="truncate">{displayName(conv)}</span>
                    <div className="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                      <button
                        onClick={(e) => startRename(conv, e)}
                        className="text-emerald-500 hover:text-emerald-700"
                        title="Renomear"
                      >
                        <Pencil className="w-3.5 h-3.5" />
                      </button>
                      <button
                        onClick={(e) => deleteConversation(conv.id, e)}
                        className="text-red-400 hover:text-red-600"
                        title="Excluir"
                      >
                        <Trash2 className="w-3.5 h-3.5" />
                      </button>
                    </div>
                  </>
                )}
              </div>
            ))
          )}
        </div>
      </div>

      {/* Main: chat */}
      <div className="flex flex-col bg-white border rounded-xl shadow-sm overflow-hidden">
        {!currentConversation ? (
          <div className="flex-1 flex flex-col items-center justify-center text-center p-8">
            <div className="w-16 h-16 rounded-full bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center text-white text-2xl font-bold mb-4">
              S
            </div>
            <h2 className="text-xl font-bold text-gray-800 mb-2">Solene</h2>
            <p className="text-sm text-muted-foreground max-w-md mb-6">
              Assistente de IA para montar solicitações de exames. Descreva o quadro clínico e ela sugere os exames, gerencia pacientes e gera o documento.
            </p>
            <Button onClick={startNewConversation} className="bg-emerald-500 hover:bg-emerald-600 text-white">
              <Sparkles className="w-4 h-4 mr-2" />
              Iniciar conversa
            </Button>
          </div>
        ) : (
          <>
            <div className="flex-1 overflow-y-auto p-4 space-y-3 bg-gradient-to-b from-gray-50 to-white">
              {messages.length === 0 && (
                <div className="text-center text-sm text-muted-foreground py-10">
                  Descreva o quadro clínico do paciente e a Solene sugerirá os exames adequados.
                </div>
              )}
              {messages.map((m, idx) => (
                <MessageBubble key={idx} message={m} />
              ))}
              {loading && (
                <div className="flex justify-start">
                  <div className="bg-white border shadow-sm rounded-2xl px-4 py-3 flex items-center gap-2">
                    <Loader2 className="w-4 h-4 animate-spin text-emerald-500" />
                    <span className="text-sm text-muted-foreground">Solene está pensando…</span>
                  </div>
                </div>
              )}
              <div ref={messagesEndRef} />
            </div>

            {solicitacaoDoc && (
              <div className="px-4 pt-2 flex flex-wrap gap-2 border-t bg-white">
                <Button size="sm" variant="outline" onClick={copiarUltimo} className="text-xs">
                  {copySuccess ? <CheckCircle className="w-3.5 h-3.5 mr-1" /> : <Copy className="w-3.5 h-3.5 mr-1" />}
                  {copySuccess ? "Copiado!" : "Copiar solicitação"}
                </Button>
                <Button size="sm" variant="outline" onClick={() => gerarPDF(solicitacaoDoc, null)} className="text-xs">
                  <Download className="w-3.5 h-3.5 mr-1" />
                  Exportar PDF
                </Button>
                <Button size="sm" variant="outline" onClick={() => imprimirPDF(solicitacaoDoc, null)} className="text-xs">
                  <Printer className="w-3.5 h-3.5 mr-1" />
                  Imprimir
                </Button>
              </div>
            )}

            <div className="p-3 border-t bg-white">
              <div className="flex gap-2 items-end">
                <Textarea
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyDown={handleKeyDown}
                  placeholder="Descreva o quadro clínico ou peça uma sugestão de exames…"
                  rows={2}
                  className="resize-none text-sm"
                />
                <Button
                  onClick={sendMessage}
                  disabled={!input.trim() || loading}
                  className="bg-emerald-500 hover:bg-emerald-600 text-white"
                >
                  <Send className="w-4 h-4" />
                </Button>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
}