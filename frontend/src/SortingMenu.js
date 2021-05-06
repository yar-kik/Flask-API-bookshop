import {DropdownButton, Dropdown} from "react-bootstrap";
import React, {useState} from "react";


export const SortingMenu = (props) => {
    const [dropdownValue, setDropdownValue] = useState("Filter");
    const dropdownData = [
        {value: "price", order: "desc", title: "From expensive to cheap"},
        {value: "price", order: "asc", title: "From cheap to expensive"}
    ]
    const handleDropdownSorting = (dropdown) => {
        setDropdownValue(dropdown.title);
        props.checkSort(dropdown);
    }
    const dropdownItems = dropdownData.map(dropdown =>
        <Dropdown.Item key={dropdown.value}
                       onClick={() => handleDropdownSorting(dropdown)}
                       value={dropdown.value}
                       type="checkbox">{dropdown.title}</Dropdown.Item>
    )

    return (
        <DropdownButton id="dropdown-sorting-menu" size="lg"
                        title={dropdownValue}
                        className="m-2">
            {dropdownItems}
        </DropdownButton>

    )
}