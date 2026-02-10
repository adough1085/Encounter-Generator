import React, { useState } from 'react';
import './InputField.css'; // Import your CSS file

const LocatePokemonForm = ({ locatePokemon }) => {
  const [pokemonName, setPokemonName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (pokemonName) {
      locatePokemon(pokemonName);
    }
  };

  return (
    <form className="form-grid" onSubmit={handleSubmit}>
      <div className="form-group-locate">
        <label htmlFor="pokemonName">Find Pokémon's Habitats</label>
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
      <button className="start-at-second-col" type="submit">Locate Pokémon</button>
    </form>
  );
};

export default LocatePokemonForm;