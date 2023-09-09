import React from 'react'
import { useNavigate} from 'react-router-dom'

export default function TaskCard({task, handlerDelete}) {
    
    const navigate = useNavigate()

    return (
        <div>
            <div className='bg-zinc-950 p-4 hover:cursor-pointer hover:bg-gray-950'>
                <h2>{task.title}</h2>
                <p>{task.description}</p>
                
                <button onClick={() => { navigate(`/tasks/${task._id}`)}} className='bg-blue-500 px-3 mr-3 rounded'>
                    Editar
                </button>
                
                <button onClick={() => handlerDelete(task)} className='bg-red-400 px-3 rounded'>Excluir</button>
            </div>
        </div>
    )
}
