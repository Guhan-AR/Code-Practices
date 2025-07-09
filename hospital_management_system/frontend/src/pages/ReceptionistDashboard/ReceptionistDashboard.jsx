// File: ./ReceptionistDashboard/ReceptionistDashboard.jsx
import React, { useState, useEffect } from 'react';
import '../../styles/ReceptionistDashboard.css';
import StatCard from './StatCard';
import AppointmentForm from './AppoinmentForm';
import AppointmentTable from './AppoinmentTable';
import ProfileMenu from '../../components/ProfileMenu';

export default function ReceptionistDashboard() {
  const [loginTime, setLoginTime] = useState('');
  const [appointments, setAppointments] = useState([]);
  const [form, setForm] = useState({ patient: '', doctor: '', time: '' });
  const [editingIndex, setEditingIndex] = useState(null);

  useEffect(() => {
    const now = new Date();
    const formatted = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    setLoginTime(formatted);
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = () => {
    if (!form.patient || !form.doctor || !form.time) return alert("All fields required!");

    if (editingIndex !== null) {
      const updated = [...appointments];
      updated[editingIndex] = form;
      setAppointments(updated);
      setEditingIndex(null);
    } else {
      setAppointments([...appointments, form]);
    }

    setForm({ patient: '', doctor: '', time: '' });
  };

  const handleEdit = (index) => {
    setForm(appointments[index]);
    setEditingIndex(index);
  };

  const handleDelete = (index) => {
    const updated = appointments.filter((_, i) => i !== index);
    setAppointments(updated);
  };

  return (
    <div className="reception-container">

      <div className="topbar">
        <h1>Receptionist Dashboard</h1>
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
          <span>Logged in at: {loginTime}</span>
          <ProfileMenu />
        </div>
      </div>


      <div className="stats-grid">
        <StatCard label="Today's Appointments" value={appointments.length} />
        <StatCard label="New Registrations" value="13" />
        <StatCard label="Cancelled Bookings" value="5" />
        <StatCard label="Pending Confirmations" value="9" />
      </div>

      <div className="section-box">
        <h3>Book New Appointment</h3>
        <AppointmentForm
          form={form}
          editingIndex={editingIndex}
          handleChange={handleChange}
          handleSubmit={handleSubmit}
        />
      </div>

      <div className="section-box">
        <h3>Appointments List</h3>
        <AppointmentTable
          appointments={appointments}
          handleEdit={handleEdit}
          handleDelete={handleDelete}
        />
      </div>
    </div>
  );
}
