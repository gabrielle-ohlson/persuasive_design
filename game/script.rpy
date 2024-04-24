default preferences.skip_after_choices = True

# screen whatever:
#     on "show" action With(my_imagedissolve)
#     on "replace" action With(my_imagedissolve)



# frame:
#                 style_group "pref"
#                 has vbox

#                 textbutton _("Auto Read") action Preference("auto-forward", "toggle")
#     # config.skipping

# Define the character variables:
# image source: https://charactercreator.org/#sex=f&skinColor=%23704139&irisColor=%23552200&hairColor=%231a1a1a&pupils=round&nose=strong&hair=down&emotion=neutral&shirt=structured_smart&shirtColor=%23e5e4e4&pants=jeans_bellbottoms&pantsColor=%23353743&shoes=moon
define s = Character("Student")

define t = Character(None, image="tara", kind=bubble)


# image source: https://charactercreator.org/#sex=m&skinColor=%23e5b887&irisColor=%23784421&hairColor=%231a1a1a&pupils=round&hair=wavy&ears=default&nose=default&facialhair=beard_raw&glasses=hipster&tie=striped&jacket=suit_open&shirt=colar&pants=suit&shoes=leather
define p = Character(None, image="student and professor meeting", kind=bubble)

# define e = Character("Eileen", image="eileen")



# https://www.renpy.org/doc/html/style_properties.html

# width of nvl is 1205

# 352+17
define n = Character(None, kind=nvl, what_xpos=410, what_ypos=0, what_xsize=1105, what_xalign=0.0, what_color="#000000") #, what_style="nvl_dialogue", window_style="nvl_narration", mode="nvl", screen="nvl") 



# 358+52 (52 width margin)
define nw = Character(None, kind=nvl, what_style="nvl_shadow", what_color="#ffffff")

define nb = Character(None, kind=nvl, what_style="nvl_paper", what_color="#000000") # screen="narrator_desk", retain=True, 


# #TODO: https://www.renpy.org/doc/html/other.html
# renpy.load_string(s, filename='<string>')link
# Loads s as Ren'Py script that can be called.

# Returns the name of the first statement in s.

# filename is the name of the filename that statements in the string will appear to be from.



# style bubble_speech_text:
#     xsize None # needed - otherwise it uses a gui setting
#     align (0,0) # also likely needed

#     # You could include your standard font specific stuff
#     color "#F00"
#     # font ""
#     kerning -1.0
#     size 26
#     bold True
#     # etc etc


style gamer:
    size 120
    color "#ffffff"
    font "Orbitron-Black.ttf"


image game_over = Text("GAME OVER", style="gamer")


screen narrator_full_overlay(txt, **kwargs):
    frame:
        background "nvl_full"


screen narrator_overlay(txt, **kwargs):
    style_prefix "narrator" # This is actually passed through keywords
    
    fixed:
        yanchor 0.0
        xsize 1080
        pos (0.0, 0.0) # Our x, y position, also through keywords
        # pos (450, 320) # Our x, y position, also through keywords

        frame:
            text txt # "The Text" # Actually transcluded from the parent screen


style narrator_frame:
    # our background picture
    background Frame(
        "gui/nvl_textbox.png"
        # left = Borders(0, 32, 0, 0)
        # left = Borders(32, 33, 88, 80)
        )

    # These are the distance between the text area and frame outer edge
    # left_padding 24
    # top_padding 12 #22
    # right_padding 23
    # bottom_padding 73
    # We *could* do all that in one line with
    # padding (24, 22, 23, 73) # (left, top, right, base)

    minimum (121, 114) #?

    xsize 1920 # full width

    # Now the anchor (the pixel of this widget to place at the stated pos)
    # This should generally reflect where the end of the tail lies
    anchor (0.0, 0.0) # (1.0, 1.0)
    # # You could add a slight offset if wanted (so show_pos is on the tail)
    # offset (12, 7)



style narrator_text:
    xpos 410 #gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign # 0.0
    ypos 0 # gui.nvl_thought_ypos
    xsize 1105 #1105 #gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
    #
    # outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    color "#ffffff00"
    # outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]



image laptop composite = Composite(
    (1920, 1080),
    (0, 0), "bg black",
    (200, 100), "bg email"
)

init python:
    achievement.register("test4", stat_max=4) #`stat_max`: number of times a condition must be met before the achievement is granted


