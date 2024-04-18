# Define the character variables:
define s = Character("Student")
# https://charactercreator.org/#sex=f&skinColor=%23704139&irisColor=%23552200&hairColor=%231a1a1a&pupils=round&nose=strong&hair=down&emotion=neutral&shirt=structured_smart&shirtColor=%23e5e4e4&pants=jeans_bellbottoms&pantsColor=%23353743&shoes=moon

define p = Character("Professor")
# https://charactercreator.org/#sex=m&skinColor=%23e5b887&irisColor=%23784421&hairColor=%231a1a1a&pupils=round&hair=wavy&ears=default&nose=default&facialhair=beard_raw&glasses=hipster&tie=striped&jacket=suit_open&shirt=colar&pants=suit&shoes=leather


# The game starts here with the built-in `start` label:
label start:
    # Here we use the `default` statement to initialize a flag containing information about a choice the player has made.  The `win` flag starts off initialized to the special value `False` (as with the rest of Ren'Py, capitalization matters), meaning that it is not set. If certain paths are chosen, we can set it to `True` using a Python assignment statement.
    default win = False

    # The `scene` statement clears all images and displays a background image.  Here, the "tag" is `bg`, and the "attribute" is `meadow` (see the [images](#images) section for more details)
    scene bg classroom
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fthirstymag.com%2FArtStation-Anime-Classroom-1897355.html&psig=AOvVaw1x5lUKg4yhVjqvZKt1ghO9&ust=1713558298099000&source=images&cd=vfe&opi=89978449&ved=0CBQQjhxqGAoTCLD985_MzIUDFQAAAAAdAAAAABC0AQ
    # https://wallpaper.mob.org/image/anime-classroom-1063499.html

    # narration (a "say statement" [line of text in quotes] that is not preceded by a character variable)
    "You and another student walk into a classroom on the first day of school." 

    # The `show` statement displays a sprite on top of the background.  Here, the "tag" is `student`, and the attributes are `full` and `neutral`.
    show student full neutral

    # Dialogue between the two characters (`say` statement is preceded by the given character variable, telling the game to use the characters we've defined):
    s "Hi there!"

    # Another `show` statement changes the displaying sprite:
    show student upper nervous

    s "Are you the professor who teaches intro to HRI?"

    #TODO: explain
    hide student
    
    show professor upper friendly

    p "Yes!  Are you enrolled?"

    hide professor

    show student upper happy

    s "Yes I am!"

    hide student

    show professor upper happy

    p "Great!  I see you have a friend here --"

    show professor closeup happy

    "The professor turns to you"

    show professor closeup talking
    
    p "-- what's your name?"

    # Lines beginning with a dollar-sign are interpreted as Python statements. The assignment statement here assigns a value to a variable. Ren'Py has support for other ways of including Python, such as a multi-line Python statement, that are discussed in other sections of this manual. Ren'Py supports Python 2.7, though we strongly recommend you write Python that runs in Python 2 and Python 3.
    # We can use `renpy.input` to get an input value from the player
    # We can also add styling, such as surrounding text by `{i}` and `{\i}` for italics
    $ player_name = renpy.input("{i}enter your name here:{/i}").strip() or "Player" # default name is "Player" if no text entered

    show professor closeup happy

    # The variable `player_name` is inserted into the `say` statement text, since it is surrounded by square brackets
    p "Nice to meet you [player_name]!  Are you enrolled too?"

    show student full neutral at left
    show professor full neutral at right

    
    # The menu statement introduces an in-game choice. It takes an indented block of lines, each consisting of a string followed by a colon. These are the menu choices that are presented to the player. Each menu choice takes its own indented block of lines, which is run when that menu choices is chosen.
    menu:
        "You admit to the professor that you are still on the wait list.":
            jump opt1 # The jump statement transfers control to the a label defined using the label statement. After a jump, script statements following the label are run.
        
        "You nod your head \"yes\", deciding not to mention the waitlist in hopes that the professor might not notice and let you in.": #here, backslashes are used to escape double quotes in the statement
            jump opt2
        
        "You get nervous and shake your head \"no\", then quick run out of the classroom":
            jump opt3
    
    # Here is a label that we might jump to, with its own block of code:
    label opt1:
        # Transitions change what is displayed from what it was at the end of the last interaction (dialogue, menu, or transition – among other statements) to what it looks like after scene, show, and hide statements have run.
        # The `with` statement takes the name of a transition to use. The most common one is `dissolve` which dissolves from one screen to the next. Another useful transition is `fade` which fades the screen to black, and then fades in the new screen.
        with dissolve

        hide student
        hide professor

        show professor closeup laugh

        p "Hey, that is ok.  Are you are Robotics major?  If so, I'd be happy to make an exception and let you in!"

        show student full neutral at left
        show professor full neutral at right

        menu:
            "You lie and mutter \"uhhh yeah\", even though you are really majoring in gardening.":
                jump opt2

            "You admit that you're a gardening major, but you are extremely interesting in the topic and are considering a Robotics minor.":
                jump opt1_2

    label opt1_2:
        hide student
        hide professor

        show professor closeup caring

        p "I appreciate your honesty and passion.  You know what, welcome to the game, you're in!"

        $ win = True

        jump game_end

    label opt2:
        hide student
        hide professor

        show student closeup angry

        s "THAT'S A LIE!!!!  GET OUT OF HERE!!!!!!!!!!"
        jump game_end

    label opt3:
        hide student
        hide professor

        show professor closeup surprised

        p "Ummm..... bye?"

        jump game_end
    

    label game_end:
        hide student
        hide professor

        with fade

        # Here we use a python `if` statement to check the flag and determine what text is displayed:
        if win: 
            # We can also show text like an image with placement:
            show text "GAME OVER - YOU WIN!" at truecenter
        else:
            show text "GAME OVER - YOU LOSE!" at truecenter

        # Have text display for just a second:
        with dissolve
        pause 1
        hide text
        with dissolve

    # This return statement at the end of the `start` block ends the game:
    return