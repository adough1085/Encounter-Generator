import React, { useEffect } from 'react';
import './App.css';
import PokemonList from './components/Pokemons';

const App = () => {
  useEffect(() => {
    // This runs after the component mounts
    document.title = "Pokémon Scarlet and Violet Pokémon Picker Tool";
  }, []); // Empty dependency array means it runs once on mount


  return (
    <div className="App">
      <header className="App-header">
        <h1>Pokémon Scarlet and Violet Pokémon Picker Tool</h1>
      </header>
      <main>
        <PokemonList />
      </main>
    </div>
  );
};

export default App;