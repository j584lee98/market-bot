"use client";

import ReactMarkdown from "react-markdown";

export type ChatRole = "user" | "bot";

type ChatMessageBubbleProps = {
  role: ChatRole;
  content: string;
};

export function ChatMessageBubble({ role, content }: ChatMessageBubbleProps) {
  const isUser = role === "user";

  return (
    <div
      className={`flex w-full items-start gap-3 ${
        isUser ? "flex-row-reverse" : "flex-row"
      }`}
    >
      <div className="mt-1 flex h-8 w-8 items-center justify-center rounded-full bg-zinc-800 text-xs font-semibold text-zinc-100">
        {isUser ? "You" : "MB"}
      </div>
      <div
        className={`max-w-[80%] rounded-2xl px-4 py-3 text-sm leading-relaxed shadow-sm ${
          isUser
            ? "bg-emerald-500 text-emerald-950"
            : "bg-zinc-900 text-zinc-50 ring-1 ring-zinc-800"
        }`}
      >
        <div className="prose prose-invert prose-sm max-w-none">
          <ReactMarkdown>{content}</ReactMarkdown>
        </div>
      </div>
    </div>
  );
}
