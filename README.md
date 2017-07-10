# Olli-game
shh, this game is a surprise!

## To Do

* make game engine "pass" player input to parser
* update movement tests based on parser actually moving player
* make sure engine runs, parser passes new movement tests
* write tests for looking around
* make sure parser passes tests for looking
* add looking to parse_shortcuts
* write tests for inventory
* make sure inventory passes tests
* add inventory to parse_shortcuts
* make it impossible to talk to the robot
* implement a "good end" and a "bad end"
* write tests for parser to do sentences??
* make sure parser passes new tests??
* write fun responses for extra things I think Olli will try
* add lengthier room descriptions for the first time a room is entered

## Development Log

### July 10, 2017

Got shortcuts working for directions! Starting to get worried about how to use the results of all this parsing in the game itself... moving "make game engine 'pass' player input to parser" to the top of the to-do list as the next thing to figure out.

### July 8, 2017

Today is an experiment in seeing how well I can get my parser and my lexicon to work together when I only MOSTLY understand how either one works...

But it seems to have been a successful one! The parser now uses the lexicon to understand phrases like "go north" and "Run North," and it can EVEN handle one-letter shortcuts! (Or, well, it handles those shortcuts by saying "shortcut" but I can add in the actual desired response to each shortcut later.)

### July 6 2017

I think have the parser almost ready to work! For now I will just return text strings describing what I want to happen after the parser has determined what the player is trying to do.

My parser clearly isn't calling the lexicon at any point, though...? (I don't think it is, anyway??) How..... do I do that?

### July 4 2017

What would be some good easter eggs for Olli?
* giving various game items to the robot, especially the dunb items like the water
* intangibles: love, friendship, happiness, support
    * I bet I could parse a bunch of these with the parser to use a standard response for similar ones!
* gestures: hug, high-five, kiss
* verbs to try? fix things, find things? take a nap? text for help?

### July 1 2017

Confirmed that map tests account for current map. The map passes all the tests!

Added functionality for rooms to have longer descriptions -- and I actually wrote it test-first, which was very useful for when I, e.g., forgot to actually give the longdesc to the Room as an attribute! A successful test of test-first coding! :D

At first I thought I'd use the longer descriptions for when the player first enters a room, because I didn't like the way the room descriptions repeated so much and definitely didn't want to put a lot of detail into something shown so often -- but then I found a better way to implement room descriptions in the game engine! So instead, the long descriptions can be for when the player looks at the room!

This room-looking has been implemented!!

The game engine is getting needlessly bulked up with parsing input, though -- I need to make a very rough parser that will just handle directions and "look" commands, and have the engine pass the player input to that parser. Should be doable!

### June 18 2017

Commented game engine code -- couldn't think of a way to refactor it to be better.

Should the game engine be calling functions that I define elsewhere, when it comes to the variety of actions that players can take within a given room?

### June 17 2017

CAN I actually write tests for the game engine, if it doesn't "return" anything???? I don't feel like I understand how it works, and I think maybe I should refactor it until I do...

### June 16 2017

Are there any extra features I want to implement just to learn new Python skills? I've gotten better at writing programs to do basic file management so this has started to feel less urgent for skill-building. I suppose the answer is "rigorous testing", really...

### May 29 2017

Deciding not to run the game in the browser made it WAY SUPER EASY to get the game engine running the current version of the game! :D

I am intimidated by not really feeling like I know how to write good tests, but I **want** to get in the habit of writing test-based code (especially since doing so would have saved me **hours** of work on typesToTags.py...) so my next priority is to tackle figuring out how to write tests.

### May 28 2017

Upsides of running the game in trinket.io: extremely easy; keeps my troubleshhooting focus on writing code instead of making code play nicely with the internet

Downsides of running the game in trinket.io: makes the code as visible as the game (which can be an upside if I put cute comments in it); may not let me use libraries that I need, limiting the game itself

Decision: host the game on trinket.io! only reconsider if there's a library I need and really can't figure out how to work around.

Workflow: get the whole game working in TextWrangler, terminal, etc like usual, then move it to trinket.io at the end.

### May 25 2017

Implemented supply closet with teddy bear in it. I also started implementing the inventory, I think, but I need to figure out the game engine will work before I can be sure that my code as-is is going to be ok.

I copied all my "reference" code into one place for that to be the "real" game, and I am feeling a little intimidated about hacking it all together.

To keep the bedtime story in it, could try to implement it so that the robot still accepts/needs the bedtime story, but can't read it without the teddy bear.

### May 16 2017

I do want to beef up the story a little, so it will have new surprises for Olli. My priorities are being adorable, and having good responses to things I think ve will try to do.

Maybe a different object is required to put the robot to sleep?
Other things that cause sleep:
* cookies and milk (does the robot.... eat? but this would be good for a more complicated "puzzle" of finding the individual items and heating up the cookies)
* sleepytime pajamas
* special blanket! or teddy bear!! or teddy bot???

What would a robot's teddy bear be like? Something soft but unexpected, like a pillow? Or a sweater/scarf from the lost and found? Or something mechanical? Maybe one that has a pleasing static or a subtle vibration? Like.... an external hard drive? (that feels weirdly like a brain, in this context, and brains are gross.) Not something too warm, computers are prone to overheating anyway. A... printout of a teddy bear? Cardboard box teddy bear??

Definitely a Comfort Object, anyway. Which is simple enough that I don't need to get into the "puzzles" (no need to bite off more than I can chew) and can just implement some rooms and an inventory system.

I definitely don't want to do dialogue. Why can't the protagonist speak? A lampshade reason, like, "Dialogue is beyond the scope of this game. You wave at the distressed robot librarian, and it says, "Error during shutdown process."

Oh! It could even say a particular error code, which could be listed in a manual somewhere? To... have a robust hinting system... for my one-"puzzle" non-game. Well. Olli might appreciate the depth of the worldbuilding.

### May 1 2017

Maybe use https://trinket.io/ for Olli to play the game in, so I don't have to muck about with web servers? Since the web server stuff won't be as relevant for my future work?

But I really like how the web interface lets the description stay visible without repeating. I could also try to do that by only printing the description when the player **enters** the room?
