import React from "react";

class Container extends React.Component {
  constructor(props){
    super(props);
    this.state = {show: true};
  }

  delHeader = () => {
    this.setState({show: false});
  }

  redner() {
    let myheader;
    if (this.state.show) {
      myheader = <Child />
    };
    return(
      <div>
        {myheader}
        <button type="button" onClick={this.delHeader}>Delete Header</button>
      </div>
    )
  }
}

class Child extends React.Component {
  componentWillUnmount() {
    alert("The component Header is about to be unmounted.");
  }

  render() {
    return(
      <h1>Information and Communication Engineering!</h1>
    );
  }
}



export default Container;