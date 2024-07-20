import React from 'react';
import ImageGrid from './components/ImageGrid';
import './App.css';


function App() {
  return (
    <div className="App">
      <header className="header">
        <h1>Golden Gate</h1>
      </header>
      <main className="main-content main-container">
        <ImageGrid />
      </main>
      {/*<footer className="footer">*/}
      {/*  <p>&copy; 2024 Golden Gate</p>*/}
      {/*</footer>*/}
    </div>
  );
}

export default App;
