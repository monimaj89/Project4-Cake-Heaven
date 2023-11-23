/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePubliKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePubliKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');


// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});


// Handle form submit
var form = document.getElementById('payment-form');

// Event listener for payment form submit
form.addEventListener('submit', function(ev) {
    ev.preventDefault();

    // Disables the submit button & card input to prevent multiple submission
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    // Passes card details to Stripe
    stripe.confirmCardPayment(clientSecret, {

        // Sends payment details 
        payment_method: {
            card: card,
        }
    }).then(function(result) {

        // Send error message in case of error occurs
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);

            // Re-enable the submit button and card input
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
            
            // if payment details are valid submit payment form
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});