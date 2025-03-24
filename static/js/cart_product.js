let cartItemCount = 0;
const addToCartBtns = document.querySelectorAll('.product-item-btn-addcart');
const quantity = document.querySelector(".quantity-cart");

addToCartBtns.forEach(function(btn) {
    btn.addEventListener('click', function(event) {
        cartItemCount++;
        quantity.innerText = `${cartItemCount}`;

        // this.closest được sử dụng để tìm phần tử gần nhất (closest) có selector khớp với một điều kiện nào đó từ phần tử đang thực thi mã (context element).
        // this.closest('.home-product-item') sử dụng để tìm phần tử cha gần nhất có class home-product-item bằng cách đi lên từ phần tử hiện tại  (this).
        var tagImg = this.closest('.home-product-item').querySelector('.product-item-img');
        var backgroundImage = tagImg.style.backgroundImage; // lấy giá trị bên trong thuộc tính bg-img (url(...))
        var productImg = backgroundImage.match(/url\(['"]?([^'"]+)['"]?\)/)[1]; //để trích xuất đường dẫn của hình ảnh từ giá trị của thuộc tính CSS background-image.

        var productName = this.closest('.home-product-item').querySelector(".product-item-name").innerText;
        var productPrice = this.closest('.home-product-item').querySelector(".price-current").innerText;

        addcart(productImg, productName, productPrice);
    });
});

function addcart(productImg, productName, productPrice) {
    var addli = document.createElement("li");

    var licontent = '<li class="item"> <div class="row row2 justify-content-between"> <div class="col-md-2 img-item"><img src="' + productImg + '" alt=""></div><div class="col-md-8 info-product"><div class="name-product">' + productName + '</div><div class="cost-product">' + productPrice + '</div><div class="quantity"><input type="number" value="1" min="0"></div></div><div class="col-md-2 delete-product"><div class="delete-icon"><i class="ti-trash"></i></div></div></div></li>';
    addli.innerHTML = licontent;
    var cartul = document.querySelector(".list-item-cart");
    cartul.append(addli); //để chèn phần tử <li> mới (biến addli) vào cuối phần tử đã chọn trong bước trước.

    cardtotal();
    deleteCart();
    inputChange();
}

// -------------------------total price------------------------
function cardtotal() {
    var cardItem = document.querySelectorAll(".list-item-cart .item");
    var totalEnd = 0;

    for (var i = 0; i < cardItem.length; i++) {
        var inputValue = cardItem[i].querySelector("input").value;
        var productPrice = cardItem[i].querySelector(".cost-product").innerHTML;

        totalBegin = productPrice * inputValue * 1000;
        totalEnd = totalEnd + totalBegin;
    }

    var cartTotalBegin = document.querySelector(".total-cost");
    cartTotalBegin.innerHTML = totalEnd.toLocaleString('de-DE');
}

function deleteCart() {
    var cardItem = document.querySelectorAll(".list-item-cart .item");

    for (var i = 0; i < cardItem.length; i++) {
        var productT = document.querySelectorAll(".ti-trash");
        productT[i].addEventListener('click', function(event) {
            var cardDelete = event.target.parentElement;
            var carttemR = cardDelete.parentElement.parentElement.parentElement;
            carttemR.remove();
            cardtotal();
        });
    }
}

function inputChange() {
    var cardItem = document.querySelectorAll(".list-item-cart .item");

    for (var i = 0; i < cardItem.length; i++) {
        var inputValue = cardItem[i].querySelector("input");
        inputValue.addEventListener("change", function() {
            cardtotal();
        });
    }
}