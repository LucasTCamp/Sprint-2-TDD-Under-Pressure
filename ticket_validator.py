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

def calculate_total(code):
    pass