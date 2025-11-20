"use client";

import React, { useState, useRef, useEffect } from "react";

function ChatMessage({ sender, text }: { sender: string; text: string }) {
  return (
    <div className={`flex ${sender === "user" ? "justify-end" : "justify-start"} mb-2`}>
      <div
        className={`rounded-lg px-4 py-2 max-w-xs text-sm shadow-sm ${
          sender === "user"
            ? "bg-blue-600 text-white"
            : "bg-zinc-200 text-black dark:bg-zinc-700 dark:text-zinc-50"
        }`}
      >
        {text}
      </div>
    </div>
  );
}

export default function Chat() {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "Hello! How can I help you today?" },
  ]);
  const [input, setInput] = useState("");
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = () => {
    if (!input.trim()) return;
    setMessages((msgs) => [...msgs, { sender: "user", text: input }]);
    setInput("");
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") handleSend();
  };

  return (
    <div className="flex flex-col w-full h-[500px] max-w-md mx-auto border rounded-lg bg-white dark:bg-zinc-900 shadow-lg">
      <div className="flex-1 overflow-y-auto p-4">
        {messages.map((msg, idx) => (
          <ChatMessage key={idx} sender={msg.sender} text={msg.text} />
        ))}
        <div ref={messagesEndRef} />
      </div>
      <div className="flex items-center gap-2 border-t p-3 bg-zinc-50 dark:bg-zinc-800">
        <input
          className="flex-1 rounded-full border px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400 dark:bg-zinc-700 dark:text-zinc-50"
          type="text"
          placeholder="Type your message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button
          className="rounded-full bg-blue-600 text-white px-4 py-2 font-semibold hover:bg-blue-700 transition"
          onClick={handleSend}
        >
          Send
        </button>
      </div>
    </div>
  );
}
