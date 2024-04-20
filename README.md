# Using Renpy

See the [example code](#code) section for a detailed run-through of usage.


## Installation
Download renpy at: https://www.renpy.org/latest.html

Once you've downloaded Ren'Py, you'll want to extract and run it.

- On Windows, double click on the executable file you download. It will extract Ren'Py into a folder named `renpy-<version>`. You can change into that folder and run `renpy.exe`. (It may be presented as `renpy` if extensions are hidden.)
- On Mac OS X, double-click on the downloaded drive image to mount it as a drive. When the drive opens, copy the folder named `renpy-<version>` somewhere else. (Where does not matter, but it has to be moved out of the read-only drive image. Do not move the renpy app out of the folder it's in – it won't work elsewhere.) Then change (`cd`) into it, and run the `renpy` application.
- On Linux, unpack the tarball, change into the `renpy-<version>` directory, and then run `./renpy.sh`.

After running this, the Ren'Py launcher should run.

## Getting Started
You can follow the renpy [quickstart guide](https://www.renpy.org/doc/html/quickstart.html) to get started, and for more details on installation.

# Renpy Feature Guide
## Dialogue and Narration
*Main article: [Dialogue and Narration](https://www.renpy.org/doc/html/dialogue.html)*

See [say statement](https://www.renpy.org/doc/html/dialogue.html#say-statement) and [defining character objects](https://www.renpy.org/doc/html/dialogue.html#defining-character-objects) in the main article linked above.

TODO: copy over details

## <a name="images"></a>Images
<!-- ## Images {#images} -->
*Main article: [Displaying Images](https://www.renpy.org/doc/html/displaying_images.html)*

In Ren'Py, each image has a name. The name consists of a tag, and optionally one or more attributes. Both the tag and attributes should begin with a letter, and contain letters, numbers, and underscores.

Only one image with a given tag can be shown at the same time. When a second image with the same tag is show, it replaces the first image.

Ren'Py searches for image files in the images directory, which can be found by selecting "images" in the "Open Directory" section of the launcher. Ren'Py expects character art to be an PNG, WEBP, or AVIF file, while background art should be a JPG, JPEG, PNG, WEBP, or AVIF file. SVG files are also supported, but mostly used to customize the interface. The name of a file is very important – the extension is removed, the file name is forced to lowercase, and that's used as the image name.

For example, the following files, placed in the images directory, define the following images:
- "bg classroom.jpg" -> `bg classroom`
- "student full neutral.png" -> `student full neutral`
- "professor upper friendly.png" -> `professor upper friendly`
- 
Since the filenames are lowercase, the following also holds:
- "Professor Upper Friendly.png" -> `professor upper friendly`

Images can be placed in subdirectories (subfolders) under the images directory. The directory name is ignored and only the filename is used to define the image name.

### Image Statement
Sometimes, a creator might not want to let Ren'Py define images automatically. This is what the image statement is for. It should be at the top level of the file (unindented, and before label start), and can be used to map an image name to an image file. For example:
```python
image logo = "renpy logo.png"
image eileen happy = "eileen_happy_blue_dress.png"
```

## Menus, Labels, and Jumps
*Main articles: [In-Game Menus](https://www.renpy.org/doc/html/menus.html) and [Labels & Control Flow](https://www.renpy.org/doc/html/label.html)*

The `menu` statement presents a choice to the player.

The menu statement introduces an in-game choice. It takes an indented block of lines, each consisting of a string followed by a colon. These are the menu choices that are presented to the player. Each menu choice takes its own indented block of lines, which is run when that menu choice is chosen.

Each of the menu choices runs a single `jump` statement. The `jump` statement transfers control to a label defined using the `label` statement. After a `jump`, script statements following the `label` are run.

If there is no `jump` statement at the end of the block associated with the `label`, Ren'Py will continue on to the next statement. A `jump` statement in the very last block is technically unnecessary, but is included since it makes the flow of the game clearer.

Labels may be defined in any file that is in the game directory, and ends with .rpy. The filename doesn't matter to Ren'Py, only the labels contained inside it. You can think of all the .rpy files as being equivalent to a single big .rpy file, with jumps used to transfer control. This gives you flexibility in how you organize the script of a larger game.


## Other Relevant Features to Checkout
- [Transitions](https://www.renpy.org/doc/html/quickstart.html#transitions) (*Main article: [Transitions](https://www.renpy.org/doc/html/transitions.html)*)
- [Positions](https://www.renpy.org/doc/html/quickstart.html#positions) (*Main article: [Transforms](https://www.renpy.org/doc/html/transforms.html)*)
- [Music and Sound](https://www.renpy.org/doc/html/quickstart.html#music-and-sound) (*Main article: [Audio](https://www.renpy.org/doc/html/audio.html)*)
- [Pause Statement](https://www.renpy.org/doc/html/quickstart.html#pause-statement)
- [Ending the Game](https://www.renpy.org/doc/html/quickstart.html#ending-the-game)
- [Supporting Flags using the Default, Python and If Statements](https://www.renpy.org/doc/html/quickstart.html#supporting-flags-using-the-default-python-and-if-statements) (*Main articles: [Python Statements](https://www.renpy.org/doc/html/python.html) and [Conditional Statements](https://www.renpy.org/doc/html/conditional.html)*)
- [Releasing Your Game](https://www.renpy.org/doc/html/quickstart.html#releasing-your-game)
- [GUI Customization Guide](https://www.renpy.org/doc/html/gui.html#gui)
- 
## Example Code: {#code}

Dialogue goes in the `script.rpy` file, which is located inside the `game` folder.
Here's an example of some code that could go in the script (with comments explaining what is going on):

<!-- <div style="width: 100%; height: 100%">
  <img src="example_code.svg" style="width: 100%;" alt="Click to see the source">
</div> -->

```python
# Define the character variables:
define s = Character("Student")
define p = Character("Professor")


# The game starts here with the built-in `start` label:
label start:
    # Here we use the `default` statement to initialize a flag containing information about a choice the player has made.  The `win` flag starts off initialized to the special value `False` (as with the rest of Ren'Py, capitalization matters), meaning that it is not set. If certain paths are chosen, we can set it to `True` using a Python assignment statement.
    default win = False

    # The `scene` statement clears all images and displays a background image.  Here, the "tag" is `bg`, and the "attribute" is `meadow` (see the "Images" section of this README for more details)
    scene bg classroom

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
```


## Notes:
- use shift+R to refresh the game after editing code
- shift+D for developer menu
- display is 1080x1920

## Image sources:
- [bg wood](https://images.app.goo.gl/e7D5cbBJv4g1iQfw7)
- [bg desk](https://www.canadianunderwriter.ca/insurance/what-happened-to-the-ex-broker-who-claimed-he-was-a-ce-instructor-but-wasnt-1004194769/)