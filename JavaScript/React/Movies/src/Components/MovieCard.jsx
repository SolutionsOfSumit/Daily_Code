function MovieCard({movie}) {
    function onFavoriteClick() {
        alert("Clicked")
    }

    return <div className = "movie-card">
        <div className = "movie-poster" ><img src={movie.url} alt={movie.title} /></div>
        <div className = "movie-overlay">
            <button className = "favorite-btn" onCLick = {onFavoriteClick}>
                ♥
            </button>
        </div>
        <div className="MovieInfo">
            <h3>{movie.title}</h3>
            <p>{movie.genre}</p>
        </div>
    </div>
}


export default MovieCard