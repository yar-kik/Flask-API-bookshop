import React, {Component} from "react";
import {Col, Row, Button} from "react-bootstrap";
import axios from "axios";
import {ModalAdd} from "./Modals";
import Paginator from "./Paginator";
import BookListContent from "./BookListContent";
import {FilterMenu} from "./FilterMenu";


class BookList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            bookList: [],
            modalAdd: false,
            unique: false,
            currentPage: Number.parseInt(new URLSearchParams(this.props.history.location.search).get("page")) || 1,
            amountPages: 0
        }
        this.showModalAdd = this.showModalAdd.bind(this);
        this.createNewBook = this.createNewBook.bind(this);
        this.handlePageClick = this.handlePageClick.bind(this);
        this.handlePageChange = this.handlePageChange.bind(this);
        this.checkChange = this.checkChange.bind(this);

    }

    componentDidMount() {
        this.refreshList({page: this.state.currentPage});
    }

    handlePageClick = (event) => {
        const pageNumber = Number.parseInt(event.target.getAttribute("data-page"));
        this.setState({currentPage: pageNumber});
        const params = new URLSearchParams({page: pageNumber.toString()});
        this.refreshList(params);
    }
    handlePageChange = (pageNumber) => {
        this.setState({currentPage: pageNumber});
        const params = new URLSearchParams({page: pageNumber});
        this.refreshList(params);
    }

    checkChange = (event) => {
        const checked = event.target.checked;
        const value = event.target.value;
        const params = new URLSearchParams({category: "fantasy"});
        params.append("category", value);
        if (checked)
            this.refreshList(params)
        else
            this.refreshList({page: this.state.currentPage})
        console.log(checked);
        console.log(value);
        return checked;
    }

    refreshList = (params) => {
        axios
            .get("/books", {params: params})
            .then((result) => {
                this.setState({bookList: result.data.books});
                this.setState({amountPages: result.data.pages_amount});
                this.props.history.push({search: params.toString()});
            })
            .catch((error) => console.error(error));
    }

    createNewBook = (data) => {
        axios
            .post('/books/', data)
            .then(() => this.refreshList())
            .catch((error) => console.error(error.response.data.message));
    }

    showModalAdd = () => {
        this.setState({modalAdd: !this.state.modalAdd})
    }

    handleSubmit = (data) => {
        this.createNewBook(data);
    }

    render() {
        return (
            <>
                <Row key="buttonRow">
                    <Col className="d-flex justify-content-end">
                        <Button size="lg" variant="primary"
                                onClick={this.showModalAdd}>Add new
                            item</Button>
                    </Col>
                </Row>
                <ModalAdd show={this.state.modalAdd}
                          onHide={this.showModalAdd}
                          handleSubmit={this.handleSubmit}/>
                <Row>
                    <Col md={2}>
                        <FilterMenu checkChange={this.checkChange}/>
                    </Col>
                    <Col md={10}>
                        <BookListContent bookList={this.state.bookList}/>
                    </Col>
                </Row>
                <Row className="d-flex justify-content-center">
                    <Col md={{span: "auto"}} className="mt-5">
                        <Paginator amountPages={this.state.amountPages}
                                   currentPage={this.state.currentPage}
                                   handlePageClick={this.handlePageClick}
                                   handlePageChange={this.handlePageChange}
                        />
                    </Col>
                </Row>
            </>
        );
    }
}

export default BookList;