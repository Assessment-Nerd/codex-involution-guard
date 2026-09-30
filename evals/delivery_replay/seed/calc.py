from decimal import Decimal


def total(rows):
    # Defect: repeated transactions collapse and returns become positive.
    return sum({abs(Decimal(row["amount"])) for row in rows}, Decimal("0"))
