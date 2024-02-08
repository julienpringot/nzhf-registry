import { signInWithGooglePopup } from "./GoogleSignin"

const SignIn = () => {
    const logGoogleUser = async () => {
        const response = await signInWithGooglePopup();
        console.log(response);
        console.log(response.user.email);

    }
    return (
        <div>
            <button onClick={logGoogleUser}>Sign In With Google</button>
        </div>

    )
}

export default SignIn;