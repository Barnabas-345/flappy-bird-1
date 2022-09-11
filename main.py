import play

bird = play.new_circle(
    color='yellow',
    x=play.screen.left + 100,
    y=play.screen.top - 40,
    radius=30,
)

# adding gravity and lotsa other physics to our bird
bird.start_physics(bounciness=0.4)

boxes = []


@play.repeat_forever
def do():
    if play.key_is_pressed('up', 'w'):
        # if the up key is pressed, make the bird jump
        bird.y += 7.5

    for box in boxes:

        # if the box is out of the screen, lets delete it
        if (box.x < (play.screen.left - 50)):
            boxes.remove(box)
            box.remove()

        # detect if the bird is touching any box
        if bird.is_touching(box):
            box.color = "red"

        # make the box move to the left
        box.x -= 1


@play.repeat_forever
async def block():
    # height of the top block
    top = play.random_number(lowest=300, highest=500)
    # height of the bottom block
    bottom = play.random_number(lowest=300, highest=500)

    # creating the top box of width 100, emerging from behind the current screen
    boxes.append(
        play.new_box(
            color="blue",
            y=play.screen.top,
            x=play.screen.right + 50,
            width=50,
            height=top))
    # creating the bottom box of width 100, emerging from behind the current screen
    boxes.append(
        play.new_box(
            color="blue",
            y=play.screen.bottom,
            x=play.screen.right + 50,
            width=50,
            height=bottom))

    # creating the next box after a random duration between 2 and 5 seconds
    await play.timer(seconds=play.random_number(1.0, 4.0))


play.start_program()