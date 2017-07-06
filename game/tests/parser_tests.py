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
    
    result = parser.parse_input([('verb','run'), ('direction','north')])
    assert_equal(result, "make player go north now")
    
    result = parser.parse_input([('verb','go'), ('direction','south')])
    assert_equal(result, "make player go south now")
    
    result = parser.parse_input([('verb','go'), ('direction','east')])
    assert_equal(result, "make player go east now")
    
    result = parser.parse_input([('verb','go'), ('direction','west')])
    assert_equal(result, "make player go west now")
    
    
    # test taking
    result = parser.parse_input([('verb','take'), ('noun','book')])
    assert_equal(result, "make player take the book")
    
    
    # test giving
    result = parser.parse_input([('verb','give'), ('noun','book')])
    assert_equal(result, "make player give the book to the robot")
    
    
    # test dropping
    result = parser.parse_input([('verb','drop'), ('noun','book')])
    assert_equal(result, "make player drop the book")
    
    
    # test looking
    result = parser.parse_input([('verb','look')])
    assert_equal(result, "look around the room")

def test_errors():
    assert_raises(parser.ParserError, parser.parse_verb, ('noun','robot'))