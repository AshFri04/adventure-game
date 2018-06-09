# coding=latin1

from sys import exit

user_name = " "
why_fuel_low_signal = " "
why_fuel_low_signal2 = " "

def start():
    route_a = """
    \tTravel 3 billon miles to Pluto using our interstellar technology that runs in 
    \tthe Falcon 1. Once on Pluto, you MUST find Quuatum and use it! Quuatum is a 
    \tteleport system found on the outer shell of Pluto's existence. This teleport 
    \tsystem will project you to a galaxy named Luna, where Planet X lives. Secure
    \tthe geode from Planet X and bring it safely back to Earth."""

    route_b = """
    \tTravel to Saturn where there is a black hole 32,000 miles north of its largest
    \tring. You must travel through the black hole, which will take you to Luna. Find
    \tPlanet X and secure the geode where you will bring it safely back to Earth!"""
    
    print """
    \tYou have entered the Falcon 1...
    \tInside you see 2 intergalactic routes you can take to achieve your mission. 
    \n\t\t\t\t  You must ONLY choose one.
    """
    
    print "Intergalactic Route A: ", route_a
    print
    print "Intergalactic Route B: ", route_b
    print
    print
    
    #Chooses between the two paths in game:
    print "Which route do you ulimately choose? (Type a or b):" 
   
    global choice_of_route
    
    choice_of_route = raw_input("> ").lower()

    if choice_of_route == "a":
        route_pluto()
        if green_or_purple == "green":
            green_choice()
            not_enough_fuel_pluto_conflict()
            low_fuel_signal()
            low_fuel_signal_route_a()
            wait_or_repair_choice()
            mystical_creature_riddle()    
            
        elif green_or_purple == "purple":
            purple_choice()    #Game Over
            
            
    elif choice_of_route == "b":
        route_saturn()


def rocket_ship():
    print """                   
    
    
    
                                 /\ 
                                |  |
                                |  |
                                |  |
                                |  |
                                |  |
                               /____\ 
                               |    |
                               |    |
                               |    |
                              /|    |\ 
                             /_|____|_\ 
                               /_\/_\ 
                               ###### 
                             ########## 
                               ###### 
                                ####
                                ####
                                 ## 
                                 ## 
                                 ##    
                                 ##
                                 
                                 
                                 
                                 
                                 """
    
def winning_stars():
    print "                 ^                                          ^        "
    print "           '. __/ \__ .'                              '. __/ \__ .'  "
    print "            __\     /__                                __\     /__   "
    print "              /_   _\                                    /_   _\     "
    print "            .'  \ /  '.                ^                .' \ / '.    "
    print "                 v               '. __/ \__ .'              v        "
    print "                                  __\     /__                        "
    print "                                    /_   _\                          "
    print "                                  .'  \ /  '.                        "
    print "                                       v                             "


def route_pluto():
    """Route to Pluto. User conflict 1: Meteor Shower. Must decide between choice green or purple."""
    rocket_ship()
    print """
    
    You can hear Falcon 1's engines roar as you make your way towards Pluto. 
    Halfway there, you begin to feel the spacecraft shake as you have enter a 
    meteor shower. Two large buttons are blinking on your dashboard -- one green
    that says Collision Avoidance Maneuver and the other purple stating Engage
    Shields. You begin to sweat as it seems obvious that you must pick between
    these two choices as both cannot be activated at the same time.
    
    """
    print "Which button do you press (green or purple)? Hurry you have 20 seconds!"
    
    global green_or_purple
    
    green_or_purple =raw_input("> ").lower()
    
    return green_or_purple
    
def purple_choice():
    #User dies. GAME OVER.
    print """
    The shields have activated and you see the whole spacecraft covered in a 
    massive, multi-layered shield. Shields can resist hypervelocity impacts 
    of particles only up to a millimeter. Trembling in fear, the Falcon 1 gets
    hit! You feel the huge implosion on the lower end of the spacecraft where
    the engines are located. The Falcon 1 gets hit again and you, injured and 
    bleeding, get stucked into space, where you ultimately die minutes later.
    
    """
    game_over()
    
