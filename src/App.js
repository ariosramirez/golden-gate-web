import React from 'react';
import ImageGrid from './components/ImageGrid';

function App() {
  return (
    <div className="App">
      <header>
        <h1>Golden Gate</h1>
      </header>
      <main>
        <ImageGrid />
      </main>
      <footer>
        <p>&copy; 2024 Golden Gate</p>
      </footer>
    </div>
  );
}

export default App;