import React from "react";

class Student extends React.Component {
  check = (a) => {
    alert(a);
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