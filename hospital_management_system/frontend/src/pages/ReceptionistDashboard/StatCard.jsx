// File: ./ReceptionistDashboard/StatCard.jsx
import React from 'react';

export default function StatCard({ label, value }) {
  return (
    <div className="stat-card">
      <h4>{label}</h4>
      <p>{value}</p>
    </div>
  );
}
