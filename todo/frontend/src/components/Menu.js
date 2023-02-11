import React from 'react';
import { Link } from 'react-router-dom';
import App from '../App';
import is_authenticated from '../App.js'


function Menu() {
    return (
        <nav>
            <ul>
                <li>
                    <Link to='/projects'>Projects</Link>
                </li>
                <li>
                    <Link to='/todo'>Todo_list</Link>
                </li>
                <li>
                    <Link to='/'>Users</Link>
                </li>
            </ul>
        </nav>
    )
}

export default Menu