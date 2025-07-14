import { useState, useEffect } from 'react';
import { Dialog, DialogActions, DialogContent, DialogTitle, TextField, Button } from '@mui/material';

const MedicineTypeModal = ({ open, onClose, onSave, item }) => {
  const [name, setName] = useState('');

  useEffect(() => {
    setName(item ? item.name || '' : '');
  }, [item, open]);

  const handleSave = () => {
    onSave({ id: item?.id, name });
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>{item ? 'Edit Medicine Type' : 'Add New Medicine Type'}</DialogTitle>
      <DialogContent>
        <TextField autoFocus margin="dense" label="Type Name" type="text" fullWidth variant="standard" value={name} onChange={(e) => setName(e.target.value)} />
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button onClick={handleSave}>Save</Button>
      </DialogActions>
    </Dialog>
  );
};

export default MedicineTypeModal;