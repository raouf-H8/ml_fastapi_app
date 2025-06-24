from app.models import format_username

def test_format_username():
    assert format_username(" alice ") == "Alice"
    assert format_username("BOB") == "Bob"



from app.utils import clean_text

def test_clean_text():
    assert clean_text(" Hello ") == "hello"
    assert clean_text("WORLD") == "world"



from app.main import load_models

def test_load_models():
    models = load_models()

    # Vérifie que les clés attendues sont présentes
    assert "en_sm" in models
    assert "fr_sm" in models

    # Vérifie que ce sont bien des objets spaCy
    assert hasattr(models["en_sm"], "pipe_names")
    assert hasattr(models["fr_sm"], "pipe_names")

    # Vérifie que le pipeline contient au moins le ner
    assert "ner" in models["en_sm"].pipe_names
    assert "ner" in models["fr_sm"].pipe_names