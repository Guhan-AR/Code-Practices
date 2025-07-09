import MovieCard from "../components/MovieCard"
import SearchBar from "../components/SearchBar"
import { getPopularMovies,searchMovies } from "../services/api";
import { useEffect } from "react";
import { useState } from "react"

function Home() {
    const [searchQuery, setSearchQuery] = useState("");
    const [movies,setmovies] = useState([])
    const [error,seterror] = useState(null)
    const [loading,setloading] = useState(true)
    useEffect(()=>{
        const LoadPopularmovies = async () => {
            try{
                console.log('trying');
                const PopularMovies = await getPopularMovies();
                setmovies(PopularMovies);
            }
            catch(err){
                console.log('error');
                console.log(err);
                seterror("Failed to load movies..");
            }
            finally{
                console.log('final');

                setloading(false);
            }
        }
        LoadPopularmovies()
    },[])
    
    console.log('here');
    const filtered_Movies = movies.filter((movie) => movie.title.toLowerCase().includes(searchQuery.toLowerCase()));
    console.log('here:',filtered_Movies);
    return <div className="home">
        <SearchBar searchQuery={searchQuery} setSearchQuery={setSearchQuery} />
        {filtered_Movies.map((movie) => (<MovieCard movie={movie} key={movie.id} />))}
    </div>
}

export default Home


    // const movies = [{
    //     id: 1,
    //     title: "john wick",
    //     year: 2017,
    //     rating: 9.5
    // }, {
    //     id: 2,
    //     title: "HTTYD",
    //     year: 2016,
    //     rating: 9.4
    // }, {
    //     id: 3,
    //     title: "Indian 2",
    //     year: 2024,
    //     rating: 9.5
    // },];
