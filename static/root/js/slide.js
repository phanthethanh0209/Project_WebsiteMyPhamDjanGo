// Lấy tất cả các hình ảnh thumbnail
const thumbnails = document.querySelectorAll('.thumbnail');

// Duyệt qua từng thumbnail và thêm sự kiện click
thumbnails.forEach((thumbnail) => {
    thumbnail.addEventListener('click', () => {
        // Lấy đường dẫn của hình ảnh được click
        const imagePath = thumbnail.src;

        // Gán đường dẫn của hình ảnh được click vào hình ảnh lớn
        const mainImage = document.querySelector('#main-img');
        mainImage.src = imagePath;
    });
});