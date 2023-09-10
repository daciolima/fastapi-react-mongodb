import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { fetchOneTask, fetchPostTask, fetchPutTask } from '../api/api';

export default function Form() {

    const params = useParams();
    const navigate = useNavigate();

    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const handlerSubmit = async (e) => {
        e.preventDefault();

        try {
          if (!params.id) {
            await fetchPostTask({title, description});
          } else {
            await fetchPutTask(params.id, {title, description});
          }
          navigate("/")
        } catch (error) {
          console.log(error)
        }
        e.target.reset();

    }

    useEffect(() => {
      if(params.id) {
        fetchOneTask(params.id)
        .then((res) => {
          setTitle(res.data.title);
          setDescription(res.data.description);
        })
        .catch((err) => console.log(err));
      }
    }, [])

  return (
    <div className='flex items-center justify-center h-[calc(100vh-10rem)]'>
        <form className='bg-zinc-950 p-10' onSubmit={handlerSubmit}>
          <h1 className='text-2xl font-bold my-4'>
            {params.id ? "Atualizar Task" : "Criar Task"}
          </h1>
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
            <button className='bg-yellow-800 hover:bg-yellow-900 px-3 py-1 w-full rounded'>
              {params.id ? "Atualizar Task" : "Criar Task"}
            </button>
         </form>
    </div>
  )
}
