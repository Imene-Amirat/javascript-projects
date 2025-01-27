const cart = {
    cartItems: undefined,
    
    loadFromStorage() {
        this.cartItems = JSON.parse(localStorage.getItem('cart-oop'));
    
        if(!this.cartItems){
            this.cartItems = [{
                productId: '54e0eccd-8f36-462b-b68a-8182611d9add',
                quantity: 1,
                deliveryOptionId: '1'
            }, {
                productId: '3ebe75dc-64d2-4137-8860-1f5a963e534b',
                quantity: 2,
                deliveryOptionId: '2'
            }];
        }
    },
    
    saveToStorage() {
        localStorage.setItem('cart-oop', JSON.stringify(this.cartItems));
    },

    addToCart(productId) {
        let matchingItem;
        
        this.cartItems.forEach((cartItem) => {
            if(productId === cartItem.productId){
                matchingItem = cartItem;
            }
        })
    
        if(matchingItem)
            matchingItem.quantity += 1;
        else {
            this.cartItems.push({
                productId: productId,
                quantity: 1,
                deliveryOptionsId: '1'
            });
        }
    
        this.saveToStorage();
    },

    removeFromCart(productId){
        const newCart = [];
    
        this.cartItems.forEach((cartItem) => {
            if(cartItem.productId !== productId){
                newCart.push(cartItem);
            }
        });
    
        this.cartItems = newCart;
    
        this.saveToStorage();
    },

    updateDeliveryOption(productId, deliveryOptionId) {
        let matchingItem;
        
        this.cartItems.forEach((cartItem) => {
            if(productId === cartItem.productId){
                matchingItem = cartItem;
            }
        });
    
        matchingItem.deliveryOptionId = deliveryOptionId;
    
        this.saveToStorage();
    }
};

cart.loadFromStorage();

