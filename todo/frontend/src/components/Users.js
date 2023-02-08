import React from 'react'

const UserItem = ({ item }) => {
    return (
        <tbody>
            <tr>
                <td>
                    {item.username}
                </td>
                <td>
                    {item.first_name}
                </td>
                <td>
                    {item.last_name}
                </td>
            </tr>
        </tbody>
    )
}

const UserList = ({ users }) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>User name</th>
                    <th>First name</th>
                    <th>Last name</th>
                </tr>
            </thead>
            {users.map((user) => <UserItem item={user} />)}
        </table>
    )
}

export default UserList