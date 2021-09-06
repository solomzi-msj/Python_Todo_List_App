const todos = document.querySelector('ul#todos');

todos.addEventListener('click', e => {
    if(e.target.tagName === 'LI') {
        e.target.classList.toggle('complete');
    } else if (e.target.tagName === 'SPAN') {
        e.target.parentElement.classList.toggle('complete');
    }
});