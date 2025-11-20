"use client";

import { useEffect, useRef } from "react";
import type { ChatRole } from "./chat-message-bubble";
import { ChatMessageBubble } from "./chat-message-bubble";

export type ChatMessage = {
  id: string;
  role: ChatRole;
  content: string;
};

type ChatMessageListProps = {
  messages: ChatMessage[];
};

export function ChatMessageList({ messages }: ChatMessageListProps) {
  const endRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  if (messages.length === 0) {
    return (
      <div className="flex h-full flex-col items-center justify-center text-center text-sm text-zinc-500">
        <p className="mb-2 font-medium text-zinc-300">
          Welcome to Market Bot
        </p>
        <p className="max-w-sm text-xs text-zinc-500">
          Ask anything about stocks, crypto, macro trends, or strategies.
        </p>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-4 pb-6">
      {messages.map((m) => (
        <ChatMessageBubble key={m.id} role={m.role} content={m.content} />
      ))}
      <div ref={endRef} />
    </div>
  );
}
