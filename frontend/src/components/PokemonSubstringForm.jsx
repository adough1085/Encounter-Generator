import React, { useState } from 'react';
import './InputField.css'; // Import your CSS file

const PokemonSubstringForm = ({ pokemonSubstring }) => {
  const [pokemonName, setPokemonName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (pokemonName) {
      pokemonSubstring(pokemonName);
    }
  };

  return (
    <form className="form-grid" onSubmit={handleSubmit}>
      <div className="form-group-locate">
        <label htmlFor="pokemonName">Find Possible Pokémon</label>
        <input
          
          id="pokemonName"
          type="text"
          value={pokemonName}
          onChange={(e) => setPokemonName(e.target.value)}
          autoComplete="off"
          placeholder="Enter Pokémon name"
        />
      </div>
      <br/>
      <button className="start-at-second-col" type="submit">Match Pokémon Names</button>
    </form>
  );
};

export default PokemonSubstringForm;