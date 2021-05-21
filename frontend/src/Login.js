import React, {Component} from "react";
import axios from "axios";
import {LoginForm} from "./LoginForm"
import {Col, Row} from "react-bootstrap";

class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: ""
        };
    }

    componentDidMount() {
    }

    sendLoginRequest = (data) => {
        const token = Buffer.from(`${data.username}:${data.password}`, 'utf8').toString('base64');
        axios
            .post("/auth/login", data, {
                headers: {'Authorization': `Basic ${token}`}
            })
            .then(result => {
                localStorage.setItem("userToken", result.data.token);
                this.props.history.replace({
                    pathname: '/books',
                    state: {isAuthenticated: true}
                });
            })
            .catch(error => {
                console.error(error);
                this.setState({error: error.response.data.message});
            })
    }

    handleLogin = (data) => {
        this.sendLoginRequest(data);
    }

    render() {
        return (
            <Row>
                <Col md={{span: 5, offset: 3}}>
                    <LoginForm loginSubmit={this.handleLogin}
                               error={this.state.error}/>
                </Col>
            </Row>
        )
    }
}

export default Login;