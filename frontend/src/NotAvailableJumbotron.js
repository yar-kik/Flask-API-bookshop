import {Jumbotron, Button} from "react-bootstrap";
import React from "react";
import {Link} from "react-router-dom";


export const NotAvailableJumbotron = (props) => {

    return (
        <Jumbotron>
            <h1>No such page!</h1>
            <p>
                If you see this message, that means something went wrong.
                Please, return to main page.
            </p>
            <p>
                <Link to="/books?page=1"><Button variant="primary">Main page</Button></Link>
            </p>
        </Jumbotron>
    )
}