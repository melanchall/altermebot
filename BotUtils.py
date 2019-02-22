import re


ALIAS_MAX_LENGTH = 32
ALIAS_MIN_LENGTH = 2
ALIASES_MAX_COUNT = 10

ALIASING_ENABLED = 1
ALIASING_DISABLED = 0


def escape_markdown(text):
    """Helper function to escape telegram markup symbols."""
    escape_chars = '\*_`\['
    return re.sub(r'([%s])' % escape_chars, r'\\\1', text)
