import { useState, useEffect } from 'react';
import { Box, Typography, Button, IconButton } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import apiClient from '../api/axiosConfig';
import MedicineTypeModal from '../components/MedicineTypeModal';

const MedicineTypePage = () => {
  const [types, setTypes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentItem, setCurrentItem] = useState(null);

  const fetchTypes = async () => {
    setLoading(true);
    try {
      const response = await apiClient.get('/medicine-types/');
      setTypes(response.data);
    } catch (error) { console.error("Failed to fetch medicine types:", error); }
    finally { setLoading(false); }
  };

  useEffect(() => { fetchTypes(); }, []);

  const handleSave = async (data) => {
    try {
      if (data.id) {
        await apiClient.put(`/medicine-types/${data.id}/`, data);
      } else {
        await apiClient.post('/medicine-types/', data);
      }
      fetchTypes();
      setIsModalOpen(false);
    } catch (error) { console.error("Failed to save medicine type:", error); }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure?')) {
      try {
        await apiClient.delete(`/medicine-types/${id}/`);
        fetchTypes();
      } catch (error) { alert('Could not delete type. It may be in use.'); }
    }
  };
  
  const columns = [
    { field: 'id', headerName: 'ID', width: 90 },
    { field: 'name', headerName: 'Type Name', flex: 1 },
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
        <Typography variant="h4">Manage Medicine Types</Typography>
        <Button variant="contained" onClick={() => { setCurrentItem(null); setIsModalOpen(true); }}>Add New Type</Button>
      </Box>
      <DataGrid rows={types} columns={columns} loading={loading} />
      <MedicineTypeModal open={isModalOpen} onClose={() => setIsModalOpen(false)} onSave={handleSave} item={currentItem} />
    </Box>
  );
};

export default MedicineTypePage;