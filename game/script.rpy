# Define the character variables:
# image source: https://charactercreator.org/#sex=f&skinColor=%23704139&irisColor=%23552200&hairColor=%231a1a1a&pupils=round&nose=strong&hair=down&emotion=neutral&shirt=structured_smart&shirtColor=%23e5e4e4&pants=jeans_bellbottoms&pantsColor=%23353743&shoes=moon
define s = Character("Student")

# image source: https://charactercreator.org/#sex=m&skinColor=%23e5b887&irisColor=%23784421&hairColor=%231a1a1a&pupils=round&hair=wavy&ears=default&nose=default&facialhair=beard_raw&glasses=hipster&tie=striped&jacket=suit_open&shirt=colar&pants=suit&shoes=leather
define p = Character("Professor")

# define e = Character("Eileen", image="eileen")



# https://www.renpy.org/doc/html/style_properties.html
# define n = Character(None, kind=nvl, what_xpos=360, what_ypos=0, what_xsize=1170, screen="nvl_narration") #, what_prefix="{cps=25}", what_suffix="{/cps}", ctc="ctc_anchored", ctc_position="fixed")

define n = Character(None, kind=nvl, what_xpos=360, what_ypos=0, what_xsize=1170, what_xalign=0.0, what_color="#000000") #, what_prefix="{cps=25}", what_suffix="{/cps}", ctc="ctc_anchored", ctc_position="fixed")


define n_bg = Character(None, kind=nvl, what_xpos=360, what_ypos=0, what_xsize=1170, what_xalign=0.0, window_background="gui/nvl.png") #, what_prefix="{cps=25}", what_suffix="{/cps}", ctc="ctc_anchored", ctc_position="fixed")

# # top narrator
# define nt = Character(None, kind=nvl, what_xpos=360, what_xsize=1170, what_ypos=50, window_background="gui/textbox.png") #, window_background=None) 
# define centered = Character(None, kind=nvl, what_style="centered_text", window_style="centered_window")
# define narrator = nvl_narrator
# define menu = nvl_menu

