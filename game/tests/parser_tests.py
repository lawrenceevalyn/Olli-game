from nose.tools import *
from game import parser

def test_sentence_parser():
    result = parser.parse_sentence([('verb','go'), ('direction','north')])
    assert_equal(result.subject, "player")
    assert_equal(result.verb, "go")
    assert_equal(result.object, "north")

def test_input_parser():
    # test movement
    result = parser.parse_input([('verb','go'), ('direction','north')])
    assert_equal(result, "make player go north now")
    
    # test taking
    
    # test giving
    
    # test dropping
    
    # test looking

def test_errors():
    assert_raises(parser.ParserError, parser.parse_verb, ('noun','robot'))