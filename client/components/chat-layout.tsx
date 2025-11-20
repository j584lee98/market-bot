"use client";

import type { ReactNode } from "react";

type ChatLayoutProps = {
  header: ReactNode;
  messages: ReactNode;
  input: ReactNode;
};

export function ChatLayout({ header, messages, input }: ChatLayoutProps) {
  return (
    <div className="flex h-dvh w-full flex-col bg-zinc-950 text-zinc-50">
      <div className="mx-auto flex h-full w-full max-w-4xl flex-col bg-zinc-950/60">
        {header}
        <div className="flex-1 overflow-y-auto px-3 pb-24 pt-4 sm:px-4">
          {messages}
        </div>
        <div className="pointer-events-auto fixed inset-x-0 bottom-0 z-10 bg-zinc-950/90 backdrop-blur">
          <div className="mx-auto w-full max-w-4xl px-3 py-3 sm:px-4 sm:py-4">
            {input}
          </div>
        </div>
      </div>
    </div>
  );
}