def green_choice():
    #Continues game
    print """ 
    You feel the main engines initiate on hyperdrive as a huge burst of fuel is
    used to create energy to move the Falcon 1 out of the way of the meteors. 
    The Collision Avoidance Maneuver is activated and the spacecraft is weaving 
    through the meteors!
    
    """
    print "\t\tYou sigh in relief as you continue your mission!"
    print
    
    winning_stars()
    
def not_enough_fuel_pluto_conflict():
    
    
    
    print
    print "\tAfter 15 more days of space travel, you see a grayish, dwarf planet."
    
    ascii_pluto = """
    
                                       *       +
                                   '                  |
                            ()       ,="``"=.    - o -
                                    /        \     |
                                *  |          |
                          '         \        /   +       '
                                 .   '=.__.='          *
                             +                      +
                                    O      *        '       .
    
    
    """
    print ascii_pluto
    
    print "                      AH, you made it to Pluto, {}!".format(user_name)
    print "        You can see the Quuatum as it glows vibrant green and blue rays!"
    
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print """
    You fly the Falcon 1 over it and it takes you through to Luna. Falcon 1
    navigational signal activates. It has spotted Planet X and is in route. As you
    advanced towards Planet X, Falcon 1 signals a serious and shocking warning...
    
    """
    
def low_fuel_signal():
    
    fuel_signal = """\t\t\t\tWARNING WARNING! 
                       
                       Battery operation system defective!
            Fuel cells at low critical point! MUST replenish resources!"""
    print
    print fuel_signal
    
def low_fuel_signal_route_a():
    avoidance_maneuver = "performed the Collision Avoidance Maneuver"
    meteor_shower = "through the Meteor Shower"
        
    why_fuel_low_signal = """
    You discovered that when you {},
    you used up the majority of your resources to create the thrust that you
    needed to propel {}! It somehow caused an unknown
    defect in the battery operational system!""".format(avoidance_maneuver,meteor_shower)
    
    print why_fuel_low_signal
    
    # User choice (3) to fix Falcon 1 now or wait.
    print """
    Do you wait to arrive at Planet X to restore and repair the fuel system
    (choice A) or do you head towards the nearest space station, diverting
    the current route -- adding time and possible danger to the overall 
    mission (choice B)? (Type A or B)
                                                                                         
    """
    
    global wait_or_repair
    
    wait_or_repair = raw_input("> ").upper()
    
    return wait_or_repair
    
