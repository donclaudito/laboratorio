import React, { useState } from "react";
import ReactMarkdown from "react-markdown";
import { ChevronDown, ChevronRight, Loader2, CheckCircle2, XCircle, Wrench } from "lucide-react";

function FunctionDisplay({ toolCall }) {
  const [expanded, setExpanded] = useState(false);
  const status = toolCall.status || "pending";
  const proj = toolCall.display_projection || {};
  const hideDetails = proj.hide_details && proj.details_redacted;

  let parsedResults = null;
  try {
    parsedResults = typeof toolCall.results === "string" ? JSON.parse(toolCall.results) : toolCall.results;
  } catch {
    parsedResults = toolCall.results;
  }
  const failed =
    status === "failed" || status === "error" ||
    (typeof parsedResults === "object" && parsedResults && parsedResults.success === false) ||
    /error|failed/i.test(typeof toolCall.results === "string" ? toolCall.results : "");

  let StatusIcon = Loader2;
  let statusText = "Executando…";
  let iconClass = "text-amber-500 animate-spin";
  if (status === "success" || status === "completed") {
    StatusIcon = failed ? XCircle : CheckCircle2;
    statusText = failed ? "Falhou" : "Concluído";
    iconClass = failed ? "text-red-500" : "text-emerald-500";
  } else if (status === "failed" || status === "error") {
    StatusIcon = XCircle;
    statusText = "Falhou";
    iconClass = "text-red-500";
  }

  const activeLabel = proj.active_label || statusText;
  const label = proj.label || toolCall.name || "ferramenta";
  const errorLabel = proj.error_label || "Falhou";

  if (hideDetails) {
    return (
      <div className="mt-2 text-xs flex items-center gap-1.5 text-muted-foreground">
        <StatusIcon className={`w-3.5 h-3.5 ${iconClass}`} />
        <span className="font-medium">{label}</span>
        <span className="opacity-70">— {failed ? errorLabel : activeLabel}</span>
      </div>
    );
  }

  let parsedArgs = null;
  try {
    parsedArgs = toolCall.arguments_string ? JSON.parse(toolCall.arguments_string) : {};
  } catch {
    parsedArgs = toolCall.arguments_string;
  }

  return (
    <div className="mt-2 text-xs border rounded-lg bg-muted/40 overflow-hidden">
      <button
        type="button"
        onClick={() => setExpanded(!expanded)}
        className="w-full flex items-center gap-1.5 px-3 py-2 hover:bg-muted/60 transition-colors"
      >
        {expanded ? <ChevronDown className="w-3.5 h-3.5" /> : <ChevronRight className="w-3.5 h-3.5" />}
        <Wrench className="w-3.5 h-3.5 text-muted-foreground" />
        <span className="font-medium">{label}</span>
        <span className="opacity-70">— {statusText}</span>
        <StatusIcon className={`w-3.5 h-3.5 ml-auto ${iconClass}`} />
      </button>
      {expanded && (
        <div className="px-3 pb-3 space-y-2">
          {parsedArgs !== null && (
            <div>
              <div className="font-semibold text-muted-foreground mb-1">Parâmetros:</div>
              <pre className="bg-background border rounded p-2 text-[11px] overflow-x-auto whitespace-pre-wrap break-words">
                {JSON.stringify(parsedArgs, null, 2)}
              </pre>
            </div>
          )}
          {parsedResults !== null && parsedResults !== undefined && (
            <div>
              <div className="font-semibold text-muted-foreground mb-1">Resultado:</div>
              <pre className={`bg-background border rounded p-2 text-[11px] overflow-x-auto whitespace-pre-wrap break-words ${failed ? "border-red-300" : ""}`}>
                {typeof parsedResults === "object" ? JSON.stringify(parsedResults, null, 2) : String(parsedResults)}
              </pre>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default function MessageBubble({ message }) {
  const isUser = message.role === "user";
  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div className={`max-w-[85%] rounded-2xl px-4 py-3 ${isUser ? "bg-emerald-500 text-white" : "bg-white border shadow-sm"}`}>
        {!isUser && (
          <div className="flex items-center gap-2 mb-1">
            <div className="w-7 h-7 rounded-full bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center text-white text-xs font-bold">
              S
            </div>
            <span className="text-xs font-semibold text-gray-600">Solene</span>
          </div>
        )}
        {message.content && (
          isUser ? (
            <p className="whitespace-pre-wrap leading-relaxed">{message.content}</p>
          ) : (
            <div className="prose prose-sm max-w-none prose-p:my-1 prose-ul:my-1 prose-li:my-0 prose-headings:mb-1 prose-headings:mt-2 prose-code:bg-gray-100 prose-code:px-1 prose-code:rounded">
              <ReactMarkdown>{message.content}</ReactMarkdown>
            </div>
          )
        )}
        {message.tool_calls?.map((toolCall, idx) => (
          <FunctionDisplay key={idx} toolCall={toolCall} />
        ))}
      </div>
    </div>
  );
}