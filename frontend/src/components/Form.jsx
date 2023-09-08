import { useState } from 'react'
import axios from 'axios';

export default function Form() {

    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const handlerSubmit = async (e) => {
        e.preventDefault();

        const res = await axios.post("http://localhost:8080/api/tasks", {
            title, 
            description
        })
        console.log(res)
        e.target.reset();
    }

  return (
    <div className='flex items-center justify-center h-[calc(100vh-10rem)]'>
        <form className='bg-zinc-950 p-10' onSubmit={handlerSubmit}>
            <input type='text' placeholder='title' onChange={(e) => setTitle(e.target.value)} className='block items-start py-3 px-20 w-full text-slate-900' />
            <textarea placeholder='descrição' onChange={(e) => setDescription(e.target.value)}  className='block py-2 px-3 mb-4 w-full text-black' rows={5}></textarea>
            <button>Salvar</button>
         </form>
    </div>
  )
}
