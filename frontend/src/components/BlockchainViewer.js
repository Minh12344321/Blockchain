import React, { useState, useEffect } from "react";
import axios from "axios";
import Block from "./Block";

const BlockchainViewer = () => {
  const [chain, setChain] = useState([]);

  // Lấy dữ liệu blockchain khi component mount
  useEffect(() => {
    fetchChain();
  }, []);

  // Hàm lấy blockchain từ backend
  const fetchChain = () => {
    axios
      .get("http://127.0.0.1:5000/chain")
      .then((response) => {
        setChain(response.data.chain);
      })
      .catch((error) => {
        console.error("Lỗi khi lấy blockchain:", error);
      });
  };

  // Hàm đào block mới (gọi endpoint /mine)
  const mineBlock = () => {
    axios
      .get("http://127.0.0.1:5000/mine")
      .then((response) => {
        alert("Block mới đã được đào thành công!");
        // Sau khi đào xong, gọi lại fetchChain() để cập nhật chain
        fetchChain();
      })
      .catch((error) => {
        console.error("Lỗi khi đào block:", error);
      });
  };

  return (
    <div style={{ width: "80%", margin: "0 auto", textAlign: "center" }}>
      <h2
        style={{
          borderBottom: "2px solid #007BFF",
          paddingBottom: "10px",
          color: "#007BFF",
        }}
      >
        Blockchain
      </h2>

      {/* Nút "Đào Block" */}
      <button
        onClick={mineBlock}
        style={{
          marginBottom: "20px",
          padding: "10px 20px",
          backgroundColor: "#007BFF",
          color: "white",
          border: "none",
          cursor: "pointer",
          borderRadius: "4px",
        }}
      >
        Đào Block
      </button>

      <div style={{ marginTop: "20px" }}>
        {chain.map((block) => (
          <Block key={block.index} block={block} />
        ))}
      </div>
    </div>
  );
};

export default BlockchainViewer;
