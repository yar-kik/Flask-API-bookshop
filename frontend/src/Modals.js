import React, {useEffect, useState} from "react";
import {Button, Modal, Form} from "react-bootstrap";

export const ModalConfirm = (props) => {
    const onSubmit = () => {
        props.onHide();
        props.onDelete();
    }
    return (
        <Modal show={props.show} onHide={props.onHide}>
            <Modal.Header closeButton>
                <Modal.Title>Delete book</Modal.Title>
            </Modal.Header>
            <Modal.Body>Do you want to delete book?</Modal.Body>
            <Modal.Footer>
                <Button variant="danger" onClick={onSubmit}>
                    Delete
                </Button>
                <Button variant="primary" onClick={props.onHide}>
                    Close
                </Button>
            </Modal.Footer>
        </Modal>
    );
}

export const ModalEdit = (props) => {
    const [author, setAuthor] = useState();
    const [title, setTitle] = useState();
    const [category, setCategory] = useState();
    const [publisher, setPublisher] = useState();
    const [description, setDescription] = useState();
    const [pages, setPages] = useState();
    const [published, setPublished] = useState();
    const [price, setPrice] = useState();
    const [language, setLanguage] = useState();

    useEffect(() => {
        setAuthor(props.bookDetail.author);
        setTitle(props.bookDetail.title);
        setCategory(props.bookDetail.category);
        setPublisher(props.bookDetail.publisher);
        setDescription(props.bookDetail.description);
        setPages(props.bookDetail.pages);
        setPublished(props.bookDetail.published);
        setPrice(props.bookDetail.price);
        setLanguage(props.bookDetail.language);
    }, [props]);


    const submitForm = (event) => {
        event.preventDefault();
        const data = {
            author: author,
            title: title,
            category: category,
            publisher: publisher,
            description: description,
            published: published,
            pages: pages,
            language: language,
            price: price
        };
        props.handleSubmit(data);
        props.onHide();
    }
    return (
        <Modal show={props.show} onHide={props.onHide}>
            <Modal.Header closeButton>
                <Modal.Title>Edit tea</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form onSubmit={submitForm}>
                    <Form.Group controlId="editForm.authorInput">
                        <Form.Label>Author</Form.Label>
                        <Form.Control type="text"
                                      required
                                      defaultValue={author}
                                      onChange={e => setAuthor(e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="editForm.titleInput">
                        <Form.Label>Title</Form.Label>
                        <Form.Control type="text"
                                      required
                                      defaultValue={title}
                                      onChange={e => setTitle(e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="editForm.categoryInput">
                        <Form.Label>Choose category of book</Form.Label>
                        <Form.Control as="select"
                                      defaultValue={category}
                                      onChange={e => setCategory(e.target.value)}>
                            <option value="">Select category</option>
                            <option value="detective">Detective</option>
                            <option value="adventure">Adventure</option>
                            <option value="fantasy">Fantasy</option>
                        </Form.Control>
                    </Form.Group>
                    <Form.Group controlId="editForm.inputOrigin">
                        <Form.Label>Publisher</Form.Label>
                        <Form.Control type="text"
                                      defaultValue={publisher}
                                      onChange={e => setPublisher(e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="editForm.inputDescription">
                        <Form.Label>Description</Form.Label>
                        <Form.Control as="textarea" rows={4}
                                      defaultValue={description}
                                      onChange={e => setDescription(e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="editForm.inputPublished">
                        <Form.Label>Year of published</Form.Label>
                        <Form.Control type="number" min={2000} max={2021}
                                      required
                                      defaultValue={published}
                                      onChange={e => setPublished(+(e.target.value))}/>
                    </Form.Group>
                    <Form.Group controlId="editForm.inputPages">
                        <Form.Label>Number of pages</Form.Label>
                        <Form.Control type="number" min={0}
                                      defaultValue={pages}
                                      onChange={e => setPages(+(e.target.value))}/>
                    </Form.Group>
                    <Form.Group controlId="editForm.inputPrice">
                        <Form.Label>Price</Form.Label>
                        <Form.Control type="number" step="0.01" min={0} required
                                      defaultValue={price}
                                      onChange={e => setPrice(+(e.target.value))}/>
                    </Form.Group>
                    <Form.Group controlId="editForm.inputLanguage">
                        <Form.Label>Language</Form.Label>
                        <Form.Control as="select"
                                      defaultValue={language}
                                      onChange={e => setLanguage(e.target.value)}>
                            <option value="">Select language</option>
                            <option value="russian">Russian</option>
                            <option value="ukrainian">Ukrainian</option>
                            <option value="english">English</option>
                        </Form.Control>
                    </Form.Group>
                    <div className="d-flex justify-content-end">
                        <Button variant="success" type="submit"
                                className="mr-2">
                            Save
                        </Button>
                        <Button variant="primary" onClick={props.onHide}>
                            Close
                        </Button>
                    </div>
                </Form>
            </Modal.Body>
        </Modal>
    )
}

export const ModalAdd = (props) => {
    const [author, setAuthor] = useState();
    const [title, setTitle] = useState();
    const [category, setCategory] = useState();
    const [publisher, setPublisher] = useState();
    const [description, setDescription] = useState();
    const [pages, setPages] = useState();
    const [published, setPublished] = useState();
    const [price, setPrice] = useState();
    const [language, setLanguage] = useState();


    const submitForm = async (event) => {
        event.preventDefault();
        const data = {
            author: author,
            title: title,
            category: category,
            publisher: publisher,
            description: description,
            published: published,
            pages: pages,
            price: price,
            language: language
        };
        props.handleSubmit(data);
        props.onHide();
    }
    return (
        <Modal show={props.show} onHide={props.onHide}>
            <Modal.Header closeButton>
                <Modal.Title>Add book</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form onSubmit={submitForm} validated>
                    <Form.Group controlId="addForm.authorInput">
                        <Form.Label>Author</Form.Label>
                        <Form.Control required
                                      type="text"
                                      onChange={e => setAuthor(e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="addForm.titleInput">
                        <Form.Label>Title</Form.Label>
                        <Form.Control required
                                      type="text"
                                      onChange={e => setTitle(e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="addForm.inputType">
                        <Form.Label>Choose category</Form.Label>
                        <Form.Control required
                                      as="select"
                                      onChange={e => setCategory(e.target.value)}>
                            <option value="">Select category</option>
                            <option value="detective">Detective</option>
                            <option value="adventure">Adventure</option>
                            <option value="fantasy">Fantasy</option>
                        </Form.Control>
                    </Form.Group>
                    <Form.Group controlId="addForm.inputPublisher">
                        <Form.Label>Publisher</Form.Label>
                        <Form.Control type="text"
                                      onChange={e => setPublisher(e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="addForm.inputDescription">
                        <Form.Label>Description</Form.Label>
                        <Form.Control as="textarea" rows={4}
                                      onChange={e => setDescription(e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="addForm.inputPublished">
                        <Form.Label>Published</Form.Label>
                        <Form.Control type="number" min={2000} max={2021}
                                      required
                                      onChange={e => setPublished(+(e.target.value))}/>
                    </Form.Group>
                    <Form.Group controlId="addForm.inputPage">
                        <Form.Label>Number of pages</Form.Label>
                        <Form.Control type="number" min={0}
                                      onChange={e => setPages(+(e.target.value))}/>
                    </Form.Group>
                    <Form.Group controlId="addForm.inputPrice">
                        <Form.Label>Price</Form.Label>
                        <Form.Control type="number" step="0.01" min={0} required
                                      onChange={e => setPrice(+(e.target.value))}/>
                    </Form.Group>
                    <Form.Group controlId="addForm.inputLanguage">
                        <Form.Label>Language</Form.Label>
                        <Form.Control
                            onChange={e => setLanguage(e.target.value)}
                            as="select">
                            <option value="">Select language</option>
                            <option value="russian">Russian</option>
                            <option value="ukrainian">Ukrainian</option>
                            <option value="english">English</option>
                        </Form.Control>
                    </Form.Group>
                    <div className="d-flex justify-content-end">
                        <Button variant="success" type="submit"
                                className="mr-2">
                            Save
                        </Button>
                        <Button variant="primary" onClick={props.onHide}>
                            Close
                        </Button>
                    </div>
                </Form>
            </Modal.Body>
        </Modal>
    )
}