import './App.css'
import MovieCard from './Components/MovieCard'

function App() {
  const movieNumber = 1;

  return (

    <>
    {movieNumber === 1 && <MovieCard movie = {{ title: "Joes Film", genre: "Action"}} />}
    </> 
  )
}

export default App
