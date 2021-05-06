import {Card, Col, Row} from "react-bootstrap";
import {Link} from "react-router-dom";
import React, {Component} from "react";


class BookListContent extends Component {
    render() {
        const splitBy = 3;
        const rows = [...Array(Math.ceil(this.props.bookList.length / splitBy))];
        const bookList = rows
            .map((row, idx) =>
                this.props.bookList.slice(idx * splitBy, idx * splitBy + splitBy));

        return (
            bookList.map((row, idx) => (
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
                                    <Card.Footer style={{fontSize: "20px"}}>{book.price} ₴</Card.Footer>
                                </Card>
                            </Col>
                        ))}
                    </Row>
                )
            ));
    }
}

export default BookListContent;