const boxes = document.querySelectorAll('.box');

// //duyệt từng phần tử (class box) trong mảng boxes 
boxes.forEach((box) => {
    //lấy phần tử đầu tiên trong box có thẻ là button hay class text
    const button = box.querySelector('.btn');
    const text = box.querySelector('.text');
    button.addEventListener('click', () => {
        // Kiểm tra xem phần trả lời đã hiển thị hay chưa, nếu block rồi thì giá trị trả về là true
        const isTestShow = text.style.display === 'block';

        // Tất cả các phần trả lời đều được ẩn đi
        // giúp khi click vào button khác thì sẽ duyệt lại và để các button thành none
        boxes.forEach((box) => {
            box.querySelector('.text').style.display = 'none';
            box.querySelector('.btn').innerHTML = '<i class="fas fa-plus"></i>';
        })

        // Nếu phần trả lời chưa hiển thị, thì hiển thị nó
        if (!isTestShow) {
            text.style.display = 'block';
            button.innerHTML = '<i class="fas fa-minus"></i>';
        }
    });
});