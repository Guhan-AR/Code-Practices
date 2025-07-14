import { useState, useEffect } from 'react';
import { Dialog, DialogActions, DialogContent, DialogTitle, TextField, Button } from '@mui/material';

// This modal receives the item to edit, or null if creating a new one
const DepartmentModal = ({ open, onClose, onSave, item }) => {
  const [name, setName] = useState('');

  // When the 'item' prop changes, update the form state
  useEffect(() => {
    if (item) {
      setName(item.name || '');
    } else {
      // If no item, it's a new entry, so clear the form
      setName('');
    }
  }, [item, open]); // Re-run effect if item or open status changes

  const handleSave = () => {
    // Pass the form data back to the parent page to handle the API call
    onSave({ id: item?.id, name });
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>{item ? 'Edit Department' : 'Add New Department'}</DialogTitle>
      <DialogContent>
        <TextField
          autoFocus
          margin="dense"
          label="Department Name"
          type="text"
          fullWidth
          variant="standard"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        {/* If your model had more fields, you would add more TextFields here */}
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button onClick={handleSave}>Save</Button>
      </DialogActions>
    </Dialog>
  );
};

export default DepartmentModal;