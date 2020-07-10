import React from 'react';
import logo from './logo.svg';
import './App.css';
import Button from 'react-bootstrap/Button';
import Header from './components/header';
import Signup from './components/signup_body';

function App() {
  return (
    <div className="App">
      <Header/>
      <Signup/>
    </div>
  );
}

export default App;
