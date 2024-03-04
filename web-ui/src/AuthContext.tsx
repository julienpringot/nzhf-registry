import React, { createContext, useContext, useState, ReactNode } from 'react';

interface AuthContextProps {
    idToken: string | null;
    fullName: string | null;
    role: string | null;
    setInfo: (token: string, fullName?: string, role?: string) => void;
}

const AuthContext = createContext<AuthContextProps | undefined>(undefined);

interface AuthProviderProps {
    children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
    const [idToken, setIdToken] = useState<string | null>(null);
    const [fullName, setFullName] = useState<string | null>(null);
    const [role, setRole] = useState<string | null>(null);

    const setInfo: AuthContextProps['setInfo'] = (token, fullName, role) => {
        setIdToken(token);
        setFullName(fullName || null);
        setRole(role || null);
    };

    const contextValue: AuthContextProps = {
        idToken,
        fullName,
        role,
        setInfo,
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
