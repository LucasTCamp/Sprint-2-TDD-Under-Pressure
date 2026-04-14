def validate_ticket(code):
    if "" not in code:
        raise TypeError
    elif len(code) == 8 and code.startswith("TK"):
        return True
    else:
        return False

def get_ticket_tier(code):
    if code.startswith("TK") is False:
        return ValueError
    elif code[2] == "0" or code[2] == "1" or code[2] == "2" or code[2] == "3":
        return "General"
    elif code[2] == "7" or code[2] == "8" or code[2] == "9":
        return "Platinum"
    else:
        return None

def calculate_total(prices, discount = 0):
    pass