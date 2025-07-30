import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Text text="Sumit" />
    <Text text="Sumit" />
    </>
  )
}

function Text({text}) {
  return (
  <div>
    <p>My Name is</p>
    <p>{text} is a Monster</p>
  </div>
  )
}
export default App