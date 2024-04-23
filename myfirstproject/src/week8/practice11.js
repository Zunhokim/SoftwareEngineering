import React from "react";

class StdInfo_11 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      std_name: "",
      age: null,
      errormessage: "",
    };
  }

  myChangeHandler = (event) => {
    let nam = event.target.name;
    let val = event.target.value;
    let err = "";
    if (nam === "age") {
      if (val != "" && !Number(val)) {
        err = <strong>Your age must be a number</strong>
      }
    }
    this.setState({errormessage: err});
    this.setState({[nam]: val});
  }

  render() {
    return (
      <form>
        <h2>Your Student ID {this.state.std_name}, age {this.state.age}</h2>
        <p>Please enter your student ID</p>
      <input
        type="text"
        name="std_name"
        onChange={this.myChangeHandler}
      />
      <input
        type="text"
        name="age"
        onChange={this.myChangeHandler}
      />
      {this.state.errormessage}
      </form>
    )
  }
}

export default StdInfo_11;