def wait_or_repair_choice():
    print""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    print
    print
    print
    for i in wait_or_repair:
        if i == "A":
            #Choice A: waiting to arrive at Planet X.
            print """
    The Falcon 1 ran out out of energy and fuel to propel the spacecraft
    to Planet X and now, to any planet. You are at a standstill, drifting
    in the emptiness of Luna until you meet your death due to starvation 
    and suffocation. 
    
            """
            
            game_over()
        
        elif i == "B":
            """Choice B: Head towards nearest space station to repair Falcon 1."""
            print
            print
            print
            print
            print
            print
            print
            print
            alien_chuck = """
.     .       .  .   . .   .   . .    +  .
  .     .  :     .    .. :. .___---------___.
       .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
    .  :       .  .  .:../:            . .^  :.:\.
        .   . :: +. :.:/: .   .    .        . . .:\

  .. . .   . - : :.:./.                        .  .:\

    .       . : : ..||        .                . . !:|
  .     . . . ::. ::\(                           . :)/
 .   .     : . : .:.|. ######              .#######::|
  :.. .  :-  : .:  ::|.#######           ..########:|
 .  .  .  ..  .  .. :\ ########          :######## :/
  .        .+ :: : -.:\ ########       . ########.:/
    .  .+   . . . . :.:\. #######       #######..:/
      :: . . . . ::.:..:.\           .   .   ..:/
   .   .   .  .. :  -::::.\.       | |     . .:/
      .  :  .  .  .-:.":.::.\             ..:/
 .      -.   . . . .: .:::.:.\.           .:/
.   .   .  :      : ....::_:..:\   ___.  :/
   .   .  .   .:. .. .  .: :.:.:\       :/
     +   .   .   : . ::. :.:. .:.|\  .:/|
     .         +   .  .  ...:: ..|  --.:|
.      . . .   .  .  . ... :..:.."(  ..)"
 .   .       .      :  .   .: ::/  .  .::\  """
 
            print alien_chuck
 
            print """
    You rush the Falcon 1 to the nearest space station. Upon entering the
    space station, you are greeted by an alien that goes by the name 'Chuck.'
    Somehow, you are not afraid as Chuck seems kind and helpful. Chuck, 
    inspired that a human made it into his galaxy, happily gives you the
    resources you need, repairs your battery systems and gives you a reward!
    
    Do you accept the award from Chuck? (Type y or n) """
            accept_award = raw_input(">")
            if accept_award == "y":
                print
                print
                print
                print
                print
                print
                print
                print
                print
                print
                print
                print
                print
                print
                winning_stars()
        
                print """
                                                                        
                            CONGRATULATIONS!!!                             
                                                                        
    You have obtained a TOSFLH!! A TOSFLH stand for Teleporting Operational
    System For Lucky Humans -- use the TOSFLH when you collect the geode on
    Planet X to travel back to Earth within seconds!!!"""
    
                print """
    You thank Chuck and say goodbye as you head back into the Falcon 1. After
    5 more days of space travel, you have finally landed on Planet X!! As you 
    explore the planet in search of the Geode, you encounter a mystical creature."""
                
                print """
    Do you encounter this mystical creature or run away cowardly?
    (Please type encounter or run):
    """
                encounter_or_run = raw_input("> ")
                    
                if "encounter" in encounter_or_run:
                    mystical_creature_riddle()
                elif "run" in encounter_or_run:
                    print """
                Oh my, you really are a coward. This is no place
                for you. Good luck getting back to Earth!"""
                    exit(0)
                else:
                    exit(0)
                
                
            elif accept_award == "n":
                print "Ok, that's kind of weird. No judgement though!"
                print """
                Because you didn't take the reward - you ended up
                stranded on Planet X and starved to death."""
                game_over()
                
            else:
                print "Invaid Entry. Game will now end. Goodbye!"
                exit(0)
                
        else:
            print "Invaid Entry. Please type A or B"
            i = raw_input("> ")
#******^QUESTION FOR MENTOR: how can I loop this around so the user can add a or b again?            
    
def mystical_creature_riddle():
    #Creature introduces himself.
   
    print""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    creature = """
    
    
  
    ##############~._________  ################ __` ~~.______.~##############
    ############~.' `.`-'   /   ~#############~ .  \   `-'.'  `.~############
    ##########~.'    |     |  .__ ~##########~ __.  |     |     `.~##########
    ######~.'        `.    |  `.. .@@@@@@@@@@  ..'  |    .'         `.~######
    ####~.'            \   | #.`.`._`.'--`.'_.'.'.# |   /             `.~####
    ##~.'       ......  \  | ###.`~'(o\||/o)`~'.### |  /  ......        `.~##
    ~.`.......'~      `. \  \~####  |\_  _/|  ####~/  / .'      ~`........'.~
    ;.'                 \ .----.__.'` (||)'`.__.----. /                  `; 
    `.                  .'    .'   `. \  / .'   `.    `.                  .' 
    #:               ..':      :    '. ~~ .`    :      :`..               :# 
    #:             .'   :     .'     .'  `.     `.     :   `.             :# 
    #:           .'    .`   .'       . || .       `.   '.    `.           :# 
    #:         .'    .' :       ....'      `....       : `.    `.         :# 
    ##.`       '#####\__~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~__/#####`      '.##                                   
    ###        #######  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #######       ### """
    
    print creature
    
    print""" 
    This creature seems to be floating as he has no legs. As you approach the dark,
    15 ft mystical thing, he begins to speak to you...

    "Oh my, if it isn't a human. I've never seen one up close. {}, is it? You can
    call me Rubeus Hagrid. I am the keeper of all things on this planet.""".format(user_name)
    
    #Rubeus Hagrid gives user a riddle
    print """
    {}, I see that you desire the geode. I'm feeling generous today and am willing
    to help you out. You may have it on one condition. You must correctly guess 
    my magical number. I will give you a riddle to help you succeed and one clue: 
    the number is between 1 and 10. I will grant you 3 guesses.
    
    """.format(user_name)
    
    print "My riddle is:"
    print """
    My magical number is an odd number and if you take away an alphabet letter,
    the number becomes even.                                                                                                        
                                                                                 
                            What is my magical number?" """
                            
    for guesses_taken in range (1,4):
        guess = int(raw_input("> ")) 
        
        if guess < 7:
            print '"Too low, my friend."'
            print
        elif guess > 7:
            print '"Haha, that is too high."'
            print
        else:
            break

    if guess == 7:
            #Wins! Reward is the geode.
            print """
            "AHHHH, yes!! {}, you have guessed my Magical Number!! 
            \t\t(Seven: Seven - S = even)                       
            You are smarter than you look! Here, you have earned the geode." """.format(user_name)   
            print
            winning_stars()
            game_won()
    else:
        #Loses
        print """
        "Tisk tisk tisk. Your 3 guesses are up, {}. 
        Pity, I really didn't want to have to kill you." 
        
        Hagrid grabs you at your waist and eats you alive!!
        
        """.format(user_name)
        
        game_over()
        
        
