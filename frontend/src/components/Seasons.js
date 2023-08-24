import React, { useState, useEffect } from 'react';
import api from './api';
import { useNavigate } from 'react-router-dom';


const Seasons = () => {
  const [activeSeasons, setActiveSeasons] = useState([]);
  const [pastSeasons, setPastSeasons] = useState([]);

  const navigate = useNavigate()
  useEffect(() => {
    // Make the API call to fetch the list of leagues
    const selectedLeagueId = JSON.parse(sessionStorage.getItem('league')).league_id;

    api.get('/seasons/', { params: { league: selectedLeagueId} })
      .then(response => {
        setActiveSeasons(response.data.filter(season => !season.is_complete));
        setPastSeasons(response.data.filter(season => season.is_complete));
      })
      .catch(error => {
        console.error('Error fetching seasons:', error);
      });
  }, []); // Empty dependency array ensures the effect runs only once
  
  const handleSeasonClick = (seasonId) => {
    const selectedLeagueId = JSON.parse(sessionStorage.getItem('league')).league_id;
    const selectedLeagueName = JSON.parse(sessionStorage.getItem('league')).name;

    api.get('/seasons/', { params: { league_id: selectedLeagueId, season_id: seasonId } }) // Make the API call with league_id as a parameter
      .then(response => {
        const season = response.data[0]; // Assuming the response is a list with one league
        sessionStorage.setItem('season', JSON.stringify(season));
        console.log(season.name)
        navigate(`/${encodeURIComponent(selectedLeagueName)}/${encodeURIComponent(season.name)}`);
      })
      .catch(error => {
        console.error('Error fetching league:', error);
      });
  };

  return (
    <div>
      <h2>Active Seasons List</h2>
      <ul>
        {activeSeasons.map(season => (
          <li key={season.season_id}> 
            <button   onClick={() => handleSeasonClick(season.season_id)}>{season.name}</button>
          </li>
        ))}
      </ul>
      <h2>Past Seasons List</h2>
      <ul>
        {pastSeasons.map(season => (
          <li key={season.season_id}> 
            <button   onClick={() => handleSeasonClick(season.season_id)}>{season.name}</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Seasons;
