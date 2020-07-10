import React, { Component } from 'react';
//import{SplitButton,MenuItem}from'react-bootstrap';
//import { Button } from 'react-bootstrap';

export class header extends Component {
    render() {
        return (
            <div>
                <nav class="navbar navbar-expand-sm bg-white">        
                    <div class="container-fluid">
                        <a class="navbar-brand" href="#"><img src="/Images/consultadd_logo.png" height="50"/></a>
                    </div>
                </nav>
            </div>
        )
    }
}

export default header
