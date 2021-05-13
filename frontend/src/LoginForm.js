import React, {useState} from "react";
import {Button, Form} from "react-bootstrap";

export const LoginForm = (props) => {

    const [showPass, setShowPass] = useState(false);
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const submitForm = (e) => {
        e.preventDefault();
        const data = {
            username: username,
            password: password
        };
        props.loginSubmit(data);
    }

    return (
        <Form onSubmit={submitForm}>
            <Form.Group controlId="formLoginUsername">
                <Form.Label>Email address or username</Form.Label>
                <Form.Control type="text" placeholder="Enter email or username"
                              autoComplete="username"
                              onChange={event => setUsername(event.currentTarget.value)}/>
            </Form.Group>

            <Form.Group controlId="formLoginPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control type={showPass? "text": "password"}
                              placeholder="Password" autoComplete="current-password"
                              onChange={event => setPassword(event.currentTarget.value)}/>
            </Form.Group>

            <Form.Group controlId="formLoginCheckbox">
                <Form.Check type="checkbox"
                            label={showPass? "Hide password": "Show password"}
                            onChange={() => setShowPass(!showPass)}
                />
            </Form.Group>
            <Button variant="primary" type="submit">
                Submit
            </Button>
        </Form>
    )
}