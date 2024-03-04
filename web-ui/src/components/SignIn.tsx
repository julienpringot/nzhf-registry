import { signInWithGooglePopup } from "./GoogleSignin"
import { login } from "../utilities/Requests"
import { useAuth } from '../AuthContext';
import { useNavigate } from 'react-router-dom';

const SignIn = () => {
    const { setInfo } = useAuth();
    const navigate = useNavigate();

    const logGoogleUser = async () => {
        const response = await signInWithGooglePopup();
        const idToken = await response.user.getIdToken();

        try {
            const ret = await login(idToken);
            const user = ret.data;
            setInfo(idToken, user.full_name, user.role);
            console.log(ret);
            console.log(user.full_name, user.role);
            navigate('/home');
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