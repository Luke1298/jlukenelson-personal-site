import './MathProject.css';
import {
  useParams
} from "react-router-dom";
import JupViewer from './JupViewer'

const HTMLtoJSX = require("htmltojsx")
const converter = new HTMLtoJSX({ createClass: false })
//import nb from "notebookjs"

function MathProject() {
  let { projectId } = useParams();
  console.log(projectId);
  const metaMap = {"naive-bayes" : {"title" : "Naive Bays Implementation",
                                    "fileLoc" : process.env.PUBLIC_URL + '/ipynotebooks/naive_bayes.ipynb'},
                   "heat-flow" : {"title" : "Conservation Laws and Heat Flow",
                                  "fileLoc" : process.env.PUBLIC_URL + '/ipynotebooks/conservation-laws-and-heat-flow.ipynb'},
                   "wave-phenomena" : {"title" : "Wave Phenomena",
                                       "fileLoc" : process.env.PUBLIC_URL + '/ipynotebooks/wave-phenomena.ipynb'},
                   "volume-methods" : {"title" : "Finite Volume Methods",
                                       "fileLoc" : process.env.PUBLIC_URL + '/ipynotebooks/finite-volume-methods.ipynb'},
                   "river-cross" : {"title" : "Minimizing Transit Time Crossing a River",
                                    "fileLoc" : process.env.PUBLIC_URL + '/ipynotebooks/transit-time-crossing-a-river.ipynb'},
                   "hiv-treatment" : {"title" : "Treating HIV with Control Theory",
                                      "fileLoc" : process.env.PUBLIC_URL + '/ipynotebooks/hiv-treatment.ipynb'},


                  };
  let {title, fileLoc} = metaMap[projectId];
  console.log(title, fileLoc);
  return (
    <div className="math-project-home-page">
      <div className="math-project-title">
        {title}
      </div>
      <JupViewer
              title={title}
              file={fileLoc}
      />
    </div>
  );
}

export default MathProject;
