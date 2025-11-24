"use client";

import { useState } from "react";
import { ChatHeader } from "./chat-header";
import { ChatInput } from "./chat-input";
import { ChatLayout } from "./chat-layout";
import type { ChatMessage } from "./chat-message-list";
import { ChatMessageList } from "./chat-message-list";
import { sendChatMessage } from "../lib/api";

export default function Chat() {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: "welcome-1",
      role: "bot",
      content:
        "Hi, I’m **Market Bot**, your research assistant for stocks, ETFs, crypto, and macro.\n\n" +
        "I can help you with things like:\n\n" +
        "- Recent price action and volatility for a symbol\n" +
        "- Company news and major headlines\n" +
        "- Past and upcoming earnings events\n" +
        "- Analyst ratings, upgrades/downgrades, and price targets\n" +
        "- A detailed snapshot of a company when you’re not sure what to look at",
    },
  ]);

  const [isLoading, setIsLoading] = useState(false);

  const handleSend = async (text: string) => {
    const userMessage: ChatMessage = {
      id: crypto.randomUUID(),
      role: "user",
      content: text,
    };

    setMessages((prev) => [...prev, userMessage]);

    try {
      setIsLoading(true);
      const data = await sendChatMessage(text);
      const botMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: "bot",
        content: data.response ?? "",
      };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      const botMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: "bot",
        content:
          "Sorry, I ran into an error talking to the server. Please try again.",
      };
      setMessages((prev) => [...prev, botMessage]);
      console.error(error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <ChatLayout
      header={<ChatHeader />}
      messages={<ChatMessageList messages={messages} />}
      inputArea={
        <div className="space-y-2">
          {isLoading && (
            <div className="flex items-center gap-2 text-xs text-zinc-400">
              <span className="flex h-2 w-2 animate-pulse rounded-full bg-emerald-400" />
              <span>Market Bot is thinking…</span>
            </div>
          )}
          <ChatInput onSend={handleSend} />
        </div>
      }
    />
  );
}
