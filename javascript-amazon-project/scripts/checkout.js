import {renderOrderSummary} from './checkout/orderSummary.js';
import {renderPaymentSummary} from './checkout/paymentSummary.js';
import {loadProducts, loadProductsFetch} from '../data/products.js';
//import '../data/cart-class.js';
//import '../data/backend-practice.js';

loadProductsFetch().then(() => {
    renderOrderSummary();
    renderPaymentSummary();
});


/* // This is the same as the code above but we use callback functions
loadProducts(() => {
    renderOrderSummary();
    renderPaymentSummary();
});
*/
