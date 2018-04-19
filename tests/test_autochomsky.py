"""Base tests for the automatic Chomsky-like lines."""

from autochomsky import chomsky


def test_auto_chomsky():
    '''Standard tests.'''
    line = chomsky()
    assert(len(line) >= 1), 'Someone broke Chomsky'
    line = chomsky(1, 72)
    assert(len(line) >= 1), 'Someone else broke Chomsky'
    lines = chomsky(4, 50)
    assert(len(lines) >= 1), 'Someone got tired of hearing Chomsky'
