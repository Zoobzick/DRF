import React from 'react';
import { Link } from 'react-router-dom';

function Menu() {
    return (
        <nav>
            <ul>
                <li>
                    <Link to='/projects'>projects</Link>
                </li>
                <li>
                    <Link to='/todo'>todo_list</Link>
                </li>
                <li>
                    <Link to='/'>users</Link>
                </li>
            </ul>
        </nav>
    )
}

export default Menu