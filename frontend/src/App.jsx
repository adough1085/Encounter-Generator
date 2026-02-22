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
        <h1>Pokémon Scarlet and Violet Pokémon Selector Tool</h1>
      </header>
      <main>
        <b>Pokémon Box</b><br/>
        Used to keep track of dupes or a specific subset to use only (subset is toggleable with checkbox below).<br/>
        Pokémon names are caps insensitive. Separate Pokémon names with commas. Version exclusive tag is not mandatory.<br/>
        Example: Tauros (Combat Breed), tAUROS (Blaze Breed), Deino (Scarlet)<br/>
        <br/>

        <b>Find Pokémon's Habitats</b><br/>
        Used to find habitats (and times of day if only found during specific times) of a specified Pokémon such as Misdreavus.<br/>

        <b>Find Possible Pokémon</b><br/>
        Used to find possible name matches of Pokémon in game by typing a substring like "Oink".<br/> 
        Used to distinguish between forms of Pokémon with different abilities or stats.<br/>

        <br/><br/>
        Link to GitHub repository: https://github.com/adough1085/Encounter-Generator
        <PokemonList />
        
      </main>
    </div>
  );
};

export default App;