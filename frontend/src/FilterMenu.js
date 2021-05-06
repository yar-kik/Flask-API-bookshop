import {Button, DropdownButton, Form} from "react-bootstrap";
import React from "react";

export const FilterMenu = (props) => {
    const style = {
        padding: "5px",
        margin: "10px"
    }
    const handleFilterChange = (event) => {
        const checked = event.target.checked;
        const value = event.target.value;
        const filter = event.target.getAttribute("data-filter");
        props.checkChange(checked, value, filter);
    }

    const filterData = [
        {
            filter: "category", data: [
                {value: "detective", label: "Detective"},
                {value: "fantasy", label: "Fantasy"},
                {value: "adventure", label: "Adventure"},
                {value: "thriller", label: "Thriller"}
            ]
        }, {
            filter: "publisher", data: [
                {value: "Manning Publications", label: "Manning Publications"},
                {value: "O'Reilly", label: "O'Reilly"},
                {value: "No Starch Press", label: "No Starch Press"},
                {value: "Packt Publishing", label: "Packt Publishing"}
            ]
        }, {
            filter: "language", data: [
                {value: "ukrainian", label: "Ukrainian"},
                {value: "russian", label: "Russian"},
                {value: "english", label: "English"}
            ]
        }];


    const filters = filterData.map(filter =>
        <Form.Group>
            <Form.Label>{filter.filter}</Form.Label>
            {filter.data.map(data =>
                <Form.Check
                    key={data.value}
                    type="checkbox"
                    data-filter={filter.filter}
                    label={data.label}
                    id={data.value}
                    value={data.value}
                    custom
                    onChange={handleFilterChange}/>
            )}
        </Form.Group>
    )

    return (
        <DropdownButton title="Filter"
                        id="dropdown-filter-menu"
                        size="lg"
                        className="m-2">
            <Form style={style}>
                <Form.Label as="h3">Filters</Form.Label>
                {filters}
            </Form>
        </DropdownButton>
    )
}