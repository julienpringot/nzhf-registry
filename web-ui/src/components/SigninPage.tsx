import SignIn from './SignIn';
import logo from '../logo.jpg';

const SignInPage = () => {
    return (
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
    )
}

export default SignInPage;