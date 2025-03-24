var form1 = document.querySelector('#register')
var username = document.querySelector('#fullname')
var email = document.querySelector('#email')
var pass = document.querySelector('#password')
var confirmPass = document.querySelector('#password_confirm')

function showError(input, message) {
    let parent = input.parentElement;
    let errorMessage = parent.querySelector('.form-message')

    errorMessage.innerText = message
}

function showSuccess(input) {
    let parent = input.parentElement;
    let errorMessage = parent.querySelector('.form-message')

    errorMessage.innerText = ''

}

function checkEmptyError(listInput) { // Array listInput
    // let isEmptyError = false;
    listInput.forEach(input => {
        input.value = input.value.trim()

        if (!input.value) {
            showError(input, 'Không được để trống')
        } else {
            showSuccess(input)
        }
    });

    // return isEmptyError
}

function checkEmailError(input) {
    const regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    input.value = input.value.trim()

    let isEmailError = !regexEmail.test(input.value)
    if (regexEmail.test(input.value)) {
        showSuccess(input)
    } else {
        showError(input, 'Email không hợp lệ')
    }

    // return isEmailError
}

function checkLengthError(input, min, max) {
    input.value = input.value.trim()

    if (input.value.length < min) {
        showError(input, 'Mật khẩu có tối thiểu 6 kí tự')
        return true
    }

    if (input.value.length > max) {
        showError(input, 'Mật khẩu có tối đa 32 kí tự')
        return true
    }

    showSuccess(input)
        // return false
}

function checkMatchPassword(pass, confirmPass) {
    if (pass.value !== confirmPass.value) {
        showError(confirmPass, 'Mật khẩu không trùng khớp')
        return true
    }

    return false
}

form1.addEventListener('submit', function(e) {
    e.preventDefault()

    let isEmptyError = checkEmptyError([username, email, pass, confirmPass])
    let isEmailError = checkEmailError(email)
    let isUsernameLengthError = checkLengthError(pass, 6, 32)
    let isCheckMatchPassword = checkMatchPassword(pass, confirmPass)
})