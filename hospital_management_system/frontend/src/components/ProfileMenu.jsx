import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './ProfileMenu.css'; // Separate styling for the menu


export default function ProfileMenu() {
  const [open, setOpen] = useState(false);
  const navigate = useNavigate();

  const handleProfileClick = () => {
    navigate('/profile');
    setOpen(false);
  };

  const handleLogout = () => {
    // Replace with real logout logic
    alert('Logged out');
    setOpen(false);
  };

  return (
    <div className="profile-menu">
      <img
        src="https://ui-avatars.com/api/?name=Receptionist"
        alt="Profile"
        onClick={() => setOpen(!open)}
        className="profile-icon"
      />
      {open && (
        <div className="profile-dropdown">
          <button onClick={handleProfileClick}>👤 Profile</button>
          <button onClick={handleLogout}>🚪 Logout</button>
        </div>
      )}
    </div>
  );
}
