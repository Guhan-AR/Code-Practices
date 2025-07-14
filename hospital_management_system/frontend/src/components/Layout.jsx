import { Outlet, Link } from 'react-router-dom';
import { Box, Drawer, List, ListItem, ListItemButton, ListItemIcon, ListItemText, AppBar, Toolbar, Typography, Button } from '@mui/material';
import DashboardIcon from '@mui/icons-material/Dashboard';
import PeopleIcon from '@mui/icons-material/People';
import LocalHospitalIcon from '@mui/icons-material/LocalHospital';
import MedicalServicesIcon from '@mui/icons-material/MedicalServices';
import AssignmentIcon from '@mui/icons-material/Assignment';
import ScienceIcon from '@mui/icons-material/Science';
import ScheduleIcon from '@mui/icons-material/Schedule';
import { useAuth } from '../context/AuthContext';

const drawerWidth = 240;

// An array to make the sidebar items easier to manage
const menuItems = [
  { text: 'Dashboard', path: '/', icon: <DashboardIcon /> },
  { text: 'Departments', path: '/departments', icon: <LocalHospitalIcon /> },
  { text: 'Shifts', path: '/shifts', icon: <ScheduleIcon /> },
  { text: 'Doctors', path: '/doctors', icon: <PeopleIcon /> },
  { text: 'Patients', path: '/patients', icon: <PeopleIcon color="secondary" /> },
  { text: 'Appointments', path: '/appointments', icon: <AssignmentIcon /> },
  { text: 'Medicines', path: '/medicines', icon: <MedicalServicesIcon /> },
  { text: 'Medicine Types', path: '/medicine-types', icon: <ScienceIcon /> },
];

const Layout = () => {
  const { logout } = useAuth();
  return (
    <Box sx={{ display: 'flex' }}>
      <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
        <Toolbar>
          <Typography variant="h6" noWrap component="div" sx={{ flexGrow: 1 }}>
            Hospital Dashboard
          </Typography>
          <Button color="inherit" onClick={logout}>Logout</Button>
        </Toolbar>
      </AppBar>
      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' },
        }}
      >
        <Toolbar />
        <Box sx={{ overflow: 'auto' }}>
          <List>
            {menuItems.map((item) => (
              <ListItem key={item.text} disablePadding component={Link} to={item.path} sx={{ color: 'inherit', textDecoration: 'none' }}>
                <ListItemButton>
                  <ListItemIcon>{item.icon}</ListItemIcon>
                  <ListItemText primary={item.text} />
                </ListItemButton>
              </ListItem>
            ))}
          </List>
        </Box>
      </Drawer>
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <Toolbar />
        <Outlet /> {/* Your page content renders here */}
      </Box>
    </Box>
  );
};

export default Layout;