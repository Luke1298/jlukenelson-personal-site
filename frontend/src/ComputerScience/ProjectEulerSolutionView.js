import './ProjectEuler.css';
import CodeViewer from './CodeViewer'
import React, { Component } from 'react';
import {
  useParams,
  withRouter
} from "react-router-dom";

function getProejctEulerLink(problemId){
  return "https://projecteuler.net/problem=" + problemId.split(" ")[1];
}

function getProejctEulerSolutionLink(problemId){
  return process.env.PUBLIC_URL + "/computer-science/project-euler-solutions/" + problemId.toLowerCase().replace(" ", "-") + ".py";
}

function getProblemNumber(problemId){
  return parseInt(problemId.split(" ")[1])
}

function ProjectEulerSolutionViewInternal(problemId) {
  //let { problemId } = useParams();
  console.log(problemId);
  return(
    <div className="project-euler-solution-page">
      <div className="project-euler-solution-title">{problemId} Solution</div>
      <div className="project-euler-solution-subtitle">
        See problem statment here: <a href={getProejctEulerLink(problemId)}>{problemId}</a>
      </div>
      <CodeViewer
              file={getProejctEulerSolutionLink(problemId)}
      />
    </div>
  )
}

class ProjectEulerSolutionView extends Component<*, State> {
  render(){
    if ( getProblemNumber(this.props.match.params.problemId) <= 100) {
      return(ProjectEulerSolutionViewInternal(this.props.match.params.problemId));
    }
    else {
      else {
        return(
          <div className="project-euler-solution-page">
            <div className="project-euler-solution-title">
              {this.props.match.params.problemId}
            </div>
            <div className="project-euler-need-to-understand">
              <p className="project-euler-need-to-understand-first-paragraph">
                Project Euler has asked that participants not share solutions past
                the 100th problem. If you are viewing this page to evaluate his
                problem solving skills email him at <a href="mailto:lukenelson1298@gmail.com">lukenelson1298@gmail.com</a>
                and at his disgression he can discuss how he solved these problems.
              </p>
            </div>
          </div>
        )
      }
    }
  }
};

export default withRouter(ProjectEulerSolutionView);
