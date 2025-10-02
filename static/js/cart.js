document.addEventListener("DOMContentLoaded", function () {
    function updateCart() {
        let subtotal = 0;

        document.querySelectorAll("tbody tr").forEach(row => {
            let price = parseFloat(
                row.querySelector("td:nth-child(3)").innerText.replace("$", "")
            );
            let qtyInput = row.querySelector(".quantity-amount");
            let qty = parseInt(qtyInput.value);

            // nếu số lượng không hợp lệ thì đặt = 0
            if (isNaN(qty) || qty < 0) {
                qty = 0;
                qtyInput.value = 0;
            }

            let total = price * qty;
            row.querySelector("td:nth-child(5)").innerText = "$" + total.toFixed(2);
            subtotal += total;
        });

        // cập nhật subtotal và total
        document.querySelector("#cart-subtotal").innerText = "$" + subtotal.toFixed(2);
        document.querySelector("#cart-total").innerText = "$" + subtotal.toFixed(2);
    }

    // tăng số lượng (+1)
    document.querySelectorAll(".increase").forEach(btn => {
        btn.addEventListener("click", function () {
            let input = this.closest(".quantity-container").querySelector(".quantity-amount");
            input.value = parseInt(input.value || 0) + 1;
            updateCart();
        });
    });

    // giảm số lượng (-1, không nhỏ hơn 0)
    document.querySelectorAll(".decrease").forEach(btn => {
        btn.addEventListener("click", function () {
            let input = this.closest(".quantity-container").querySelector(".quantity-amount");
            let current = parseInt(input.value || 0);
            input.value = current > 0 ? current - 1 : 0;
            updateCart();
        });
    });

    // nhập trực tiếp (chỉ tính khi đổi xong)
    document.querySelectorAll(".quantity-amount").forEach(input => {
        input.addEventListener("change", updateCart);
    });

    // xóa sản phẩm
    document.querySelectorAll(".product-remove a").forEach(btn => {
        btn.addEventListener("click", function (e) {
            e.preventDefault();
            this.closest("tr").remove();
            updateCart();
        });
    });

    // chạy lần đầu
    updateCart();
});
