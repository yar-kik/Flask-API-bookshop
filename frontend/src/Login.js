import React, {Component} from "react";
import axios from "axios";
import {LoginForm} from "./LoginForm"
import {Col, Row} from "react-bootstrap";

class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    componentDidMount() {
    }

    sendLoginRequest = (data) => {
        const username = data.username;
        const password = data.password;
        const token = Buffer.from(`${username}:${password}`, 'utf8').toString('base64');
        axios
            .post("/auth/login", data, {
                headers: {'Authorization': `Basic ${token}`}
            })
            .then(result => {
                localStorage.setItem("userToken", result.data.token);
                this.props.history.replace("/books")
            })
            .catch(error => console.error(error))
    }

    handleLogin = (data) => {
        this.sendLoginRequest(data);
    }

    render() {
        return (
            <Row>
                <Col md={{span: 5, offset: 3}}>
                    <LoginForm loginSubmit={this.handleLogin}/>
                </Col>
            </Row>
        )
    }
}

export default Login;