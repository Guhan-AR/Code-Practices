import { useState, useEffect } from 'react';
import { Dialog, DialogActions, DialogContent, DialogTitle, TextField, Button } from '@mui/material';

const PatientModal = ({ open, onClose, onSave, item }) => {
  const [formData, setFormData] = useState({ name: '', age: '', dob: '', sugar_level: '', blood_pressure: '' });

  useEffect(() => {
    // Format the date for the date input if the item exists
    const initialData = item ? { ...item, dob: item.dob || '' } : { name: '', age: '', dob: '', sugar_level: '', blood_pressure: '' };
    setFormData(initialData);
  }, [item, open]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>{item ? 'Edit Patient' : 'Add New Patient'}</DialogTitle>
      <DialogContent>
        <TextField autoFocus margin="dense" name="name" label="Patient Name" type="text" fullWidth variant="standard" value={formData.name} onChange={handleChange} />
        <TextField margin="dense" name="age" label="Age" type="number" fullWidth variant="standard" value={formData.age} onChange={handleChange} />
        <TextField margin="dense" name="dob" label="Date of Birth" type="date" fullWidth variant="standard" value={formData.dob} onChange={handleChange} InputLabelProps={{ shrink: true }}/>
        <TextField margin="dense" name="sugar_level" label="Sugar Level (mg/dL)" type="number" fullWidth variant="standard" value={formData.sugar_level || ''} onChange={handleChange} />
        <TextField margin="dense" name="blood_pressure" label="Blood Pressure (mmHg)" type="number" fullWidth variant="standard" value={formData.blood_pressure || ''} onChange={handleChange} />
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button onClick={() => onSave({ ...formData, id: item?.id })}>Save</Button>
      </DialogActions>
    </Dialog>
  );
};

export default PatientModal;