import React from 'react';
import './App.css';
import LoginForm from './components/Auth';
import axios from 'axios';
import Menu from './components/Menu'
import UserList from './components/Users'
import TodosList from './components/Todo'
import ProjectsList from './components/Projects'
import { Route, Link, BrowserRouter, Switch } from 'react-router-dom';
import Cookies from 'universal-cookie';


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'todos': [],
      'token': ''
    }
  }

  get_headers() {
    let headers = {
      'Content-Type': 'application/json'
    }
    if (this.is_authenticated()) {
      headers['Authorization'] = 'Token ' + this.state.token
    }
    return headers
  }


  set_token(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({ 'token': token }, () => this.load_data())
  }

  is_authenticated() {
    return this.state.token != ''
  }

  logout() {
    this.set_token('')
  }


  get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({ 'token': token }, () => this.load_data())
  }

  get_token(username, password) {
    axios.post('http://192.168.0.20:8000/api-token-auth/', {
      username: username,
      password: password
    }).then(response => {
      this.set_token(response.data['token'])
    }).catch(error => alert('Invalid login or password'))
  }

  load_data() {
    const headers = this.get_headers()
    axios.get('http://192.168.0.20:8000/api/users/', { headers })
      .then(response => {
        const users = response.data.results
        console.log(users)
        this.setState({
          'users': users
        }
        )
      }).catch(error => {
        console.log(error)
        this.setState({ users: [] })
      })

    axios.get('http://192.168.0.20:8000/api/todo/', { headers })
      .then(response => {
        const todos = response.data.results
        this.setState({
          'todos': todos
        }
        )
      }).catch(error => {
        console.log(error)
        this.setState({ todos: [] })
      })

    axios.get('http://192.168.0.20:8000/api/projects/', { headers })
      .then(response => {
        const projects = response.data.results
        this.setState({
          'projects': projects
        }
        )
      }).catch(error => {
        console.log(error)
        this.setState({ projects: [] })
      })

  }

  componentDidMount() {
    this.get_token_from_storage()
  }




  render() {

    return (
      < div className='App'>
        <li>
          {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> :
            <Link to='/login'>Login</Link>}
        </li>

        < Menu />


        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />

        <Route exact path='/' component={() => <UserList users={this.state.users} />} />

        <Route exact path='/todo' component={() => <TodosList todos={this.state.todos} />} />

        <Route exact path='/projects' component={() => <ProjectsList projects={this.state.projects} />} />


      </div >
    )
  }
}
export default App;
