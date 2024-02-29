import { signInWithGooglePopup } from "./GoogleSignin"
import axios from 'axios';

const SignIn = () => {
    const logGoogleUser = async () => {
        const response = await signInWithGooglePopup();
        console.log(response);
        console.log(response.user.email);
        const idToken = await response.user.getIdToken();
        console.log('ID Token:', idToken);

        try {
            const ret = await axios.post('http://localhost:5000/login', {}, {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${idToken}`,
                }
            });

            // Assuming a successful response with a JSON payload containing the 'username' field
            const username = ret.data;
            console.log(username);
        } catch (error) {
            console.log('login failed');
        }

    }
    return (
        <div>
            <button onClick={logGoogleUser}>Sign In With Google</button>
        </div>

    )
}

export default SignIn;