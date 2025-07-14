import { useState, useEffect } from 'react';
import { Dialog, DialogActions, DialogContent, DialogTitle, TextField, Button, Select, MenuItem, InputLabel, FormControl } from '@mui/material';

const MedicineModal = ({ open, onClose, onSave, item, medicineTypes }) => {
  const [formData, setFormData] = useState({ name: '', expiry_date: '', medicine_type: '', warning: '' });

  useEffect(() => {
    const initialType = item ? (item.medicine_type?.id || item.medicine_type) : '';
    setFormData(item ? { ...item, medicine_type: initialType } : { name: '', expiry_date: '', medicine_type: '', warning: '' });
  }, [item, open]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>{item ? 'Edit Medicine' : 'Add New Medicine'}</DialogTitle>
      <DialogContent>
        <TextField autoFocus margin="dense" name="name" label="Medicine Name" type="text" fullWidth variant="standard" value={formData.name} onChange={handleChange} />
        <TextField margin="dense" name="expiry_date" label="Expiry Date" type="date" fullWidth variant="standard" value={formData.expiry_date} onChange={handleChange} InputLabelProps={{ shrink: true }} />
        <FormControl fullWidth margin="dense" variant="standard">
          <InputLabel>Type</InputLabel>
          <Select name="medicine_type" value={formData.medicine_type} label="Type" onChange={handleChange}>
            {medicineTypes.map(type => <MenuItem key={type.id} value={type.id}>{type.name}</MenuItem>)}
          </Select>
        </FormControl>
        <TextField margin="dense" name="warning" label="Warning" type="text" multiline rows={2} fullWidth variant="standard" value={formData.warning} onChange={handleChange} />
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button onClick={() => onSave({ ...formData, id: item?.id })}>Save</Button>
      </DialogActions>
    </Dialog>
  );
};

export default MedicineModal;