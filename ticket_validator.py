def validate_ticket(code):
    if "" not in code:
        raise TypeError
    elif len(code) == 8 and code.startswith("TK"):
        return True
    else:
        return False

def get_ticket_tier(code):
    if 0 or 1 or 3 in code[2]:
        return "General"
    elif code[2] == "7" or "8" or "9":
        return "Platinum"
    else:
        return None

def calculate_total(prices, discount = 0):
    pass