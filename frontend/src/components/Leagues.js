import React, { useState, useEffect } from 'react';
import api from './api';
import { useNavigate } from 'react-router-dom';


const Leagues = () => {
  const [leagues, setLeagues] = useState([]);
  const navigate = useNavigate()
  useEffect(() => {
    
    // Make the API call to fetch the list of leagues
    api.get('/leagues/?is_open=false')
      .then(response => {
        setLeagues(response.data);
      })
      .catch(error => {
        console.error('Error fetching leagues:', error);
      });
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
      <h2>Leagues List</h2>
      <ul>
        {leagues.map(league => (
          <li key={league.league_id}> 
            <button   onClick={() => handleLeagueClick(league.league_id)}>{league.name}</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Leagues;
