from nose.tools import *
from game import lexicon


def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    assert_equal(lexicon.scan("south"), [('direction', 'south')])
    assert_equal(lexicon.scan("East"), [('direction', 'east')])
    assert_equal(lexicon.scan("West"), [('direction', 'west')])
    
    result = lexicon.scan("north south west east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'west'),
                          ('direction', 'east')])
    
    result = lexicon.scan("n e s w")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'east'),
                          ('direction', 'south'),
                          ('direction', 'west')])
    
    result = lexicon.scan("North South West East")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'west'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    
    result = lexicon.scan("go take give")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'take'),
                          ('verb', 'give')])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])

#def test_nouns():
#    assert_equal(lexicon.scan("robot"), [('noun', 'robot')])
#    
#    result = lexicon.scan("robot book")
#    assert_equal(result, [('noun', 'robot'),
#                          ('noun', 'book')])
#    
#    result = lexicon.scan("librarian stories")
#    assert_equal(result, [('noun', 'robot'),
#                          ('noun', 'book')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])

def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    
    result = lexicon.scan("give IAS room")
    assert_equal(result, [('verb', 'give'),
                          ('error', 'IAS'),
                          ('noun', 'room')])