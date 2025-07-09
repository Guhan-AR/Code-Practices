import Favorite from './pages/Favorites'
import Home from './pages/Home'
import NavBar from './components/Navbar'
import { Route, Routes } from 'react-router'

function App() {

  var movielist = {
    title: "john wick",
    year: 2017,
    rating: 9.5
  }

  return <>
  <div>
    <NavBar/>
  </div>
  <main className='main content'>
    <div>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/favorites" element={<Favorite/>} />
      </Routes>
    </div>
  </main>
  </>
}

export default App
