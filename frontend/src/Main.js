import {Component} from "react";
import {Route, NavLink, BrowserRouter, Switch} from "react-router-dom";
import Home from "./Home";
import BookDetail from "./BookDetail";
import BookList from "./BookList"
import {Container, Navbar, Nav} from "react-bootstrap";
import NotFound from "./NotFound";

class Main extends Component {
    render() {
        return (
            <BrowserRouter>
                <Navbar bg="dark" variant="dark">
                    <Nav className="mr-auto">
                        <Navbar.Brand as={NavLink} exact
                                      to="/">Home</Navbar.Brand>
                        <Nav.Link as={NavLink} to="/books">Assortment</Nav.Link>
                    </Nav>
                </Navbar>
                <Container fluid className="p-5">
                    <Switch>
                        <Route exact path="/" component={Home}/>
                        <Route path="/books/:id" component={BookDetail}/>
                        <Route path="/books" component={BookList}/>
                        <Route component={NotFound}/>
                    </Switch>
                </Container>
            </BrowserRouter>
        );
    }
}

export default Main;