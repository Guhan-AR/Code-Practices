import { createContext, useState, useContext, useEffect } from 'react';
import apiClient from '../api/axiosConfig';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if a token exists on initial load
    const token = localStorage.getItem('accessToken');
    if (token) {
      // You could also add a call here to a '/api/profile/' endpoint
      // to verify the token and get user data
      setUser({ token });
    }
    setLoading(false);
  }, []);

  const login = async (username, password) => {
    const response = await apiClient.post('/token/', { username, password });
    localStorage.setItem('accessToken', response.data.access);
    localStorage.setItem('refreshToken', response.data.refresh);
    setUser({ token: response.data.access });
  };

  const logout = () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);