function MovieCard({ movie }) {
    
  return (<>
    
    <div className="movie-card">
      <img 
        src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`} 
        alt={movie.title}
        className="movie-poster"
      />
      <div className="favorite-btn">
        <p>&hearts;</p>
        {/* &#x1F90D; */}
      </div>
      <div className="movie-info">
        <h3>{movie.title}</h3>
        <p>Year: {movie.year}</p>
        {movie.rating && <p>Rating: {movie.rating}/10</p>}
      </div>
    </div>
    </>
  );
}
export default MovieCard;