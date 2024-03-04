import React, { createContext, useContext, useState, ReactNode } from 'react';

interface AuthContextProps {
    idToken: string | null;
    setToken: (token: string) => void;
}

const AuthContext = createContext<AuthContextProps | undefined>(undefined);

interface AuthProviderProps {
    children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
    const [idToken, setIdToken] = useState<string | null>(null);

    const setToken = (token: string) => {
        setIdToken(token);
    };

    const contextValue: AuthContextProps = {
        idToken,
        setToken,
    };

    return <AuthContext.Provider value={contextValue}>{children}</AuthContext.Provider>;
};

export const useAuth = (): AuthContextProps => {
    const context = useContext(AuthContext);

    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }

    return context;
};
