import React, { useState } from 'react';
import Seasons from './Seasons';
import Teams from './Teams';
// import PlayersComponent from './PlayersComponent';

const LeagueHomePage = () => {
  const [activeTab, setActiveTab] = useState('seasons');

  const handleTabClick = (tab) => {
    setActiveTab(tab);
  };

  return (
    <div>
      <div className="tab-buttons">
        <button
          onClick={() => handleTabClick('seasons')}
          className={activeTab === 'sesasons' ? 'active' : ''}
        >
          Seasons
        </button>
        <button
          onClick={() => handleTabClick('teams')}
          className={activeTab === 'teams' ? 'active' : ''}
        >
          Teams
        </button>
        <button
          onClick={() => handleTabClick('players')}
          className={activeTab === 'players' ? 'active' : ''}
        >
          Players
        </button>
      </div>
      <div className="tab-content">
        {activeTab === 'seasons' && <Seasons />}
        {activeTab === 'teams' && <Teams />}
        {/* {activeTab === 'players' && <PlayersComponent />} */}
      </div>
    </div>
  );
};

export default LeagueHomePage;
