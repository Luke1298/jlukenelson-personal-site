import './ComputerScience.css';
import {
  Link
} from "react-router-dom";

function ComputerScienceHome() {
  return (
      <div className="computer-science-home-page">
        <div className="center-square">
          <div className="square-line">
            <Link to="/cs/project/kevin-bacon" className="math-link">
              Kevin Bacon
            </Link>
            <Link to="/project-euler" className="math-link">
              Project Euler
            </Link>
            <Link to="/cs/project/yelp-help" className="math-link">
              Yelp Help
            </Link>
          </div>
        </div>
      </div>
  );
}

export default ComputerScienceHome;
