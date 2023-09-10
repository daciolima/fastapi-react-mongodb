import React, { useEffect, useState } from 'react'
import TaskList from '../components/TaskList';
import { fetchGetAllTask } from '../api/api';
import axios from 'axios';


function Home() {

  const [tasks, setTasks] = useState([]);

  useEffect(() => {

    async function fetchTasks() {
      fetchGetAllTask()
      .then((res) => {
        setTasks(res.data)
      })
    }

    fetchTasks();
  }, [])

  return <TaskList tasks={tasks}/>;

}

export default Home
