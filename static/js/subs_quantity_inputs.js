    // Check that a subscription / size has been selected before submitting form
    $('.submit-button').click(function(e) {
        e.preventDefault();
        var form = document.getElementById('add-basket');
        var itemId = $(this).attr('id').split('add_')[1];
        var quantity = parseInt($(`#id_qty_${itemId}`).val());
        var redirect_url = document.getElementById("redirect_url").value;
        var selected_subs = document.getElementById("purchase_subs_size_id").value;
        var size_or_sub = document.getElementById("has_sizes_val").value;
        var submit_msg;
        var url = `/basket/add/${itemId}/`;
        var data = {'csrfmiddlewaretoken': csrfToken, 'quantity': quantity, 
                    'selected_subs_size_id': selected_subs, 'redirect_url': redirect_url};
        
        // Check if product has a subscription or a size
        if (size_or_sub == "False") {
            submit_msg = "A subscription for this product must be selected before adding to basket";
        } else {
            submit_msg = "A product size must be selected before adding to basket";
        }            
        
        if (selected_subs == "None") {
            // If size or subscription hasn't been selected - display message
            document.getElementById("submit-error").innerHTML = submit_msg;
        } else { 
            //Check quantity against stock before submitting
            var qty_status = checkStockAvailable(itemId);
            if (qty_status == "OK") {
                // Submit the form
                $.post(url, data)
                .done(function() {
                    form.submit();
                });
            }
                
        }
    });
