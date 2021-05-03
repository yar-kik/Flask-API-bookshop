import {Button, Form} from "react-bootstrap";
import React, {useState} from "react";

export const FilterMenu = (props) => {
    const [checked, setChecked] = useState(false);
    const handleCheckChange = (event) => {
        setChecked(props.checkChange(event));
    }
    return (
        <Form>
            <Form.Label as="h2">Filters</Form.Label>
            <Form.Group>
                <Form.Label>Category</Form.Label>
                <Form.Check
                    type="checkbox"
                    label="Detective"
                    id="detective"
                    value="detective"
                    custom
                    onChange={handleCheckChange}
                    checked={checked}
                />
                <Form.Check
                    type="checkbox"
                    label="Fantasy"
                    id="fantasy"
                    custom
                />
                <Form.Check
                    type="checkbox"
                    label="Adventure"
                    id="adventure"
                    custom
                />
                <Form.Check
                    type="checkbox"
                    label="Thriller"
                    id="thriller"
                    custom
                />
            </Form.Group>
            <Form.Group>
                <Form.Label>Publisher</Form.Label>
                <Form.Check
                    type="checkbox"
                    label="Manning Publications"
                />
                <Form.Check
                    type="checkbox"
                    label="O'Reilly"
                />
                <Form.Check
                    type="checkbox"
                    label="No Starch Press"
                />
                <Form.Check
                    type="checkbox"
                    label="Packt Publishing"
                />
            </Form.Group>
            <Form.Group>
                <Form.Label>Language</Form.Label>
                <Form.Check
                    type="checkbox"
                    label="English"
                />
                <Form.Check
                    type="checkbox"
                    label="Russian"
                />
                <Form.Check
                    type="checkbox"
                    label="Ukrainian"
                />
            </Form.Group>
            <Button>Clear filters</Button>
        </Form>
    )
}