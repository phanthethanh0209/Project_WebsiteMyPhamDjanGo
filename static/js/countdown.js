const hours = document.getElementById('hours');
const minutes = document.getElementById('min');
const seconds = document.getElementById('sec');

const currentYear = new Date().getFullYear();

const endTime = new Date(currentYear, new Date().getMonth(), new Date().getDate() + 1);

function updateCountdown() {
    const currentTime = new Date();
    const diff = endTime - currentTime;
    // diff có đơn vị mili giây
    // dùng Math.floor để làm tròn xuống thành số nguyên gần nhất
    const h = Math.floor(diff / 1000 / 60 / 60) % 24;
    const m = Math.floor(diff / 1000 / 60) % 60;
    const s = Math.floor(diff / 1000) % 60;

    hours.innerHTML = h;
    minutes.innerHTML = m < 10 ? '0' + m : m;
    seconds.innerHTML = s < 10 ? '0' + s : s;
}

setInterval(updateCountdown, 1000);