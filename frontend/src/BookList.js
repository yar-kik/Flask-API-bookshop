import React, {Component} from "react";
import {Col, Card, Row, Button} from "react-bootstrap";
import axios from "axios";
import {Link} from "react-router-dom";
import {ModalAdd} from "./Modals";


class BookList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            bookList: [],
            modalAdd: false,
            unique: false
        }
        this.showModalAdd = this.showModalAdd.bind(this);
        this.createNewBook = this.createNewBook.bind(this);
    }

    componentDidMount() {
        this.refreshList();
    }

    refreshList = () => {
        axios
            .get("/books/")
            .then((result) =>
                this.setState({bookList: result.data}))
            .catch((error) => console.error(error));
    }

    createNewBook = (data) => {
        axios
            .post('/books/', data)
            .then((response) => this.refreshList())
            .catch((error) => console.error(error.response.data.message));
    }

    showModalAdd = () => {
        this.setState({modalAdd: !this.state.modalAdd})
    }

    handleSubmit = (data) => {
        this.createNewBook(data);
    }

    render() {
        const splitBy = 3;
        const rows = [...Array(Math.ceil(this.state.bookList.length / splitBy))];
        const teaList = rows
            .map((row, idx) =>
                this.state.bookList.slice(idx * splitBy, idx * splitBy + splitBy));

        const content = teaList.map((row, idx) => (
            <Row key={idx} className="m-3">
                {row.map(book => (
                    <Col md={12 / 2} lg={12 / 3} key={book.id}>
                        <Card>
                            <Link to={`/books/${book.id}`}>
                                <Card.Img variant="top"
                                          src="https://covervault.com/wp-content/uploads/2018/07/092-5.5x8.5-Standing-Paperback-Book-Mockup-Prev1.jpg"/>
                            </Link>
                            <Card.Body>
                                <Card.Title>{book.author} "{book.title}"</Card.Title>
                                <Card.Text>{book.description}</Card.Text>
                            </Card.Body>
                            <Card.Footer>Number of pages - {book.pages}</Card.Footer>
                        </Card>
                    </Col>
                ))}
            </Row>
        ))
        return (
            <>
                <Row key="buttonRow">
                    <Col className="d-flex justify-content-end">
                        <Button size="lg" variant="primary"
                                onClick={this.showModalAdd}>Add new
                            item</Button>
                    </Col>
                </Row>
                {content}
                <ModalAdd show={this.state.modalAdd}
                          onHide={this.showModalAdd}
                          handleSubmit={this.handleSubmit}
                />
            </>
        );
    }
}

export default BookList;