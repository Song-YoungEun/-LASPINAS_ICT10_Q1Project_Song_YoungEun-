

def SKU_generator(e):
    document["sku_output"].innerHTML = ""

    category = document["category"].value.strip()
    product_name = document["product_name"].value.strip()
    stock_qty = document["quantity"].value.strip()

    if not category or not product_name or not stock_qty:
        document["sku_output"].innerHTML = "Please fill in all fields."
        return

    try:
        quantity = int(stock_qty)
        if quantity < 0:
            raise ValueError()
    except ValueError:
        document["sku_output"].innerHTML = "Enter a valid stock quantity."
        return

    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(quantity)

    document["sku_output"].innerHTML = (
        "<strong>Generated SKU</strong><br>" +
        "SKU: " + sku + "<br>" +
        "Category: " + category + "<br>" +
        "Product: " + product_name + "<br>" +
        "Stock: " + str(quantity)
    )



def create_order(e):
    prod1 = document["item1"]
    prod2 = document["item2"]
    prod3 = document["item3"]
    prod4 = document["item4"]
    prod5 = document["item5"]

    
    subtotal = (
        float(prod1.value) * prod1.checked +
        float(prod2.value) * prod2.checked +
        float(prod3.value) * prod3.checked +
        float(prod4.value) * prod4.checked +
        float(prod5.value) * prod5.checked
    )

    if not any([
        prod1.checked, prod2.checked, prod3.checked,
        prod4.checked, prod5.checked
    ]):
        document["show"].innerHTML = "Please select at least one drink."
        return

    
    tax_rate = 0.12
    tax = subtotal * tax_rate
    total = subtotal + tax

   
    receipt = f"""
    <h3>♡ Your Receipt</h3>
    <p>Subtotal: ₱{subtotal:.2f}</p>
    <p>VAT (12%): ₱{tax:.2f}</p>
    <p class="receipt-total">Total: ₱{total:.2f}</p>
    <p>Thank you for ordering! ♡</p>
    """

    document["show"].innerHTML = receipt



document["sku_btn"].bind("click", SKU_generator)
document["order_btn"].bind("click", create_order)