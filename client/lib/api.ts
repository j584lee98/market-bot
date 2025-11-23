export type ChatApiResponse = {
  response: string;
};

export async function sendChatMessage(message: string): Promise<ChatApiResponse> {
  const res = await fetch("/api/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });

  if (!res.ok) {
    const errorText = await res.text().catch(() => res.statusText);
    throw new Error(errorText || `Request failed with ${res.status}`);
  }

  return res.json();
}
