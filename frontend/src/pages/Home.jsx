import React, { useEffect, useState } from 'react'
import axios from 'axios'
import TaskList from '../components/TaskList';


function Home() {

  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    async function fetchTasks() {
      const res = await axios.get("http://localhost:8080/api/tasks");
      setTasks(res.data)
    }
    
    fetchTasks();
  
  }, [])

  return (
    <div>
        <h1>Home</h1>
        <TaskList tasks={tasks}/>
    </div>
  )
}

export default Home