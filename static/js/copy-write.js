const copyBtn = document.querySelector('#copy-button');
const codeSnippet = document.querySelector('#code-snippet');

copyBtn.addEventListener('click', () => {
    const code = codeSnippet.innerText.trim(); // lấy nội dung mã
    navigator.clipboard.writeText(code); // sao chép vào clipboard
    // Thay đổi văn bản trạng thái
    copyBtn.textContent = 'Đã sao chép';

    // Đặt lại văn bản trạng thái cũ sau 2 giây
    setTimeout(() => {
        copyBtn.textContent = 'Sao chép mã';
    }, 2000);
});

// const copyBtn = document.querySelectorAll('.btn-copy');
// const codeSnippet = document.querySelector('.code-snippet');
// for (const btncopy of copyBtn) {
//     btncopy.addEventListener('click', () => {
//         const code = codeSnippet.innerText.trim(); // lấy nội dung mã
//         navigator.clipboard.writeText(code); // sao chép vào clipboard
//         // Thay đổi văn bản trạng thái
//         btncopy.textContent = 'Đã sao chép';

//         // Đặt lại văn bản trạng thái cũ sau 2 giây
//         setTimeout(() => {
//             btncopy.textContent = 'Sao chép mã';
//         }, 2000);
//     });
// }