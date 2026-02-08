import React, { useEffect, useState } from 'react';
import api from "../api.js";
import AddPokemonForm from './AddPokemonForm';
import LocatePokemonForm from './LocatePokemonForm.jsx';
import DistributionForm from './DistributionForm.jsx';
import GenerationForm from './GenerationForm.jsx';

const PokemonList = () => {
  const [pokemons, setPokemons] = useState([]);
  const [locations, setLocations] = useState([]);
  const [locateName, setLocateName] = useState([]);
  const [distributions, setDistributions] = useState([]);
  const [generation, setGeneration] = useState([]);

  const fetchPokemons = async () => {
    try {
      const response = await api.get('/pokemons');
      setPokemons(response.data.pokemons);
    } catch (error) {
      console.error("Error fetching pokemons", error);
    }
  };

  const addPokemon = async (pokemonName) => {
    try {
      await api.post('/pokemons', { name: pokemonName });
      fetchPokemons();  // Refresh the list after adding a pokemon
    } catch (error) {
      console.error("Error adding Pokémon", error);
    }
  };

  const generate = async (game, area, time, pkmnType, power, dupes) => {
    try {
      const response = await api.post('/generate', {
        game: game,
        area: area, 
        time: time, 
        pkmnType: pkmnType, 
        power: power, 
        dupes: dupes
    });
    setGeneration(response.data)
    //console.log(response.data)
    } catch (error) {
        c
        console.error("Error generating Pokémon", error);
    }
  };


  const distribution = async (game, area, time, pkmnType, power, dupes) => {
    try {
      const response = await api.post('/distribution', {
        game: game,
        area: area, 
        time: time, 
        pkmnType: pkmnType, 
        power: power, 
        dupes: dupes
    });
    setDistributions(response.data.distributions)
    } catch (error) {
        console.error("Error distributing Pokémon", error);
    }
  };

  const locatePokemon = async (pokemonName) => {
    try {
      const response = await api.post('/locate', { name: pokemonName });
      setLocations(response.data.locations)
      setLocateName(response.data.pkmn_name)
    } catch (error) { 
      console.error("Error locating Pokémon", error);
    }
  };


  useEffect(() => {
    fetchPokemons();
  }, []);

  return (
    <div>
      <h2>Pokémon Box</h2>
      <ul>
        {pokemons.map((pokemon, index) => (
          <li key={index}>{pokemon.name}</li>
        ))}
      </ul>
      <AddPokemonForm addPokemon={addPokemon} />
      <GenerationForm generate={generate} />
        <div>{generation !== null ? <p>{generation.area} ({generation.time}): {generation.pkmn_name}</p> : <p></p>}</div>

      <DistributionForm distribution={distribution}/>
      <ul>
        {distributions.map((distribution, index) => (
          <li key={index}>{distribution.pkmn_name}: {distribution.percentage}%</li>
        ))}
      </ul>
      <LocatePokemonForm locatePokemon={locatePokemon} />
      <div>{locations.length > 0 ? <p>{locateName} can be found in:</p> : <p>{locateName} cannot be found in the game.</p>}</div>
      <ul>
        {locations.map((location, index) => (
          <li key={index}>{location.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default PokemonList;