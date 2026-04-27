import { useState } from "react";
import axios from "axios";

function App() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!query.trim()) return;

    const userMessage = { type: "user", text: query };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const res = await axios.get("http://127.0.0.1:8000/ask", {
    params: {
    query,
    history: JSON.stringify(messages)
           },
    });

      const botMessage = { type: "bot", text: res.data.answer };

      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      const botMessage = {
        type: "bot",
        text: "Error getting response. Please try again.",
      };
      setMessages((prev) => [...prev, botMessage]);
    }

    setQuery("");
    setLoading(false);
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#0f172a",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        padding: "20px",
      }}
    >
      {/* Header */}
      <h1 style={{ color: "white", marginBottom: "20px" }}>
         AI College Chatbot
      </h1>

      {/* Chat Container */}
      <div
        style={{
          width: "100%",
          maxWidth: "800px",
          height: "70vh",
          background: "#111827",
          borderRadius: "12px",
          padding: "20px",
          overflowY: "auto",
          display: "flex",
          flexDirection: "column",
          gap: "10px",
          boxShadow: "0 10px 30px rgba(0,0,0,0.4)",
        }}
      >
        {messages.length === 0 && (
          <p style={{ color: "#9ca3af", textAlign: "center" }}>
            Ask anything about the college...
          </p>
        )}

        {messages.map((msg, index) => (
          <div
            key={index}
            style={{
              alignSelf: msg.type === "user" ? "flex-end" : "flex-start",
              background:
                msg.type === "user" ? "#22c55e" : "#1f2937",
              color: "white",
              padding: "10px 15px",
              borderRadius: "10px",
              maxWidth: "75%",
              whiteSpace: "pre-wrap",
            }}
          >
            {msg.text}
          </div>
        ))}

        {loading && (
          <p style={{ color: "#9ca3af" }}>Thinking...</p>
        )}
      </div>

      {/* Input Section */}
      <div
        style={{
          width: "100%",
          maxWidth: "800px",
          marginTop: "15px",
          display: "flex",
          gap: "10px",
        }}
      >
        <input
          type="text"
          placeholder="Type your question..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{
            flex: 1,
            padding: "12px",
            borderRadius: "8px",
            border: "none",
            outline: "none",
            background: "#1f2937",
            color: "white",
          }}
          onKeyDown={(e) => {
            if (e.key === "Enter") handleAsk();
          }}
        />

        <button
          onClick={handleAsk}
          style={{
            padding: "12px 20px",
            background: "#22c55e",
            border: "none",
            borderRadius: "8px",
            color: "white",
            fontWeight: "bold",
            cursor: "pointer",
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default App;