import React, { useState } from 'react';

const AddPokemonForm = ({ addPokemon }) => {
  const [pokemonName, setPokemonName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (pokemonName) {
      addPokemon(pokemonName);
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
      <button type="submit">Add Pokémon</button>
    </form>
  );
};

export default AddPokemonForm;