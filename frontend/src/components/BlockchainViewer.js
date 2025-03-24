import React, { useState, useEffect } from "react";
import axios from "axios";
import Block from "./Block";

const BlockchainViewer = () => {
  const [chain, setChain] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/chain").then((response) => {
      setChain(response.data.chain);
    });
  }, []);

  return (
    <div style={{ width: "80%", margin: "0 auto", textAlign: "center" }}>
      <h2 style={{ borderBottom: "2px solid #007BFF", paddingBottom: "10px", color: "#007BFF" }}>
        Blockchain
      </h2>
      <div style={{ marginTop: "20px" }}>
        {chain.map((block) => (
          <Block key={block.index} block={block} />
        ))}
      </div>
    </div>
  );
};

export default BlockchainViewer;
