import { useState, useEffect } from 'react';
import { Box, Typography, Button, IconButton } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import apiClient from '../api/axiosConfig';
import DoctorModal from '../components/DoctorModal'; // Import the new modal

const DoctorsPage = () => {
  const [doctors, setDoctors] = useState([]);
  // Add state for related models needed for the modal dropdowns
  const [departments, setDepartments] = useState([]);
  const [shifts, setShifts] = useState([]);

  const [loading, setLoading] = useState(true);
  
  // Add state for managing the modal
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentItem, setCurrentItem] = useState(null);

  // Fetch all necessary data: doctors, departments, and shifts
  const fetchData = async () => {
    setLoading(true);
    try {
      const [doctorsRes, departmentsRes, shiftsRes] = await Promise.all([
        apiClient.get('/doctors/'),
        apiClient.get('/departments/'),
        apiClient.get('/shifts/'),
      ]);
      setDoctors(doctorsRes.data);
      setDepartments(departmentsRes.data);
      setShifts(shiftsRes.data);
    } catch (error) {
      console.error("Failed to fetch data:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
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

// In src/pages/DoctorsPage.jsx

// ... (imports and most of the component code is fine) ...

  const handleSave = async (data) => {
    try {
      // Build the payload with correct data types
      const payload = {
        name: data.name,
        age: data.age,
        department: data.department, // This MUST be a valid ID
        salary: data.salary,
        shift: data.shift || null, // Correctly handles optional shift
        phone_number: data.phone_number,
        email: data.email,
        experience: data.experience,
        dob: data.dob,
      };
      
      // Basic frontend validation for the most likely error
      if (!payload.department) {
        alert("Please select a department.");
        return; // Stop the function before making the API call
      }
      // You could add more checks for name, email, etc.

      if (data.id) {
        await apiClient.put(`/doctors/${data.id}/`, payload);
      } else {
        await apiClient.post('/doctors/', payload);
      }
      fetchData(); // Refresh the data grid
      handleCloseModal();
    } catch (error) {
      // THE GOLDEN RULE OF DEBUGGING:
      console.error("Validation failed:", error.response.data);
      alert("Save failed. Check console for details.");
    }
  };

// ... (rest of the component is fine) ...

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this doctor?')) {
      try {
        await apiClient.delete(`/doctors/${id}/`);
        fetchData();
      } catch (error) {
        console.error("Failed to delete doctor:", error);
        alert('Could not delete doctor.');
      }
    }
  };

  const columns = [
    { field: 'name', headerName: 'Name', width: 200 },
    // Use valueGetter to safely access nested data from your 'depth=1' serializer
    { field: 'department', headerName: 'Department', width: 150, valueGetter: (params) => params.row.department?.name || 'N/A' },
    { field: 'email', headerName: 'Email', width: 250 },
    { field: 'phone_number', headerName: 'Phone', width: 150 },
    {
      field: 'actions',
      headerName: 'Actions',
      width: 120,
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
        <Typography variant="h4">Manage Doctors</Typography>
        {/* The "Add New" button that was missing */}
        <Button variant="contained" onClick={() => handleOpenModal()}>
          Add New Doctor
        </Button>
      </Box>
      <DataGrid
        rows={doctors}
        columns={columns}
        loading={loading}
        pageSize={10}
        rowsPerPageOptions={[5, 10, 20]}
      />
      {/* Render the modal, passing all necessary props */}
      <DoctorModal
        open={isModalOpen}
        onClose={handleCloseModal}
        onSave={handleSave}
        item={currentItem}
        departments={departments}
        shifts={shifts}
      />
    </Box>
  );
};

export default DoctorsPage;