import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import { AuthProvider } from './AuthContext';
import SignInPage from './components/SigninPage';
import HomePage from './components/HomePage';


function App() {

  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<SignInPage />} />
          <Route path="/home" element={<HomePage />} />
        </Routes>
      </Router>
    </AuthProvider >
  );
}

export default App;
