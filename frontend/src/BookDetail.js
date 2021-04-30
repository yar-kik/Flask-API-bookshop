import React, {Component} from "react";
import {Button, Row, Col, Image, Card, Table} from "react-bootstrap";
import axios from "axios";
import NotFound from "./NotFound";
import {ModalEdit, ModalConfirm} from "./Modals"

class BookDetail extends Component {
    constructor(props) {
        super(props);
        this.state = {
            bookDetail: {},
            error: false,
            modalEdit: false,
            modalConfirm: false
        };
        this.deleteBook = this.deleteBook.bind(this);
        this.showModalEdit = this.showModalEdit.bind(this);
        this.showModalConfirm = this.showModalConfirm.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentDidMount() {
        this.getDetail();
    }

    deleteBook() {
        axios
            .delete(`/tea/${this.state.bookDetail.slug}`)
            .then(() => this.props.history.push('/book'))
            .catch(error => console.error(error))
    }

    getDetail() {
        axios
            .get(`/tea/${this.props.match.params.slug}`)
            .then((result) =>
                this.setState({bookDetail: result.data}))
            .catch(error => {
                console.error(error);
                this.setState({error: true})
            });
    }

    editBook(data){
        axios
            .patch(`/tea/${this.state.bookDetail.slug}`, data)
            .then(Object.assign(this.state.bookDetail, data))
            .catch(error => console.error(error))
    }

    showModalEdit() {
        this.setState({modalEdit: !this.state.modalEdit})
    }

    showModalConfirm() {
        this.setState({modalConfirm: !this.state.modalConfirm})
    }

    handleSubmit(data){
        let newData = {};
        for (let [key, value] of Object.entries(data))
            if (this.state.bookDetail[key] !== value)
                newData[key] = value;
        if (Object.keys(newData).length) {
            this.editBook(newData);
        }
    }

    render() {
        if (!this.state.error) {
            return (
                <>
                    <Row className="m-3">
                        <Col sm={9} md={4} className="mb-3">
                            <Image
                                src="https://miychay.com/upload/iblock/7c6/7c664063ba5e6215cb3567de3330c187.jpg"
                                fluid/>
                        </Col>
                        <Col sm={9} md={6}>
                            <Card>
                                <Card.Header
                                    as="h2">{this.state.bookDetail.brand} {this.state.bookDetail.title}
                                </Card.Header>
                                <Card.Body>
                                    <Card.Title>Description</Card.Title>
                                    <Card.Text>{this.state.bookDetail.description}</Card.Text>
                                    <Table borderless>
                                        <tbody>
                                        <tr>
                                            <td>Origin</td>
                                            <td>{this.state.bookDetail.origin}</td>
                                        </tr>
                                        <tr>
                                            <td>Type</td>
                                            <td>{this.state.bookDetail.type}</td>
                                        </tr>
                                        </tbody>
                                    </Table>
                                    <Card.Title>Price {this.state.bookDetail.price}₴</Card.Title>
                                </Card.Body>
                                <Card.Footer>
                                    <Row>
                                        <Col><Button block onClick={this.showModalEdit}
                                                     variant="outline-primary">Edit</Button></Col>
                                        <Col><Button block onClick={this.showModalConfirm}
                                                     variant="outline-danger">Delete</Button></Col>
                                    </Row>
                                </Card.Footer>
                            </Card>
                        </Col>
                    </Row>
                    <ModalConfirm show={this.state.modalConfirm}
                                  onHide={this.showModalConfirm}
                                  onDelete={this.deleteBook}/>
                    <ModalEdit show={this.state.modalEdit}
                               onHide={this.showModalEdit}
                               teaDetail={this.state.bookDetail}
                               handleSubmit={this.handleSubmit}/>
                </>
            );
        } else {
            return <NotFound/>
        }
    }

}

export default BookDetail;