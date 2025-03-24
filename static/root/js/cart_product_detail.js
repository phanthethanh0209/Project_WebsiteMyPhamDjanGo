let cartItemCount = 0;
// const cartIcon = document.querySelector('heading-cart');
const addToCartBtn = document.getElementById('btn-buynow');
const quantity = document.querySelector(".quantity-cart");

addToCartBtn.addEventListener('click', (event) => {
    cartItemCount++;
    quantity.innerText = `${cartItemCount}`;
    // quantity.innerText = card.length;

    var productImg = document.querySelector(".product-card img").src
    var productName = document.querySelector(".name-product").innerText
    var productPrice = document.querySelector(".price-new").innerText
    var productQuantity = document.querySelector("#amount").value
        // console.log(productImg, productName, productPrice)
    var cardItem = document.querySelectorAll(".list-item-cart .item")

    console.log(productQuantity)
    addcart(productImg, productName, productPrice, productQuantity);
});

function addcart(productImg, productName, productPrice, productQuantity) {
    var addli = document.createElement("li")

    var licontent = '<li class="item"> <div class="row row2 justify-content-between"> <div class="col-md-2 img-item"><img src="' + productImg + '" alt=""></div><div class="col-md-8 info-product"><div class="name-product">' + productName + '</div><div class="cost-product">' + productPrice + '</div><div class="quantity"><input type="number" value="' + productQuantity + '" min="0"></div></div><div class="col-md-2 delete-product"><div class="delete-icon"><i class="ti-trash"></i></div></div></div></li>'
    addli.innerHTML = licontent
    var cartul = document.querySelector(".list-item-cart")
    cartul.append(addli)

    cardtotal()
    deleteCart()
    inputChange()
}

// -------------------------total price------------------------ 
function cardtotal() {
    var cardItem = document.querySelectorAll(".list-item-cart .item")
    var totalEnd = 0;
    // console.log(cardItem.length)
    for (var i = 0; i < cardItem.length; i++) {
        var inputValue = cardItem[i].querySelector("input").value
        var productPrice = cardItem[i].querySelector(".cost-product").innerHTML

        totalBegin = productPrice * inputValue * 1000
        totalEnd = totalEnd + totalBegin
        console.log(totalBegin)
    }
    var cartTotalBegin = document.querySelector(".total-cost")
    cartTotalBegin.innerHTML = totalEnd.toLocaleString('de-DE') //xử lý chuỗi để có các số 0 sau dấu chấm vd: 500.000

}

function deleteCart() {
    var cardItem = document.querySelectorAll(".list-item-cart .item")
    for (var i = 0; i < cardItem.length; i++) {
        var productT = document.querySelectorAll(".ti-trash")
        productT[i].addEventListener('click', function(event) {
            var cardDelete = event.target.parentElement

            var carttemR = cardDelete.parentElement.parentElement.parentElement
                // console.log(carttemR)
            carttemR.remove()
            cardtotal()

            // quantity.innerText = `${cartItemCount}`
        })
        console.log(cartItemCount)

    }
}

function inputChange() {
    var cardItem = document.querySelectorAll(".list-item-cart .item")

    for (var i = 0; i < cardItem.length; i++) {
        var inputValue = cardItem[i].querySelector("input")
        inputValue.addEventListener("change", function() {
            cardtotal()
        })
    }
}