import './ProjectEuler.css';
import {
  Link
} from "react-router-dom";

const problemList = Array.from({length:117},(v,k)=>{
    return "Problem " + (k+1)
  }
)
console.log(problemList)

var problemSelectorItems = []

for (const problemName of problemList) {
  problemSelectorItems.push(<Link to={"/project-euler/"+problemName}
                                  className="problem-link">
                              {problemName}
                            </Link>)
}


function ProjectEuler(currentActor) {
  return(
    <div className="project-euler-home-page">
      <div className="project-euler-solution-title">
        Project Euler Solutions
      </div>
      <div className="problem-links">
        {problemSelectorItems}
      </div>
    </div>
  )
}

export default ProjectEuler;
