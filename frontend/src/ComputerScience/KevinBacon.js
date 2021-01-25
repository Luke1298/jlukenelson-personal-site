import './KevinBacon.css';
import actors from './media/actors'
import actorConnections from './media/actors_connection_to_kevin_bacon'
import AsyncSelect from 'react-select/async';
import 'react-dropdown/style.css';
import React, { Component } from 'react';

const actorOptions = actors.map(i => {
  return {label : i, value : i}
});
console.log(actorOptions)

const filterColors = (inputValue: string) => {
  return actorOptions.filter(i =>
    i.label.toLowerCase().includes(inputValue.toLowerCase())
  ).slice(0, 10);
};
const loadOptions = (inputValue, callback) => {
  setTimeout(() => {
    callback(filterColors(inputValue));
  }, 1000);
};

function KevinBaconGraph(currentActor) {
  if (!!currentActor){
    const actorPath = actorConnections[currentActor.label] || "No connection";
    console.log(currentActor);
    console.log(actorPath);
    var items = []

    for (const [index, value] of actorPath.entries()) {
      if (!(index%2)) {
        items.push(<div key={index} className="graph-actor">{value}</div>)
      }
      else{
        items.push(<div key={index} className="graph-movie">{value}</div>)
      }
    }

    return (
      <div className="graph-outer">
        <div className="bacon-number-title">
          Bacon Number: {(items.length - 1)/2}
        </div>
        <div className="graph">
          {items}
        </div>
      </div>
    )
  }
  else{
    return (
      <div>
      </div>
    )
  }
}

export default class KevinBacon extends Component<*, State> {
  state = { inputValue: '', currentActorSelected: null};
  handleInputChange = (newValue: string) => {
    const inputValue = newValue;//.replace(/\W/g, '');
    this.setState({ inputValue });
    return inputValue;
  };
  handleOnChange = (newValue: string) => {
    const currentActorSelected = newValue;
    this.setState({ currentActorSelected });
    return newValue;
  };
  render() {
    return (
        <div className="kevin-bacon-home-page">
          <div className="kevin-bacon-title">
            Select an actor to see how they connect to Kevin Bacon
          </div>
          <div className="actor-selector">
            <AsyncSelect
              cacheOptions
              isClearable={true}
              maxMenuHeight={175}
              loadOptions={loadOptions}
              defaultOptions
              onInputChange={this.handleInputChange}
              onChange={this.handleOnChange}
            />
          </div>
          {KevinBaconGraph(this.state.currentActorSelected)}
        </div>
    );
  }
}
