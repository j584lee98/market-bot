"use client";

import { useState } from "react";
import { ChatHeader } from "./chat-header";
import { ChatInput } from "./chat-input";
import { ChatLayout } from "./chat-layout";
import type { ChatMessage } from "./chat-message-list";
import { ChatMessageList } from "./chat-message-list";

export default function Chat() {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: "welcome-1",
      role: "bot",
      content:
        "Hi, I’m **Market Bot**. Ask me about stocks, crypto, macro trends, or trading ideas.",
    },
  ]);

  const handleSend = (text: string) => {
    setMessages((prev) => [
      ...prev,
      { id: crypto.randomUUID(), role: "user", content: text },
    ]);
  };

  return (
    <ChatLayout
      header={<ChatHeader />}
      messages={<ChatMessageList messages={messages} />}
      input={<ChatInput onSend={handleSend} />}
    />
  );
}
