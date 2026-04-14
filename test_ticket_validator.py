from ticket_validator import validate_ticket, get_ticket_tier, calculate_total

def test_validate_ticket_works_with_valid_code():
    result = validate_ticket("TK874568")
    assert result == True

def test_validate_ticket_fails_with_invalid_start():
    result = validate_ticket("BG874568")
    assert result == False

def test_validate_ticket_fails_with_invalid_length():
    result = validate_ticket("TK8745689")
    assert result == False

def test_validate_ticket_raises_TypeError_with_not_string():
    result = validate_ticket(TK8745689)
    assert result == TypeError

def test_get_ticket_tier_works_with_valid():
    result = get_ticket_tier("TK123456")
    assert result == "General"

def test_get_ticket_tier_works_with_valid_2():
    result = get_ticket_tier("TK987654")
    assert result == "Platinum"

def test_get_ticket_tier_raises_ValueError_with_invalid():
    result = get_ticket_tier("GK123456")
    assert result == ValueError

def test_calculate_total_works():
    result = calculate_total([8.0, 6.0, 10.0], 0.5)
    assert result == 12.0

def test_calculate_total_raises_ValueError_with_empty_prices():
    result = calculate_total([], 0.5)
    assert result == ValueError

def test_calculate_total_raises_TypeError_with_prices_not_list():
    result = calculate_total((8.0, 6.0, 10.0), 0.5)
    assert result == TypeError