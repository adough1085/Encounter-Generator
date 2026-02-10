import React from 'react';
import './App.css';
import PokemonList from './components/Pokemons';

const App = () => {

  useEffect(() => {
    // Set the document title when the component mounts or updates
    document.title = "Pokémon Scarlet and Violet Pokémon Picker Tool"
    
    // Optional: Reset the title when the component unmounts
    return () => {
      // document.title = "Original App Title"; 
    };
  }, []); // The empty dependency array [] ensures this runs once when mounted

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