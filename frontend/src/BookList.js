import React, {Component} from "react";
import {Pagination, Col, Card, Row, Button} from "react-bootstrap";
import axios from "axios";
import {Link} from "react-router-dom";
import {ModalAdd} from "./Modals";


class BookList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            bookList: [],
            modalAdd: false,
            unique: false,
            currentPage: Number.parseInt(new URLSearchParams(this.props.history.location.search).get("page")) || 1,
            amountPages: 2
        }
        this.showModalAdd = this.showModalAdd.bind(this);
        this.createNewBook = this.createNewBook.bind(this);
        this.handlePageClick = this.handlePageClick.bind(this);
        this.handlePageChange = this.handlePageChange.bind(this);

    }

    componentDidMount() {
        this.refreshList(this.state.currentPage);
    }

    handlePageClick = (event) => {
        const pageNumber = Number.parseInt(event.target.getAttribute("data-page"));
        this.setState({currentPage: pageNumber});
        this.refreshList(pageNumber);
    }
    handlePageChange = (pageNumber) => {
        this.setState({currentPage: pageNumber});
        this.refreshList(pageNumber);
    }

    refreshList = (page) => {
        axios
            .get(`/books?page=${page}`)
            .then((result) => {
                this.setState({bookList: result.data});
                this.props.history.push(`?page=${page}`)
            })
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
                            <Card.Footer>Number of pages
                                - {book.pages}</Card.Footer>
                        </Card>
                    </Col>
                ))}
            </Row>
        ))

        let paginationItems = [];
        // const amountPages = pagination.data.length / pagination.numberPerPage;
        const amountPages = this.state.amountPages;
        const currentPage = this.state.currentPage;
        let ellipsis = true;
        for (let number = 1; number <= amountPages; number++) {
            if (amountPages > 4) {
                if (number <= 3 || number >= amountPages - 1)
                    paginationItems.push(
                        <Pagination.Item onClick={this.handlePageClick}
                                         key={number}
                                         active={number === currentPage}
                                         data-page={number}>
                            {number}
                        </Pagination.Item>
                    );
                else if (ellipsis) {
                    paginationItems.push(<Pagination.Ellipsis
                        // onClick={handleEllipsisClick}
                    />)
                    ellipsis = false;
                }
            } else {
                paginationItems.push(
                    <Pagination.Item onClick={this.handlePageClick}
                                     key={number}
                                     active={number === currentPage}
                                     data-page={number}>
                        {number}
                    </Pagination.Item>
                );
            }
        }

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
                          handleSubmit={this.handleSubmit}/>

                <Row className="d-flex justify-content-center">
                    <Col md={{span: "auto"}} className="mt-5">
                        <Pagination>
                            <Pagination.First
                                onClick={() => this.handlePageChange(1)}/>
                            <Pagination.Prev
                            onClick={() => this.handlePageChange(this.state.currentPage - 1)}/>
                            {paginationItems}
                            <Pagination.Next
                            onClick={() => this.handlePageChange(this.state.currentPage + 1)}/>
                            <Pagination.Last
                            onClick={() => this.handlePageChange(this.state.amountPages)}/>
                        </Pagination>
                    </Col>
                </Row>
            </>
        );
    }
}

export default BookList;