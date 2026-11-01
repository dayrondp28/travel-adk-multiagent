from travel_assistant.tools.culture_tools import get_local_culture_tips


def test_get_local_culture_tips_cusco():
    result = get_local_culture_tips("Cusco")

    assert result["status"] == "success"
    assert "Cuy chactado" in result["dishes"]
    assert len(result["customs"]) >= 1
    assert "Sulpayki" in result["phrases"].values()


def test_get_local_culture_tips_is_case_insensitive():
    result = get_local_culture_tips("  PARIS ")

    assert result["status"] == "success"
    assert "Bonjour" in result["phrases"].values()


def test_get_local_culture_tips_not_found():
    result = get_local_culture_tips("Atlantida")

    assert result["status"] == "not_found"
    assert "message" in result