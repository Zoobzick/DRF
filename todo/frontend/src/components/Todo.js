import React from 'react'

const TodoItem = ({ item }) => {
    console.log(item)
    return (
        <tbody>
            <tr>
                <td>
                    {item.url}
                </td>
                <td>
                    {item.text}
                </td>
                <td>
                    {item.is_active}
                </td>
                <td>
                    {item.project.name}
                </td>
                <td>
                    {item.user}
                </td>
            </tr>
        </tbody>
    )
}

const TodosList = ({ todos }) => {

    return (
        <table>
            <thead>
                <tr>
                    <th>URL</th>
                    <th>Text</th>
                    <th>Is_active</th>
                    <th>Project_name</th>
                    <th>User</th>
                </tr>
            </thead>
            {todos.map((todo) => <TodoItem item={todo} />)}
        </table>
    )
}

export default TodosList