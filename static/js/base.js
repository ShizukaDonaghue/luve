// Close Bootstrap hamburger menu when clicked outside the menu
$(document).ready(function() {
    $(document).click(function() {
        $('#main-nav').collapse('hide');
    });
});

// Validate article forms and raise error messages where required
$(document).ready(function() {
    $('.article-form').validate({
        rules: {
            title: 'required',
            description: 'required',
        },

        messages: {
            title: 'Please enter the title.',
            description: 'Please enter the description.',
        },

        submitHandler: function(form) {
            form.submit();
        }
    });
});

// Validate order forms and raise error messages where required
$(document).ready(function() {
    $('.order-form').validate({
        rules: {
            full_name: 'required',
            email: 'required',
            phone_number: 'required',
            street_address1: 'required',
            town_or_city: 'required',
            country: 'required',
        },

        messages: {
            full_name: 'Please enter your name.',
            email: 'Please enter your email address.',
            phone_number: 'Please enter your phone number.',
            street_address1: 'Please enter your street address.',
            town_or_city: 'Please enter you town or city.',
            country: 'Please select your country.',
        },

        submitHandler: function(form) {
            form.submit();
        }
    });
});

// Validate contact forms and raise error messages where required
$(document).ready(function() {
    $('#contact-form').validate({
        rules: {
            query_type: 'required',
            name: 'required',
            email: 'required',
            message: 'required',
        },

        messages: {
            query_type: 'Please select a query type.',
            name: 'Please enter your name.',
            email: 'Please enter your email address.',
            message: 'Please enter your message here.',
        },

        submitHandler: function(form) {
            form.submit();
        }
    });
});

// Validate product forms and raise error messages where required
$(document).ready(function() {
    $('.product-form').validate({
        rules: {
            name: 'required',
            description: 'required',
            price: 'required',
        },

        messages: {
            name: 'Please enter the product name.',
            description: 'Please enter the product description.',
            price: 'Please enter a unit price greater than 0.01.',
        },

        submitHandler: function(form) {
            form.submit();
        }
    });
});
