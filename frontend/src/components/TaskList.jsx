import React from 'react'
import TaskCard from './TaskCard'

export default function TaskList({tasks}) {

    return (
        <div className='grid grid-cols-3 gap-4'>
            {
                tasks.map((task) => (
                    <TaskCard task={task} key={task._id}/>
                ))
            }

        </div>
  )
}
