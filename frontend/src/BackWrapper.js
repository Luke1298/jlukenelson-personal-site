import './BackWrapper.css';
import React from "react";

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons'
import {
  Link
} from "react-router-dom";


export default class BackWrapper extends React.Component{
  render() {
    console.log(this.props)
    return (
      <div className="wrapper">
        <Link to={this.props.backPath} className="back-button" style={{color : this.props.iconColor}}>
          <FontAwesomeIcon  icon={faArrowLeft}/>
        </Link>
          {this.props.children}
      </div>
    );
  }
};
