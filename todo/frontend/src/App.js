import React from 'react';
import logo from './logo.svg';
import './App.css';
import UsersList from './components/Users';
import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }

  componentDidMount() {
    axios.get('http://192.168.0.20:8000/api/users/')
      .then(response => {
        const users = response.data
        this.setState({
          'users': users
        }
        )
      }).catch(error => console.log(error))
  }

  render() {
    return (
      <div>
        <UsersList users={this.state.users} />
      </div>
    )
  }
}
export default App;