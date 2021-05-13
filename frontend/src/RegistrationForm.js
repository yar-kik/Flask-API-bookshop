import React, {useState} from "react";
import {Button, Form} from "react-bootstrap";

export const RegistrationForm = (props) => {

    const [showPass, setShowPass] = useState(false);
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const submitForm = (e) => {
        e.preventDefault();
        const data = {email: email, username: username, password: password};
        props.registrationSubmit(data);
    }

    return (
        <Form onSubmit={submitForm}>
            <Form.Group controlId="formRegistrationEmail">
                <Form.Label>Email address</Form.Label>
                <Form.Control type="email" placeholder="Enter email" autoComplete="email"
                              onChange={event => setEmail(event.currentTarget.value)}/>
            </Form.Group>

            <Form.Group controlId="formRegistrationUsername">
                <Form.Label>Username</Form.Label>
                <Form.Control type="text" placeholder="Enter username" autoComplete="username"
                              onChange={event => setUsername(event.currentTarget.value)}/>
            </Form.Group>

            <Form.Group controlId="formRegistrationPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control type={showPass? "text": "password"}
                              placeholder="Password" autoComplete="new-password"
                              onChange={event => setPassword(event.currentTarget.value)}/>
            </Form.Group>

            <Form.Group controlId="formRegistrationCheckbox">
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