def route_saturn():
    print
    print
    print
    print
    print
    print
    print
    print"""
    You enter the Falcon 1 and prepare the spacecraft for departure. The engines
    start and you begin to leave the Earth's atmosphere! After 10 days of space 
    travel, you begin to smile as you can see Saturn. Navigating your way towards 
    the black hole located near Saturn, you see in the distance something coming at
    you at lighting speed. You begin to question what it is and before you can take
    your next breath, your eyes open wide as you see 5 alien ships surrounding you
    that won't let you pass into the black hole!"""
    print """
                                                    .::.
                                                 .:'  .:
                                       ,MMM8&&&.:'   .:'
                                     MMMMM88&&&&  .:'
                                    MMMMM88&&&&&&:'
                                    MMMMM88&&&&&&
                                  .:MMMMM88&&&&&&
                               .:'  MMMMM88&&&&
                            .:'   .:'MMM8&&&'
                            :'  .:'
                            '::'  """
                            
    print """
    
    👽               👽                  👽                 👽                👽    
    
    Outnumbered, your instincts are telling you to fight as fear has taken over. You
    look over to your dashboard and see a red button with the words "Hyperdrive."
    You instantly realize that you have 2 choices.
    
    Do you fight the aliens or launch the Falcon 1 into hyperdrive?
    
    """
   
    
    fight_or_hyperdrive = raw_input("> ").lower()
    
    if "aliens" in fight_or_hyperdrive or "fight" in fight_or_hyperdrive:
        fight_aliens()   #GAME OVER
        
    elif "hyperdrive" in fight_or_hyperdrive or "falcon" in fight_or_hyperdrive:
        falcon1_in_hyperdrive()
        not_enough_fuel_saturn_conflict()
        wait_or_repair_choice()
        mystical_creature_riddle()
    
def fight_aliens():
    #User dies. GAME OVER.
    
    print"""
    Locked and loaded, you begin to fire! The alien ships surround you and attack!
    No match for their advanced technology. You die instantly.
    
    """
    game_over()
    
def falcon1_in_hyperdrive():
    #User continues the game.
    
    print"""
    You engage the Falcon 1 in hyperdrive which launches you straight through
    the black hole. You survived the alien attack and made it to Luna, home of 
    Planet X!"""

