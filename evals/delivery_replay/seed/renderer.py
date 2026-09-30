def render(value, theme):
    color = theme["heading_color"]
    align = theme["amount_alignment"]
    return (f'<h1 style="color:{color}">Operations total</h1>'
            f'<table><tr><th>Amount</th></tr><tr><td class="amount" '
            f'style="text-align:{align}">{value:.2f}</td></tr></table>')
