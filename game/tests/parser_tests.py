from nose.tools import *
from game import parser
from game.map import *
from game.lexicon import scan
from game.inventory import items


def test_parser():
    
    # parse movement
    
    result = parser.parse_sentence([('verb','go'), ('direction','north')])
    assert_equal(result.verb, "go")
    assert_equal(result.object, "north")
    
    result = parser.parse_sentence(scan("go north"))
    assert_equal(result.verb, "go")
    assert_equal(result.object, "north")
    
    # parse giving
    
    result = parser.parse_sentence(scan("give book to robot"))
    assert_equal(result.verb, "give")
    assert_equal(result.object, "book")
#    assert_equal(result.indirectobj, "robot")
    
    result = parser.parse_sentence(scan("give book"))
    assert_equal(result.verb, "give")
    assert_equal(result.object, "book")
#    assert_equal(result.indirectobj, "implied indirect object") # should I take
                                                                # out indobj?
    # parse taking
    
    result = parser.parse_sentence(scan("take broom"))
    assert_equal(result.verb, "take")
    assert_equal(result.object, "broom")
#    assert_equal(result.indirectobj, "implied indirect object")
    
    result = parser.parse_sentence(scan("pick up broom"))
    assert_equal(result.verb, "take")
    assert_equal(result.object, "broom")
#    assert_equal(result.indirectobj, "implied indirect object")
    
    result = parser.parse_sentence(scan("take the broom"))
    assert_equal(result.verb, "take")
    assert_equal(result.object, "broom")
#    assert_equal(result.indirectobj, "implied indirect object")
    
    # parse dropping
    
    result = parser.parse_sentence(scan("drop towels"))
    assert_equal(result.verb, "drop")
    assert_equal(result.object, "paper towels")
#    assert_equal(result.indirectobj, "implied indirect object")
    
    result = parser.parse_sentence(scan("drop the paper towels"))
    assert_equal(result.verb, "drop")
    assert_equal(result.object, "paper towels")
#    assert_equal(result.indirectobj, "implied indirect object")
    
    result = parser.parse_sentence(scan("put down the paper towels"))
    assert_equal(result.verb, "drop")
    assert_equal(result.object, "paper towels")
#    assert_equal(result.indirectobj, "implied indirect object")


def test_directions_parser():
    # test multiple ways to express "go south"
    # don't have to test the whole map, because map_tests will do that;
    # but do have to test many ways of saying the same action
    
    result = parser.parse_sentence(scan("go south"))
    assert_equal(result.verb, "go")
    assert_equal(result.object, "south")
    
    result = parser.parse_sentence(scan("Go South"))
    assert_equal(result.verb, "go")
    assert_equal(result.object, "south")
    
    result = parser.parse_sentence(scan("run south"))
    assert_equal(result.verb, "go")
    assert_equal(result.object, "south")
    
    result = parser.parse_sentence(scan("walk south"))
    assert_equal(result.verb, "go")
    assert_equal(result.object, "south")


def test_looking():
    # test looking at the room
    
    result = parser.parse_sentence(scan("look at room"))
    assert_equal(result.verb, "look")
    assert_equal(result.object, "room")
    
    result = parser.parse_sentence(scan("look"))
    assert_equal(result.verb, "look")
    assert_equal(result.object, "implied object")
    
    result = parser.parse_sentence(scan("look around"))
    assert_equal(result.verb, "look")
    assert_equal(result.object, "implied object")
    
    result = parser.parse_sentence(scan("look at stacks"))
    assert_equal(result.verb, "look")
    assert_equal(result.object, "room")
    
    result = parser.parse_sentence(scan("examine room"))
    assert_equal(result.verb, "look")
    assert_equal(result.object, "room")


def test_parsererrors():
    assert_raises(parser.ParserError, parser.parse_verb, ('noun','robot'))