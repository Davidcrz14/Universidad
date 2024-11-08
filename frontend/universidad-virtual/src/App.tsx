import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import LoginForm from './components/auth/LoginForm'
import RegisterForm from './components/auth/RegisterForm'
import Dashboard from './components/dashboard/Dashboard'
import { useEffect, useState } from 'react'

import './App.css'

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);

  useEffect(() => {
    // Verificar si existe un token en localStorage
    const token = localStorage.getItem('token');
    setIsAuthenticated(!!token);
  }, []);

  // Componente para proteger rutas
  const ProtectedRoute = ({ children }: { children: JSX.Element }) => {
    if (!isAuthenticated) {
      return <Navigate to="/login" replace />;
    }
    return children;
  };

  return (
    <Router>
      <Routes>
        {/* Redirige la ruta raíz al dashboard si está autenticado, sino al login */}
        <Route
          path="/"
          element={
            isAuthenticated ?
              <Navigate to="/dashboard" replace /> :
              <Navigate to="/login" replace />
          }
        />

        {/* Rutas de autenticación */}
        <Route
          path="/login"
          element={
            isAuthenticated ?
              <Navigate to="/dashboard" replace /> :
              <LoginForm />
          }
        />
        <Route
          path="/register"
          element={
            isAuthenticated ?
              <Navigate to="/dashboard" replace /> :
              <RegisterForm />
          }
        />

        {/* Ruta protegida del dashboard */}
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <div className="h-screen">
                <Dashboard />
              </div>
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  )
}

export default App
