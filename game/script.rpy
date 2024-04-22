﻿# Define the character variables:
# image source: https://charactercreator.org/#sex=f&skinColor=%23704139&irisColor=%23552200&hairColor=%231a1a1a&pupils=round&nose=strong&hair=down&emotion=neutral&shirt=structured_smart&shirtColor=%23e5e4e4&pants=jeans_bellbottoms&pantsColor=%23353743&shoes=moon
define s = Character("Student")

# image source: https://charactercreator.org/#sex=m&skinColor=%23e5b887&irisColor=%23784421&hairColor=%231a1a1a&pupils=round&hair=wavy&ears=default&nose=default&facialhair=beard_raw&glasses=hipster&tie=striped&jacket=suit_open&shirt=colar&pants=suit&shoes=leather
define p = Character("Professor")

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


default timely = 0
default flexible = 0
default teach = 0

init python:
    class ChoiceItem:
        def __init__(self, caption, next_label=None):
            self.caption = caption
            if next_label: self.action = Jump(next_label)
            else: self.action = None

    class QuizItem:
        def __init__(self, caption, quality=None):
            self.caption = caption
            if quality: self.action = IncrementVariable(quality[0], quality[1])
            # if quality: self.action = IncrementVariable(quality[0], quality[1])
            else: self.action = None





screen choose(items):
    style_prefix "choice"

    tag bg

    window: #?
    # frame:
        xfill True
        yfill True
        background "bg desk"

        vbox:
            for i in items:
                if i.action:
                    textbutton i.caption action i.action
                else:
                    text i.caption

        on "show" action Show("navigation")
        on "hide" action Hide("navigation")


screen quiz(prompt, items):
    default tt = Tooltip("No button selected.")

    # $ renpy.say(nb, txt)
    
    style_prefix "choice"

    tag bg

    window: #?
    # frame:
        xfill True
        yfill True
        background "bg black"

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


init python:
    # https://www.renpy.org/doc/html/python.html#default-statement
    bg_img = None

    # def narrate(txt, bg="paper_desk composite", white=False):
    def narrate(txt, bg=None, alpha=False):
        
        global bg_img
        if bg is not None and (bg_img is None or bg_img != bg):
            
            # Fade(0.5)
            # renpy.pause(0.5)
            renpy.with_statement(trans=dissolve) # fade)
            renpy.show(bg, tag="bg")
            # renpy.show_screen("narration_background", img=bg) #, _tag="bg")
            # _window_show(trans=fade)


            bg_img = bg

            # renpy.notify(bg_img)

        if alpha: renpy.show("nvl_full", tag="alpha")

        if bg_img == "paper_desk composite":
            # bg = "paper_desk composite"
            renpy.say(nb, txt)
        else:
            renpy.say(nw, txt)


    def clear():
        
        # _window_hide() #trans=fade)
        nvl_clear()
        renpy.hide("alpha")
        renpy.hide("bg")
        # renpy.hide_screen("bg")
        
        # renpy.with_statement(trans=fade)
        # _window_show(trans=fade)
        #
        global bg_img
        bg_img = None



