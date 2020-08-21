$("#qty-alert").hide();

// Check that a subscription / size has been selected before submitting form
$('.submit-button').click(function(e) {
    var form = document.getElementById('add-basket');
    var itemId = $(this).attr('id').split('add_')[1];
    var quantity = parseInt($(`#id_qty_${itemId}`).val());
    var redirect_url = document.getElementById("redirect_url").value;
    var selected_subs = document.getElementById("purchase_subs_size_id").value;
    var size_or_sub = document.getElementById("has_sizes_val").value;
    //var qty_available = parseInt(document.getElementById("purchase_qty_available").value);
    if (document.getElementById("purchase_qty_available") != null) {
        var qty_available = Number(document.getElementById("purchase_qty_available").value);
    } else {
        var qty_available = 0;
    }
    var submit_msg;

    var csrfToken = "{{ csrf_token }}";
    var url = `/basket/add/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrfToken, 'quantity': quantity, 
                'selected_subs_size_id': selected_subs, 'redirect_url': redirect_url};
    
    //Check if product has a subscription or a size
    if (size_or_sub == "False") {
        submit_msg = "A subscription for this product must be selected before adding to basket";
    } else {
        submit_msg = "A product size must be selected before adding to basket";
    }            
    
    if (selected_subs == "None") {
        //If size or subscription hasn't been selected - display message
        document.getElementById("submit-error").innerHTML = submit_msg;
    } else {
        //Check for quantity against Quantity available - if manually entered
        if (quantity > qty_available) {
            /* Credit: https://stackoverflow.com/a/48863795 - answer to a question:
                "How to use bootstrap alert message inside a javascript function?" 
                - This code displays the qty-alert box and then slides it up
                    after a number of seconds of being displayed
            */
            $("#qty-alert").fadeTo(2000, 500).slideUp(1000, function(){
                $("#qty-alert").slideUp(1000);
            });
        } else {
            //Post the form to add to basket
            $.post(url, data)
            .done(function() {
                form.submit()
            });
        }
    }
})