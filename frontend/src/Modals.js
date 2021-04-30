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
    const [brand, setBrand] = useState("");
    const [title, setTitle] = useState("");
    const [type, setType] = useState("");
    const [origin, setOrigin] = useState("");
    const [description, setDescription] = useState("");
    const [price, setPrice] = useState(0);

    useEffect(() => {
        setBrand(props.teaDetail.brand);
        setTitle(props.teaDetail.title);
        setType(props.teaDetail.type);
        setOrigin(props.teaDetail.origin);
        setDescription(props.teaDetail.description);
        setPrice(props.teaDetail.price);
    }, [props]);

    const submitForm = (event) => {
        event.preventDefault();
        const data = {
            brand: brand,
            title: title,
            type: type,
            origin: origin,
            description: description,
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
                    <Form.Group controlId="editForm.brandInput">
                        <Form.Label>Brand</Form.Label>
                        <Form.Control type="text"
                                      required
                                      defaultValue={brand}
                                      onChange={e => setBrand(e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="editForm.titleInput">
                        <Form.Label>Title</Form.Label>
                        <Form.Control type="text"
                                      required
                                      defaultValue={title}
                                      onChange={e => setTitle(e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="editForm.inputType">
                        <Form.Label>Choose type of tea</Form.Label>
                        <Form.Control as="select"
                                      defaultValue={type}
                                      onChange={e => setType(e.target.value)}>
                            <option value="black tea">Black tea</option>
                            <option value="green tea">Green tea</option>
                            <option value="fruit tea">Fruit tea</option>
                        </Form.Control>
                    </Form.Group>
                    <Form.Group controlId="editForm.inputOrigin">
                        <Form.Label>Origin</Form.Label>
                        <Form.Control type="text"
                                      defaultValue={origin}
                                      onChange={e => setOrigin(e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="editForm.inputDescription">
                        <Form.Label>Description</Form.Label>
                        <Form.Control as="textarea" rows={4}
                                      defaultValue={description}
                                      onChange={e => setDescription(e.target.value)}/>
                    </Form.Group>
                    <Form.Group controlId="editForm.inputPrice">
                        <Form.Label>Origin</Form.Label>
                        <Form.Control type="number" step="0.01" min={0}
                                      required
                                      defaultValue={price}
                                      onChange={e => setPrice(+(e.target.value))}/>
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
    const [author, setAuthor] = useState("");
    const [title, setTitle] = useState("");
    const [category, setCategory] = useState("black tea");
    const [publisher, setPublisher] = useState("");
    const [description, setDescription] = useState("");
    const [pages, setPages] = useState(0);
    const [published, setPublished] = useState(0);

    const submitForm = async (event) => {
        event.preventDefault();
        const data = {
            author: author,
            title: title,
            category: category,
            publisher: publisher,
            description: description,
            // published: published,
            pages: pages
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
                        <Form.Label>Choose type of tea</Form.Label>
                        <Form.Control required
                                      as="select"
                                      onChange={e => setCategory(e.target.value.toLowerCase())}>
                            <option value="">Select category</option>
                            <option value="Detective">Black tea</option>
                            <option value="Adventure">Green tea</option>
                            <option value="Fantasy">Fruit tea</option>
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
                    <Form.Group controlId="addForm.inputPrice">
                        <Form.Label>Published</Form.Label>
                        <Form.Control type="number" step="0.01" min={0}
                                      onChange={e => setPublished(+(e.target.value))}/>
                    </Form.Group>
                    <Form.Group controlId="addForm.inputPrice">
                        <Form.Label>Number of pages</Form.Label>
                        <Form.Control type="number" step="0.01" min={0}
                                      onChange={e => setPages(+(e.target.value))}/>
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