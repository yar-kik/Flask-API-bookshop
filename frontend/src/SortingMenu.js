import {ButtonGroup, ToggleButton} from "react-bootstrap";
import React, {useState} from "react";


export const SortingMenu = (props) => {
    const [buttonValue, setButtonValue] = useState("title");
    return (
        <>
            <ButtonGroup toggle aria-label="sorting-menu" className="m-2">
                <ToggleButton checked={buttonValue === "title"}
                              onChange={e => setButtonValue(e.currentTarget.value)}
                              type="radio"
                              variant="primary"
                              value="title">Title</ToggleButton>
                <ToggleButton checked={buttonValue === "price"}
                              onChange={e => setButtonValue(e.currentTarget.value)} type="radio" variant="primary" value="price">Price (Ascending)</ToggleButton>
                <ToggleButton checked={buttonValue === "pr"}
                              onChange={e => setButtonValue(e.currentTarget.value)} type="radio" variant="primary" value="pr">Price (Descending)</ToggleButton>
            </ButtonGroup>
        </>
    )
}