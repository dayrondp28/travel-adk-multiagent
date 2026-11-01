LOCAL_CULTURE = {
    "cusco": {
        "dishes": ["Cuy chactado", "Chiri uchu", "Sopa de quinua"],
        "customs": [
            "Greet with a friendly 'buenos días' when entering shops and restaurants.",
            "Ask permission before photographing local people.",
            "Coca tea is traditional and is often offered to help with altitude.",
        ],
        "phrases": {
            "Hello (Quechua)": "Allillanchu",
            "Thank you (Quechua)": "Sulpayki",
            "How much does it cost?": "¿Cuánto cuesta?",
        },
    },
    "arequipa": {
        "dishes": ["Rocoto relleno", "Adobo arequipeño", "Ocopa"],
        "customs": [
            "Lunch is the main meal of the day and is usually long.",
            "Locals are proud of their city, so showing interest is appreciated.",
        ],
        "phrases": {
            "Good morning": "Buenos días",
            "Thank you": "Gracias",
            "The check, please": "La cuenta, por favor",
        },
    },
    "paris": {
        "dishes": ["Croissant", "Steak frites", "Crêpes", "Coq au vin"],
        "customs": [
            "Always say 'bonjour' before asking anything in a shop or cafe.",
            "Tipping is optional because service is usually included.",
            "Meals are unhurried; asking for the check is normal after finishing.",
        ],
        "phrases": {
            "Hello": "Bonjour",
            "Thank you": "Merci",
            "Please": "S'il vous plaît",
            "Do you speak English?": "Parlez-vous anglais ?",
        },
    },
    "buenos aires": {
        "dishes": ["Asado", "Empanadas", "Milanesa", "Alfajores"],
        "customs": [
            "Dinner starts late, usually after 9 pm.",
            "A single kiss on the cheek is a common greeting.",
            "Sharing mate is a sign of friendship; accept it if offered.",
        ],
        "phrases": {
            "Hello": "Hola, ¿qué tal?",
            "Thank you": "Gracias",
            "How much is it?": "¿Cuánto sale?",
        },
    },
}


def get_local_culture_tips(destination: str) -> dict:
    """Return typical dishes, local customs and useful phrases for a destination.

    Args:
        destination: Travel destination, for example "Cusco" or "Paris".

    Returns:
        Dictionary with dishes, customs and phrases, or a not_found status.
    """
    key = destination.lower().strip()

    for name, info in LOCAL_CULTURE.items():
        if name in key:
            return {"status": "success", "destination": destination, **info}

    return {
        "status": "not_found",
        "destination": destination,
        "message": "No local culture data available for this destination.",
    }