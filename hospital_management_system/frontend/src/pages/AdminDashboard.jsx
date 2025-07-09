import React, { useEffect, useState } from 'react';
import '../styles/AdminDashboard.css';

export default function AdminDashboard() {
  const [loginTime, setLoginTime] = useState('');

  useEffect(() => {
    const now = new Date();
    const formatted = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    setLoginTime(formatted);
  }, []);

  return (
    <div className="admin-container">

      {/* Sidebar */}
      <aside className="sidebar">
        <h2>🛠️ Admin Panel</h2>
        <nav>
          <a href="#">Dashboard</a>
          <a href="#">User Management</a>
          <a href="#">Branch Management</a>
          <a href="#">Permissions</a>
          <a href="#">Reports</a>
          <a href="#">System Settings</a>
          <a href="#">Patient Records</a>
          <a href="#">Doctor Scheduling</a>
          <a href="#">Pharmacy Stocks</a>
          <a href="#">Lab Results</a>
          <a href="#">Billing & Invoices</a>
          <a href="#">Radiology Reports</a>
          <a href="#">Staff Attendance</a>
          <a href="#">Leave Requests</a>
          <a href="#">Payroll</a>
          <a href="#">Feedback</a>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="main-content">

        {/* Top Bar */}
        <div className="topbar">
          <h1>Welcome, Admin 👋</h1>
          <div>
            <span style={{ color: '#f59e0b' }}>🔔 Notifications</span>
            <span>🕒 Logged in at: {loginTime}</span>
            <span>👤 Admin User</span>
          </div>
        </div>

        {/* Stat Cards */}
        <div className="stat-cards">
          <StatCard label="Total Staff" value="182" />
          <StatCard label="Active Branches" value="5" />
          <StatCard label="Monthly Revenue" value="₹12.6 Lakhs" />
          <StatCard label="Pending Reports" value="37" />
        </div>

        {/* Chart Section */}
        <div className="chart-section">
          <ChartBox title="📈 User Growth">
            <ul>
              <li>Jan - 120 users</li>
              <li>Feb - 160 users</li>
              <li>Mar - 210 users</li>
              <li>Apr - 260 users</li>
              <li>May - 320 users</li>
            </ul>
          </ChartBox>

          <ChartBox title="💸 Revenue Distribution">
            <ul>
              <li>Consultations - ₹4.1L</li>
              <li>Lab Tests - ₹2.7L</li>
              <li>Pharmacy - ₹3.5L</li>
              <li>Other - ₹2.3L</li>
            </ul>
          </ChartBox>
        </div>

      </main>
    </div>
  );
}

function StatCard({ label, value }) {
  return (
    <div className="stat-card">
      <h4>{label}</h4>
      <p>{value}</p>
    </div>
  );
}

function ChartBox({ title, children }) {
  return (
    <div className="chart-box">
      <h3>{title}</h3>
      {children}
    </div>
  );
}
