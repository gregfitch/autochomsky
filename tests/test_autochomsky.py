"""Base tests for the automatic Chomsky-like lines."""

from autochomsky import chomsky


def test_general_use():
    """Test a basic sentence request."""
    line = chomsky()
    assert(len(line) >= 1), 'No sentence returned'
    if len(line) > 72:
        assert(line.count('\n') >= 1), 'Expected one line continuation'
    assert(line.endswith('.')), 'Expected a period ending the sentence'


def test_one_sentence_with_wrapping():
    """Test a single sentence with wrapping request."""
    line = chomsky(1, 45)
    assert(len(line) >= 1), 'No sentence returned'
    assert(len(line.split('\n')) > 1), 'No wrapping found'
    assert(line.endswith('.')), 'Expected a period ending the sentence'


def test_multi_sentence_with_wrapping():
    """Test a multi-sentence request."""
    lines = chomsky(4, 50)
    assert(len(lines) >= 1), 'No sentence returned'
    assert(len(lines.split('\n')) > 1), 'No wrapping found'
    assert(lines.count('.') >= 4), 'Expected at least 4 periods'
    assert(lines.endswith('.')), 'Expected a period ending the final sentence'
