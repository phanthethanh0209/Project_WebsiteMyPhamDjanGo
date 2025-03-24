const account = document.querySelectorAll('.js-login');
const form = document.querySelector('.js-form')
const formClose = document.querySelector('.js-formClose')

// Hàm hiển thị form mua vé (thêm class open form)
function showaccount() {
    form.classList.add('open')
}

// Hàm ẩn form mua vé  (gỡ bỏ class open của form)
function hideaccount() {
    form.classList.remove('open')
}

// Lặp qua từng thẻ button và nghe hành vi click
for (const accBtn of account) {
    accBtn.addEventListener('click', showaccount)
}

// Nghe hành vi click vào button close
formClose.addEventListener('click', hideaccount)

// var s = document.getElementById("submit");
// s.onclick = function() {
//     alert("Lỗi hệ thống đang cập nhật !");

// }