"use client";

import { useState } from "react";

type ChatInputProps = {
  onSend: (value: string) => void;
};

export function ChatInput({ onSend }: ChatInputProps) {
  const [value, setValue] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!value.trim()) return;
    onSend(value.trim());
    setValue("");
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex items-end gap-2 rounded-2xl bg-zinc-900/80 px-3 py-2 shadow-lg shadow-black/40"
    >
      <textarea
        className="max-h-32 min-h-[44px] flex-1 resize-none bg-transparent px-2 py-2 text-sm text-zinc-50 placeholder-zinc-500 focus:outline-none"
        placeholder="Ask a question about the market..."
        value={value}
        onChange={(e) => setValue(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(e);
          }
        }}
      />
      <button
        type="submit"
        disabled={!value.trim()}
        className="mb-1 inline-flex h-9 items-center justify-center rounded-full bg-emerald-500 px-4 text-sm font-semibold text-emerald-950 transition hover:bg-emerald-400 disabled:opacity-40"
      >
        Send
      </button>
    </form>
  );
}
