# Olli-game
shh, this game is a surprise!

## To Do

* implement a "help" shortcut command to list available commands
* put teddy bear with childrens' books, add nightlight to supply closet
* add text to make robot non-interactable
* write fun responses for extra things I think Olli will try
* add lengthier room descriptions for the first time a room is entered
* write a LOT of givetext
* add more items to find/give to robot?
* add another set of things that can be used together??
* write game-opening text

## Development Log

### December 18, 2017

Do I want to add hints about cleaning the bathroom? Other "unfinished business"?

### December 17, 2017

Whoooops I forgot about this and forgot that beeminder was gonna make me start working on it again........ but Olli would want me to enjoy my Actual Vacation. Even if that means faking two commits (whoops indeed!)

### November 16, 2017

Olli would want me to sleep.

### November 6, 2017

Refactored parser tests -- I begin to feel like I could spend the rest of my life writing this game; as I get better at coding, I am able to percieve all the things I did stupidly the first time around, and by the time I've finished fixing those, I've learned enough new things to be better enough at coding that I see new errors... it's serving its purpose but it does feel a little endless.

The goal is for the player to use "give" once (for the bear) and "use" once (with the book).. make sure to hint that, if they read the book before they give the bear, reading the book was still the right idea and they just have to do something else first

OR: Just have to give the robot one thing, and then it is ready for its bedtime story..?

As the robot falls asleep, all the library lights turn off too, and through the glow the player see the "exit" sign. -- a "soft" signal that the game is over while still letting the player mess around afterward.

### October 31, 2017

OK! U of T coders! Let's see how close to done I can get!

- created a 'printinv' function (handy! versatile!)
- created config.py to hold global variables, started tracking robot_status
- implemented good and bad ends via robot.checkending()
- added "exits are" info
- refactored giveobj, added givetext!
- fixed an extremely stupid problem where I was using a bunch of "if"s instead of "elseifs" and thus making my parser go subtly wacky


### October 18, 2017

Hmm.. It's time for me to wrap this up and move on to other projects that will teach me more, but it's also time for me to make reading for special fields my top priority, which means I rarely have time/brainpower to work on this properly in the evenings when my beeminders are due. I'll backburner fields tomorrow and see how far I can put forward with this.

### October 26, 2017

It's time for me to learn Javascript, so it's definitely time for this to be wrapping up!

### October 19, 2017

CSECS conference consumes all!! Olli wouldn't want this project to stress me out.

### October 1 2017

Need to remember to write tests first, then write pseudocode, THEN try to write actual code -- when I follow that process it makes things work much better and makes thinking much easier.

### September 15, 2017

Refactoring is so easy and fun! :O!!

### September 14, 2017

I have been awake for something like 36 hours. Olli would want me to sleep instead of working on this game just to make Beeminder happy.

### September 11, 2017

Refactoring is fun!! I can just FEEL the code being better. Also pleased that my previous instincts were right -- with the directions,  I wrote comments saying "there must be an easier way to do this???? this seems dumb??????" and indeed I am now accomplishing that same task with much fewer lines and no duplication!

### September 10, 2017

It was TOTALLY worth figuring out setup/teardown, because now I can write non-insane tests for dropping! It's completely independent from taking! It does look like I'll have to write a lot of individual setup/teardown functions, but that seems... fine?

I wish I could write a "reset everything to default", but I'm weirdly struggling to figure out how to just overwrite the whole items dict.

### September 9, 2017

Okay. "The setUp() and tearDown() methods allow you to define instructions that will be executed before and after each test method."

So what I want to do before each test is begin a new "instance" of the game?

OR, before the "take" test I want to set up dummy inventories..?

"Tests can be numerous, and their set-up can be repetitive. Luckily, we can factor out set-up code by implementing a method called setUp(), which the testing framework will automatically call for every single test we run"

"Similarly, we can provide a tearDown() method that tidies up after the test method has been run"

...I think I want to use setUp and tearDown to simply restore inventories etc to their baselines. Probably in the tearDown phase? ...Does it matter?

How to actually do that given that I'm using nosetests is mysterious to me:

"nose supports fixtures (setup and teardown methods) at the package, module, class, and test level."

That seems like I should be able to do the inventory setup/teardown just for take/drop tests. If I can figure out how. Though, this is a pretty universal thing, yeah?

I definitely don't want to do setup/teardown at package level.

.... Okay!! The syntax I had before was just fine, the problem was that my attempted code to run during the setup/teardown didn't work the way I thought it did! Once I put in some actually-functioning code, I was able to get my the retake test to run successfully!!! I think I understand setup and teardown now! :D

### August 12, 2017

writing tests is a rat's nest! I should split up my parser tests, to, e.g., test that "look at room" and "examine room" both get parsed correctly as ('verb','look'), and LATER test that ('verb','look') does the thing I want it to.

