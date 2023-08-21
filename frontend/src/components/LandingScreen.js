import React, { useEffect } from 'react';
import api from './api';
import { useNavigate } from 'react-router-dom';
const LandingScreen = () => {
  const navigate = useNavigate(); 

  useEffect(() => {
    // Clear the 'league' item from sessionStorage when the component mounts
    sessionStorage.removeItem('league');
  }, []);

  const handleOpenGamesButtonClick = () => {    
    // Navigate to the first route when Button 1 is clicked
    api.get('/leagues/?is_open=true')
    .then(response => {
      const league = response.data[0]
      sessionStorage.setItem('league',JSON.stringify(league));
      navigate(`/${encodeURIComponent(league.name)}`);
    })
    .catch(error => {
      console.error('Error fetching leagues:', error);
    });
  };


  const handleLeaguesButtonClick = () => {
    // Navigate to the second route when Button 2 is clicked
    navigate('/leagues');
  };

  return (
    <div>
      <h1>My Component</h1>
      <button onClick={handleOpenGamesButtonClick}>Stand-Alone Games</button>
      <button onClick={handleLeaguesButtonClick}>View Leagues</button>
    </div>
  );
};

export default LandingScreen;
