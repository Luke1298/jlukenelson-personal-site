import logo from './logo.svg';
import './App.css';

import React from "react";
import About from "./About/About";
import MathHome from "./Math/Math";
import ComputerScienceHome from "./ComputerScience/ComputerScience";
import ProjectEuler from "./ComputerScience/ProjectEuler";
import ProjectEulerSolutionView from "./ComputerScience/ProjectEulerSolutionView";
import KevinBacon from "./ComputerScience/KevinBacon";
import YelpHelp from "./ComputerScience/YelpHelp";
import MathProject from "./Math/MathProject";
import BackWrapper from "./BackWrapper";
import BirthdayMessage from "./BirthdayMessage";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
} from "react-router-dom";

function App() {
  return (
    <Router>
      <div>
        {/*<nav className="header">
          <ul>
            <div className="header">
              <Link to="/">Home</Link>
            </div>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/users">Users</Link>
            </li>
          </ul>
        </nav>*/}

        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Switch>
          <Route path="/project-euler/:problemId">
            <BackWrapper backPath="/project-euler" iconColor="#E8E8EC">
              <ProjectEulerSolutionView/>
            </BackWrapper>
          </Route>
          <Route path="/project-euler">
            <BackWrapper backPath="/computer-science" iconColor="#E8E8EC">
              <ProjectEuler/>
            </BackWrapper>
          </Route>
          <Route path="/cs/project/yelp-help">
            <BackWrapper backPath="/computer-science" iconColor="#E8E8EC">
              <YelpHelp />
            </BackWrapper>
          </Route>
          <Route path="/cs/project/kevin-bacon">
            <BackWrapper backPath="/computer-science" iconColor="#E8E8EC">
              <KevinBacon />
            </BackWrapper>
          </Route>
          <Route path="/math/project/:projectId">
            <BackWrapper backPath="/math" iconColor="#E8E8EC">
              <MathProject />
            </BackWrapper>
          </Route>
          <Route path="/j-luke-nelson-computer-science-showcase">
            <BackWrapper backPath="/" iconColor="#E8E8EC">
              <ComputerScienceHome />
            </BackWrapper>
          </Route>
          <Route path="/j-luke-nelson-math-showcase">
            <BackWrapper backPath="/" iconColor="#282c34">
              <MathHome />
            </BackWrapper>
          </Route>
          <Route path="/about-j-luke-nelson">
            <BackWrapper backPath="/" iconColor="#282c34">
              <About />
            </BackWrapper>
          </Route>
          <Route path="/happy-18th-bday-lily">
            <BirthdayMessage />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

function Home() {
  return (
    <div className="home">
      <div className="passions">
        <div className="math-home">
          <Link to="/j-luke-nelson-math-showcase" className="home-link">
            <h2> Math </h2>
          </Link>
          <div className="about left-about">
            <Link to="/about-j-luke-nelson" className="small-link home-link">
              About
            </Link>
          </div>
        </div>
        <div className="computers-home">
          <Link to="/j-luke-nelson-computer-science-showcase" className="home-link">
            <h2> Computer Science </h2>
          </Link>
          <div className="about right-about">
            <Link to="/about-j-luke-nelson" className="small-link home-link">
              J. Luke Nelson
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
