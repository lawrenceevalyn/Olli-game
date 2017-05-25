# Olli-game
shh, this game is a surprise!

## To Do

* figure out how the game will be played online
* get game engine running
* write tests for game engine
* write tests for map
* get basic map running
* write tests for inventory
* get inventory running
* make it impossible to talk to the robot
* implement a "good end" and a "bad end"
* improve the parser (can I kidnap somebody else's code for this?)
* write fun responses for extra things I think Olli will try

## Development Log

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