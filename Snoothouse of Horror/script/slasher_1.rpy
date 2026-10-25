label shh_slasher_1:    
    scene black with Dissolve(2)

    pause 1

    play music SHH + "audio/music/suburb sounds.mp3" fadein 0.5

    scene home fang outside with Dissolve(3)
    $ quick_menu = True
    pause 3
    play sound SHH + "audio/sfx/front door.mp3"

    pause 3

    show fang neutral with Dissolve(3):
        xcenter 0.5 ycenter 0.655
 
    F "{i}{cps=*0.2}*YAAAAAAAAAAAAAAAAAAWN*" #shaking text doesn't work with wait/cps text tags
    
    "My body moves on instinct as it stretches out."

    "Eyes squinting against the light of the morning sun as its blinding light welcomes me back to the world of the living."

    "A bright blue sky overlooks our tranquil suburban paradise,{w=0.20} enveloped by the low hum of distant traffic and some boomer mowing his lawn a couple blocks down."

    show fang unimpressed with dissolve

    "The sight of everyone's perfect little lives ticking along used to make me sick,"

    show fang happy with dissolve

    "But I think I'm starting to come around."

    "A stiff breeze blows through, {nw}"
    
    show fang sad:
        easein .2 ycenter 0.75
        easein .2 ycenter 0.655
    "A stiff breeze blows through, {fast}and I'm quickly snapped back to reality."
    
    show fang neutral with Dissolve (.25)

    "Guess that's it for summer."

    show fang neutral flip with dissolve 
    "I can't be bothered to go back in for a coat, so I suck it up and begin the long walk to Reed's place."
    show fang neutral with dissolve:
        pause 1
        parallel:
            easein 3 xcenter 1.5
        parallel:
            block:
                easein 0.15 ycenter 0.60
                easein 0.15 ycenter 0.655
                repeat 10


    scene black with Dissolve(1)
    pause 2
    hide fang

    scene shh_neighborhood  with Dissolve(1):
        zoom 2.5
        yalign .7
        parallel:
            xpan 0
            linear 40 xpan 360
            repeat

    show fang neutral at walking_cycle_aligned:
        xcenter -.5
        parallel:
            linear 3.0 xcenter 0.5

    pause 0.5

    "Sadly there’s no one home to drive me,{w=.25} and I ain’t paying for a cab."

    show fang considering with dissolve

    "He's not {i}that{/i} far away."

    show fang neutral with dissolve

    "Besides, that's kind of the point."

    "With Mom and my brother out this weekend doing campus tours,{w=.25} and Dad practically welded to his desk..."

    show fang happy with dissolve

    "I’ve finally got the house all to myself for once."

    "Probably won’t get too many more opportunities like this before classes start,{w=.25} so I'm hoping to make the most of it."

    play sound SHH + "audio/sfx/leaf rustle.mp3"

    pause 0.1
    show fang surprised at walking_cycle_stop

    show shh_neighborhood :
        zoom 2.5
        yalign .7

    pause 2

    show fang flip neutral

    pause 0.5

    scene shh_sidewalk1
    hide fang

    "?"

    pause 2

    "Huh."

    #show shh_neighborhood :
    #    zoom 2.5
    #    yalign .7

    #show fang flip neutral at walking_cycle_aligned

    #show fang flip neutral at walking_cycle_stop

    #pause 1

    #scene shh_neighborhood:
    #    zoom 2.5
    #    yalign .7
    #    parallel:
    #        xpan 0
    #        linear 40 xpan 360
    #        repeat

    #show fang neutral at walking_cycle_aligned

    #pause 2

    scene black with Dissolve(1)

    scene shh_neighborhood  with Dissolve(1):
        zoom 2.5
        yalign .7
        parallel:
            xpan 0
            linear 40 xpan 360
            repeat

    show fang neutral at walking_cycle_aligned:
        xcenter -.5
        parallel:
            linear 3.0 xcenter 0.5

    pause 1

    "Let's see what the dweeb is up to."

    play sound SHH + "audio/sfx/purse.mp3"

    pause 2

    stop sound

    pause 0.5

    play sound SHH + "audio/sfx/phone_buzz.mp3"
    pause 3

    A "Frank's crematory,{w=.5} you kill'em {w=.2}we grill'em!"

    show fang considering with dissolve
    pause .5
    show fang happy with dissolve

    F "Hey Anon, you ready for tonight?"

    A "Of course! {w=.2}So what's the plan?"

    show fang neutral with dissolve

    F "I don't know,{w=.2} haven't thought that far ahead yet."

    show fang happy with dissolve

    F "But I'm looking forward to a little quality time somewhere that doesn't smell like a crack den."

    A "Heh.{w=.2} You and me both."

    F "So how are you getting over to Reed's?{w=.2} We can pick you up if you want."

    A "Don't worry about me,{w=.2} I've got it taken care of."

    show fang considering with dissolve

    F "Really? But the bus doesn't run that way."

    show fang happy with dissolve

    F "And I know your broke ass can't drive."

    A "There's always fast travel."

    show fang neutral

    F "What?"

    A "So I select my destination on the world map, and then-" #(interrupt)

    show fang angry with dissolve

    F "Knock it off dweeb, I'm being serious."

    show fang neutral with dissolve

    A "Yeah? Well so am I."

    A "In fact, I'm closer than you think."

   # show fang neutral at walking_cycle_aligned:
   #     parallel:
            #Shifts her right so there is room for Anon on screen
   #         easein 2 xcenter .75


    F "Anon what are you-"
    
    show anon grin behind fang: #Doesnt use walking_cycle_aligned transform because Anon is running up behind her
        xcenter -.5 ycenter 0.655
        parallel:
            easein 1 xcenter .4
        parallel:
                easein 0.1 ycenter 0.68
                easein 0.1 ycenter 0.655
                repeat 5

    pause 1
    show fang neutral at walking_cycle_stop

    show shh_neighborhood:
        zoom 2.5
        yalign .7

    A "{sc}BOO!{w=.3}{nw}"

    F "{sc}Aaaa{nw}"

    show fang shocked:
        parallel:
            easein .2 yalign 0.5
            easein .2 yalign 0.1
        parallel:
            easein .2 xcenter .74
            easein .2 xcenter .76
            easein .2 xcenter .75

    show fang shocked flip

    F "Aaaa{fast}h!!!"
    
    pause .5

    show anon grin with dissolve

    show fang angry flip with dissolve

    show fang angry flip:
        easein .25 xcenter .6
        easein .25 xcenter .75

    
    play sound "audio/effects/slapstickPunch.ogg"

    show anon fear:
        easein .25 xcenter .35
        easein .25 xcenter .4

    pause 0.5

    show anon neutral

    F "Asshole! What are you doing here?"

    show anon shrug with dissolve

    A "Heading to Reed's,{w=.25} thought you might like some company."

    show fang considering with dissolve #eye roll ***

    pause .3

    show fang neutral with dissolve
    show anon neutral with dissolve

    #show fang neutral:
    #    parallel:
    #        easein 2 xcenter .65
    #    parallel:
    #        walking_cycle_aligned
    
    #show anon neutral:
    #    parallel:
    #        easein 2 xcenter .35
    #    parallel:
    #        walking_cycle_aligned
    show fang neutral at walking_cycle_aligned
    show anon neutral at walking_cycle_aligned

    show shh_neighborhood :
        linear 3 xpan 360

    pause 3 #Transition from stopping to scrolling again may need slight tweaking ***

    show shh_neighborhood :
        parallel:
            xpan 0
            linear 40 xpan 360
            repeat

    F "Don't tell me you walked all this way just for a bit."

    A "Of course not."

  #  show fang neutral at walking_cycle_stop

  #  show anon neutral at walking_cycle_stop

    #Stop panning background
  #  show shh_neighborhood:
  #      zoom 2.5
  #      yalign .7

    pause 0.5

    pause 1

    show anon happy with dissolve

    A "I took the bus."

    pause 1
    
    show fang hiding with dissolve

   # show fang hiding:
   #     parallel:
   #         easein .15 xcenter .64
   #         easein .15 xcenter .65
   #         repeat 7

    pause 0.5

    F "U{w=.1}G{w=.1}G{w=.1}G{w=.1}G{w=.1}G{w=.1}G{w=.1}G{w=.1}G{w=.1}G{w=.1}G{w=.1}H"

    show anon shrug with dissolve

    A "Sorry, I didn't think you'd scare that easily."

    show anon neutral with dissolve

    show fang neutral with dissolve

    A "Something bothering you?"

    show fang sad with dissolve

    F "No, not exactly..."

    A "Whats up?"

    F "I just{cps=*0.5}..."

    F "I'm not really sure."
   
    show fang sad with dissolve

    pause 1

    F "Maybe it's just how quiet it is."
    
    F "I mean you're the first person I've seen since I left..."

    A "Well yeah, it's a weekday."

    show anon shrug with dissolve

    A "Most people have jobs."

    show anon neutral with dissolve

    F "..."

    A "And besides, this place is always like this."

    show anon shrug with dissolve
    
    A "You couldn't find a more boring slice of suburban America if you tried."

    show anon neutral with dissolve

    show fang neutral with dissolve

    F "Yeah, I guess you're right."
    
    A "You want action, then come to my place and spend an afternoon on the balcony."

    A "Shit's like you're own personal episode of COPS."

    show fang happy with dissolve
    
    F "Like when they met that guy who filled his house with snakes?"

    show anon sad with dissolve

    A "You'd be surprised."

    show anon neutral with dissolve

    F "Heh."
    
    F "Race you the rest of the way!"

    show fang very happy:
        easein .2 ycenter 0.5
        easein .2 ycenter 0.655

    pause .5

    #Fang runs off stage right
    show fang happy: 
        parallel:
            easein 1 xcenter 1.5
        parallel:
                easein 0.1 yalign .075
                easein 0.1 yalign .09
                repeat 5

    pause 1

    show anon ohshit

    A "Hey, wait up!"

    #Anon runs off stage right
    show anon ohshit: 
        parallel:
            easein 1 xcenter 1.5
        parallel:
                easein 0.1 yalign .075
                easein 0.1 yalign .09
                repeat 5

    scene black with Dissolve(1)
    pause 1
    hide fang
    hide anon

    scene shh_sidewalk2

    show fang happy:
        xcenter 0.46 ycenter 0.6 zoom 0.8
        easein 2.5 zoom 0.1 ycenter 0.5

    F "Last one there pays for drinks!{w=1}{nw}"

    hide fang with dissolve
    
    show anon pissed:
        xcenter 0.46 ycenter 0.6 zoom 0.8
        easein 2.0 zoom 0.1 ycenter 0.5

    A "No fair! You got a headstart!{w=1}{nw}"

    hide anon with dissolve

    pause 0.5

    F "Less whining, more running!"

    A "*grumble*"

    stop music fadeout 1.0

    scene shh_sidewalk3 with Dissolve(2)

    pause 1

    scene black with Dissolve(3)

    pause 2

    play music "audio/OST/Fuck You I Like This Chick.ogg" fadein 1.0
    scene shh_reedHouse with Dissolve(1)

    pause 2

    show fang very happy:
        xcenter -.5 ycenter 0.655
        parallel:
            easein 1.4 xcenter 0.3
        parallel:
                easein 0.1 ycenter .75
                easein 0.1 ycenter .655
                repeat 7
        easein 0.1 ycenter 0.655
    
    F "I win!"

    pause .5

    show fang happy

    pause 1
    show reed neutral flip:
        xcenter 1.5 ycenter 0.655
        easein 2 xcenter 0.7

    Re "Whatcha win?"

    F "Twenty kilos."

    show reed happy flip

    Re "No shit, gonna share?"

    F "Already snorted."

    show reed neutral flip

    show trish smile flip:
        xcenter 1.5 ycenter 0.655
        easein 2 xcenter 0.8

    pause 0.5

    T "Morning Fang."

    F "Oh hey Trish! When did you get here?"

    show trish neutral flip with dissolve

    T "I've been here all day, waiting on you."

    show trish considering flip with dissolve

    T "Some of us don't have the luxury of sleeping to noon."

    show trish neutral flip with dissolve

    pause 0.5

    show fang considering   #Eye roll. Might need work
    pause 0.5
    show fang happy with dissolve

    F "Well great, that's everyone then."

    show reed explanatory flip

    Re "What about Anon?"

    show reed neutral flip

    F "Give it a minute."

    pause 2

    show anon concerned:
        xcenter -.15 ycenter 0.655
        parallel: #horizontal movement
            easeout 1 xcenter -0.05
            pause 1
            easeout 1 xcenter 0
            pause 1
            easeout 1 xcenter 0.05
            pause 1
            easeout 1 xcenter 0.1
            pause 1
            easeout 1 xcenter 0.15
            pause 1
            easeout 1 xcenter 0.2
        parallel: #vertical movement
            easein 1 ycenter 0.7
            easeout 1 ycenter 0.655
            repeat 6

    show fang surprised flip:
        pause 4
        ease 3 xcenter .5

    show reed shocked flip:
        pause 5
        ease 2 xcenter 0.75

    A "{i}Huff...{w=2} Huff...{w=2} Ughhh...{/i}"

    show anon sad with dissolve

    show reed explanatory flip

    Re "You ok bro?"

    show reed neutral flip

    A "{i}No...{/i}"

    show trish smug flip

    T "Thought skinnies were supposed to be great runners."

    show fang neutral flip with Dissolve(1)
    
    show trish neutral flip

    F "For real, and it was only like a mile, don't be such a baby."

    A "{i}I never had the makings of a varsity athlete...{/i}"

    show fang neutral flip:
        easein 1 xcenter 0.45
    
    pause 0.5

    show fang neutral

    pause 0.5 

    show reed explanatory flip

    Re "Y'all ready to rip?"

    play sound "audio/effects/anonGardenFall.ogg"
    hide anon concerned with easeoutbottom
    
    
    show fang surprised

    pause 1

    show reed happy flip

    Re "I'll take that as a yes!"

    # As we fade to black Fang moves down to "pick up" anon and he rises back up with her as all three move off the right side
    show fang surprised flip
     
    stop music fadeout 1.0
    scene black with Dissolve(2)
    pause 2

    play music SHH + "audio/music/reed van.mp3" fadein 2.0

    hide fang
    hide anon
    hide trish
    hide reed

    # Add video background footage
    camera:
        linear 0.1 ycenter 0.49
        linear 0.1 ycenter 0.50
        pause 4
        linear 0.1 ycenter 0.495
        linear 0.1 ycenter 0.50
        pause 6.5
        linear 0.1 ycenter 0.505
        linear 0.1 ycenter 0.50
        pause 3.5
        linear 0.1 ycenter 0.51
        linear 0.1 ycenter 0.50
        pause 5
        repeat
   
    scene shh_suburbRoad
    show shh_reedVan
    show anon shh vanNeutral behind fang,reed,trish
    show fang shh vanSmile
    show reed shh vanSmile
    show trish shh lookLeft
    with Dissolve (2)
    play ambient SHH + "audio/sfx/inside car noise.mp3" fadein 2.0 volume 0.5
    show reed shh vanSpeaking

    Re "So first I gotta stop by a place downtown and meet a friend about some music equipment."

    Re "But other than that we have the whole day for whatever. What's the move muchachos?"
    
    show shh_reedVan
    show reed shh vanSmile
    show fang shh vanSpeaking

    F "Depends on what we want to do tonight."

    show fang shh vanSmile
    show anon shh vanSpeaking 
    show trish shh lookRight
    
    A "Rager at Fang's?"

    show anon shh vanNeutral
    show fang shh vanSpeaking

    F "Sure, if you'll break the news to Dad."
    
    show trish shh lookLeft
    show anon shh vanSad #keep this one
    show fang shh vanSmile

    A "..."

    show fang shh vanSpeaking

    F "Yeah that's what I thought."

    # Around here we will see car will turn onto the road behind them and start to follow about a length behind. 
    # It'll be apart of a video file playing in the background layer since the start
    scene shh_suburbRoadCar
    show shh_reedVan 
    show anon shh vanNeutral
    show fang shh vanSmile
    show reed shh vanSpeaking
    show trish shh lookRight
    with Dissolve(1)
    Re "We don't need to do anything crazy, besides Stell's already gonna be throwing a wild party for Halloween at her boyfriend's new place."

    show reed shh vanSmile
    show fang shh vanSpeaking

    F "Agreed, {w=0.2}let's keep things simple, {w=0.2}go pick up some snacks and watch a movie or something."

    show fang shh vanSmile 
    show reed shh vanSpeaking 

    Re "Sounds good. {w}I'll see if I've got anything special for the occasion."

    Re "Speaking of which, anyone want a hit?"

    show reed shh vanSmile

    "Reed holds out his pipe in hospitality."

    show reed shh vanSpeaking
   # stop music fadeout 3.0
    Re "How bout you Anon?"

    show reed shh vanSmile
    show shh_reedVan
    "To hit or not to hit, that is the question."
    
    show shh_reedVan
    menu:
        

        "{i}Absolutely not{/i}": #Option 1
            show anon shh vanSpeaking

            A "Thanks man, but I don't know what's been in that bowl."

            show anon shh vanNeutral
            show reed shh vanSpeaking

            Re "Anyone else?"

            show reed shh vanSmile
            show trish shh lookLeft
            "..."
            
            pause 0.25

            show reed shh vanSpeaking

            Re "Alright, more for me then."
            show trish shh lookRight
            show reed shh vanSmile
        
        "{i}Absolutely{/i}": #Option 2
            show anon shh vanSpeaking

            A "Fuck it."

            "Anon snatches the pipe and lights up."
            play music SHH + "audio/music/sun_araw.ogg" fadein 1.0
            show anon shh vanNeutral
            show trish shh vanScared
            show fang shh vanSmile 
             
            T "Oh Shit."
             
            show trish shh lookRight
            show fang shh vanScared

            F "Don't smoke that retard!"

            "Anon blows out a thick cloud into the front row."

            show anon shh vanSpeaking

            A "Too late."

            show anon shh vanNeutral 

            pause 2

            show anon shh vanSad with Dissolve(1)

            A "Oh damn, this isn't weed..."

            pause 1

            play sound "audio/effects/anonDumbassFall.ogg"

            hide anon with dissolve

            F "Reed what did you pack in that!?"

            show reed shh vanSpeaking

            Re "Relax."

            Re "It's just salvia."

            show reed shh vanSmile

            F "{sc}WHAT!?" # Add text shaking

            F "Reed, stop the car. Where's the NARCAN?" 

            show reed shh vanSpeaking

            Re "Calm down amigo, it's not that serious. You can't OD on Psyches."

            show reed shh vanNeutral

            Re "{cps=20}{size=*.5}I don't think anyway...{/size}" 
            
            camera:
                ycenter 0.50
            scene shh_trippin with dissolve

            Re "How we doing back there?"

            pause 1

            F "God dammit Anon, say something!"

            scene Salvia with dissolve

            camera:
                ycenter 0.5
                linear 0.5 matrixcolor HueMatrix(60)
                linear 0.5 matrixcolor HueMatrix(120)
                linear 0.5 matrixcolor HueMatrix(180)
                linear 0.5 matrixcolor HueMatrix(240)
                linear 0.5 matrixcolor HueMatrix(300)
                linear 0.5 matrixcolor HueMatrix(360)
                repeat
            
            pause 2

            A "{wave=nSalvia_Text}Whrmmuhwhssgon{/wave}"

            Re "See? He's fine. Give him a few minutes and he'll snap out of it."
            camera:
                linear 0.5 matrixcolor HueMatrix(0) 

            scene black with dissolve
            
            $ quick_menu = False
            stop music fadeout 0.1
            $ renpy.movie_cutscene("mods/Snoothouse of Horror/assets/images/bg/tv_scene/Timecard1.webm")
           
            scene shh_trippin2      
            
            pause 1.0

            F "Reed he looks like he's gonna be sick."
            
            Re "Annnnnnnny minute now."

            scene black with dissolve
            $ renpy.movie_cutscene("mods/Snoothouse of Horror/assets/images/bg/tv_scene/Timecard2.webm")

            scene shh_suburbRoadCar
            play music SHH + "audio/music/reed van.mp3" fadein 1.0
            
            show shh_reedVan
            show fang shh vanSmile
            show reed shh vanSmile 
            show trish shh lookLeft
            with Fade (0.5,0.5,0.5)

            pause 2
            $ quick_menu = True
            A "{i}Ughhhhh....{/i}"
            
            pause 1
            show shh_reedVan 
            show anon shh vanSad behind fang with Dissolve(2) 

            pause 1

            show reed shh vanSpeaking
            Re "There he is! Have a good trip bud?"

            show reed shh vanSmile
            #show anon shh vanSpeaking
            A "What's going on? What's life? Are we even real?"

            show anon shh vanSad
            show reed shh vanSpeaking

            Re "Who can say? How do you feel?"

            show reed shh vanSmile
            #show anon shh vanSpeaking

            A "Like a windows 95 PC that just got force restarted. {w}That was fucking crazy. Can't say I'll be doing that again."

            show anon shh vanSad
            show fang shh vanSpeaking
            show trish shh lookRight
            
            F "So what have we learned today?"

            show fang shh vanSmile
            show trish shh lookLeft

            T "Anon's a total idiot."

            T "Though some of us knew that already."

            show trish shh lookRight
            show anon shh vanSad

            A "{i}Fuck off trigger.{/i}"
            
            show fang shh vanSmile
            show anon shh vanNeutral
            show trish shh vanSpeaking
            with vpunch
            T "{b}{size=*1.5}WHAT DID YOU SAY!?{/b}{/size}"

            show reed shh vanNeutral

            Re "{b}HEY!{/b} None of that in here ok?!"
            
            show fang shh vanSmile
            pause 1
            show anon shh vanSad
            show trish shh lookRight
            with dissolve
            "Anon and Trish exchange quick glances of mutual distaste, silently agreeing to continue their feud at a later time."

            "After a few minutes, tensions fall back to normal and discussion resumes."
    
    camera:
        linear 0.1 ycenter 0.49
        linear 0.1 ycenter 0.50
        pause 4
        linear 0.1 ycenter 0.495
        linear 0.1 ycenter 0.50
        pause 6.5
        linear 0.1 ycenter 0.505
        linear 0.1 ycenter 0.50
        pause 3.5
        linear 0.1 ycenter 0.51
        linear 0.1 ycenter 0.50
        pause 5
        repeat
        
    pause 2
    play ambient SHH + "audio/sfx/inside car noise.mp3" fadeout 1.0
    show trish shh lookLeft

    T "Well, I'm fine with whatever you guys want to do today, but I'm gonna need you to drop me off at my place in a few hours."
    
    show shh_reedVan
    show trish shh lookRight
    show fang shh vanSpeaking

    F "Aw, why?"

    show fang shh vanSmile
    show trish shh lookLeft

    T "My siblings. School lets out at 3, so I've gotta get home before them and make sure nobody burns down the complex."
    show shh_reedVan
    show trish shh lookRight
    show reed shh vanSpeaking

    Re "You need help with anything?"

    show reed shh vanSmile
    show trish shh lookLeft

    T "No, I can manage them just fine on my own."

    T "You guys have fun, and I'll be over after my mom gets off work."
    
    show trish shh lookRight
    show anon shh vanSpeaking

    A "Well I for one, appreciate your sacrifice to prevent the triggocalypse."

    A "We'll be sure to dedicate a plaque in your memory."

    show anon shh vanNeutral
    show trish shh lookLeft

    T "And I'll make one when we donate you to the zoo."

    show trish shh lookRight
    show fang shh vanSpeaking
    
    F "Alright you two, knock it off."
     
    show reed shh vanSmile    
    
    F "Besides, I still need him, he owes us a case."

    show fang shh vanSmile
    show anon shh vanSpeaking

    A "I'm not paying for shit."

    show anon shh vanNeutral
    show reed shh vanSpeaking

    Re "S'cool Anon. I got it covered."

    Re "I met this guy who runs a bodega down on the west side."

    Re "He's got the good stuff and won't card me for it."

    show reed shh vanSmile
    show anon shh vanSpeaking
    show trish shh lookLeft
    
    A "Oh fuck yeah."

    show anon shh vanNeutral
    show fang shh vanSpeaking

    F "Duuude, we should get some stuff to mix drinks with!"
    
    show trish shh lookRight
    show fang shh vanSmile
    show reed shh vanSpeaking

    Re "I'm down for that."

    Re "Actually, I've been working on a recipe, you guys should try it and tell me what you think!"

    show reed shh vanSmile
    show anon shh vanSpeaking

    A "What's in it?"
    
    show shh_reedVan
    show anon shh vanNeutral
    show reed shh vanSpeaking

    Re "Ok, so you start with some Everclear."

    Re "Then add some kool-aid powder. Dealer's choice."
    
    show shh_reedVan
    
    Re "Then top it off with mountain dew, "

    extend "and then stir in a full can of Bang."

    scene shh_suburbRoad

    show shh_reedVan
    show anon shh vanNeutral
    show fang shh vanSmile
    show reed shh vanSpeaking 
    show trish shh lookLeft
    with Dissolve(1)
    
    Re "I call it the Tsar Bomba, what do you think?"

    show reed shh vanSmile
    show anon shh vanSpeaking

    A "Well, it certainly sounds radioactive."

    show anon shh vanNeutral
    show fang shh vanSpeaking

    F "Yeah that's fucking vile man."

    show anon shh vanNeutral
    show reed shh vanSpeaking
    show fang shh vanSmile
    
    Re "Trish?"

    show reed shh vanSmile
    show trish shh lookRight

    T "Sorry Reed, but I don't have health insurance."
    
    show fang shh vanSmile
    show trish shh lookLeft
    show reed shh vanSpeaking

    Re "Meh, a true artist is never appreciated in their time."

    show reed shh vanSmile
    show anon shh vanSpeaking

    A "I learned to make a half-decent martini at Moe's. We'll just see what we have to work with."
    
    camera:
        ycenter 0.5
    show shh_police behind anon, shh_reedVan:
        blend "add" blur 10.0 alpha 0.5 xzoom 1.0 zoom 1.0
        crop (0,0,960,1080) xcenter 0.25 
        linear 0.5 alpha 0.0
        crop (960,0,960,1080) xcenter 0.75 alpha 0.5
        linear 0.5 alpha 0.0
        crop (0,0,960,1080) xcenter 0.75 alpha 0.5
        linear 0.5 alpha 0.0
        crop (960,0,960,1080) xcenter 0.25 alpha 0.5
        linear 0.5 alpha 0.0    
        repeat
    
    show fang shh vanSmile
    show reed shh vanSmile
    show anon shh vanSad
    pause 1.5
   # show anon shh vanSpeaking

    A "Did someone have an accident?"

    show anon shh vanSad
    show trish shh vanScared

    T "Fang I think that's your dad over there."
    # show fang shh vanSpeaking
    # show reed shh vanSpeaking
    
    show fang shh vanScared
    show reed shh vanScared
    SHH_FR "Oh Shit."
    
    "Reed scrambles for an aerosol can in his glove compartment, and begins desperately trying to wipe out the smell of skunk." 
    play sound SHH + "audio/sfx/spray.ogg"
    
    F "We don't have time for that."

    F "Just pull over and I'll handle it."

    # BG video is paused. 
    show fang shh vanNeutral
    stop ambient fadeout 0.5
    scene black with Dissolve(1)
    play sound SHH + "audio/sfx/car door.mp3"

    pause 1
    hide trish
    hide reed
    hide anon
    hide fang
    
    pause 1
   
    play music SHH + "audio/music/Crime scene.mp3" fadein 1.0 
    scene shh_crimeScene  
    show fangdad neutral:
        xcenter .3 ycenter 0.655
        block:
            xzoom -1
            pause 0.75
            xzoom 1
            pause 0.75
            repeat 3
    with Dissolve(1)

    pause 3

    show fang neutral flip:
        xcenter .7 ycenter 0.655
    with easeinright
 
    pause 1

    show fangdad shh shocked

    SHH_Ri "{sc}Lucy!?{/sc} What are you doing here?" #Maybe add slight text shake to "Lucy!?" with a small wait between it and the next sentence?

    F "Me and the guys were driving by. What's going on? I didn't think you responded to calls anymore?"

    show fangdad neutral

    SHH_Ri "I don't. Just passed by on my commute and thought it prudent to see what the fuss was about."

    F "Was there a break in?"

    SHH_Ri "Mhm. And they found the night clerk's body stuffed into a supply closet."

    show fang shocked flip

    F "Oh God."

    SHH_Ri "Shouldn't say too much, but there's something about it that just doesn't sit right with me."

    show fang neutral flip

    F "What do you mean?"

    SHH_Ri "There isn't much of a mess to speak of, which wouldn't be unusual for a situation like this."

    SHH_Ri "Except that every speck of cash is still present and accounted for, same for all the other valuables."

    SHH_Ri "The only things the owner is missing are some camping and cooking tools."

    SHH_Ri "And a cheap Halloween mask. But who knows what's related."  #This line can be changed to fit whatever design we use.

    F "Yeah that's oddly specific. What would someone want any of that for?"

    SHH_Ri "Not sure. At first I thought it was probably just some punks or a homeless fella,"

    SHH_Ri "Maybe there was an accident during an altercation and they panicked. But something about this doesn't add up."

    SHH_Ri "We discovered the security cam was offline for hours before the call was made, and no one can tell me why. So there must be more to it than we know."

    show fangdad unimpressed

    SHH_Ri "I hate this damn holiday. Just an excuse for people to act up and give us more work to do. We've barely got enough men to spare as is."

    show fangdad neutral with dissolve

    SHH_Ri "Anyway, You kids stay out of trouble ya hear?"

    F "We will."

    show fang considering with dissolve

    F "Actually since I've got you here, is it alright if I bring the guys over tonight?"

    show fangdad unimpressed

    SHH_Ri "Hmmm."

    show fangdad neutral

    SHH_Ri "Guess it couldn't hurt. I certainly don't like the idea of you being all alone over there."

    SHH_Ri "Just don't do anything your mother wouldn't approve of."

    SHH_Ri "And if I call to check in, I expect you to pick up by the second ring, understood?"

    F "Yes sir."

    SHH_Ri "Good, then get out of here. Media will be here any minute, and I don't want any civilians thinking it's ok to loiter."

    pause 0.5

    show fang neutral

    show fangdad neutral flip:
        parallel:
            block:
                xzoom -1
                pause 0.75
                xzoom 1
                pause 0.75
                repeat 3
    
    pause 0.5

    hide fang with easeoutright

    scene black with Dissolve(1)

    hide fangdad
    stop music fadeout 1.0
    # We fade to black, then fade to the van with fang missing, then play a car door open/slam sound and she fades back in.
    pause 1
    play sound SHH + "audio/sfx/car door.mp3"
    camera:
        matrixcolor TintMatrix("#fce6ca") #make it looks like evening came (so the time skip for the night seem more smooth)
    scene shh_cityRoad
    show shh_reedVan
    show anon shh vanNeutral
    show reed shh vanSmile
    show trish shh lookLeft
    show fang shh vanSmile
    with Dissolve (2)
    play music SHH + "audio/music/reed van.mp3" fadein 1.0
    
    pause 1

    show trish shh lookRight
    T "So what was that all about?"

    show trish shh lookLeft
    show fang shh vanSpeaking

    F "Just some shoplifters."

    F "More importantly, we're in the clear for tonight."

    show fang shh vanSmile
    show reed shh vanSpeaking
    Re "Alright! Let's get this party started!"

    show reed shh vanSmile

    play sound SHH + "audio/sfx/Car Start Sound.mp3"

    stop music fadeout 1.0
   
    scene black with Dissolve(1)
    camera:
        matrixcolor TintMatrix('#fff')
    stop sound fadeout 2.0

    pause 2
    
    play ambient1 "audio/effects/nightLoop.ogg" fadein 1.0
    scene home fang outside night with Dissolve (2)

    queue sound SHH + "audio/sfx/car door.mp3"

    show reed neutral:
        xcenter 1.25 ycenter 0.655 matrixcolor BrightnessMatrix(-0.5) xzoom -1.0
        easein 2 xcenter 0.2

    pause 1

    show fang neutral:
        xcenter 1.25 ycenter 0.655 matrixcolor BrightnessMatrix(-0.5) xzoom -1.0
        easein 2 xcenter 0.45
    
    pause 2

    show fang neutral:
        xzoom 1.0
    with dissolve 
    
    pause 0.5
    
    show reed neutral:
        xzoom 1.0
    with dissolve
    
    pause 0.5
    
    show reed explanatory
    
    Re "You good man?"
    
    show reed neutral with dissolve

    A "{cps=*0.5}Yeah,{nw}"
    
    play sound SHH + "audio/sfx/glass_clink.ogg" 

    show anon concerned flip:
        xcenter 1.15 yalign 0.1 yoffset 108  matrixcolor BrightnessMatrix(-0.5)

        easeout 1 xcenter 1.1
        pause .75
        easeout 1 xcenter .95
        pause .75
        easeout 1 xcenter .9
        pause .75
        easeout 1 xcenter .8

        # Wanted to have him wobble a little as he comes to a stop
        pause .5
        easein .5 xcenter .82
        easein .5 xcenter .78
        easein .5 xcenter .8


    A "Yeah,{fast} I got it." 

    F "Well don't drop it dweeb, that shit was expensive."

    A "{size=*0.5}You could help you know..." 

    # The sprites all move one by one to the approximate entrance before fading out. Anon of course takes the longest. Then we fade to black.
   
    jump shh_slasher_2
    
    
    
    
