'use client';

import Chat from "../components/Chat";

export default function Home() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-center py-32 px-4 bg-white dark:bg-black sm:items-center">
        <Chat />
      </main>
    </div>
  );
}
