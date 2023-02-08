import React from 'react';
import './App.css';

import axios from 'axios';
import Menu from './components/Menu'
import UserList from './components/Users'
import TodosList from './components/Todo'
import ProjectsList from './components/Projects'
import { Route, Link, BrowserRouter, Switch } from 'react-router-dom';


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'todos': []
    }
  }

  componentDidMount() {
    axios.get('http://192.168.0.20:8000/api/users/')
      .then(response => {
        const users = response.data.results
        console.log(users)
        this.setState({
          'users': users
        }
        )
      }).catch(error => console.log(error))

    axios.get('http://192.168.0.20:8000/api/todo/')
      .then(response => {
        const todos = response.data.results
        this.setState({
          'todos': todos
        }
        )
      }).catch(error => console.log(error))
    axios.get('http://192.168.0.20:8000/api/projects/')
      .then(response => {
        const projects = response.data.results
        this.setState({
          'projects': projects
        }
        )
      }).catch(error => console.log(error))
  }




  render() {

    return (
      < div className='App'>

        < Menu />

        <Route exact path='/' component={() => <UserList users={this.state.users} />} />

        <Route exact path='/todo' component={() => <TodosList todos={this.state.todos} />} />

        <Route exact path='/projects' component={() => <ProjectsList projects={this.state.projects} />} />


      </div >
    )
  }
}
export default App;