import './Math.css';
import {
  Link
} from "react-router-dom";

function MathHome() {
  return (
      <div className="math-home-page">
        <div className="center-square">
          <div className="square-line">
            <Link to="/math/project/naive-bayes" className="math-link">
              Naive Bayes
            </Link>
            <Link to="/math/project/heat-flow" className="math-link">
              Heat Flow
            </Link>
            <Link to="/math/project/wave-phenomena" className="math-link">
              Wave Phenomena
            </Link>
          </div>
          <div className="square-line">
            <Link to="/math/project/volume-methods" className="math-link">
              Finite Volume
            </Link>
            <Link to="/math/project/hiv-treatment" className="math-link">
              HIV Treatment
            </Link>
            <Link to="/math/project/river-cross" className="math-link">
              River Crossing
            </Link>
          </div>
        </div>
      </div>
  );
}

export default MathHome;
