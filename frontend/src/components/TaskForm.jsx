import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

export default function Form() {

    const params = useParams();
    const navigate = useNavigate();

    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const handlerSubmit = async (e) => {
        e.preventDefault();

        try {
          if (!params.id) {

            const res = await axios.post("http://localhost:8080/api/tasks", {
                title, 
                description
            })
          } else {
            const res = await axios.put(`http://localhost:8080/api/tasks/${params.id}`, {
                title, 
                description
            })
          }
          navigate("/")
        } catch (error) {
          console.log(error)
        }
        e.target.reset();

    }

    useEffect(() => {
      if(params.id) {
        fetchTask();
      }

      async function fetchTask() {
        const res = await axios.get(`http://localhost:8080/api/tasks/${params.id}`)
        setTitle(res.data.title)
        setDescription(res.data.description)
      }
    }, [])

  return (
    <div className='flex items-center justify-center h-[calc(100vh-10rem)]'>
        <form className='bg-zinc-950 p-10' onSubmit={handlerSubmit}>
            <input 
              type='text' 
              placeholder='title' 
              onChange={(e) => setTitle(e.target.value)} 
              className='block py-3 px-3 mb-4 w-full text-black' value={title} autoFocus />
            <textarea 
              placeholder='descrição' 
              onChange={(e) => setDescription(e.target.value)}  
              className='block py-2 px-3 mb-4 w-full text-black' value={description} 
              rows={5}></textarea>
            <button className='bg-gray-500 px-3 py-1 w-full bd'>
              {params.id ? "Atualizar Task" : "Criar Task"}
            </button>
         </form>
    </div>
  )
}
