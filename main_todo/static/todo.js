const todos = document.querySelector('ul#todos');
const searchInput = document.querySelector('#search');

todos.addEventListener('click', e => {
    if(e.target.tagName === 'LI') {
        e.target.classList.toggle('complete');
    } else if (e.target.tagName === 'SPAN') {
        e.target.parentElement.classList.toggle('complete');
    }
});

// searching Todos
const tasks = document.querySelectorAll('ul li span');
searchInput.addEventListener('keyup',() => {
    tasks.forEach(task => {
        if(!task.textContent.includes(searchInput.value)) {
            task.parentElement.classList.add('d-none');
        } else {
            task.parentElement.classList.remove('d-none');
        }
    });
});