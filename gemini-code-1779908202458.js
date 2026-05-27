import React, { useState } from 'react';

const GenDInterface = () => {
  const [file, setFile] = useState(null);

  const handleEncrypt = () => {
    alert("Démarrage du processus de chiffrement via DN-35gmx...");
  };

  return (
    <div style={{ padding: '50px', textAlign: 'center', backgroundColor: '#1e1e1e', color: 'white', height: '100vh' }}>
      <h1>🔒 GEN-D Web Portal</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} style={{ margin: '20px' }} />
      <br />
      <button 
        onClick={handleEncrypt}
        style={{ padding: '10px 20px', backgroundColor: '#ff9900', border: 'none', borderRadius: '5px', cursor: 'pointer' }}
      >
        Chiffrer le Fichier
      </button>
    </div>
  );
};

export default GenDInterface;