import React, {Component} from "react";
import {Container, Table} from "react-bootstrap";

class Home extends Component {
    render() {
        return (
            <Container className="mt-3" fluid>
                <Table striped bordered hover>
                    <thead>
                    <tr>
                        <th>Brand</th>
                        <th>Title</th>
                        <th>Type</th>
                        <th>Price</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>Hyleys</td>
                        <td>English Aristocratic Tea</td>
                        <td>Black tea</td>
                        <td>50</td>
                    </tr>
                    </tbody>
                </Table>
            </Container>
        );
    }
}

export default Home;