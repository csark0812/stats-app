import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginScreen from './components/LoginScreen';
import LandingScreen from './components/LandingScreen';
import Leagues from './components/Leagues';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<LoginScreen />} />
        <Route exact path="/home" element={<LandingScreen />} />
        <Route exact path="/leagues" element={<Leagues />} />
        <Route path="/league/:slug([a-z-]+)" exact />
        <Route exact path="/open"/>
      </Routes>
    </Router>
  );
};


export default App;
