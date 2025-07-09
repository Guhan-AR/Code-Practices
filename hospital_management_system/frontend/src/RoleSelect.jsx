import { useNavigate } from 'react-router-dom';

const roles = [
  { name: 'Admin', route: '/admin-dashboard' },
  { name: 'Receptionist', route: '/receptionist-dashboard' },
  { name: 'Doctor', route: '/doctor-dashboard' },
  { name: 'Nurse', route: '/nurse-dashboard' },
  { name: 'Pharmacist', route: '/pharmacist-dashboard' },
  { name: 'Lab Technician', route: '/lab-technician-dashboard' },
  { name: 'Patient', route: '/patient-dashboard' },
  { name: 'Accountant', route: '/accountant-dashboard' },
  { name: 'Radiologist', route: '/radiologist-dashboard' },
  { name: 'HR/Staff Manager', route: '/hr-dashboard' },
  { name: 'Branch Manager', route: '/branch-manager-dashboard' },
];

export default function RoleSelect() {
  const navigate = useNavigate();

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Select Your Role</h1>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '1rem' }}>
        {roles.map((role) => (
          <button
            key={role.name}
            onClick={() => navigate(role.route)}
            style={{
              padding: '1rem',
              fontSize: '1rem',
              cursor: 'pointer',
              borderRadius: '8px',
              border: '1px solid #ccc',
            }}
          >
            {role.name}
          </button>
        ))}
      </div>
    </div>
  );
}
