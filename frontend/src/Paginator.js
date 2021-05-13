import {Pagination} from "react-bootstrap";
import React, {Component} from "react";

class Paginator extends Component {

    render() {
        const delta = 1;
        const pageNumbers = [];
        const paginationItems = [];
        let temp;
        const amountPages = this.props.amountPages;
        const currentPage = this.props.currentPage;

        for (let i = 1; i <= amountPages; i++) {
            if (i === 1 ||
                i === amountPages ||
                ((currentPage - delta) <= i &&
                i < (currentPage + delta + 1))) {
                pageNumbers.push(i);
            }
        }

        for (let i of pageNumbers) {
            if (temp) {
                if (i - temp === 2)
                    paginationItems.push(
                        <Pagination.Item
                            onClick={(e) => this.props.handlePageChange(temp + 1)}
                            key={temp + 1}
                            active={temp + 1 === currentPage}>
                            {temp + 1}
                        </Pagination.Item>
                    );
                else if (i - temp !== 1) {
                    paginationItems.push(<Pagination.Ellipsis
                        key={i + "..."}
                        disabled={true}/>)
                }
            }
            paginationItems.push(
                <Pagination.Item
                    onClick={(e) => this.props.handlePageChange(i)}
                    key={i}
                    active={i === currentPage}>
                    {i}
                </Pagination.Item>
            )
            temp = i;
        }

        return (
            <Pagination>
                <Pagination.First
                    onClick={() => this.props.handlePageChange(1)}
                    disabled={currentPage === 1}
                    key="first"/>
                <Pagination.Prev
                    onClick={() => this.props.handlePageChange(currentPage - 1)}
                    disabled={currentPage === 1}
                    key="prev"/>

                {paginationItems}

                <Pagination.Next
                    onClick={() => this.props.handlePageChange(currentPage + 1)}
                    disabled={currentPage === amountPages}
                    key="next"/>
                <Pagination.Last
                    onClick={() => this.props.handlePageChange(amountPages)}
                    disabled={currentPage === amountPages}
                    key="last"/>
            </Pagination>
        )
    }
}

export default Paginator;