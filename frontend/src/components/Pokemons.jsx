import React, { useEffect, useState } from 'react';
import api from "../api.js";
import AddPokemonForm from './AddPokemonForm';
import LocatePokemonForm from './LocatePokemonForm.jsx';
import DistributionForm from './DistributionForm.jsx';
import GenerationForm from './GenerationForm.jsx';

const PokemonList = () => {
  const [locations, setLocations] = useState([]);
  const [locateName, setLocateName] = useState([]);
  const [distributions, setDistributions] = useState([]);
  const [generation, setGeneration] = useState([]);
  const [sharedText, setSharedText] = useState("");

  const handleChange = (e) => {
    setSharedText(e.target.value)
  };

  const generate = async (game, area, time, pkmnType, power, dupes) => {
    try {
      const response = await api.post('/generate', {
        game: game,
        area: area, 
        time: time, 
        pkmnType: pkmnType, 
        power: power, 
        dupes: dupes,
        sharedText: sharedText
    });
    setGeneration(response.data)
    } catch (error) {
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
        dupes: dupes,
        sharedText: sharedText
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

  // Not actually sure what this snippet does, used to run something on launch presumably
  useEffect(() => {
    //
  }, []);

  return (
    <div>
      <h2>Pokémon Box</h2>
      <textarea 
        type="text"
        value={sharedText}
        onChange={handleChange}
        placeholder="Separate Pokémon by Commas..."
        style={{
          width: '600px',
          height: '400px',
          fontSize: '16px',
          padding: '10px'
        }}
      />
      
      {/*<AddPokemonForm addPokemon={[addPokemon]} />*/}
      <GenerationForm generate={generate} 
      />
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