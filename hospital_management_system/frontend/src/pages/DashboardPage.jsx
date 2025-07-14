import { useEffect, useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { Grid, Paper, Typography, Box } from '@mui/material';
import apiClient from '../api/axiosConfig';

const StatCard = ({ title, value }) => (
  <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', height: 140 }}>
    <Typography component="h2" variant="h6" color="primary" gutterBottom>
      {title}
    </Typography>
    <Typography component="p" variant="h4">
      {value}
    </Typography>
  </Paper>
);

const DashboardPage = () => {
  const [stats, setStats] = useState({ doctors: 0, patients: 0, appointments: 0 });
  const { user, loading: authLoading } = useAuth();

  useEffect(() => {
    const fetchStats = async () => {
      try {
        // These requests will run in parallel
        const [doctorsRes, patientsRes, appointmentsRes] = await Promise.all([
          apiClient.get('/doctors/'),
          apiClient.get('/patients/'),
          apiClient.get('/appointments/'),
        ]);
        setStats({
          doctors: doctorsRes.data.length,
          patients: patientsRes.data.length,
          appointments: appointmentsRes.data.length,
        });
      } catch (error) {
        console.error("Failed to fetch dashboard stats:", error);
      }
    };
    fetchStats();
  }, []);

  return (
    <Box>
      <Typography variant="h4" gutterBottom>Dashboard</Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} md={4} lg={3}>
          <StatCard title="Total Doctors" value={stats.doctors} />
        </Grid>
        <Grid item xs={12} md={4} lg={3}>
          <StatCard title="Total Patients" value={stats.patients} />
        </Grid>
        <Grid item xs={12} md={4} lg={3}>
          <StatCard title="Upcoming Appointments" value={stats.appointments} />
        </Grid>
      </Grid>
    </Box>
  );
};

export default DashboardPage;