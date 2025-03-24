function myFunction() {
    var flipElement = document.getElementById('flip');

    if (flipElement.innerText === 'Xem Thêm') {
        flipElement.innerText = 'Ẩn Bớt';
        document.getElementById("panel").style.display = "block";
    } else {
        flipElement.innerText = 'Xem Thêm';
        document.getElementById("panel").style.display = "none";
    }

}