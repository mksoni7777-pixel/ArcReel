"""SDK options assembler Agent language prompt tests and configuration."""

from __future__ import annotations

from lib.prompts.agent_language import agent_language_name


def test_agent_language_name_preserves_supported_locales() -> None:
    assert agent_language_name("zh") == "Chinese"
    assert agent_language_name("en") == "English"
    assert agent_language_name("vi") == "Vietnamese"


def test_agent_language_name_supports_roman_script_hinglish_aliases() -> None:
    for locale in ("hinglish", "hi-Latn", "hi_Latn", "hi-latin", "roman-hindi", "romanized-hindi"):
        assert agent_language_name(locale) == "natural Indian Hinglish in Roman (Latin) script"


def test_agent_language_name_has_safe_default_for_missing_locale() -> None:
    assert agent_language_name("") == "natural Indian Hinglish in Roman (Latin) script"
    assert agent_language_name("unknown-locale") == "natural Indian Hinglish in Roman (Latin) script"