screen achievements: #TODO: figure out what to do with this

    # The background of the main menu.
    window:
        style "bg_white"
    
    grid 2 2:
        # if achievement.has("test"):
        #     image test_icon_granted
        # else:
        #     image test_icon_notgranted
        #
        if achievement.has("test"):
            text "You got the Test Achievement!"
        else:
            text "Get this achievement by playing the game"

        # if achievement.has("test4"):
        #     image test_icon_granted
        # else:
        #     image test_icon_notgranted
        #
        if achievement.has("test4"):
            text "You got the Test4 Achievement!"
        else:
            text "Get this achievement by clicking 4 times"



screen choice_list(opts):
    style_prefix "choice_list"
    frame:
        area (10, 60, 200, 480)
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            vbox:
                text "OPTIONS:"
                for caption, next_label in opts.items():
                    textbutton caption action Jump(next_label)


#remove #v
default timely = 0
default flexible = 0
default teach = 0
#^

# default character_stats.chloe_substore.friends = {"Eileen",}
init python in quiz_attr:
    timely = 0
    flexible = 0
    teach = 0

init python in game_attr:
    timely = 0
    flexible = 0
    teach = 0

init python:
    # class Attributes:
    #     def __init__(self):
    #         self.timely = 0
    #         self.flexible = 0
    #         self.teach = 0

    # quiz_attr = Attributes()
    # game_attr = Attributes()

    class ChoiceItem:
        def __init__(self, caption, next_label=None, attr=None):
            self.caption = caption
            if next_label:
                if attr is None: self.action = Jump(next_label)
                else: self.action = Jump(next_label), IncrementVariable(attr[0], attr[1]) #check
            else: self.action = Return(None) #equivalent of `pass`

    class QuizItem:
        def __init__(self, caption, attr=None):
            self.caption = caption
            if attr: self.action = IncrementVariable(attr[0], attr[1])
            # if quality: self.action = IncrementVariable(quality[0], quality[1])
            else: self.action = None



screen black:
    # style_prefix "choice"
    tag bg

    window: #?
    # frame:
        xfill True
        yfill True
        background "bg black"



init python:
    class ChoiceLayout:
        def __init__(self, xalign=0.5, ypos=405, yanchor=0.5, spacing=33):
            self.xalign = xalign
            self.ypos = ypos
            self.yanchor = yanchor
            self.spacing = spacing #gui.choice_spacing


screen choose(items, bg="bg desk", layout=ChoiceLayout()): #, y_align=0.5): #check
    style_prefix "choice"

    tag bg

    window: #?
    # frame:
        xfill True
        yfill True
        background bg

        vbox:
            xalign layout.xalign
            ypos layout.ypos
            yanchor layout.yanchor
            spacing layout.spacing
            # yanchor .3
            # yalign 1.0 #y_align
            for i in items:
                if i.action:
                    textbutton i.caption action i.action
                else:
                    # textbutton i.caption action NullAction #check
                    text i.caption

        on "show" action Show("navigation")
        on "hide" action Hide("navigation")


screen quiz(prompt, items, bg="bg black", layout=ChoiceLayout()): #TODO: layout stuff
    style_prefix "choice"

    tag bg

    
    # gui.choice_button_width = 1860
    # gui.choice_button_text_size = 45


    # define gui.choice_button_width = 1185
    # define gui.choice_button_height = None
    # define gui.choice_button_tile = False
    # define gui.choice_button_borders = Borders(150, 8, 150, 8)
    # define gui.choice_button_text_font = gui.text_font
    # define gui.choice_button_text_size = gui.text_size
    # define gui.choice_button_text_xalign = 0.5
    # define gui.choice_button_text_idle_color = '#888888'
    # define gui.choice_button_text_hover_color = "#000000"
    # define gui.choice_button_text_insensitive_color = '#8888887f'
    

    # window: #?
    frame:
        xfill True
        yfill True
        background bg

        text prompt yalign 0.0 color "#fff"

        vbox:
            for i in items:
                if i.action:
                    textbutton i.caption:
                        action i.action, Return(None)
                else:
                    text i.caption

        on "show" action Show("navigation")
        on "hide" action Hide("navigation")


# screen narrator(what, bg="bg baclk"):
#     style_prefix "narrator"
#     # define gui.button_width = None
#     # define gui.button_height = None
#     # style_prefix "say"

#     frame:
#         xfill True
#         yfill True
#         background bg

#         vbox:
#             for i in items:
#                 textbutton i.caption action i.action
#             textbutton


