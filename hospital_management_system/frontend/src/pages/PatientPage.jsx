import { useState, useEffect } from 'react';
import { Box, Typography, Button, IconButton } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import apiClient from '../api/axiosConfig';
import PatientModal from '../components/PatientModal';

const PatientPage = () => {
  const [patients, setPatients] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentItem, setCurrentItem] = useState(null);

  const fetchPatients = async () => {
    setLoading(true);
    try {
      const response = await apiClient.get('/patients/');
      setPatients(response.data);
    } catch (error) { console.error("Failed to fetch patients:", error); }
    finally { setLoading(false); }
  };

  useEffect(() => { fetchPatients(); }, []);

  const handleSave = async (data) => {
    try {
      // Handle optional fields that might be empty strings
      const payload = {
        ...data,
        sugar_level: data.sugar_level || null,
        blood_pressure: data.blood_pressure || null
      };
      if (data.id) {
        await apiClient.put(`/patients/${data.id}/`, payload);
      } else {
        await apiClient.post('/patients/', payload);
      }
      fetchPatients();
      setIsModalOpen(false);
    } catch (error) { console.error("Failed to save patient:", error); }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this patient?')) {
      try {
        await apiClient.delete(`/patients/${id}/`);
        fetchPatients();
      } catch (error) { alert('Could not delete patient.'); }
    }
  };
  
  const columns = [
    { field: 'id', headerName: 'ID', width: 90 },
    { field: 'name', headerName: 'Name', flex: 1 },
    { field: 'age', headerName: 'Age', width: 100 },
    { field: 'dob', headerName: 'DoB', width: 120 },
    { field: 'sugar_level', headerName: 'Sugar Level', width: 150 },
    { field: 'blood_pressure', headerName: 'Blood Pressure', width: 150 },
    {
      field: 'actions', headerName: 'Actions', width: 120, sortable: false,
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
        <Typography variant="h4">Manage Patients</Typography>
        <Button variant="contained" onClick={() => { setCurrentItem(null); setIsModalOpen(true); }}>Add New Patient</Button>
      </Box>
      <DataGrid rows={patients} columns={columns} loading={loading} />
      <PatientModal open={isModalOpen} onClose={() => setIsModalOpen(false)} onSave={handleSave} item={currentItem} />
    </Box>
  );
};

export default PatientPage;