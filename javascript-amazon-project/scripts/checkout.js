import {renderOrderSummary} from './checkout/orderSummary.js';
import {renderPaymentSummary} from './checkout/paymentSummary.js';
import {loadProducts, loadProductsFetch} from '../data/products.js';
//import '../data/cart-class.js';
//import '../data/backend-practice.js';

// This is the same as the code below but we use async/await
async function loadPage(){
    try{
        // throw new Error('Unexpected error, Please try again later.');
        
        await loadProductsFetch();
    }
    catch(error){
        console.log('Unexpected error, Please try again later.');
    }
    renderOrderSummary();
    renderPaymentSummary();
}

loadPage();

/* // This is the same as the code above but we use promises
loadProductsFetch().then(() => {
    renderOrderSummary();
    renderPaymentSummary();
});
*/


/* // This is the same as the code above but we use callback functions
loadProducts(() => {
    renderOrderSummary();
    renderPaymentSummary();
});
*/
