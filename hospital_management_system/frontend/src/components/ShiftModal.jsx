import { useState, useEffect } from 'react';
import { Dialog, DialogActions, DialogContent, DialogTitle, TextField, Button } from '@mui/material';

const ShiftModal = ({ open, onClose, onSave, item }) => {
  const [formData, setFormData] = useState({ name: '', start_time: '', end_time: '' });

  useEffect(() => {
    setFormData(item ? { ...item } : { name: '', start_time: '', end_time: '' });
  }, [item, open]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>{item ? 'Edit Shift' : 'Add New Shift'}</DialogTitle>
      <DialogContent>
        <TextField autoFocus margin="dense" name="name" label="Shift Name" type="text" fullWidth variant="standard" value={formData.name} onChange={handleChange} />
        <TextField margin="dense" name="start_time" label="Start Time" type="time" fullWidth variant="standard" value={formData.start_time} onChange={handleChange} InputLabelProps={{ shrink: true }} />
        <TextField margin="dense" name="end_time" label="End Time" type="time" fullWidth variant="standard" value={formData.end_time} onChange={handleChange} InputLabelProps={{ shrink: true }} />
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button onClick={() => onSave({ ...formData, id: item?.id })}>Save</Button>
      </DialogActions>
    </Dialog>
  );
};

export default ShiftModal;