from nose.tools import *
from ex48 import parser

def test_sentence_parser():
    result = parser.parse_sentence([('verb','run'), ('direction','north')])
    assert_equal(result.subject, "player")
    assert_equal(result.verb, "run")
    assert_equal(result.object, "north")

def test_errors():
    assert_raises(parser.ParserError, parser.parse_verb, ('noun','robot'))