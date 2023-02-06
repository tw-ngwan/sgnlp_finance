import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Mainpage from './Mainpage';
import Storedpage from './Storedpage';

class Homepage extends React.Component {
  render() {
    return (
      <Router>
        <Routes>
          <Route exact path="/" element={<Mainpage />} /> 
          <Route path="/stored" element={<Storedpage />} />
        </Routes>
      </Router>
    );
  }
}

console.log("Homepage index.js");
export default Homepage;
