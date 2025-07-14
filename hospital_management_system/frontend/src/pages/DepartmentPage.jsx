import { useState, useEffect } from 'react';
import { Box, Typography, Button, IconButton } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import apiClient from '../api/axiosConfig';
import DepartmentModal from '../components/DepartmentModal';

const DepartmentPage = () => {
  const [departments, setDepartments] = useState([]);
  const [loading, setLoading] = useState(true);

  // State for managing the modal
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentItem, setCurrentItem] = useState(null);

  // --- Data Fetching ---
  const fetchDepartments = async () => {
    setLoading(true);
    try {
      const response = await apiClient.get('/departments/');
      setDepartments(response.data);
    } catch (error) {
      console.error("Failed to fetch departments:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchDepartments();
  }, []);

  // --- Modal and CRUD Handlers ---
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
      if (data.id) {
        // Update (PUT)
        await apiClient.put(`/departments/${data.id}/`, { name: data.name });
      } else {
        // Create (POST)
        await apiClient.post('/departments/', { name: data.name });
      }
      fetchDepartments(); // Re-fetch data to show changes
      handleCloseModal();
    } catch (error) {
      console.error("Failed to save department:", error);
    }
  };

  const handleDelete = async (id) => {
    // Ask for confirmation before deleting
    if (window.confirm('Are you sure you want to delete this department?')) {
      try {
        await apiClient.delete(`/departments/${id}/`);
        fetchDepartments(); // Re-fetch data
      } catch (error) {
        console.error("Failed to delete department:", error);
        // You could show an error message, e.g., if a doctor is still in the department
        alert('Could not delete department. It may be in use.');
      }
    }
  };

  // --- Table Columns Definition ---
  const columns = [
    { field: 'id', headerName: 'ID', width: 90 },
    { field: 'name', headerName: 'Department Name', flex: 1 },
    // A special column for actions (Edit and Delete buttons)
    {
      field: 'actions',
      headerName: 'Actions',
      width: 150,
      sortable: false,
      renderCell: (params) => (
        <>
          <IconButton onClick={() => handleOpenModal(params.row)}>
            <EditIcon />
          </IconButton>
          <IconButton onClick={() => handleDelete(params.row.id)}>
            <DeleteIcon color="error" />
          </IconButton>
        </>
      ),
    },
  ];

  return (
    <Box sx={{ height: '80vh', width: '100%' }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="h4">Manage Departments</Typography>
        <Button variant="contained" onClick={() => handleOpenModal()}>
          Add New Department
        </Button>
      </Box>
      <DataGrid
        rows={departments}
        columns={columns}
        loading={loading}
        pageSize={10}
        rowsPerPageOptions={[5, 10, 20]}
      />
      <DepartmentModal
        open={isModalOpen}
        onClose={handleCloseModal}
        onSave={handleSave}
        item={currentItem}
      />
    </Box>
  );
};

export default DepartmentPage;