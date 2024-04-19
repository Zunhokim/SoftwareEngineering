// Ex 1로 풀이
// import React from "react";

// class StaffInfo extends React.Component {
//     render() {
//         return <h4>Welcome to {this.props.com_name} Customer Service. My name is {this.props.stf_name}. How can I help you?</h4>;
//     }
// }

// class Staff extends React.Component {
//     render() {
//         return (
//             <div>
//                 <h1>How to answer a phone when a customer calls.</h1>
//                 <StaffInfo com_name = "Nexon" stf_name = "Jun Ho" />
//             </div>
//         );
//     }
// }

// export default Staff;

// Ex 3으로 풀이

import React from "react";

class StaffInfo extends React.Component {
    render() {
        return <h4>Welcome to {this.props.name.com_name} Customer Service. My name is {this.props.name.stf_name}. How can I help you?</h4>;
    }
}

class Staff extends React.Component {
    render() {
        const com_info = {com_name: "NEXON", stf_name: "jun ho"}
        return (
            <div>
                <h1>How to answer a phone when a customer calls.</h1>
                <StaffInfo name = {com_info} />
            </div>
        );
    }
}

export default Staff;