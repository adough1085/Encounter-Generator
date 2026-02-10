import React, { useState } from 'react';
import './InputField.css'; // Import your CSS file

const LocatePokemonForm = ({ locatePokemon }) => {
  const [pokemonName, setPokemonName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (pokemonName) {
      locatePokemon(pokemonName);
      setPokemonName('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={pokemonName}
        onChange={(e) => setPokemonName(e.target.value)}
        placeholder="Enter Pokémon name"
      />
      <button type="submit">Locate Pokémon</button>
    </form>
  );
};

export default LocatePokemonForm;