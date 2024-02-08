import React from 'react';
import SignIn from './components/SignIn';
import logo from './logo.jpg';
import './App.css';

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} />
        <p>
          NZHF Player Registry
        </p>
        <SignIn />
        <a
          className="App-link"
          href="https://handball.org.nz/"
          target="_blank"
          rel="noopener noreferrer"
        >
          NZHF Website
        </a>
      </header>
    </div>
  );
}

export default App;
