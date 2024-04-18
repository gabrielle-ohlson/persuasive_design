# The script of the game goes in this file.


# https://charactercreator.org/#


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Student")
# https://charactercreator.org/#sex=f&skinColor=%23704139&irisColor=%23552200&hairColor=%231a1a1a&pupils=round&nose=strong&hair=down&emotion=neutral&shirt=structured_smart&shirtColor=%23e5e4e4&pants=jeans_bellbottoms&pantsColor=%23353743&shoes=moon

define p = Character("Professor")
# https://charactercreator.org/#sex=m&skinColor=%23e5b887&irisColor=%23784421&hairColor=%231a1a1a&pupils=round&hair=wavy&ears=default&nose=default&facialhair=beard_raw&glasses=hipster&tie=striped&jacket=suit_open&shirt=colar&pants=suit&shoes=leather

# define e = Character("Eileen")


define n = nvl_narrator

# define n = Character(kind=nvl) #, what_color="#FFA146", what_italic=False) #, image="gen_xsmall")



image top_text = ParameterizedText(xalign=0.5, yalign=0.0)
image center_text = ParameterizedText(xalign=0.5, yalign=0.5)

# init python:
#     style.long_text = Style(style.default)
#     style.long_text.size = 42

# # Try using the properties 'xminimum', 'xmaximum', 'yminimum' and 'ymaximum' to force limits on the size of the textbox.
# define default_height = gui.textbox_height

# Set the xmaximum and ymaximum style properties on either the Text displayable, or a container enclosing it.
# define Text.ymaximum = 10000
# define gui.textbox_height = 400
# define gui.textbox_yalign = 1.0

# define gui.nvl_height = None

define playername = "(your_name)"

# frame:
#     xminimum 50
#     xmaximum 300
#     yminimum 50
#     ymaximum 250
#     xpadding 10    # inner distance to content
#     ypadding 10
#     # show text "You are a new faculty member at CMU. \nThis semester you are teaching an undergraduate course with students across academic years and background disciplines. This class involves a final group project that requires students to work together over several weeks. Each assignment builds off of each other and is critical towards progressing through all of the milestones." at truecenter

