import React, { useState, useEffect } from 'react';
import api from './api';
import { useNavigate } from 'react-router-dom';
import Popup from './Popup'
import AddTeamForm from './AddTeamForm';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const navigate = useNavigate()
  const [isPopupOpen, setIsPopupOpen] = useState(false);

  const togglePopup = () => {
    setIsPopupOpen(!isPopupOpen);
  };

  const fetchData = () => {
    // Make the API call to fetch the list of leagues
    const selectedLeagueId = JSON.parse(sessionStorage.getItem('league')).league_id;

    api.get('/teams/', { params: { league: selectedLeagueId } })
      .then(response => {
        setTeams(response.data);
      })
      .catch(error => {
        console.error('Error fetching leagues:', error);
      });
  }
  
  useEffect(() => {
    fetchData();
  }, []); // Empty dependency array ensures the effect runs only once
  
  const handleLeagueClick = (leagueId) => {
    api.get('/leagues/', { params: { league_id: leagueId } }) // Make the API call with league_id as a parameter
      .then(response => {
        const league = response.data[0]; // Assuming the response is a list with one league
        sessionStorage.setItem('league', JSON.stringify(league));
        navigate(`/${encodeURIComponent(league.name)}`);
      })
      .catch(error => {
        console.error('Error fetching league:', error);
      });
  };

  return (
    <div>
    <Popup buttonCaption="Create New Team" isOpen={isPopupOpen} setIsOpen={setIsPopupOpen}><AddTeamForm onSubmit={() => {
          togglePopup();
          fetchData();
        }} /></Popup>
      <h2>Teams List</h2>
      <ul>
        {teams.map(team => (
          <li key={team.team_id}> 
            <button   onClick={() => handleLeagueClick(team.team_id)}>{team.name}</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Teams;
