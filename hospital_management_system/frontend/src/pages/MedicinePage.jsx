import { useState, useEffect } from 'react';
import { Box, Typography, Button, IconButton } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import apiClient from '../api/axiosConfig';
import MedicineModal from '../components/MedicineModal';

const MedicinePage = () => {
  const [medicines, setMedicines] = useState([]);
  const [medicineTypes, setMedicineTypes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentItem, setCurrentItem] = useState(null);

  const fetchData = async () => {
    setLoading(true);
    try {
      const [medRes, typeRes] = await Promise.all([
        apiClient.get('/medicines/'),
        apiClient.get('/medicine-types/'),
      ]);
      setMedicines(medRes.data);
      setMedicineTypes(typeRes.data);
    } catch (error) { console.error("Failed to fetch medicine data:", error); }
    finally { setLoading(false); }
  };

  useEffect(() => { fetchData(); }, []);

  const handleSave = async (data) => {
    try {
      const payload = {
        ...data,
        medicine_type: data.medicine_type?.id || data.medicine_type,
      };
      if (data.id) {
        await apiClient.put(`/medicines/${data.id}/`, payload);
      } else {
        await apiClient.post('/medicines/', payload);
      }
      fetchData();
      setIsModalOpen(false);
    } catch (error) { console.error("Failed to save medicine:", error); }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure?')) {
      try {
        await apiClient.delete(`/medicines/${id}/`);
        fetchData();
      } catch (error) { alert('Could not delete medicine.'); }
    }
  };

  const columns = [
    { field: 'name', headerName: 'Name', flex: 1 },
    { field: 'medicine_type', headerName: 'Type', width: 150, valueGetter: (params) => params.row.medicine_type.name },
    { field: 'expiry_date', headerName: 'Expiry Date', width: 150 },
    {
      field: 'actions', headerName: 'Actions', width: 120,
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
        <Typography variant="h4">Manage Medicines</Typography>
        <Button variant="contained" onClick={() => { setCurrentItem(null); setIsModalOpen(true); }}>Add New Medicine</Button>
      </Box>
      <DataGrid rows={medicines} columns={columns} loading={loading} />
      <MedicineModal open={isModalOpen} onClose={() => setIsModalOpen(false)} onSave={handleSave} item={currentItem} medicineTypes={medicineTypes} />
    </Box>
  );
};

export default MedicinePage;