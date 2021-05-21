import React, {Component} from "react";
import {
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
import Registration from "./Registration"
import Login from "./Login";
import PrivateRoute from "./PrivateRoute";
import jwt_decode from "jwt-decode";

class Main extends Component {

    constructor(props) {
        super(props);
        this.state = {
            isAuthenticated: false
        }
    }

    componentDidMount() {
        const userToken = localStorage.getItem("userToken");
        if (userToken) {
            const isAuthenticated = jwt_decode(userToken).exp < Date.now();
            if (!isAuthenticated)
                localStorage.clear();
            this.setState({isAuthenticated: isAuthenticated})
        }
    }

    render() {
        const user = this.state.isAuthenticated;
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
                            {user ? <Nav.Link as={NavLink}
                                               to="/auth/logout">Logout</Nav.Link> :
                                <Nav.Link as={NavLink}
                                          to="/auth/login" >Login</Nav.Link>}
                        </Nav>
                        <Form inline>
                            <FormControl type="text"
                                         placeholder="Search here..."
                                         className="mr-sm-2"/>
                            <Button variant="outline-info"
                                    className="mt-2 mt-sm-0">Search</Button>
                        </Form>
                    </Navbar.Collapse>
                </Navbar>
                <Container fluid className="p-5">
                    <ScrollToTop/>
                    <Switch>
                        <Route exact path="/" component={Home}/>
                        <Route path="/books/:id" component={BookDetail}/>
                        <Route path="/books" component={BookList}/>
                        <PrivateRoute user={user} path="/auth/registration"
                                      component={Registration}/>
                        <PrivateRoute user={user} path="/auth/login"
                                      component={Login}/>
                        <Route component={NotFound}/>
                    </Switch>
                </Container>
            </BrowserRouter>
        );
    }
}

export default Main;