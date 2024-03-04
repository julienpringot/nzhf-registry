import { signInWithGooglePopup } from "./GoogleSignin"
import { login } from "../utilities/Requests"
import { useAuth } from '../AuthContext';

const SignIn = () => {
    const { setToken } = useAuth();
    const logGoogleUser = async () => {
        const response = await signInWithGooglePopup();
        const idToken = await response.user.getIdToken();
        setToken(idToken);

        try {
            const ret = await login(idToken);
            console.log(ret);
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