#     ## If there's a side image, display it above the text. Do not display on the
#     ## phone variant - there's no room.
#     if not renpy.variant("small"):
#         add SideImage() xalign 0.0 yalign 1.0


init python:
    # https://www.renpy.org/doc/html/python.html#default-statement
    bg_img = None

    def quizMenu(prompt, items, bg="bg black", layout=ChoiceLayout()):
        # if bg is not None and (bg_img is None or bg_img != bg):
        #     renpy.hide("bg")
        #     renpy.show("bg black", tag="bg")
        #     renpy.with_statement(trans=dissolve)

        # renpy.with_statement(trans=dissolve)

        # The call screen statement shows a screen, and then hides it again at the end of the current interaction. If the screen returns a value, then the value is placed in the global _return variable.
        renpy.call_screen("quiz", _with_none=False, prompt=prompt, items=[QuizItem(*vals) for vals in items], bg=bg, layout=layout)
        renpy.with_statement(trans=fade)


    def choiceMenu(items, bg="bg desk", layout=ChoiceLayout()): #choices is list of tuples 
        if bg is not None and (bg_img is None or bg_img != bg):
            # renpy.with_statement(trans=dissolve)
            renpy.hide("bg")
            renpy.show("bg black", tag="bg")
            renpy.with_statement(trans=dissolve)

        # renpy.with_statement(trans=dissolve)
        renpy.call_screen("choose", _with_none=False, items=[ChoiceItem(*vals) for vals in items], bg=bg, layout=layout)
        renpy.with_statement(trans=fade)

    def showBg(bg):
        global bg_img
        #
        if bg is not None and (bg_img is None or bg_img != bg):
            if bg_img is not None:
                # renpy.with_statement(trans=dissolve)
                renpy.hide("bg")
                renpy.show("bg black", tag="bg") #new #check
                renpy.with_statement(trans=dissolve)
 
            renpy.show(bg, tag="bg")
            renpy.with_statement(trans=fade) # fade)
            bg_img = bg

    # def narrate(txt, bg="paper_desk composite", white=False):
    def narrate(txt, bg=None, full_overlay=False):
        global bg_img
        #
        if bg is not None and (bg_img is None or bg_img != bg):
            if bg_img is not None:
                # renpy.with_statement(trans=dissolve)
                renpy.hide("bg")
                renpy.show("bg black", tag="bg") #new #check
                renpy.with_statement(trans=dissolve)
 
            renpy.show(bg, tag="bg")
            renpy.with_statement(trans=fade) # fade)
            bg_img = bg

        if bg_img == "paper_desk composite":
            # bg = "paper_desk composite"
            renpy.say(nb, txt)
        else:
            renpy.hide_screen("narrator_overlay") #check
            if full_overlay:
                renpy.show_screen("narrator_full_overlay", _tag="narrator_overlay", txt=txt) #check
            else:
                renpy.show_screen("narrator_overlay", _tag="narrator_overlay", txt=txt)
            #
            renpy.say(nw, txt)


    def clear():
        
        # _window_hide() #trans=fade)
        nvl_clear()
        # renpy.with_statement(trans=dissolve)
        # renpy.show("bg black") #?
        renpy.hide_screen("narrator_overlay")
        # renpy.hide("overlay")
        renpy.hide("bg")
        # renpy.hide("narrator") #check
        # renpy.show(bg, tag="bg")

        renpy.show("bg black", tag="bg")
        renpy.with_statement(trans=dissolve)

        # renpy.call_screen("black")
        # renpy.hide_screen("bg")
        
        # renpy.with_statement(trans=fade)
        # _window_show(trans=fade)
        #
        global bg_img
        bg_img = None




# Here we use the `default` statement to initialize a flag containing information about a choice the player has made.  The `tara_passes` flag starts off initialized to the special value `False` (as with the rest of Ren'Py, capitalization matters), meaning that it is not set. If certain paths are chosen, we can set it to `True` using a Python assignment statement.
default tara_passes = False

default abstract_quiz = True # False
# $ abstract_quiz = False #True

default overlooked = False

