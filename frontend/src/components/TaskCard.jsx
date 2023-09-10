import React from 'react'
import { useNavigate} from 'react-router-dom'
import { fetchPutTask, handlerDelete } from '../api/api';

export default function TaskCard({task}) {

  const navigate = useNavigate()

  return (
    <div>
        <div className='bg-zinc-950 p-4 hover:cursor-pointer hover:bg-gray-950'>
            <div className='flex justify-between'>
              <h2 className='font-bold text-2xl'>{task.title}</h2>
              <button onClick={async (e) => {
                e.stopPropagation()
                const res = await fetchPutTask(task._id, {status_task: !task.status_task})
                if(res.status=== 200) {
                  window.location.reload()
                }
                console.log(res)
              }}
              >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    strokeWidth="1.5"
                    stroke="currentColor"
                    className={`w-6 h-6 ${task.status_task ? 'text-green-500' : ''}`}
                  >
                    <path strokeLinecap="round" strokeLinejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                  </svg>
              </button>
            </div>
            <p className='text-slate-300'>{task.description}</p>

            <button onClick={() => { navigate(`/tasks/${task._id}`)}} className='bg-blue-500 px-3 mr-3 rounded'>
                Editar
            </button>

            <button onClick={() => handlerDelete(task)} className='bg-red-400 px-3 rounded'>Excluir</button>
        </div>
    </div>
  )
}
