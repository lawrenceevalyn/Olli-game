from nose.tools import *
from game.map import *


def test_room():
    gold = Room("GoldRoom", "shortdesc",
                "This room has gold in it you can grab.")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.shortdesc, "shortdesc")
    assert_equal(gold.longdesc, "This room has gold in it you can grab.")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "shortdesc", "Test room in the center.")
    north = Room("North", "shortdesc", "Test room in the north.")
    south = Room("South", "shortdesc", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "shortdesc", "You can go west and down a hole.")
    west = Room("Trees", "shortdesc", "There are trees here, you can go east.")
    down = Room("Dungeon", "shortdesc", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_game_paths():
    assert_equal(entrance.go('north'), exit)
    assert_equal(entrance.go('south'), stacks)
    assert_equal(entrance.go('east'), lab)
    assert_equal(entrance.go('west'), bathroom)
    
    assert_equal(entrance.paths, {'north': exit, 'south': stacks, 'east': lab, 'west': bathroom})
    
    assert_equal(exit.paths, {'south': entrance})
    assert_equal(lab.paths, {'west': entrance, 'north':closet})
    assert_equal(stacks.paths, {'north': entrance})
    assert_equal(bathroom.paths, {'east': entrance})
    assert_equal(closet.paths, {'south':lab})

def test_errors():
    assert_equal(lab.go('south'), "invalid path")