import {Nav} from "react-bootstrap";
import {NavLink} from "react-router-dom";
import React from "react";

export const LoginLogoutButton = (props) => {

    if (props.user)
        return <Nav.Link as={NavLink}
                         to="/auth/logout">Logout</Nav.Link>
    else
        return <Nav.Link as={NavLink}
                         to="/auth/login">Login</Nav.Link>

}