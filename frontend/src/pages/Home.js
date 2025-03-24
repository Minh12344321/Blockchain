import React from "react";

import TransactionForm from "../components/TransactionForm.js";
import BlockchainViewer from "../components/BlockchainViewer";


const Home = () => {
  return (
    <div>
      <h1>Blockchain Demo</h1>
      <TransactionForm />
      <BlockchainViewer />
    </div>
  )
};

export default Home;
