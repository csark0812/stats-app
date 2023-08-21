import React, { useState } from 'react';
import api from './api'; // Your API module

const AddTeamForm = ({ onSubmit }) => {
  const [teamName, setTeamName] = useState('');
  const [teamAbbreviation, setTeamAbbreviation] = useState('');
  const [teamLogo, setTeamLogo] = useState(null);

  const handleFormSubmit = (e) => {
    e.preventDefault();
    const selectedLeagueId = JSON.parse(sessionStorage.getItem('league')).league_id;

    // Create a FormData object to send the form data
    const formData = new FormData();
    formData.append('name', teamName);
    formData.append('abbreviation', teamAbbreviation.substring(0,10));
    formData.append('league', selectedLeagueId)
    // formData.append('logo', teamLogo)
    // Make the API call to submit the form data
    api.post('/teams/', formData)
      .then(response => {
        // Handle success if needed
        onSubmit();
        console.log('Team created:', response.data);
      })
      .catch(error => {
        // Handle error if needed
        console.error('Error creating team:', error);
      });
  };

  return (
    <div>
      <h2>Create a New Team</h2>
      <form onSubmit={handleFormSubmit}>
        <div>
          <label>Team Name:</label>
          <input
            type="text"
            value={teamName}
            onChange={(e) => setTeamName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Team Abbreviation:</label>
          <input
            type="text"
            value={teamAbbreviation}
            onChange={(e) => setTeamAbbreviation(e.target.value)}
            maxLength="10" 
            required
          />
        </div>
        <div>
          <label>Team Logo:</label>
          <input
            type="file"
            accept="image/*"
            onChange={(e) => setTeamLogo(e.target.files[0])}
          />
        </div>
        <button type="submit">Create Team</button>
      </form>
    </div>
  );
};

export default AddTeamForm;