# The game starts here with the built-in `start` label:
label start:
    # $ narrate("Welcome to the game, \"Will Tara Pass the Class?\"!  First, let's start with a brief quiz.", bg="paper_desk composite")
    # $ clear()

    if abstract_quiz:
        $ quizMenu("Imagine you're a tour guide leading a large group through a bustling city. As you walk, some members of the group start to lag behind due to unexpected distractions. How do you manage the situation?", [("Continue on the planned route", ("quiz_attr.timely", -1)), ("Maintaining the pace for the majority", ("quiz_attr.timely", 0)), ("Adjust your itinerary to accommodate the varying interests and needs of each member", ("quiz_attr.timely", 1))])

        # $ renpy.notify("quiz_attr.timely: " + str(quiz_attr.timely)) #remove #debug

        $ quizMenu("Imagine you're on a journey through a dense forest with a companion. As you trek along, your friend encounters a barrier blocking their path, and they're unable to overcome it on their own. How do you respond to this situation?", [("Step in immediately, offering assistance and working together to overcome the obstacle", ("quiz_attr.flexible", 1)), ("Pause to assess the situation and consider seeking outside help", ("quiz_attr.flexible", -1))]) 

        # $ renpy.notify("quiz_attr.flexible: " + str(quiz_attr.flexible)) #remove #debug


        $ quizMenu("Imagine a nest of young birds perched high in a tree. You witness the mother pushing each of her chicks out of the nest. One bird seems reluctant to leave the safety of the nest, while the others eagerly practice spreading their wings. How do you interpret this situation?", [("You believe that the anxious bird must be nudged out of the nest to learn to fly", ("quiz_attr.teach", -1)), ("You believe there are other ways for it to develop the skills and confidence needed for flight", ("quiz_attr.teach", 1))])

        # $ renpy.notify("quiz_attr.teach: " + str(quiz_attr.teach)) #remove #debug
    else:
        $ quizMenu("You're teaching a course which has a few major projects. You observe that on the eve of a big research grant deadline that your student requests for extensions are piling up in your inbox. How do you manage the situation?", [("You have a clear sense of your priorities, and realize that you can't grant everyone extensions to their project. Plus, the deadline was known to students many weeks in advance. You send an announcement to the class saying they have an additional 24 hours to work on the project. ", ("quiz_attr.timely", -1)), ("Students have had ample time to plan around deadlines, but you empathize with the fact that sometimes things happen that are unexpected. While writing your grant draft, you answer student emails as they come to hear out what's causing them difficulty.", ("quiz_attr.timely", 1))])

        # $ renpy.notify("quiz_attr.timely: " + str(quiz_attr.timely)) #remove #debug

        $ quizMenu("You notice that there's a student in your class who's struggling and not attending class consistently.\nYou want to reach out to the student to see if they're ok. So you...", [("You email the student and encourage them to come to office hours and remind them what time it is.", ("quiz_attr.flexible", -1)), ("You email the student and ask them to suggest a time that works for them, saying that your plans are flexible (they may not be).", ("quiz_attr.flexible", 1))])

        # $ renpy.notify("quiz_attr.flexible: " + str(quiz_attr.flexible)) #remove #debug

        $ quizMenu("Do you place an emphasis on learning or teaching experiences? For example, when a student is struggling, would you step in a bit later, to let the student \"figure it out\"?", [("Yes, tough love is indispensible.", ("quiz_attr.teach", -1)), ("No, what the hell.", ("quiz_attr.teach", 1))])
    

        # $ renpy.notify("quiz_attr.teach: " + str(quiz_attr.teach)) #remove #debug
    
    $ narrate("Thanks for answering! Let's begin the game and find out --\n\n\"Will Tara Pass the Class?\"", bg="paper_desk composite")

    $ choiceMenu([("Start Game", None)], bg="tara outside university", layout=ChoiceLayout(ypos=700))

    # show tara outside university as bg

    # menu:
    #     "Start Game":
    #         pass
    $ clear()

    # =====
    # show bg black

    # $ achievement.grant("test")
    # "I'm granting an achievement"

    # if achievement.has("test"): #shows that achievement works
    #     "And it worked!"
    # else:
    #     "But that didn't work."
    
    # # clear all of the user's achievements:
    # $ achievement.clear_all()

    # if not achievement.has("test4"):
    #     $ achievement.clear("test4") # remove a specific achievement

    # $ test_clicks = 0
    # # default persistent.test_clicks = 0 #if want it to be persistent through playthroughs
    # "Click this 4 times for another achievement"

    # menu loop:
    #     "Click!":
    #         $ test_clicks += 1
    #         # $ persistent.test_clicks += 1 #if want it to be persistent through playthroughs
    #         $ achievement.progress("test4", test_clicks)
    #         $ achievement.sync()
    #         $ progress = achievement.get_progress("test4")
    #         if progress == 1:
    #             "You've clicked this [progress] time."
    #         else:
    #             "You've clicked this [progress] times."
    #         if progress < 4:
    #             jump loop
    #     "No":
    #         pass

    # if achievement.has("test4"):
    #     "You got the achievement!"
    # else:
    #     "You did not get the achievement."

    # window hide
    # show screen achievements #as A
    # pause
    # hide screen achievements # hide screen A

    # # clear all of the user's achievements:
    # $ achievement.clear_all()

    #================================
    
    # show bg white
    # show screen narrator(nw, "You are a new instructor at the Carnegie Institute of Technology (CIT), teaching a course about research methods. The class is relatively large, which makes staying connected with individual students slightly more difficult. Because it is a required course for students at CIT, it is imperative that students pass your class so they can advance in their degree program.")

    # pause


    # show screen choice_list(opts)

    $ narrate("You are a new instructor at the Carnegie Institute of Technology (CIT), teaching a course about research methods. The class is relatively large, which makes staying connected with individual students slightly more difficult. Because it is a required course for students at CIT, it is imperative that students pass your class so they can advance in their degree program.", bg="university")

    $ narrate("\nYou're excited to embark on your teaching journey and are still learning about the different offices and resources that the university has to offer, including their Office of Disability Resources (ODR).", full_overlay=True)

    #--- Frame 56 ---
    $ clear()
    $ narrate("This semester, your research course includes students from various academic years and disciplinary backgrounds. The class involves a final group project that requires students to work together over several weeks. Each assignment builds upon the previous ones and is critical for progressing through all the milestones.", bg="professor teaching") #creepy #?

    $ clear()
    $ narrate("The semester is about two-thirds of the way through the course calendar. Students have already formed groups and gone through a couple of rounds of collaborative brainstorming to narrow down their specific topic and problem space. They are currently gearing up to build initial iterations of their prototype for testing.", bg="students working")

    $ clear()
    $ narrate("You have a student named Tara in your class who has been promptly attending class and has a diligent work ethic. They have been keeping up with all of their assignments and has notably contributed to their team's progress on the project so far.", bg="student classroom")
    
    #--- Frame 57 ---
    $ clear()
    $ narrate("You're sitting in your office in Scaife Hall when you hear your laptop ping. An email notification breaks the silence of your concentration. It's a message from Tara explaining a situation and asking for help.", bg="professor office")

    $ clear()
    $ narrate("The email reads:", bg="computer tara email")

    #--- Frame 80 ---
    $ clear()
    $ narrate("Tara's situation seems somewhat complex. You glance at the corner of your desk, where the grant proposal sits. There's a choice to be made...", bg="professor grant")

    $ clear()
    $ choiceMenu([("You can't afford any distractions. The grant is too important, and Tara needs to learn resilience. You ignore the email and turn your attention back to the grant proposal.", "storm", ("game_attr.timely", -1)), ("You decide to schedule a Zoom meeting with Tara to coordinate with them.", "zoom"), ("You respond to Tara's email directing them to reach out to the Office of Disability Resources (ODR) for further accommodation requests.", "odr")]) # layout=ChoiceLayout(ypos=700))

    label storm:
        $ overlooked = True
        #--- Frame 53 ---
        $ clear()
        $ narrate("When a student's outreach is not acknowledged, it could be perceived as a lack of support. Even if unable to grant the request, recognition of the student's effort to communicate can maintain a positive rapport and demonstrate that their concerns have been heard.", bg="tara")

        $ renpy.hide_screen("narrator_overlay")
        t "I feel like my efforts to communicate my situation was overlooked."
        
        t "An acknowledgement would have helped me have some sort of trust in the support system here at ICT..."

        t "I feel like my voice in this institution doesn't even matter."

        #--- Frame 67 ---
        $ clear()
        $ narrate("The storm after the calm. Your office becomes a reflection of the turmoil brewing outside it.", bg="professor office storm") #TODO: determine if should be "calm after the storm" or not

        $ narrate("\nIn the wake of your decision to prioritize the grant proposal over Tara's request, the ripples of consequence begin to surface.", full_overlay=True)

        $ narrate("\nWord spreads through the student community, and your inbox is now a testament to the oversight - a barrage of emails from the Office of Disability Resources (ODR), expressing concerns over your inaction.", full_overlay=True)

        #--- Frame 68 ---
        $ clear()
        $ narrate("You stare at the screen, the ODR email open in front of you. Training modules on accommodating students feel like a chore, something you have convinced yourself you are beyond needing.", bg="professor office stare")

        $ clear()
        $ narrate("\nSigh... this training seems like such a drag. I know all this stuff already, don't I?", bg="computer odr email")

        $ narrate("\nMaybe I'll put the grant proposal on hold for today and reach out to the student to discuss what would be helpful for them. It's not too late, right?", full_overlay=True)

        $ clear()
        $ choiceMenu([("Initiate a conversation with Tara as a way to right your wrongs.", "honest")])

    label zoom:
        #--- Frame 59 ---
        $ clear()
        $ narrate("You and Tara join the Zoom meeting room and begin to discuss Tara's options.", bg="professor zoom 2")

        $ clear()
        $ showBg(bg="tara zoom")
        t "Thanks so much for meeting with me!"  #new #check

        # $ renpy.hide_screen("narrator_overlay")
        t "I think I'll be able to catch up soon..." #new #check

        $ narrate("They are optimistic that they can recover quickly in the next week.") #, bg="tara zoom")

        $ narrate("Based on the meeting you...", full_overlay=True) #, bg="tara zoom")

        $ clear()
        $ choiceMenu([("Suggest to Tara to either drop the class or obtain official ODR documentation due to concerns about unequal treatment.", "drop", ("game_attr.flexible", -1)), ("Join Tara in their optimism and collaboratively work on a tight timeline to regain momentum.", "optimistic"), ("Encourage Tara to prioritize rest, suggest adjusting the timeline, and propose a solo project as an alternative.", "rest")])

    label drop:
        #--- Frame 60 ---
        $ clear()
        $ narrate("Suggesting a student drop a class or seek formal documentation can be a pragmatic response to a complex situation. However, it's important to balance procedural advice with empathy to ensure students feel personally supported.", "student desk")

        $ renpy.hide_screen("narrator_overlay")
        t "Getting documentation was so daunting and just thinking about starting the process added to my stress."
        
        t "Between my health issues and other coursework, I'm so so stressed about my GPA."

        jump odr

    label giveup:
        #--Frame 72 ---
        $ clear()
        $ narrate("You never heard back from the student, but receive a notification email from the system informing you that the student has dropped your class. This sits uneasy with you, but you talk to some other professors who have dealt with similar issues and who say, \"that's just how it goes sometimes, you tried your best\" -- which makes you feel better.", "professor others")

        $ clear()
        $ narrate("Next semester, while working on a research project in Wean Hall, you overhear two students talking about how the student who dropped your class has gone on to drop out of the program. One of the students starts to say, \"I don't blame them, that professor [[you] is known for being unaccommodating and difficult to talk to---\"", "whisper")

        $ clear()
        $ narrate("They see you enter the area and go silent, grab their things, and leave.", "professor door")

        $ tara_passes = False
        jump game_end
    
    label phone:
        #--- Frame 62 ---
        $ clear()
        $ narrate("You were optimistic about Tara's progress in the class, but after a couple of weeks, you notice Tara's progress updates have stopped. You're walking across The Cut to head to your office when you check your phone and see the following email from Tara...", bg="professor walking")

        # $ clear()
        # $ showBg(bg="phone email")

        #--- Frame 63 ---
        $ clear()
        $ narrate("This email catches you off guard. You're disappointed and frustrated that your efforts to help Tara are falling short.", bg="phone email") #"professor sad")

        $ narrate("But you also want to prioritize Tara's health and well being. How will you respond?", full_overlay=True) #"professor sad")

        $ clear()
        $ choiceMenu([("Hey Tara,\nI wonder if we will be able to hit the required learning goals for this course. I think the best move forward is that I'll give you the credit that I can for what work you've done throughout the course.\nRight now that means you'll end up with a C+", "c_grade", ("game_attr.flexible", -1)), ("Hey Tara,\nI see. It's difficult to see how you'll be able to hit the required learning goals for the course, so I may not be able to give you the grade you're looking for.\nAre you available during the summer? We could have you continue completing work, then, if you're willing, to take an Incomplete for the course.", "summer")])

    label c_grade:
        #--- Frame 64 ---
        $ clear()
        $ narrate("Presenting a student with a C+ based on the work completed to date, without exploring further accommodations or assistance, may seem expedient, but could be perceived as limiting. It's essential to communicate all available options, including the possibility of an incomplete, to support the student's long-term success and learning.", bg="student ponder computer")

        $ renpy.hide_screen("narrator_overlay")
        t "When I was presented with a flat grade of C+, it felt like a premature cap on my efforts, especially with all the health issues I've had to deal with this semester."
        
        t "I'm worried this might set a precedent and overshadow my efforts."

        #--- Frame 64 ---
        $ clear()
        $ narrate("After Tara sees your email, they decide to give up completely. Tara stops submitting classwork and eventually gets special permissions to withdraw from your course.", bg="student sad dorm computer")

        $ tara_passes = False
        jump game_end


    label optimistic:
        #--- Frame 71 ---
        $ clear()
        $ narrate("At first it seems like Tara is catching up, but you later receive emails from their team members complaining that they haven't been doing their part in the project and have fallen off the grid. What should you do?", bg="team project")

        $ choiceMenu([
            ("You reflect on why Tara hadn't reached out to you to ask for more support. You did everything you could to make them feel like they could still succeed, right? *You decide to email them to ask what went wrong.*", "honest"), #TODO: add bold formatting
            ("*You tell the group to \"work it out between themselves\" -- it seems Tara is failing to communicate.* Collaboration is an important skill to have in academia, so the students could use the practice with resolving interpersonal conflict on their own. Besides, you've already done your part to support Tara.", "giveup", ("game_attr.teach", -1)) #TODO: add bold formatting
            # ChoiceItem("You send an email to Tara that reads, \"Hey Tara, It's difficult to see how you'll be able to hit the required learning goals for the course, so I may not be able to give you the grade you're looking for. Are you available during the summer? We could have you continue completing work then if you're willing to take an Incomplete for the course.\"", "summer")  #remove
        ])

    label honest: #opt2_2_1
        #--- Frame 68 ---
        $ clear()
        $ narrate("Tara responds with an appreciative and honest email. Tara stated that they were optimistic that they could overcome these obstacles, but they have never had to get academic accommodations before, and it wasn't as easy as they thought it would be.", bg="student ponder computer")

        $ narrate("\nAll Tara had heard from other students with accommodations were horror stories about professors expecting them to function highly and blaming them for their difficulties. Tara apologizes for assuming you would do the same and asks where you think they should go from here.", full_overlay=True)

        $ narrate("\nBased on this email you contemplate then decide...", full_overlay=True)

        $ clear()
        $ choiceMenu([("You feel surprised by this email, and even a little offended. You wish students would give others a chance to help them, rather than ignoring emails and playing the victim last minute. This has clearly gotten out of hand and you feel awkward intervening at this point. You send Tara to ODR and suggest they either take an Incomplete or drop the class so they can focus on self-improvement.", "odr"), ("This email makes you think hard about your role as a professor and the dynamic at your university. You didn't know how unaccommodating professors have been, and you suspect you may have unknowingly made mistakes too. If you are a good person and just didn't know what to do, maybe there are other professors in the same position? You decide to organize a discussion and accessibility training for professors to share what you've learned.", "congrats")], layout=ChoiceLayout(ypos=500))

    label questioning: #remove #?
        $ clear()
        $ narrate("Questioning the timing of a student's request for accommodations can inadvertently signal distrust. It's vital to create an inclusive environment where students feel comfortable disucssing their needs at any point.", "tara")

        t "I feel somewhat uncomfortable with my integrity being questioned."
        
        t "I was already struggling with my decision to reach out and was looking for reassurance that my academic journey was still on track."

        jump giveup
    
    label congrats:
        #--- Frame 79 ---  #remove
        # $ clear()
        # $ narrate("Tara passes the class!", bg="student pass") # student happy
        
        #--- Frame 79 ---
        $ clear()
        $ narrate("Congratulations!", bg="professor celebrate 1")
        
        $ clear()
        $ narrate("You grew as a person and a mentor, and you played an important role in affecting positive change for disabled students at CIT.", bg="professor celebrate 2")
        
        $ clear()
        $ narrate("Over the years, you will become known as a fantastic and understanding professor to take a class with among students.", bg="professor celebrate 3")

        $ clear()
        $ narrate("Your efforts will contribute to an increase in neurodiversity in higher education, accessible classrooms that those who usually skip class from overwhelm instead thrive in, and the normalization of difficult dialogue surrounding accommodations between students and professors.", bg="accessible classroom")

        $ tara_passes = True
        jump game_end
            

    label rest:
        #--- Frame 61 ---
        $ clear()
        $ narrate("Tara responds positively to you proposing that they prioritize rest. You begin to work with them on the mechanics of the solo project.", bg="student dorm tv")

        $ clear()
        $ narrate("The following week you both meet in your office in Scaife Hall and map out a game plan. You state:", bg="student and professor meeting")

        $ renpy.hide_screen("narrator_overlay")
        p "Ok... So here's what's going to happen. You've already helped with designing milestone one."
        
        p "I'll look at what you contributed for that assignment later tonight..."
        
        p "I want you to go ahead and storyboard how you would improve the prototype based on my feedback, okay?"

        p "Let's make our objective that you at least go through thinking about all of the prototyping steps..."

        $ clear()
        $ narrate("You pause momentarily and observe the overwhelmed expression on Tara's face...", "student overwhelmed 2")

        jump phone

    label summer:
        #--- Frame 76 ---
        $ clear()
        $ narrate("You offer the student the option to either take summer version of the course or take an Incomplete and complete the course requirements over the summer.", bg="student summer")

        $ narrate("The student takes the summer version of the course and ends the term with a higher grade. Given the additional time and slower pace of the summer, the student feels much more relaxed which positively impacts how much information they retain.", full_overlay=True)

        jump congrats
    
    label odr:
        #--- Frame 73 ---
        $ clear()
        $ narrate("Tara has never worked with ODR and get nervous, and begin to fall behind in your class.", bg="student sad dorm bed")

        #--- Frame 74 ---
        $ clear()
        $ narrate("After a week of missed classes Tara finally goes to ODR but is told accommodations are not \"retro-active.\" This now means that the situation is out of ODR's hands and that Tara must reach out to you again.", bg="student odr meeting")

        #--- Frame 75 ---
        $ clear()
        $ narrate("As your work begins to pile up, you sit at the La Prima in Gates drinking tea and contemplate your next move...", bg="professor tea contemplating") 

        jump help_email

        # $ narrate("The student sends another email explaining their situation & requesting some kind of help.", bg="help_email")
    
    label help_email:
        #--- Frame 77 ---
        $ clear()

        $ narrate("You're still working on the grant application a week later, and you're running perilously close to the deadline. You notice another email from Tara, whom you haven't heard from in a week.", "help email")

        $ narrate("What do you do this time?", full_overlay=True)

        $ clear()
        if overlooked:
            $ choiceMenu([("You can't afford any distractions. The grant is too important, and students need to learn resilience. You ignore the email and turn your attention back to the grant proposal.", "ghost", ("game_attr.timely", -1)), ("You relent, and agree to schedule a meeting with Tara to coordinate with them.", "zoom")]) #TODO: see if the loop into prev frame is on purpose
        else:
            $ choiceMenu([("You can't afford any distractions. The grant is too important, and students need to learn resilience. You ignore the email and turn your attention back to the grant proposal.", "storm", ("game_attr.timely", -1)), ("You relent, and agree to schedule a meeting with Tara to coordinate with them.", "zoom")]) #TODO: see if the loop into prev frame is on purpose

    label ghost:
    #--- Frame 64 ---
        $ clear()
        $ narrate("Since Tara doesn't hear back from you, they decide to give up completely. Tara stops submitting classwork and eventually gets special permissions to withdraw from your course.", bg="student sad dorm computer")

        $ tara_passes = False
        jump game_end

    label game_end:
        $ clear()

        if tara_passes: 
            $ narrate("Tara passes the class!", bg="student pass") # student happy
        else:
            #--Frame 66 ---
            $ clear()
            $ narrate("Tara does not pass the class.", "student fail")


        # nvl clear #remove #v
        # hide student
        # hide professor

        # $ clear()

        # show bg white #?

        # # Here we use a python `if` statement to check the flag and determine what text is displayed:
        # if win: 
        #     # We can also show text like an image with placement:
        #     show text "GAME OVER - YOU WIN!" at truecenter
        # else:
        #     show text "GAME OVER - YOU LOSE!" at truecenter

        # Have text display for just a second:
        $ renpy.hide_screen("narrator_overlay")
        with dissolve
        show game_over at truecenter
        pause
        # pause 1
        # hide text
        # with dissolve #^

    # This return statement at the end of the `start` block ends the game:
    return


# there was one path I wasn't sure about -- the second time the prof thinks about the grant (Frame 78 on figma) that goes back to Frames 53/67 and I wasn't if it loops back to somewhere we've already been?