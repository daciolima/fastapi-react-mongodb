import Swal from 'sweetalert2'


export function SwalDelete(task, fetchDeleteTask) {
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
