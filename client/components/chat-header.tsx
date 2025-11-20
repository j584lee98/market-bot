"use client";

export function ChatHeader() {
  return (
    <header className="flex items-center gap-3 bg-zinc-950/80 px-4 py-3 sm:px-6">
      <div className="flex h-9 w-9 items-center justify-center rounded-full bg-gradient-to-br from-emerald-400 to-sky-500 text-sm font-semibold text-zinc-950">
        MB
      </div>
      <div className="flex flex-col">
        <span className="text-sm font-semibold text-zinc-50">
          Market Bot
        </span>
        <span className="text-xs text-zinc-400">Ask about markets, trends, and more.</span>
      </div>
      <div className="ml-auto hidden items-center gap-2 text-xs text-zinc-400 sm:flex">
        <span className="h-2 w-2 rounded-full bg-emerald-400" />
        <span>Ready</span>
      </div>
    </header>
  );
}
