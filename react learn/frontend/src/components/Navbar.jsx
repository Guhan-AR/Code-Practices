import {Link} from 'react-router'

function NavBar(){
    return <nav className='navbar'>
        <div>
            <Link to='/'>Movie App</Link>
        </div>
        <div>
            <Link to='/favorites'>Favorites</Link>
        </div>
        </nav>
}

export default NavBar