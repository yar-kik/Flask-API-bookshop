import React from 'react';
import {Route, Redirect} from 'react-router-dom';

const PrivateRoute = ({component: Component, user, ...rest}) => {
    return (
        <Route {...rest} render={
            props => {
                if (!user) {
                    return <Component {...rest} {...props} />
                } else {
                    return <Redirect to="/books"/>
                }
            }
        }/>
    )
}

export default PrivateRoute;