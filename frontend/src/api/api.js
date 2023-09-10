import axios from "axios";
import Swal from 'sweetalert2'
import { SwalDelete } from "../utils/SwalDelete";


const URL = 'http://localhost:8080'
const recurso = `${URL}/api/tasks`

// GET ALL TASKS
export const fetchGetAllTask = async () => await axios.get(`${recurso}`);


// GET ONE TASK
export const fetchOneTask = async (params_id) => await axios.get(`${recurso}/${params_id}`)


//  POST TASK
export const fetchPostTask = async (title, description) => {
    await axios.post("http://localhost:8080/api/tasks", {
        title,
        description
    })
}


//  PUT TASK
export const fetchPutTask = async (params_id, task) => await axios.put(`${recurso}/${params_id}`, task)


// DELETE TASK
export const handlerDelete = async (task) => SwalDelete(task, fetchDeleteTask)

async function fetchDeleteTask(id) {
    const res = await axios.delete(`http://localhost:8080/api/tasks/${id}`)
}
