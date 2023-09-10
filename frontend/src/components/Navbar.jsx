import React from 'react'
import { Link } from 'react-router-dom'

export default function Navbar() {
  return (
    <header className='flex justify-between items-center my-7'>
      <Link to='/'><h1 className='text-3xl font-bold'>Task App</h1></Link>
      <Link to='/cadastro-task' className='bg-yellow-600 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded'>Criar Task</Link>
    </header>
  )
}
