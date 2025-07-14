import { useState, useEffect } from 'react';
import { Dialog, DialogActions, DialogContent, DialogTitle, TextField, Button, Select, MenuItem, InputLabel, FormControl } from '@mui/material';

// This modal now accepts lists of doctors and patients for the dropdowns
const AppointmentModal = ({ open, onClose, onSave, item, doctors, patients }) => {
  const [formData, setFormData] = useState({ patient: '', doctor: '', scheduled_time: '', status: 'PENDING', urgency: 'ROUTINE', notes: '' });

  useEffect(() => {
    setFormData(item ? { ...item, scheduled_time: item.scheduled_time?.split('T')[0] || '' } : { patient: '', doctor: '', scheduled_time: '', status: 'PENDING', urgency: 'ROUTINE', notes: '' });
  }, [item, open]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>{item ? 'Edit Appointment' : 'Add New Appointment'}</DialogTitle>
      <DialogContent>
        <FormControl fullWidth margin="dense">
          <InputLabel>Patient</InputLabel>
          <Select name="patient" value={formData.patient} label="Patient" onChange={handleChange}>
            {patients.map(p => <MenuItem key={p.id} value={p.id}>{p.name}</MenuItem>)}
          </Select>
        </FormControl>
        <FormControl fullWidth margin="dense">
          <InputLabel>Doctor</InputLabel>
          <Select name="doctor" value={formData.doctor} label="Doctor" onChange={handleChange}>
            {doctors.map(d => <MenuItem key={d.id} value={d.id}>{d.name}</MenuItem>)}
          </Select>
        </FormControl>
        <TextField margin="dense" name="scheduled_time" label="Scheduled Time" type="datetime-local" fullWidth value={formData.scheduled_time} onChange={handleChange} InputLabelProps={{ shrink: true }} />
        <TextField margin="dense" name="notes" label="Notes" type="text" multiline rows={3} fullWidth value={formData.notes} onChange={handleChange} />
        <FormControl fullWidth margin="dense">
          <InputLabel>Status</InputLabel>
          <Select name="status" value={formData.status} label="Status" onChange={handleChange}>
            <MenuItem value="PENDING">Pending</MenuItem>
            <MenuItem value="CONFIRMED">Confirmed</MenuItem>
            <MenuItem value="CANCELED">Canceled</MenuItem>
            <MenuItem value="COMPLETED">Completed</MenuItem>
          </Select>
        </FormControl>
         <FormControl fullWidth margin="dense">
          <InputLabel>Urgency</InputLabel>
          <Select name="urgency" value={formData.urgency} label="Urgency" onChange={handleChange}>
            <MenuItem value="ROUTINE">Routine</MenuItem>
            <MenuItem value="URGENT">Urgent</MenuItem>
            <MenuItem value="EMERGENCY">Emergency</MenuItem>
          </Select>
        </FormControl>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button onClick={() => onSave({ ...formData, id: item?.id })}>Save</Button>
      </DialogActions>
    </Dialog>
  );
};

export default AppointmentModal;