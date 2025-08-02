import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {

  return (
    <>
    <Text text = "Sumit" />
    <Text text = "Is a Monster" /> 
    </>
  )
}

function Text({text}) {
  return <div>
    <p>{text}</p>
  </div>
}
export default App
