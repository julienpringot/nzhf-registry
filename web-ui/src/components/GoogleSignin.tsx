import React, { useState } from 'react';
import { initializeApp } from 'firebase/app';
import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyBJTT0j1OP_eOT7ZKpD490s099v3ZH3x-k",
    authDomain: "nzhf-database.firebaseapp.com",
    projectId: "nzhf-database",
    storageBucket: "nzhf-database.appspot.com",
    messagingSenderId: "444021049715",
    appId: "1:444021049715:web:416987dbe186dd107cdd06"
};

const app = initializeApp(firebaseConfig);

// Initialize Firebase Auth provider
const provider = new GoogleAuthProvider();

// whenever a user interacts with the provider, we force them to select an account
provider.setCustomParameters({
    prompt: "select_account "
});

export const auth = getAuth();
export const signInWithGooglePopup = () => signInWithPopup(auth, provider);