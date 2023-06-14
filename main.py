@namespace
class SpriteKind:
    stationaryobject = SpriteKind.create()
mySprite: Sprite = None
scene.camera_follow_sprite(mySprite)
playerpurse = 10
# this is a game, trust bro //
print("This is a roulette game made to earn all your money and scam you.")
# let userInput = game.askForString("Enter your username!");//
bet = game.ask_for_number("Enter your bet amount")
scoree = randint(0, 36)
if bet > 10:
    bet = 10
playerpurse1 = playerpurse - bet
mySprite = sprites.create(assets.image("""
        myImage1
    """),
    SpriteKind.stationaryobject)
mySprite2 = sprites.create(assets.image("""
    bubble1
"""), SpriteKind.projectile)
mySprite2.set_position(77, 15)
mySprite2.set_scale(0.75, ScaleAnchor.MIDDLE)
print("I CANT SPIN THE GODDAMN ROULETTE PRETEND ITS ANIMATED SCREW MAKECODE")
rollscore = randint(0, 36)

def on_forever():
    if True:
        pass
forever(on_forever)

print("Your first roll was:")
print(rollscore)
print("The second roll was:")
print(scoree)
finalwinnings = (bet * (rollscore - scoree))
if rollscore > scoree:
    print("Your winnings are:")
if rollscore > scoree:
    print(bet * (rollscore - scoree))
if scoree > rollscore:
    print("You won nothing!")
playerpurse2 = playerpurse + finalwinnings
print(playerpurse2)