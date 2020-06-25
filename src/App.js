import React from "react";
import "../src/Style/Main.scss";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import NavBar from "./Components/navBar";
import TamingCalc from "./Components/tamingCalc";

function App() {
  return (
    <Router>
      <div className='App'>
        <NavBar />
        <Switch>
          <Route path='/tamingcalc' component={TamingCalc} />
        </Switch>
        <TamingCalc />
      </div>
    </Router>
  );
}

export default App;
