import { useState, useEffect } from 'react';
import {
  Dialog, DialogActions, DialogContent, DialogTitle, TextField, Button,
  Select, MenuItem, InputLabel, FormControl, Grid
} from '@mui/material';

// The modal needs to receive lists of departments and shifts to populate the dropdowns
const DoctorModal = ({ open, onClose, onSave, item, departments, shifts }) => {
  const [formData, setFormData] = useState({
    name: '', age: '', department: '', salary: '', shift: '',
    phone_number: '', email: '', experience: '', dob: '',
  });

  useEffect(() => {
    if (item) {
      // If we are editing, populate the form. Ensure related fields use just the ID.
      setFormData({
        name: item.name || '',
        age: item.age || '',
        department: item.department?.id || item.department || '',
        salary: item.salary || '',
        shift: item.shift?.id || item.shift || '',
        phone_number: item.phone_number || '',
        email: item.email || '',
        experience: item.experience || '',
        dob: item.dob || '',
      });
    } else {
      // If creating a new one, reset the form
      setFormData({
        name: '', age: '', department: '', salary: '', shift: '',
        phone_number: '', email: '', experience: '', dob: '',
      });
    }
  }, [item, open]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSave = () => {
    // Pass the completed form data (with its ID if editing) back to the parent page
    onSave({ ...formData, id: item?.id });
  };

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>{item ? 'Edit Doctor' : 'Add New Doctor'}</DialogTitle>
      <DialogContent>
        <Grid container spacing={2} sx={{ mt: 1 }}>
          <Grid item xs={12} sm={6}>
            <TextField autoFocus name="name" label="Doctor Name" fullWidth value={formData.name} onChange={handleChange} />
          </Grid>
          <Grid item xs={12} sm={6}>
            <TextField name="email" label="Email Address" type="email" fullWidth value={formData.email} onChange={handleChange} />
          </Grid>
          <Grid item xs={12} sm={6}>
            <FormControl fullWidth>
              <InputLabel>Department</InputLabel>
              <Select name="department" value={formData.department} label="Department" onChange={handleChange}>
                {departments.map(d => <MenuItem key={d.id} value={d.id}>{d.name}</MenuItem>)}
              </Select>
            </FormControl>
          </Grid>
           <Grid item xs={12} sm={6}>
            <FormControl fullWidth>
              <InputLabel>Shift</InputLabel>
              <Select name="shift" value={formData.shift} label="Shift" onChange={handleChange}>
                {shifts.map(s => <MenuItem key={s.id} value={s.id}>{s.name}</MenuItem>)}
              </Select>
            </FormControl>
          </Grid>
          <Grid item xs={12} sm={6}>
            <TextField name="phone_number" label="Phone Number" fullWidth value={formData.phone_number} onChange={handleChange} />
          </Grid>
          <Grid item xs={12} sm={6}>
             <TextField name="salary" label="Salary" type="number" fullWidth value={formData.salary} onChange={handleChange} />
          </Grid>
          <Grid item xs={12} sm={6}>
            <TextField name="experience" label="Experience (Years)" type="number" fullWidth value={formData.experience} onChange={handleChange} />
          </Grid>
          <Grid item xs={12} sm={6}>
             <TextField name="age" label="Age" type="number" fullWidth value={formData.age} onChange={handleChange} />
          </Grid>
          <Grid item xs={12}>
            <TextField name="dob" label="Date of Birth" type="date" fullWidth value={formData.dob} onChange={handleChange} InputLabelProps={{ shrink: true }}/>
          </Grid>
        </Grid>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button onClick={handleSave}>Save</Button>
      </DialogActions>
    </Dialog>
  );
};

export default DoctorModal;