import React from "react";

const Block = ({ block }) => {
  return (
    <div style={{
      border: "1px solid #ddd",
      borderRadius: "8px",
      padding: "15px",
      margin: "10px 0",
      backgroundColor: "#f9f9f9",
      boxShadow: "0 2px 5px rgba(0,0,0,0.1)"
    }}>
      <h3 style={{ color: "#333" }}>Block {block.index}</h3>
      <p><strong>Timestamp:</strong> {new Date(block.timestamp * 1000).toLocaleString()}</p>
      <p><strong>Previous Hash:</strong> {block.previous_hash}</p>
      <p><strong>Proof:</strong> {block.proof}</p>
    </div>
  );
};

export default Block;
