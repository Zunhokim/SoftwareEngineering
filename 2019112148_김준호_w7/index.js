import React from 'react';
import ReactDOM from 'react-dom';
import Dongguk from './practice4.js';
import Staff from './practice5.js';
// import App from './App';
// import reportWebVitals from './reportWebVitals';

const practice2 = <h1>Hi everyone!</h1>;
ReactDOM.render(practice2, document.getElementById('root2'));

const practice3_1 = (
    <div>
        <h1>Class Name</h1>
        Mobile Software
    </div>
    
);
ReactDOM.render(practice3_1, document.getElementById('root3_1'));

const practice3_2 = (
    <div>
        <h1> Proffesor's Name</h1>
        Woongsup Kim
    </div>
)
ReactDOM.render(practice3_2, document.getElementById('root3_2'));

const practice3_3 = (
    <div>
        <h1>List of Students</h1>
        <ul>
            <li>Junho Kim</li>
            <li>Hyundo Park</li>
            <li>Heonyoung Jeong</li>
        </ul>
    </div>
)
ReactDOM.render(practice3_3, document.getElementById('root3_3'));

ReactDOM.render(<Dongguk/>, document.getElementById('root4'));

ReactDOM.render(<Staff/>, document.getElementById('root5'))

// reportWebVitals();