# The game starts here.
label start:
    
    # define gui.textbox_height = gui.textbox_height*2

    # Show a background. This uses a placeholder by default, but you can add a file (named either "bg room.png" or "bg room.jpg") to the images directory to show it.

    scene bg room

    # gui.textbox_height *= 2

    # # define gui.textbox_height = 400
    # $ t = Text("Hello World!")
    # $ z = t.size()

    # fixed:
    #     xysize (100, 500)
    #     add "foo.png"
    #     text "Hello, World" xalign 0.5
    
    # "[z]"

    
    n "You are a new faculty member at CMU. This semester you are teaching an undergraduate course with students across academic years and background disciplines. This class involves a final group project that requires students to work together over several weeks. Each assignment builds off of each other and is critical towards progressing through all of the milestones."

    # define gui.textbox_height = default_height

    # gui.textbox_height = h
    # show center_text "The semester is about two-thirds of the way into the course calendar. Students have already formed groups and gone through a couple rounds of collaborative brainstorming to narrow down their specific topic and problem space. They are currently gearing up to build initial iterations of their prototype for testing."

    # $ define gui.textbox_height = 200
    n "You have a student named Tara in your class — who has been promptly attending class and has a diligent work ethic. She has been a keeping up with all of her assignments and been notably contributing towards her team's progress for the project so far."

    with fade
    "An email notification breaks the silence of your concentration. It's a follow-up from a student explaining their situation in detail and asking for help. You glance at the corner of your desk, where the grant proposal sits. There's a choice to be made."

    # This shows a character sprite. A placeholder is used, but you can replace it by adding a file named "eileen happy.png" to the images directory.
    show student happy # show eileen happy

    n "Dear Professor [playername],\n\nI hope this message finds you well. I am writing to request an extension for today’s assignment due to experiencing some health issues for the past few days."
    
    n "I thought I was going to be able to make the deadline, but sadly I don’t think I’ll be able to finish everything by midnight tonight. An extension would greatly alleviate the stress I am currently facing and help me get back on track.
    Best,
    Tara"

    # These display lines of dialogue.
    s "Welcome to the game!  What would you like to do next?"

    menu:
        "You can't afford any distractions. The grant is too important, and students need to learn resilience. You ignore the email and turn your attention back to the grant proposal.":
            jump opt1
        
        "Schedule a zoom meeting with the student to coordinate with them.":
            jump opt2

    label opt1:
        with fade
        "
        The storm after the calm. Your office becomes a reflection of the turmoil brewing outside it.

        In the wake of your decision to prioritize the grant proposal over Tara's request, the ripples of consequence begin to surface. Word spreads through the student community, and your inbox is now a testament to the oversight - a barrage of emails from the Office of Disability Resources (ODR), expressing concerns over your inaction.
        "

        # "Dear Professor ...."

        # "You stare at the sceen"

        menu:
            "Initiate a conversation with the student":
                jump opt2 # opt1_1
            
            "Option 1.2":
                jump op1_2

        # jump game_end

            # menu:
            #     "Option 1.1":
            #         jump opt1_1
            #     "Option 1.2":
            #         jump opt1_2
            
            # label opt1_1:
            #     s "Cool!"
            
            # label opt1_2:
            #     "WOW!"

    # label opt1_1:
    #     with dissolve
    #     s "Cool!"
    #     jump game_end

    label opt1_2:
        with dissolve
        s "WOW!"
        jump game_end

    label opt2:
        with dissolve
        "During the zoom meeting:"

        menu:
            "Suggest Tara to either drop the class or obtain official ODR documentation due to concerns about unequal treatment":
                jump opt2_1
            
            "Join in Tara's optimism and collaboratively work on a tight timeline to regain momentum.":
                jump op2_2

            "Encourage Tara to prioritize rest, suggest adjusting the timeline, and propose a solo project as an alternative.":
                jump op2_3
        jump game_end
    
    label opt2_1:
        with dissolve
        "The student has never worked with ODR and gets nervous, so they begin to fall behind on classwork."

        "After a week of missed classes, the studwent finally goes to ODR, but they are told accommodations are not \"retro-active.\"  This now means that the situation is out of ODR's hands and that the student must reach out to you again."

        "As your work begins to pile up, you sit outside the La Prima cafe in Gates Center and contemplate your next move:"

        menu:
            "The student sends another email explaining their situation and requesting some kind of help (specified).":
                jump opt2_1_1

            "Option 2.1.2":
                jump opt2_1_2
        
    label opt2_1_1:
        "TODO"
        jump game_end

    label opt2_1_2:
        "TODO"
        jump game_end


    label opt2_2:
        with dissolve

        "At first it seems like the student is catching up, but you later receive emails from their team members complaining that they haven't been doing their part in the project, and have fallen off the grid."

        menu:
            "You reflect on why the student hadn't reached out to you to express that they were struggling and ask for more support.  You did everything you could to make them feel like they could still succeed, right?  *You decide to email them to ask what went wrong.*":
                jump opt2_2_1
            "*You tell the group to \"work it out between themselves\" TODO add the rest":
                jump opt2_2_2

    label opt2_2_1:
        "The student responds with an appreciative and honest email. TODO add rest"

        menu:
            "You feel a bit surprised by this email, TODO add rest":
                jump opt2_2_2
            "This email makes you think hard TODO add rest":
                jump opt2_2_1_2

    label opt2_2_2:
        "You never hear back from the student, but receive a TODO add rest"
        jump game_end

    label opt2_2_1_2:
        "Congratulations!  You grew as a person and TODO add rest"
        jump game_end

    label opt2_3:
        p "Ok... here's what's going to happen.  You already helped with designing TODO add rest"

        "The student responds that they have TODO add rest"

        s "I'm really sorry, I haven't been doing so well over the last few TODO add rest"

        menu:
            "Hey Tara, I wonder if we will be able to TODO add rest":
                jump opt2_3_1
            "Hey Tara, I see.  It's difficult to TODO add rest":
                jump opt2_3_2

    label opt2_3_1:
        "Tara withdraws from the class in frustration."
        jump game_end

    label opt2_3_2:
        "You offer the student the option to either 1 TODO add rest"

        menu:
            "The student takes the summer version of TODO":
                jump opt2_3_2_1
            "Option 2.3.2.2":
                jump opt2_3_2_2


    label opt2_3_2_1:
        jump game_end

    label opt2_3_2_2:
        "TODO"
        jump game_end


    label game_end:
        s "Thanks for playing!"

    s "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    return
