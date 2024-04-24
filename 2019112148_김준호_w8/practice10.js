import React from "react";

class StdInfo_10 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      std_name: "",
      age: null,
    };
  }
  mySubmitHandler = (event) => {
    event.preventDefault();
    let age = this.state.age;
    if (!Number(age)) {
      alert("Your age must be a number.");
    }
  }
  myChangeHandler = (event) => {
    let nam = event.target.name;
    let val = event.target.value;
    this.setState({[nam]: val});
  }
  render() {
    return (
    <form onSubmit={this.mySubmitHandler}>
      <h2>Your Student ID {this.state.std_name}, age {this.state.age}</h2>
      <p>Please enter your student ID and your age</p>
      <input
        type='text'
        name='std_name'
        onChange={this.myChangeHandler}
      />
      <input
        type='text'
        name='age'
        onChange={this.myChangeHandler}
      />
      <br/><br/>
      <input type="submit"/>
    </form>
    );
  }
}

export default StdInfo_10;