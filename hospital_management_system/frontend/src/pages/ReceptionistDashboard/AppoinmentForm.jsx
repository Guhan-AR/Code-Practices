// File: ./ReceptionistDashboard/AppointmentForm.jsx
import React from 'react';

export default function AppointmentForm({ form, handleChange, handleSubmit, editingIndex }) {
  return (
    <div className="form">
      <input
        type="text"
        placeholder="Patient Name"
        name="patient"
        value={form.patient}
        onChange={handleChange}
      />
      <select
        name="doctor"
        value={form.doctor}
        onChange={handleChange}
      >
        <option value="">Select Doctor</option>
        <option value="Dr. Gupta">Dr. Gupta</option>
        <option value="Dr. Patel">Dr. Patel</option>
        <option value="Dr. Bose">Dr. Bose</option>
      </select>
      <input
        type="datetime-local"
        name="time"
        value={form.time}
        onChange={handleChange}
      />
      <button onClick={handleSubmit}>
        {editingIndex !== null ? 'Update' : 'Add'}
      </button>
    </div>
  );
}
