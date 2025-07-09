const API_KEY = "0781c379dd510c824b4bb6c064f36dd4"
const BASE_URL = "http://api.themoviedb.org/3"

export const getPopularMovies = async () => {
    const response = await fetch(`${BASE_URL}/movies/popular?api_key=${API_KEY}`);
    const data = await response.json();
    console.log("Got data::::" + data);
    return data.results
};


export const searchMovies = async (query) => {
    const response = await fetch(`${BASE_URL}/search/movie?api_key=${API_KEY}&query=${encodeURIComponent(query)}`);
    const data = await response.json();
    console.log("search:" + data);
    return data.results
};
