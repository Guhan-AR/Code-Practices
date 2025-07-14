import { useState, useEffect } from 'react';
import { Box, Typography, Button, IconButton } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import apiClient from '../api/axiosConfig';
import ShiftModal from '../components/ShiftModal'; // Make sure this is imported

const ShiftPage = () => {
  const [shifts, setShifts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentItem, setCurrentItem] = useState(null);

  const fetchShifts = async () => {
    setLoading(true);
    try {
      const response = await apiClient.get('/shifts/');
      setShifts(response.data);
    } catch (error) { console.error("Failed to fetch shifts:", error); }
    finally { setLoading(false); }
  };

  useEffect(() => { fetchShifts(); }, []);

  const handleOpenModal = (item = null) => {
    setCurrentItem(item);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setCurrentItem(null);
  };

  const handleSave = async (data) => {
    try {
      const payload = {
        name: data.name,
        start_time: data.start_time,
        end_time: data.end_time,
      };

      // Simple validation on the frontend
      if (!payload.name || !payload.start_time || !payload.end_time) {
        alert("All fields are required.");
        return;
      }

      if (data.id) {
        await apiClient.put(`/shifts/${data.id}/`, payload);
      } else {
        await apiClient.post('/shifts/', payload);
      }
      fetchShifts();
      handleCloseModal();
    } catch (error) {
      // THE GOLDEN RULE OF DEBUGGING:
      console.error("Validation failed:", error.response.data);
      alert("Save failed. Check console for details.");
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this shift?')) {
      try {
        await apiClient.delete(`/shifts/${id}/`);
        fetchShifts();
      } catch (error) { alert('Could not delete shift. It may be in use.'); }
    }
  };
  
  const columns = [ /* Your columns from before */ ]; // Keep your columns definition

  return (
    <Box sx={{ height: '80vh', width: '100%' }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="h4">Manage Shifts</Typography>
        <Button variant="contained" onClick={() => handleOpenModal()}>Add New Shift</Button>
      </Box>
      <DataGrid rows={shifts} columns={columns} loading={loading} />
      <ShiftModal open={isModalOpen} onClose={handleCloseModal} onSave={handleSave} item={currentItem} />
    </Box>
  );
};

export default ShiftPage;