def not_enough_fuel_saturn_conflict():
    
    print"""
    Feeling excited, Falcon 1 navigational signal activates. It has spotted
    Planet X and is in route. As you advance towards Planet X, Falcon 1 signals
    a serious and shocking warning...
    
    """
    low_fuel_signal()
    
    hyperdrive = "put Falcon 1 into hyperdrive"
    past_aliens = "you past the aliens and into the black hole" 
        
    why_fuel_low_signal2 = """
    You discovered that when you {},
    you used up the majority of your resources to create the thrust that you
    needed to propel {}! It somehow caused an unknown
    defect in the battery operational system!""".format(hyperdrive, past_aliens)
    
    print why_fuel_low_signal2
  
    # User choice to fix Falcon 1 now or wait.
    print """
    Do you wait to arrive at Planet X to restore and repair the fuel system
    (choice A) or do you head towards the nearest space station, diverting
    the current route -- adding time and possible danger to the overall 
    mission (choice B)? (Type A or B)"""
    
    global wait_or_repair
    
    wait_or_repair = raw_input("> ").upper()
    
    return wait_or_repair


def game_won():
    
    print """
    
    You quickly grab the geode and run by to the Falcon 1. Remembering
    that you won the TOSFLH, you begin to activate it!
    
    A beam of light encompasses all around you and the next thing you know
    you are in Earth's Atmosphere!!!
    
    \t\tYOU DID IT!!! You brought back the geode! 
    
    The technology located inside the geode is taken apart in San Francisco
    Transamerica Pyramid and the new Transportation system is built and 
    ready for use!!
    
    We and the people of San Francisco thank you, {}, for saving us!
    
    
    \t\t\t\t***WINNER***
    
    """.format(user_name)
    
    print "Do you want to play again (y or n)?"
    
    play_again = raw_input("> ")
    
    while True:
        if play_again == "y".lower():
            start()
        elif play_again == "n".lower():
            exit(0)   #function used from sys
        
        
        else:
            exit(0)
    
def game_over():
    print"\t\t\t\tGAME OVER"
    print
    print "Do you want to play again (y or n)?"
    
    play_again = raw_input("> ")
    
    while True:
        if play_again == "y".lower():
            start()
        elif play_again == "n".lower():
            exit(0)   #function used from sys
        else:
            break

def intro_to_game():
    #Introduction to Adventure Game

    print"""
                    Welcome to Adventure Game 
              *************************************
Where you embark on a magical quest to conquer your mission by solving problems 
and testing your decision making skills! Let's see if you have what it takes..."""

    #Ask user name
    print """
With whom am I speaking with?"""
    
    global user_name
    user_name = raw_input("> ").capitalize()
    
    return user_name

def explanation_of_game(): 
    #Explain mission of the game
    print """
{}, the people of San Francisco are always late to work due to the inefficiencies of BART!
Thousands of San Francisco commuters each day are suffering and it is up to you to help them. 
We have obtain classified information that there is advanced technology inside a geode hidden
on Planet X, located millions of galaxies away. This geode, once brought back to San Francisco,
can implement within seconds a transportation system that is far advance & efficient than any
thing on this Earth, saving the people of San Francisco from frustration, rage and tardiness!!""".format(user_name)

    print """
Your mission, {}, should you choose to accept it, is to obtain the geode hidden on Planet X 
and safely bring it back to San Francisco.
    """.format(user_name)
    
    #Ask user if they want to play
    print "Do you accept your mission (type yes or no)?"
    accept_mission = raw_input("> ").capitalize()

    if accept_mission == "Yes" or accept_mission == "Yeah" or accept_mission == "Yea":
        print
        print
        print
        print
        print
        print """
    
    
    
    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

          I knew that we and all the people of San Francisco could count on you! 

   As always, should you or any of your forces be caught or killed, the Secretary will 
   disavow any knowledge of your actions. Quickly head into the spacecraft, Falcon 1. 
                        There you will begin your mission. 

                                    Good luck, {}!

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    """.format(user_name)
    

    # ASCII ART OF USER ENTERING FALCON 1
       
        
        start()
        

    elif accept_mission == "No":
        print"""

        I didn't take you for a coward, {}. I was wrong...
        Your memory of this mission will cease to exist in 5 seconds.

        \t\t\tGoodbye, {}!

        """.format(user_name,user_name)

    
    else:
        print"""
    
        Invalid Entry: Game will now end. Goodbye!
    
        """
        exit(0)
        


#---------Begin Game--------

intro_to_game()
explanation_of_game()