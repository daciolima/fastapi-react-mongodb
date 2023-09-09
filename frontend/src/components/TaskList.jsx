import React from 'react'
import TaskCard from './TaskCard'
import axios from 'axios';
import Swal from 'sweetalert2'

export default function TaskList({tasks}) {
  
    const handlerDelete = async (task) => {

        Swal.fire({
            title: 'Confirmação de exclusão de Task',
            text: `Você deseja deletar a task: ${task.title}?`,
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sim'
        }).then((result) => {
            if (result.isConfirmed) {
                
                fetchDeleteTask(task._id);

                Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: 'Task deletada!',
                    showConfirmButton: false,
                    timer: 2500
                })
            }
        })
    }

    async function fetchDeleteTask(id) {
        const res = await axios.delete(`http://localhost:8080/api/tasks/${id}`)
    }

  return (
    <div className='grid grid-cols-3 gap-4'>
        {
            tasks.map((task) => (
                <TaskCard task={task} key={task._id} handlerDelete={handlerDelete} />
            ))
        }

    </div>
  )
}
