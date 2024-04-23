import React from "react";

class Phone extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      brand : "apple",
      model : "pro",
      color : "gold",
      year : "2020"
    };
  }
  changeInfo = () => {
    this.setState({model : "14"});
    this.setState({color : "black"});
    this.setState({year : "2022"});
  }

  render() {
    return (
      <div>
        <h1>My {this.state.brand} Phone</h1>
        <p>
          It is a {this.state.color} iphone {this.state.model} from {this.state.year}.
        </p>
        
        <button 
          type="button" 
          onClick={this.changeInfo}
          >Change Info</button>
      </div>
    );
  }
}

export default Phone;