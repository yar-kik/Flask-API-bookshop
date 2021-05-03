import {Pagination} from "react-bootstrap";
import React, {Component} from "react";

class Paginator extends Component {

    render() {
        const paginationItems = [];
        const amountPages = this.props.amountPages;
        const currentPage = this.props.currentPage;

        let ellipsis = true;
        for (let number = 1; number <= amountPages; number++) {
            if (amountPages > 5) {
                if (number <= 3 || number >= amountPages - 1)
                    paginationItems.push(
                        <Pagination.Item onClick={this.props.handlePageClick}
                                         key={number}
                                         active={number === currentPage}
                                         data-page={number}>
                            {number}
                        </Pagination.Item>
                    );
                else if (ellipsis) {
                    paginationItems.push(<Pagination.Ellipsis
                        // onClick={handleEllipsisClick}
                    />)
                    ellipsis = false;
                }
            } else {
                paginationItems.push(
                    <Pagination.Item onClick={this.props.handlePageClick}
                                     key={number}
                                     active={number === currentPage}
                                     data-page={number}>
                        {number}
                    </Pagination.Item>
                );
            }
        }

        return (
            <Pagination>
                <Pagination.First
                    onClick={() => this.props.handlePageChange(1)}
                    disabled={currentPage === 1}
                />
                <Pagination.Prev
                    onClick={() => this.props.handlePageChange(currentPage - 1)}
                    disabled={currentPage === 1}/>
                {paginationItems}
                <Pagination.Next
                    onClick={() => this.props.handlePageChange(currentPage + 1)}
                    disabled={currentPage === amountPages}/>
                <Pagination.Last
                    onClick={() => this.props.handlePageChange(amountPages)}
                    disabled={currentPage === amountPages}/>
            </Pagination>
        )
    }
}

export default Paginator;