import React from "react";

class Dongguk extends React.Component {
    constructor() {
        super();
        this.state = {name: "jun ho"};
    }
    render() {
        return <h1>HI {this.state.name}!</h1>;
    }
}

export default Dongguk;