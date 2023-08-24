import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const LoginScreen = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate(); 

  const handleLogin = () => {
    // Mock authentication process
    if (username === 'user' && password === '') {
      // Navigate to the leagues list page after successful login
      // You can use React Router's history object for this
      navigate('/home')
    } else {
      alert('Invalid username or password');
    }
  };

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      event.preventDefault(); // Prevent form submission
      handleLogin();
    }
  };

  return (
    <div>
      <h2>Login Screen</h2>
      <form>
        <div>
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            onKeyDown={handleKeyPress} // Call handleKeyPress when a key is pressed

          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            onKeyDown={handleKeyPress} // Call handleKeyPress when a key is pressed
          />
        </div>
        <button type="button" onClick={handleLogin}>
          Login
        </button>
      </form>
    </div>
  );
};

export default LoginScreen;
