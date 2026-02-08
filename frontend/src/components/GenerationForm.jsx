import React, { useState } from 'react';

const GenerationForm = ({ generate }) => {
  const [game, setGame] = useState('Scarlet');
  const [area, setArea] = useState('Alfornada Cavern');
  const [time, setTime] = useState('Dawn');
  const [pkmnType, setPkmnType] = useState('Normal');
  const [power, setPower] = useState('0');
  const [dupes, setDupes] = useState('No');

  const handleChangeGame = (e) => {
    setGame(e.target.value);
  }

  const handleChangeArea = (e) => {
    setArea(e.target.value);
  }

  const handleChangeTime = (e) => {
    setTime(e.target.value)
  }

  const handleChangePkmnType = (e) => {
    setPkmnType(e.target.value)
  }

  const handleChangePower = (e) => {
    setPower(e.target.value)
  }

  const handleChangeDupes = (e) => {
    setDupes(e.target.value)
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    generate(game, area, time, pkmnType, power, dupes);
  };

  return (
    <form onSubmit={handleSubmit}>
      <select value={game} onChange={handleChangeGame}>
        <option value="Scarlet">Scarlet</option>
        <option value="Violet">Violet</option>
      </select>
      <select value={area} onChange={handleChangeArea}>
        <option value="Alfornada Cavern">Alfornada Cavern</option>
        <option value="Asado Desert">Asado Desert</option>
        <option value="Cabo Poco">Cabo Poco</option>
        <option value="Casseroya Lake">Casseroya Lake</option>
        <option value="Dalizapa Passage">Dalizapa Passage</option>
        <option value="East Paldean Sea">East Paldean Sea</option>
        <option value="East Province (Area One)">East Province (Area One)</option>
        <option value="East Province (Area Two)">East Province (Area Two)</option>
        <option value="East Province (Area Three)">East Province (Area Three)</option>
        <option value="Glaseado Mountain">Glaseado Mountain</option>
        <option value="Great Crater of Paldea">Great Crater of Paldea</option>
        <option value="Inlet Grotto">Inlet Grotto</option>
        <option value="North Paldean Sea">North Paldean Sea</option>
        <option value="North Province (Area One)">North Province (Area One)</option>
        <option value="North Province (Area Two)">North Province (Area Two)</option>
        <option value="North Province (Area Three)">North Province (Area Three)</option>
        <option value="Poco Path">Poco Path</option>
        <option value="Pokemon League">Pokemon League</option>
        <option value="Socarrat Trail">Socarrat Trail</option>
        <option value="South Paldean Sea">South Paldean Sea</option>
        <option value="South Province (Area One)">South Province (Area One)</option>
        <option value="South Province (Area Two)">South Province (Area Two)</option>
        <option value="South Province (Area Three)">South Province (Area Three)</option>
        <option value="South Province (Area Four)">South Province (Area Four)</option>
        <option value="South Province (Area Five)">South Province (Area Five)</option>
        <option value="South Province (Area Six)">South Province (Area Six)</option>
        <option value="Tagtree Thicket">Tagtree Thicket</option>
        <option value="West Paldean Sea">West Paldean Sea</option>
        <option value="West Province (Area One)">West Province (Area One)</option>
        <option value="West Province (Area Two)">West Province (Area Two)</option>
        <option value="West Province (Area Three)">West Province (Area Three)</option>
      </select>
      <select value={time} onChange={handleChangeTime}>
        <option value="Dawn">Dawn</option>
        <option value="Day">Day</option>
        <option value="Dusk">Dusk</option>
        <option value="Night">Night</option>
      </select>
      <select value={pkmnType} onChange={handleChangePkmnType}>
        <option value="Normal">Normal</option>
        <option value="Fighting">Fighting</option>
        <option value="Flying">Flying</option>
        <option value="Poison">Poison</option>
        <option value="Ground">Ground</option>
        <option value="Rock">Rock</option>
        <option value="Bug">Bug</option>
        <option value="Ghost">Ghost</option>
        <option value="Steel">Steel</option>
        <option value="Fire">Fire</option>
        <option value="Water">Water</option>
        <option value="Grass">Grass</option>
        <option value="Electric">Electric</option>
        <option value="Psychic">Psychic</option>
        <option value="Ice">Ice</option>
        <option value="Dragon">Dragon</option>
        <option value="Dark">Dark</option>
        <option value="Fairy">Fairy</option>
      </select>
      <select value={power} onChange={handleChangePower}>
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
      </select>
      <select value={dupes} onChange={handleChangeDupes}>
        <option value="No">No</option>
        <option value="Yes">Yes</option>
      </select>
      <button type="submit">Generate Generation</button>
    </form>
  );
};

export default GenerationForm;