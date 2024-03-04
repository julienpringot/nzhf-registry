import React, { FC } from 'react';
import { useAuth } from '../AuthContext';

interface HomePageProps {
    fullName?: string;
    profile?: string;
}

const HomePage: FC<HomePageProps> = () => {
    const { fullName, role } = useAuth();
    return (
        <div>
            <h1>Welcome, {fullName || 'Guest'}</h1>
            <div>
                <p>Full Name: {fullName}</p>
                <p>Profile: {role}</p>
            </div>
        </div>
    );
};

export default HomePage;