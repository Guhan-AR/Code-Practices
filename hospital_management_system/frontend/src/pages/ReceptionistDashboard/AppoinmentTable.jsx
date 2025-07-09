// File: ./ReceptionistDashboard/AppointmentTable.jsx
import React from 'react';

export default function AppointmentTable({ appointments, handleEdit, handleDelete }) {
  if (appointments.length === 0) {
    return <p>No appointments booked yet.</p>;
  }

  return (
    <table className="appointment-table">
      <thead>
        <tr>
          <th>Patient</th>
          <th>Doctor</th>
          <th>Time</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {appointments.map((appt, idx) => (
          <tr key={idx}>
            <td>{appt.patient}</td>
            <td>{appt.doctor}</td>
            <td>{new Date(appt.time).toLocaleString()}</td>
            <td>
              <button className="edit-btn" onClick={() => handleEdit(idx)}>Edit</button>
              <button className="delete-btn" onClick={() => handleDelete(idx)}>Delete</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
