const clock = document.querySelector('.clock');

const tick = () => {
    const now = new Date();

    const hour = now.getHours();
    const minutes = now.getMinutes();
    const secs = now.getSeconds();

    const html = `
        <span>${hour}</span> : 
        <span>${minutes}</span> : 
        <span>${secs}</span>
    `;

    clock.innerHTML = html;
};

setInterval(tick, 1000);