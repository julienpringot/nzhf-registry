import SignIn from './components/SignIn';
import logo from './logo.jpg';
import './App.css';
import { AuthProvider } from './AuthContext';

function App() {

  return (
    <AuthProvider>
      <div className="App">
        <header className="App-header">
          <img src={logo} />
          <p>
            NZHF Player Registry
          </p>
          <SignIn />
          <a
            className="App-link"
            href="https://handball.org.nz/"
            target="_blank"
            rel="noopener noreferrer"
          >
            NZHF Website
          </a>
        </header>
      </div>
    </AuthProvider>
  );
}

export default App;
