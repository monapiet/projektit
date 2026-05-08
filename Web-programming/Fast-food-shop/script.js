// Array that stores all items added tol the cart
let cart = [];

//list for the products
let products = [
    {id: 1, name: "Burger", price: 7.90 },
    {id: 2, name: "French Fries", price: 3.90 },
    {id: 3, name: "Pizza", price: 3.90 },
    {id: 4, name: "Cola", price: 3.00 },
    {id: 5, name: "Orange Juice", price: 3.00 },
    {id: 6, name: "Icecream", price: 4.00 },
];

// event listener for every add to cart button
document.querySelectorAll(".addCart").forEach(btn => {
    btn.addEventListener("click", () => {
        //Read the product ID from the button's data attribute
        const id = Number(btn.dataset.id);
        // Find the matching product from the product list
        const product = products.find( p => p.id === id);
        // Add the selected product to the cart
        addToCart(product.name, product.price);
    });
})

// function that adds the product to cart and updates the cart display
function addToCart(name,price) {
    cart.push({ name, price });
    updateCart();
}

// Updates the cart section in the HTML with all items and total price
function updateCart() {
    const cartDiv = document.getElementById("cart");
    cartDiv.innerHTML = "";

    let total = 0;
    // Loop through all cart items and display them
    cart.forEach(item => {
        cartDiv.innerHTML += `<p>${item.name} – ${item.price} €</p>`;
        total += item.price;
    });
    // Display the total price at the bottom
    cartDiv.innerHTML += `<h3>Total: ${total.toFixed(2)} €</h3>`;
}
