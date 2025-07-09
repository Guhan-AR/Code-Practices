import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import RoleSelect from './RoleSelect';

import AdminDashboard from './pages/AdminDashboard';
import ReceptionistDashboard from './pages/ReceptionistDashboard/ReceptionistDashboard';
import DoctorDashboard from './pages/DoctorDashboard';
import NurseDashboard from './pages/NurseDashboard';
import PharmacistDashboard from './pages/PharmacistDashboard';
import LabTechnicianDashboard from './pages/LabTechnicianDashboard';
import PatientDashboard from './pages/PatientDashboard';
import AccountantDashboard from './pages/AccountantDashboard';
import RadiologistDashboard from './pages/RadiologistDashboard';
import HRDashboard from './pages/HRDashboard';
import BranchManagerDashboard from './pages/BranchManagerDashboard';
import Profile from './components/Profile';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<RoleSelect />} />
        <Route path="/admin-dashboard" element={<AdminDashboard />} />
        <Route path="/receptionist-dashboard" element={<ReceptionistDashboard />} />
        <Route path="/doctor-dashboard" element={<DoctorDashboard />} />
        <Route path="/nurse-dashboard" element={<NurseDashboard />} />
        <Route path="/pharmacist-dashboard" element={<PharmacistDashboard />} />
        <Route path="/lab-technician-dashboard" element={<LabTechnicianDashboard />} />
        <Route path="/patient-dashboard" element={<PatientDashboard />} />
        <Route path="/accountant-dashboard" element={<AccountantDashboard />} />
        <Route path="/radiologist-dashboard" element={<RadiologistDashboard />} />
        <Route path="/hr-dashboard" element={<HRDashboard />} />
        <Route path="/branch-manager-dashboard" element={<BranchManagerDashboard />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>
    </Router>
  );
}

export default App;