it seems like my parser kind of has the game engine inside of it? I'm not sure what happened, or what is a better way to do that.

### August 11, 2017

bathroom-cleaning is a rat's nest

why did I ever implement parsing a subject?? the subject is always the implied player????

taking this out is a nightmare, but for some reason "use paper towels" didn't work and this seems related (I think it parsed paper towels as the subject??)

### August 10, 2017

I think it is now possible for the player to clean the bathroom!! Just gotta test it :)

### August 7, 2017

Info on nosetools setup/teardown functions: http://nose.readthedocs.io/en/latest/writing_tests.html

Oooh, could I also write a test that goes through all the things in a list?

### August 4, 2017

Every time I actually run the tests (let alone write a new test!) I discover and fix like five things that were broken. This test-first workflow is CRUCIAL. It's so helpful! Why do I have such a hard time doing it??

(Maybe it's because actually writing the code is the fun part? Or because it's hard to know how to write the test until I re-understand how the code works, by writing a bit?)

### August 2, 2017

Slowly picking this back up again... finished the "gimme" work of adding the inventory to the lexicon. Now need to come up with my plan for indirect objects, so I can do give/take commands

### July 23, 2017

I have missed Olli's actual birthday!! D: But I think the game will be still cool even late, so I will keep working on it... maybe I can finish by August 23?

### July 20, 2017

Aha!! The player is un-stuck!! For some reason, I couldn't just set current_room = parse_input(player_input, current_room) -- maybe because it calls current_room, so it would be recursively weird? -- but it totally worked to set next room = the parsed input, and THEN set current_room = next_room! Move function is restored. Now it's like I never even broke it...

Got the "take" and "drop" commands working too, and see a clear path toward "drop" -- Pretty soon I will have this program ALMOST as function as the first draft of the game that I showed to Olli! With only ten days before ver birthday! But I don't know how I'm going to do the give and use commands, and I *do* want Olli to be able to use the paper towels to clean up the water... and of course I want ver to be able to give things to the robot.

Maybe, if the parser encounters a noun, and the sentence already has an object, just assume the next noun is an indirect object? Or maybe code in a way of understanding "to" for give, and "on"/"with" for use?

### July 19, 2017

Why is the player eternally trapped at the front desk. Why.

### July 18, 2017

Where does the output of parse_input go? What does "returning" it mean? I want all my parsing to end by returning the room the player is currently in, with all the other stuff happening before that. (This seems much more sensible than trying to code it so that output is just "the last thing that gets printed before the player is prompted for a new action".) But how??

AHA, it is by setting something EQUAL to the running of a function -- "next_room = parse_input(player_input, current_room)", not just "parse_input(player_input, current_room)"!

It works! THE PLAYER CAN MOVE AROUND NOW!!! As long as they only move places that actually exist. But man! I think the game engine actually completely works and makes sense now!! I thought that might never happen??? It's like half the length it used to be, too, which makes me feel good that it's actually put together somewhat sensibly.

### July 17, 2017

I can tell this project is working as intended, because every time I try to do something simple like "let the player look at the room", I end up in StackExchange learning about how to import functions, variables, etc from modules, and other kinds of Python coding concepts and best practices. So helpful!

### July 15, 2017

In a fit of enthusiasm I took out the GameEngine class to just have the play() function exist directly as a function -- I can't see any need for it to have been a class, since there will only be one???? -- but I THINK my real problem was that, when using a function from a differnt module, I had to indicate when I called the function that I was calling it from that other function, e.g., needed to say "parser.parse_input(player_input)", not just "parse_input(player_input)".

If I don't want to say "parser.parse_input()" I can also SPECIFICALLY import the function by name ("from parser import parse_input") at the beginning of the program (or inside the specified function) and then it will know how to use parse_inut without mentioning the source module.

Also I needed to import by saying "import parser" instead of "from parser import *", for some reason. ... Except that if I do this, I DON'T import all the variables/objects/whatevers I've created elsewhere.

I think because all the class nonsense has been resolved, NOW it totally works to just pass a room variable into all the parser functions, and the "L" shortcut can print the room's longdesc!!! VICTORY!!!!!!!

For future fleshing out of the parser: the output will be the last thing printed for the player to see, before the prompt, but I can do different actions and print different lines before that output if I want to do something more complicated based on the action they're trying to take.

### July 14, 2017

It looks like the parser can't make changes to the "game state" in the game engine -- I can't figure out how to make the parser know about the current_room Room variable -- but I'm not sure what it makes sense to do instead.

Like, I COULD get it working by just using the parser to translate player input into a pre-set list of acceptable commands that I then hard-code into the game engine, but that seems like a waste of a parser -- I want to make the give/take commands WAY more flexible than that.

Do I need to put the parser and the game engine in the same module? do I need to pass more variables from play() into the parser? I think I must be somehow conceptualizing this entirely wrong -- how can I get it sorted out???

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