# The game starts here with the built-in `start` label:
label start:
    # Here we use the `default` statement to initialize a flag containing information about a choice the player has made.  The `win` flag starts off initialized to the special value `False` (as with the rest of Ren'Py, capitalization matters), meaning that it is not set. If certain paths are chosen, we can set it to `True` using a Python assignment statement.
    default win = False

    n_bg "You are a new instructor at the Carnegie Institute of Technology (CIT) teaching a course about research methods. The class is a larger course, which makes staying connected with individual students slightly more difficult. Because it is a required course for students at CITis imperative that students pass you class so they can advance in their degree program."

    n_bg "\nYou're excited to embark on your teaching journey and are still learning about the different offices and resources that the university has to offer, including their Office of Disability Resources (or ODR)."

    nvl clear

    n_bg "This semester your research course includes students across academic years and background disciplines. This class involves a final group project that requires students to work together over several weeks. Each assignment builds off of each other and is critical towards progressing through all of the milestones."

    n_bg "\nThe semester is about two-thirds of the way into the course calendar. Students have already formed groups and gone through a couple rounds of collaborative brainstorming to narrow down their specific topic and problem space. They are currently gearing up to build initial iterations of their prototype for testing."

    n_bg "\nYou have a student named Tara in your class – who has been promptly attending class and has a diligent work ethic. She has been keeping up with all of her assignments and been notably contributing towards her team's progress for the project so far."

    nvl clear

    window hide
    scene bg email
    with fade
    window show

    n "You're sitting in your office in Scaife hall when you hear your laptop ping. An email notification breaks the silence of your concentration. It's a follow-up from a student explaining their situation in detail and asking for help. The email reads:"

    nvl clear

    window hide
    scene bg choice
    with fade
    window show

    n "Tara's situation seems somewhat complex. You glance at the corner of your desk, where the grant proposal sits. There's a choice to be made..."

    nvl clear

    # source: https://www.canadianunderwriter.ca/insurance/what-happened-to-the-ex-broker-who-claimed-he-was-a-ce-instructor-but-wasnt-1004194769/
    scene bg desk

    # The menu statement introduces an in-game choice. It takes an indented block of lines, each consisting of a string followed by a colon. These are the menu choices that are presented to the player. Each menu choice takes its own indented block of lines, which is run when that menu choices is chosen.
    menu:
        "You can't afford any distractions. The grant is too important, and Tara needs to learn resilience. You ignore the email and turn your attention back to the grant proposal.":
            jump opt1 # The jump statement transfers control to the a label defined using the label statement. After a jump, script statements following the label are run.
        
        "You decide to schedule a zoom meeting with the Tara to coordinate with them.": #here, backslashes are used to escape double quotes in the statement
            jump opt2
        
        "You respond to Tara's email.":
            jump opt3

    label opt1:
        n "The storm after the calm. Your office becomes a reflection of the turmoil brewing outside it."

        n "\nIn the wake of your decision to prioritize the grant proposal over Tara's request, the ripples of consequence begin to surface."

        n "\nWord spreads through the student community, and your inbox is now a testament to the oversight - a barrage of emails from the Office of Disability Resources (ODR), expressing concerns over your inaction."

        nvl clear

        n "You stare at the screen, the ODR email open in front of you. Training modules on accommodating students feel like a chore, something you have convinced yourself you are beyond needing."

        n "\nSigh... this training seems like such a drag. I know all this stuff already, don't I? Maybe I'll put the grant proposal on hold for today and reach out to the student to discuss what would be helpful for them. It's not too late, right?"

        menu:
            "Initiate a conversation with Tara as a way to right your wrongs.":
                jump opt2 #TODO: determine if correct

    label opt2:
        nvl clear
        n "You and Tara join the Zoom meeting room and begin to discuss Tara's options. Based on the meeting you to:"

        menu:
            "Suggest to Tara to either drop the class or obtain official ODR documentation due to concerns about unequal treatment.":
                jump opt2_1

            "Join Tara in their optimism and collaboratively work on a tight timeline to regain momentum.":
                jump opt2_2

            "Encourage Tara to prioritize rest, suggest adjusting the timeline, and propose a solo project as an alternative.":
                jump opt2_3

    label opt2_1:
        nvl clear
        n "Tara has never worked with ODR and get nervous, and begin to fall behind in your class."

        nvl clear

        n "After a week of missed classes Tara finally goes to ODR but is told accommodations are not \"retro-active.\" This now means that the situation is out of ODR's and that the student must reach out to you again."

        nvl clear

        n "As your work begins to pile up, you sit outside the La Prima in Gates and contemplate your next move:"

        menu:
            "The student sends another email explaining their situation & requesting some kind of help.":
                jump TODO

    label giveup: #TODO: determine which path this connects to
        n "Tara sees your email and decides to give up completely. Tara stops submitting classwork and eventually is able to get special permissions to withdraw from your course."

        n "\nTara does not pass the class."

        jump game_end
    
    label opt2_2:
        nvl clear
        n "At first it seems like Tara is catching up, but you later receive emails from their team members complaining that they haven't been doing their part in the project and have fallen off the grid. What should you do?"

        menu:
            "You reflect on why the Tara hadn't reached out to you to express that they were still struggling and ask for more support. You did everything you could to make them feel like they could still succeed, right? {b}You decide to email them to ask what went wrong.{\b}":
                jump opt2_2_1

            "{b}You tell the group to \"work it out between themselves\" -- it seems like the Tara is failing to communicate.{\b} You think about how collaboration is an important skill to have in academia, so they student could use the practice with resolving interpersonal conflict on their own. Besides, you've already done your part to support Tara.":
                jump opt2_2_1_1

    label opt2_2_1:
        nvl clear
        n "Tara responds with an appreciative and honest email. Tara was states that they were optimistic that they could overcome these obstacles, but they've never had to get academic accommodations before, and it wasn't as easy as they thought it would be."

        n "\nAll Tara had heard from other students with accommodations were horror stories about professors expecting them to function highly and blaming them for their difficulties.  Tara apologizes for assuming you would do the same, and ask where you think they should go from here."
        
        nvl clear

        n "\nBased on this email you contemplate then decide:"

        menu:
            "You feel a bit surprised by this email, and even a little offended. You have put it more effort than your job expects you to in order to support this student. You wish students would give professors and group members a chance to help them, rather than ignoring emails and playing the victim last minute. This has clearly gotten out of hand and you feel awkward intervening at this point. You send the Tara to ODR and suggest they either take an incomplete or drop the class so they can focus on self-improvement.":
                jump opt2_2_1_1

            "This email makes you think hard about your role as a professor and the dynamic at your university. You didn't know how unaccommodating professors at your school have been and you even feel a little embarrassed, because you suspect you may unknowingly have made other students feel this way too. If you are a good person and just didn't know what to do, maybe there are other professors in the same position? You decide to organize a discussion and accessibility training for professors to share what you've learned.":
                jump opt2_2_1_2

    label opt2_2_1_1:
        nvl clear
        n "You never heard back from the student, but receive a notification email from the system informing you that the student has dropped your class. This sits uneasy with you, but you talk to some other professors who have dealt with similar issues and who say, \"that's just how it goes sometimes, you tried your best\" -- which makes you feel better."

        nvl clear
        
        n "Next semester, while working on a research project in Wean Hall, you overhear two students talking about how the student who dropped your class has gone on to drop out of the program. One of the students starts to say, \"I don't blame them, that professor [[you] is known for being unaccommodating and difficult to talk to---\";"

        n "They see you enter the area and go silent, grab their things, and leave."

        jump game_end
    
    label opt2_2_1_2:
        nvl clear
        n "Tara passes the class!"

        n "Congratulations! You grew as a person and a mentor, and you played an important role in affecting positive change for disabled students at CIT. Over the years, you will become known as a fantastic and understanding professor to take a class with among students."
        
        n "Your efforts will contribute to an increase in neurodiversity in higher education, accessible classrooms that those who usually skip class from overwhelm instead thrive in, and the normalization of difficult dialogue surrounding accommodations between students and professors."

        $ win = True
        jump game_end
            

    label opt2_3:
        nt "Tara responds positively to you proposing that they prioritize rest. You begin to work with them on the mechanics of the solo project. The following week you both meet in your office in Scaife hall and map out a game plan. You state:"


        p "Ok... So here's what's going to happen. You've already helped with designing milestone 1. I'll look at what you contributed for that assignment later tonight. I want you to go ahead and storyboard how you would improve the prototype based on my feedback, okay? Let's make our objective that you at least go through thinking about all of the prototyping steps"

        nvl clear

        # nt "You pause momentarily and observe the overwhelmed expression on Tara's face." #?
        # jump TODO

        n "You are optimistic about Tara's progress in the class but after a couple of weeks you notice Tara's progress updates have stopped. You're walking across The Cut to head to your office when you check your phone and see the following email from Tara:"

        #TODO

        nvl clear

        nt "This email catches you off guard. You're disappointed and frustrated that your efforts to help Tara are falling short. But you also want to prioritize Tara's health and well being. How will you respond?"

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