import React, { useState } from "react";
import axios from "axios";

const TransactionForm = () => {
  const [sender, setSender] = useState("");
  const [receiver, setReceiver] = useState("");
  const [amount, setAmount] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post("http://127.0.0.1:5000/transactions/new", {
      sender,
      receiver,
      amount,
    });
    alert("Giao dịch đã được gửi!");
  };

  return (
    <div style={{
      maxWidth: "500px",
      margin: "20px auto",
      padding: "20px",
      border: "1px solid #ddd",
      borderRadius: "8px",
      boxShadow: "0 2px 5px rgba(0,0,0,0.1)"
    }}>
      <h2 style={{ textAlign: "center", color: "#007BFF" }}>Gửi Giao Dịch</h2>
      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
        <input type="text" placeholder="Người gửi" value={sender} onChange={(e) => setSender(e.target.value)} required 
          style={{ padding: "10px", borderRadius: "5px", border: "1px solid #ddd" }} />
        
        <input type="text" placeholder="Người nhận" value={receiver} onChange={(e) => setReceiver(e.target.value)} required 
          style={{ padding: "10px", borderRadius: "5px", border: "1px solid #ddd" }} />
        
        <input type="number" placeholder="Số tiền" value={amount} onChange={(e) => setAmount(e.target.value)} required 
          style={{ padding: "10px", borderRadius: "5px", border: "1px solid #ddd" }} />
        
        <button type="submit" style={{
          backgroundColor: "#007BFF",
          color: "#fff",
          padding: "10px",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer"
        }}>
          Gửi
        </button>
      </form>
    </div>
  );
};

export default TransactionForm;
