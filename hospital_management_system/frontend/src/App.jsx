// src/App.jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';

// Layout and Auth
import Layout from './components/Layout';
import ProtectedRoute from './components/ProtectedRoute';

// Public Pages
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';

// Protected CRUD Pages
import DashboardPage from './pages/DashboardPage';
import DepartmentPage from './pages/DepartmentPage';
import ShiftPage from './pages/ShiftPage';
import DoctorsPage from './pages/DoctorsPage';
import PatientPage from './pages/PatientPage';
import AppointmentPage from './pages/AppointmentPage'; // Assuming you create this one now
import MedicinePage from './pages/MedicinePage';
import MedicineTypePage from './pages/MedicineTypePage';

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          {/* Public routes */}
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />

          {/* Protected routes */}
          <Route element={<ProtectedRoute />}>
            <Route element={<Layout />}>
              <Route path="/" element={<DashboardPage />} />
              <Route path="/departments" element={<DepartmentPage />} />
              <Route path="/shifts" element={<ShiftPage />} />
              <Route path="/doctors" element={<DoctorsPage />} />
              <Route path="/patients" element={<PatientPage />} />
              <Route path="/appointments" element={<AppointmentPage />} /> {/* Assuming you've created AppointmentPage.jsx now */}
              <Route path="/medicines" element={<MedicinePage />} />
              <Route path="/medicine-types" element={<MedicineTypePage />} />
            </Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;