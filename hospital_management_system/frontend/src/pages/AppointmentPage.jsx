import { useState, useEffect } from 'react';
import { Box, Typography, Button, IconButton } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import apiClient from '../api/axiosConfig';
import AppointmentModal from '../components/AppointmentModal';

const AppointmentPage = () => {
  const [appointments, setAppointments] = useState([]);
  const [doctors, setDoctors] = useState([]);
  const [patients, setPatients] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentItem, setCurrentItem] = useState(null);

  const fetchData = async () => {
    setLoading(true);
    try {
      // Fetch all required data in parallel
      const [appRes, docRes, patRes] = await Promise.all([
        apiClient.get('/appointments/'),
        apiClient.get('/doctors/'),
        apiClient.get('/patients/'),
      ]);
      setAppointments(appRes.data);
      setDoctors(docRes.data);
      setPatients(patRes.data);
    } catch (error) {
      console.error("Failed to fetch data:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleSave = async (data) => {
    try {
      const payload = {
        ...data,
        // The modal might return nested objects from the depth setting, ensure you only send IDs
        patient: data.patient.id || data.patient,
        doctor: data.doctor.id || data.doctor,
      };
      if (data.id) {
        await apiClient.put(`/appointments/${data.id}/`, payload);
      } else {
        await apiClient.post('/appointments/', payload);
      }
      fetchData();
      setIsModalOpen(false);
    } catch (error) { console.error("Failed to save appointment:", error); }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure?')) {
      try {
        await apiClient.delete(`/appointments/${id}/`);
        fetchData();
      } catch (error) { alert('Could not delete appointment.'); }
    }
  };
  
  const columns = [
    { field: 'id', headerName: 'ID', width: 90 },
    // Use `depth` setting to easily access related names
    { field: 'patient', headerName: 'Patient', flex: 1, valueGetter: (params) => params.row.patient.name },
    { field: 'doctor', headerName: 'Doctor', flex: 1, valueGetter: (params) => params.row.doctor.name },
    { field: 'scheduled_time', headerName: 'Time', flex: 1, type: 'dateTime', valueGetter: (params) => new Date(params.row.scheduled_time)},
    { field: 'status', headerName: 'Status', flex: 1 },
    {
      field: 'actions', headerName: 'Actions', width: 150,
      renderCell: (params) => (
        <>
          <IconButton onClick={() => { setCurrentItem(params.row); setIsModalOpen(true); }}><EditIcon /></IconButton>
          <IconButton onClick={() => handleDelete(params.row.id)}><DeleteIcon color="error" /></IconButton>
        </>
      ),
    },
  ];

  return (
    <Box sx={{ height: '80vh', width: '100%' }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="h4">Manage Appointments</Typography>
        <Button variant="contained" onClick={() => { setCurrentItem(null); setIsModalOpen(true); }}>Add New Appointment</Button>
      </Box>
      <DataGrid rows={appointments} columns={columns} loading={loading} />
      <AppointmentModal open={isModalOpen} onClose={() => setIsModalOpen(false)} onSave={handleSave} item={currentItem} doctors={doctors} patients={patients}/>
    </Box>
  );
};

export default AppointmentPage;