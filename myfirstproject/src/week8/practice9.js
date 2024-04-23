import React from "react";

class Student extends React.Component {
  constructor(props) {
    super(props);
    this.state = { message: "" };
  }

  handleChange = (event) => {
    this.setState({ message: event.target.value });
  };

  handleClick = () => {
    this.check(this.state.message);
  };
  
  check = (a) => {
    alert("당신의 학번은 "+ a + " 입니다. ");
  }
  render() {
    return (
      <div>
        <h1>Event Practice.</h1>
        <input type="text" name="message" placeholder="학번 입력."
          value={this.state.message}
          onChange={this.handleChange}>
        </input>
        <button onClick={this.handleClick}>확인</button>
      </div>
    );
  }
}

export default Student;