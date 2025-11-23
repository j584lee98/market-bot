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
        "Hi, I’m **Market Bot**. Ask me about stocks, crypto, macro trends, or trading ideas.",
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
      input={<ChatInput onSend={handleSend} />}
    />
  );
}
