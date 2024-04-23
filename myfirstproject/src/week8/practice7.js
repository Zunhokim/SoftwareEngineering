import React from "react";

class StudentInfo extends React.Component {
  constructor(props) {
    super(props);
    this.state = {stdName : "Jun Ho"};
  }
  
  shouldComponentUpdate() {
    return false;
  }
  
  changeName = () => {
    this.setState({stdName : "Hyun do"});
  }

  render() {
    return (
      <div>
        <h1>The student's name is {this.state.stdName}</h1>
        <button type="button" onClick={this.changeName}>Change Name</button>
      </div>
    );
  }
}

export default StudentInfo;