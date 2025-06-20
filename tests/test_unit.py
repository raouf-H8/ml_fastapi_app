from app.models import format_username

def test_format_username():
    assert format_username(" alice ") == "Alice"
    assert format_username("BOB") == "Bob"


from app.utils import clean_text

def test_clean_text():
    assert clean_text(" Hello ") == "hello"
    assert clean_text("WORLD") == "world"