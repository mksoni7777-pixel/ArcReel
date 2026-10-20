"""Built-in locale-to-language names used by the Agent system prompt."""


def agent_language_name(locale: str) -> str:
    """Return a user-facing language label for the Agent prompt.

    Hinglish is supported as an explicit prompt language even though it is not
    an application UI locale. Locale aliases allow the Agent prompt to honor
    user-specific language preferences without changing UI translations.
    """
    normalized = (locale or "").strip().lower().replace("_", "-")
    if normalized in {"hinglish", "hi-latn", "hi-latin", "roman-hindi", "romanized-hindi"}:
        return "natural Indian Hinglish in Roman (Latin) script"
    return {
        "zh": "Chinese",
        "en": "English",
        "vi": "Vietnamese",
        "hi": "Hindi (Devanagari script)",
    }.get(normalized, "natural Indian Hinglish in Roman (Latin) script")
