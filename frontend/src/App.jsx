import React from 'react';
import './App.css';
import PokemonList from './components/Pokemons';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Pokémon Scarlet and Violet Random Generator</h1>
      </header>
      <main>
        <PokemonList />
      </main>
    </div>
  );
};

export default App;