# The game starts here with the built-in `start` label:
label start:
    $ narrate("Welcome to the game!  First, let's begin with a brief quiz.", bg="paper_desk composite")
    $ clear()

    call screen quiz(
        "You're teaching a course which has a few major projects. You observe that on the eve of a big research grant deadline that your student requests for extensions are piling up in your inbox. How do you manage the situation?", [
        QuizItem("You have a clear sense of your priorities, and realize that you can't grant everyone extensions to their project. Plus, the deadline was known to students many weeks in advance. You send an announcement to the class saying they have an additional 24 hours to work on the project. ", ("timely", -1)),
        QuizItem("Students have had ample time to plan around deadlines, but you empathize with the fact that sometimes things happen that are unexpected. While writing your grant draft, you answer student emails as they come to hear out what's causing them difficulty.", ("timely", 1))
    ]) with fade

    $ renpy.notify("timely: " + str(timely)) #remove #debug

    call screen quiz(
        "You notice that there's a student in your class who's struggling and not attending class consistently.\nYou want to reach out to the student to see if they're ok.", [
        QuizItem("You email the student and encourage them to come to office hours and remind them what time it is.", ("flexible", -1)),
        QuizItem("You email the student and ask them to suggest a time that works for them, saying that your plans are flexible (they may not be).", ("flexible", 1))
    ]) with fade

    $ renpy.notify("flexible: "+ str(flexible)) #remove #debug

    call screen quiz(
        "Do you place an emphasis on learning or teaching experiences? For example, when a student is struggling, would you step in a bit later, to let the student \"figure it out\"?", [
        QuizItem("Yes, tough love is indispensible.", ("teach", -1)),
        QuizItem("No, what the hell.", ("teach", 1))
    ]) with fade

    $ renpy.notify("teach: " + str(teach)) #remove #debug
    

    # =====

    call screen quiz(
        "Imagine you're a tour guide leading a large group through a bustling city. As you walk, some members of the group start to lag behind due to unexpected distractions. How do you manage the situation?", [
        QuizItem("Continue on the planned route", ("timely", -1)),
        QuizItem("Maintaining the pace for the majority", ("timely", 0)),
        QuizItem("Adjust your itinerary to accommodate the varying interests and needs of each member", ("timely", 1))
    ]) with fade

    $ renpy.notify("timely: " + str(timely)) #remove #debug

    call screen quiz(
        "Imagine you're on a journey through a dense forest with a companion. As you trek along, your friend encounters a barrier blocking their path, and they're unable to overcome it on their own. How do you respond to this situation?", [
        QuizItem("Step in immediately, offering assistance and working together to overcome the obstacle", ("flexible", 1)),
        QuizItem("Pause to assess the situation and consider seeking outside help", ("flexible", -1))
    ]) with fade

    $ renpy.notify("flexible: "+ str(flexible)) #remove #debug

    call screen quiz(
        "Imagine a nest of young birds perched high in a tree. You witness the mother pushing each of her chicks out of the nest. One bird seems reluctant to leave the safety of the nest, while the others eagerly practice spreading their wings. How do you interpret this situation?", [
        QuizItem("You believe that the anxious bird must be nudged out of the nest to learn to fly", ("teach", -1)),
        QuizItem("You believe there are other ways for it to develop the skills and confidence needed for flight", ("teach", 1))
    ]) with fade

    $ renpy.notify("teach: " + str(teach)) #remove #debug
    

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
    # Here we use the `default` statement to initialize a flag containing information about a choice the player has made.  The `win` flag starts off initialized to the special value `False` (as with the rest of Ren'Py, capitalization matters), meaning that it is not set. If certain paths are chosen, we can set it to `True` using a Python assignment statement.
    default win = False

    # show screen choice_list(opts)

    $ narrate("You are a new instructor at the Carnegie Institute of Technology (CIT) teaching a course about research methods. The class is a larger course, which makes staying connected with individual students slightly more difficult. Because it is a required course for students at CITis imperative that students pass you class so they can advance in their degree program.", bg="university")

    $ narrate("\nYou're excited to embark on your teaching journey and are still learning about the different offices and resources that the university has to offer, including their Office of Disability Resources (or ODR).")

    
    $ clear()
    $ narrate("This semester your research course includes students across academic years and background disciplines. This class involves a final group project that requires students to work together over several weeks. Each assignment builds off of each other and is critical towards progressing through all of the milestones.", bg="paper_desk composite")

    $ narrate("\nThe semester is about two-thirds of the way into the course calendar. Students have already formed groups and gone through a couple rounds of collaborative brainstorming to narrow down their specific topic and problem space. They are currently gearing up to build initial iterations of their prototype for testing.")

    $ clear()
    $ narrate("You have a student named Tara in your class – who has been promptly attending class and has a diligent work ethic. She has been keeping up with all of her assignments and been notably contributing towards her team's progress for the project so far.", bg="student classroom")
    
    $ clear()
    $ narrate("You're sitting in your office in Scaife hall when you hear your laptop ping. An email notification breaks the silence of your concentration. It's a follow-up from a student explaining their situation in detail and asking for help.", bg="professor office")

    $ clear()
    $ narrate("The email reads:", bg="laptop composite")

    $ clear()
    $ narrate("Tara's situation seems somewhat complex. You glance at the corner of your desk, where the grant proposal sits. There's a choice to be made...", bg="professor grant")


    $ clear()

    # The call screen statement shows a screen, and then hides it again at the end of the current interaction. If the screen returns a value, then the value is placed in the global _return variable.
    call screen choose([
        ChoiceItem("You can't afford any distractions. The grant is too important, and Tara needs to learn resilience. You ignore the email and turn your attention back to the grant proposal.", "opt1"),
        ChoiceItem("You decide to schedule a zoom meeting with the Tara to coordinate with them.", "opt2"), # here, backslashes are used to escape double quotes in the statement
        ChoiceItem("You respond to Tara's email.", "opt3")
    ]) with fade

    label opt1:
        $ clear()
        $ narrate("The storm after the calm. Your office becomes a reflection of the turmoil brewing outside it.", bg="professor office storm")

        $ narrate("\nIn the wake of your decision to prioritize the grant proposal over Tara's request, the ripples of consequence begin to surface.", alpha=True)

        $ narrate("\nWord spreads through the student community, and your inbox is now a testament to the oversight - a barrage of emails from the Office of Disability Resources (ODR), expressing concerns over your inaction.")

        $ clear()
        $ narrate("You stare at the screen, the ODR email open in front of you. Training modules on accommodating students feel like a chore, something you have convinced yourself you are beyond needing.", bg="professor office stare")

        $ narrate("\nSigh... this training seems like such a drag. I know all this stuff already, don't I? Maybe I'll put the grant proposal on hold for today and reach out to the student to discuss what would be helpful for them. It's not too late, right?", alpha=True)

        call screen choose([
            ChoiceItem("Initiate a conversation with Tara as a way to right your wrongs.", "opt2") #TODO: determine if correct
        ]) with fade

    label opt2:
        $ clear()
        $ narrate("You and Tara join the Zoom meeting room and begin to discuss Tara's options. Based on the meeting you:", bg="professor zoom")

        call screen choose([
            ChoiceItem("Suggest to Tara to either drop the class or obtain official ODR documentation due to concerns about unequal treatment.", "opt2_1"),
            ChoiceItem("Join Tara in their optimism and collaboratively work on a tight timeline to regain momentum.", "opt2_2"),
            ChoiceItem("Encourage Tara to prioritize rest, suggest adjusting the timeline, and propose a solo project as an alternative.", "opt2_3")
        ]) with fade

    label opt2_1:
        $ clear()
        $ narrate("Tara has never worked with ODR and get nervous, and begin to fall behind in your class.", bg="student sad dorm computer")

        $ clear()
        $ narrate("After a week of missed classes Tara finally goes to ODR but is told accommodations are not \"retro-active.\" This now means that the situation is out of ODR's and that the student must reach out to you again.", bg="student meeting")

        $ clear()
        $ narrate("As your work begins to pile up, you sit at the La Prima in Gates drinking tea and contemplate your next move:", bg="professor tea contemplating") 

        call screen choose([
            ChoiceItem("The student sends another email explaining their situation & requesting some kind of help.":, "TODO")
        ]) with fade

    label giveup: #TODO: determine which path this connects to
        #TODO: add img 
        n "Tara sees your email and decides to give up completely. Tara stops submitting classwork and eventually is able to get special permissions to withdraw from your course."

        n "\nTara does not pass the class."

        jump game_end
    
    label opt2_2:
        $ clear()
        $ narrate("At first it seems like Tara is catching up, but you later receive emails from their team members complaining that they haven't been doing their part in the project and have fallen off the grid. What should you do?", bg="team project")

        call screen choose([
            ChoiceItem("You reflect on why the Tara hadn't reached out to you to express that they were still struggling and ask for more support. You did everything you could to make them feel like they could still succeed, right? {b}You decide to email them to ask what went wrong.{\b}":, "opt2_2_1"),
            ChoiceItem("{b}You tell the group to \"work it out between themselves\" -- it seems like the Tara is failing to communicate.{\b} You think about how collaboration is an important skill to have in academia, so they student could use the practice with resolving interpersonal conflict on their own. Besides, you've already done your part to support Tara.", opt2_2_1_1)
        ]) with fade

    label opt2_2_1:
        #TODO: add img 
        nvl clear
        n "Tara responds with an appreciative and honest email. Tara was states that they were optimistic that they could overcome these obstacles, but they've never had to get academic accommodations before, and it wasn't as easy as they thought it would be."

        n "\nAll Tara had heard from other students with accommodations were horror stories about professors expecting them to function highly and blaming them for their difficulties.  Tara apologizes for assuming you would do the same, and ask where you think they should go from here."
        
        #TODO: add menu 
        nvl clear

        n "\nBased on this email you contemplate then decide:"

        menu:
            "You feel a bit surprised by this email, and even a little offended. You have put it more effort than your job expects you to in order to support this student. You wish students would give professors and group members a chance to help them, rather than ignoring emails and playing the victim last minute. This has clearly gotten out of hand and you feel awkward intervening at this point. You send the Tara to ODR and suggest they either take an incomplete or drop the class so they can focus on self-improvement.":
                jump opt2_2_1_1

            "This email makes you think hard about your role as a professor and the dynamic at your university. You didn't know how unaccommodating professors at your school have been and you even feel a little embarrassed, because you suspect you may unknowingly have made other students feel this way too. If you are a good person and just didn't know what to do, maybe there are other professors in the same position? You decide to organize a discussion and accessibility training for professors to share what you've learned.":
                jump opt2_2_1_2

    label opt2_2_1_1:
        #TODO: add img 
        nvl clear
        n "You never heard back from the student, but receive a notification email from the system informing you that the student has dropped your class. This sits uneasy with you, but you talk to some other professors who have dealt with similar issues and who say, \"that's just how it goes sometimes, you tried your best\" -- which makes you feel better."

        #TODO: add img 
        nvl clear
        n "Next semester, while working on a research project in Wean Hall, you overhear two students talking about how the student who dropped your class has gone on to drop out of the program. One of the students starts to say, \"I don't blame them, that professor [[you] is known for being unaccommodating and difficult to talk to---\";"

        n "They see you enter the area and go silent, grab their things, and leave."

        jump game_end
    
    label opt2_2_1_2:
        #TODO: add img 
        nvl clear
        n "Tara passes the class!"

        n "Congratulations! You grew as a person and a mentor, and you played an important role in affecting positive change for disabled students at CIT. Over the years, you will become known as a fantastic and understanding professor to take a class with among students."
        
        n "Your efforts will contribute to an increase in neurodiversity in higher education, accessible classrooms that those who usually skip class from overwhelm instead thrive in, and the normalization of difficult dialogue surrounding accommodations between students and professors."

        $ win = True
        jump game_end
            

    label opt2_3:
        #TODO: add img 
        nt "Tara responds positively to you proposing that they prioritize rest. You begin to work with them on the mechanics of the solo project. The following week you both meet in your office in Scaife hall and map out a game plan. You state:"

        p "Ok... So here's what's going to happen. You've already helped with designing milestone 1. I'll look at what you contributed for that assignment later tonight. I want you to go ahead and storyboard how you would improve the prototype based on my feedback, okay? Let's make our objective that you at least go through thinking about all of the prototyping steps"

        #TODO: add img 
        nvl clear

        # nt "You pause momentarily and observe the overwhelmed expression on Tara's face." #?
        # jump TODO

        n "You are optimistic about Tara's progress in the class but after a couple of weeks you notice Tara's progress updates have stopped. You're walking across The Cut to head to your office when you check your phone and see the following email from Tara:"

        #TODO

        #TODO: add img 
        nvl clear
        nt "This email catches you off guard. You're disappointed and frustrated that your efforts to help Tara are falling short. But you also want to prioritize Tara's health and well being. How will you respond?"

        #TODO: add menu 
        menu:
            "Hey Tara,\nI wonder if we will be able to hit the required learning goals for this course. I think the best move forward is that I'll give you the credit that I can for what work you've done throughout the course.\nRight now that means you'll end up with a C+":
                jump opt2_3_1

            "Hey Tara,\nI see. It's difficult to see how you'll be able to hit the required learning goals for the course, so I may not be able to give you the grade you're looking for.\nAre you available during the summer? We could have you continue completing work then if you're willing to take an Incomplete for the course.":
                jump opt2_3_2

    label opt2_3_1:
        n "Tara withdraws from the class in frustration"

    label opt2_3_2:
        n "You offer the student the option to either 1: take summer version of the course or take and incomplete and complete the course requirements over the summer."
        
        menu:
            "The student takes the summer version of the course and ends the term with a higher grade. Given the additional time and slower pace of the summer, the student feels much more relaxed which positively impacts how much information they retain.":
                jump game_end

    label opt3:
        jump TODO

    label TODO:
        nvl clear
        n "TODO: finish"

    label game_end:
        nvl clear
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