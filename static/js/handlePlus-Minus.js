let amountElement = document.getElementById('amount');
let amount = amountElement.value;
console.log(amount);

let render = (amount) => {
        amountElement.value = amount
    }
    //Handle Plus
let handlePlus = () => {
    console.log(amount);
    amount++
    render(amount); // cập nhật lại lên màn hình
}

let handleMinus = () => {
    if (amount > 1)
        amount--;
    render(amount);
}

amountElement.addEventListener('input', () => {
    amount = amountElement.value;
    amount = parseInt(amount); // chuyển về số nguyên
    amount = (isNaN(amount) || amount == 0) ? 1 : amount;
    render(amount);
});