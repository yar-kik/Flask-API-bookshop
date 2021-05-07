import React, {Component} from "react";
import {
    NavDropdown,
    Button,
    Container,
    Navbar,
    Nav,
    Form,
    FormControl
} from "react-bootstrap";
import {Route, NavLink, BrowserRouter, Switch} from "react-router-dom";

import Home from "./Home";
import BookDetail from "./BookDetail";
import BookList from "./BookList"
import NotFound from "./NotFound";
import ScrollToTop from "./ScrollToTop";

class Main extends Component {
    render() {
        return (
            <BrowserRouter>
                <Navbar bg="dark" variant="dark" collapseOnSelect expand="md">
                    <Navbar.Brand as={NavLink} exact to="/">Programming
                        World</Navbar.Brand>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
                    <Navbar.Collapse id="responsive-navbar-nav">
                        <Nav className="mr-auto">
                            <Nav.Link as={NavLink}
                                      to="/books">Assortment</Nav.Link>
                        </Nav>
                        <Form inline>
                            <FormControl type="text" placeholder="Search here..."
                                         className="mr-sm-2"/>
                            <Button variant="outline-info" className="mt-2 mt-sm-0">Search</Button>
                        </Form>
                    </Navbar.Collapse>
                </Navbar>
                <Container fluid className="p-5">
                    <ScrollToTop/>
                    <Switch>
                        <Route exact path="/" component={Home}/>
                        <Route path="/books/:id" component={BookDetail}/>
                        <Route path="/books" component={BookList}/>
                        <Route component={NotFound}/>
                    </Switch>
                </Container>
            </BrowserRouter>
        )
            ;
    }
}

export default Main;