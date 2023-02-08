import React from 'react'

const ProjectItem = ({ item }) => {
    return (
        <tbody>
            <tr>
                <td>
                    {item.url}
                </td>
                <td>
                    {item.name}
                </td>
                <td>
                    {item.repo_name}
                </td>
                <td>
                    {item.users}
                </td>
            </tr>
        </tbody>
    )
}

const ProjectsList = ({ projects }) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>
                        URL
                    </th>
                    <th>
                        Name
                    </th>
                    <th>
                        Repo_link
                    </th>
                    <th>
                        Users
                    </th>
                </tr>
            </thead>
            {projects.map((project) => <ProjectItem item={project} />)}
        </table>
    )
}

export default ProjectsList