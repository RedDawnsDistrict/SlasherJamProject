label dw_slasher_1:
    #Council here, my general rule of thumb is have dissolve for most facial expression changes and just flat cuts between body movements. 
    #Sometimes I switch it up but thats just how I do it

    # *** indicates parts that I think need a final level of polish I'm having trouble achieving.

    # I don't really have a good sense of what music should go where so I'm leaving that up to either of you
    #Fade in from black at the front of Fang's house, morning. Door opens and shut sound plays and fang/neutral fades in somewhere around the center.

    
    scene home fang outside with Dissolve(1)
    
    
    play sound DW + "audio/sfx/door creeking.mp3"
    pause 0.5
    #play door sfx, wait .5, show Fang
    
    show fang very happy with dissolve:
        xcenter 0.5 yalign 0.1 yoffset 108
     
    play music DW + "audio/music/sh3.ogg"
    
    F "{cps=20} YAAAAAAAAAAAAAAAAAAWN {/cps}" #Maybe add side to side shake with this?
    
    show fang happy
    F "(My body moves on instinct as it stretches out, eyes squinting against the light of the morning sun as its blinding light welcomes me back to the world of the living.)"

    F "(A bright blue sky overlooks our tranquil suburban paradise, enveloped by the low hum of distant traffic and some boomer mowing his lawn a couple blocks down.)"

    F "(The sight of everyone's perfect little lives ticking along used to make me sick,)"

    show fang happy with dissolve

    F "(But I think I'm starting to come around.)"

    F "(A stiff breeze blows through, {nw})"
    
    show fang sad:
        easein .2 yalign 0.2
        easein .2 yalign 0.1
    F "(A stiff breeze blows through, {fast}and I'm quickly snapped back to reality.)"
    
    show fang neutral with Dissolve (.25)

    F "(Guess that's it for summer.)"

    show fang neutral flip with dissolve 
    F "(I can't be bothered to go back in for a coat, so I suck it up and begin the distant walk to Reed's place.)"
    show fang neutral with dissolve:
        pause 1
        parallel:
            easein 3 xcenter 1.5
        parallel:
            block:
                easein 0.15 yalign .075
                easein 0.15 yalign .1
                repeat 10


    scene black with Dissolve(1)
    pause 2
    hide fang

    # Moving background
    scene dw_neighborhood  with Dissolve(1):
        zoom 2.5
        yalign .7
        parallel:
            xpan 0
            linear 15 xpan 360
            repeat

    show fang neutral at walking_cycle_aligned:
        xcenter -.5 yoffset 108
        parallel:
            linear 3.0 xcenter 0.5

    play sound DW + "audio/sfx/phone_buzz.mp3"
    pause 5 # however long the effect plays for + 3 seconds

    A "Frank's crematory,{w=.5} you kill'em {w=.5}we grill'em!"

    # switch fang to smile sprite with a quick eye roll back
    show fang considering with Dissolve (1.5)
    pause .5
    show fang happy with dissolve

    F "Hey Anon, you ready for tonight?"

    A "Of course! You sure your parent's don't mind?"

    show fang neutral with dissolve

    F "Nah, Mom and Nas are out doing campus tours for the weekend."

    F "And Dad might as well be welded to his desk."

    show fang happy with dissolve

    F "So we've got the whole place to ourselves, at least for tonight."

    A "Exciting, so what's the plan?"

    show fang neutral with dissolve

    F "I don't know, haven't thought that far ahead yet."

    show fang happy with dissolve

    F "But I'm looking forward to a little quality time somewhere that doesn't smell like a crack den."

    A "Heh. Can't argue with that."

    F "So how are you getting over to Reed's? We can pick you up if you want."

    A "Don't worry about me, I've got it taken care of."

    show fang considering with dissolve

    F "Really? But the bus doesn't run that way."

    show fang happy with dissolve

    F "And I know your broke ass can't drive."

    A "There's always fast travel."

    show fang neutral

    F "What?"

    A "So I select my destination on the world map, and then-" #(interrupt)

    show fang sad with dissolve

    F "Knock it off dweeb, I'm being serious."

    A "Yeah? Well so am I."

    A "In fact, I'm closer than you think."

    show fang neutral with dissolve

    show fang neutral at walking_cycle_aligned:
        parallel:
            #Shifts her right so there is room for Anon on screen
            easein 2 xcenter .75


    F "Anon what are you-"
    
    show anon grin behind fang: #Doesnt use walking_cycle_aligned transform because Anon is running up behind her
        xcenter -.5 yalign 0.1 yoffset 108
        parallel:
            easein 1 xcenter .5
        parallel:
                easein 0.1 yalign .075
                easein 0.1 yalign .09
                repeat 5

    pause 1
    #Fang stop walking
    show fang neutral at walking_cycle_stop

    #Stop panning background
    show dw_neighborhood :
        zoom 2.5
        yalign .7

    show anon shocked behind fang with dissolve
    A "BOO!" #Add shaking text effect

    F "Aaaa{nw}" #Add shaking text effect

    #Fang jumping and flipping to face Anon
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

    F "Asshole! What are you doing here?"

    show fang angry flip:
        easein .25 xcenter .6
        # Add punch sfx here
        easein .25 xcenter .75
    
    play sound "audio/effects/slapstickPunch.ogg"
    
    pause 1

    show anon shrug with dissolve

    A "Heading to Reed's, thought you might like some company."

    show fang considering with dissolve #eye roll ***

    pause .5

    show fang neutral with dissolve
    show anon neutral with dissolve

    #Both start walking and bg starts to move again (shifts them both to be equidistant from the center)

    show fang neutral:
        parallel:
            easein 2 xcenter .65
        parallel:
            walking_cycle_aligned
    
    show anon neutral:
        parallel:
            easein 2 xcenter .35
        parallel:
            walking_cycle_aligned


    show dw_neighborhood :
        linear 3 xpan 360

    pause 3 #Transition from stopping to scrolling again may need slight tweaking ***

    show dw_neighborhood :
        parallel:
            xpan 0
            linear 15 xpan 360
            repeat

    F "Don't tell me you walked all this way just for a bit."

    A "Of course not."

    show fang neutral at walking_cycle_stop

    show anon neutral at walking_cycle_stop

    #Stop panning background
    show dw_neighborhood:
        zoom 2.5
        yalign .7

    pause 0.5

    show fang neutral flip 

    pause 1.5

    show anon happy

    A "I took the bus."

    F "{w=1}.{w=1}.{w=1}." # Thought this helps with the comedic timing

    F "{cps=5}UGG{nw}{/cps}"

    show fang hiding flip:
        parallel:
            easein .15 xcenter .64
            easein .15 xcenter .65
            repeat 7

    F "{cps=5}UGG{fast}GGGGGGGGH{/cps}"

    show anon sad with dissolve

    A "Sorry, I didn't think you'd scare that easily."

    show anon neutral with dissolve

    show fang neutral flip with dissolve

    A "Something bothering you?"

    show fang sad flip with dissolve

    F "No, not exactly..."

    A "Whats up?"

    F "I just,"

    F "..."

    F "I'm not really sure."
    stop music fadeout 5.0
    show fang sad:
        pause 0.5
        xzoom -1
        pause 0.5
        xzoom 1
        pause 0.5
        xzoom -1

    pause 2

    F "Maybe it's just how quiet it is."

    F "I mean you're the first person I've seen since I left..."

    A "Well yeah, it's a weekday."

    show anon shrug

    A "Most people have jobs"

    show anon neutral 

    F "..."

    A "And besides, this place is always like this."

    show anon shrug
    
    A "You couldn't find a more boring slice of suburban America if you tried."

    show fang happy flip with dissolve

    F "Yeah, I guess you're right."
    
    A "You want action, then come to my place and spend an afternoon on the balcony."

    A "Shit's like you're own personal episode of COPS."

    show fang happy flip with dissolve
    
    F "Like when they met that guy who filled his house with snakes?"

    show anon sad 

    A "You'd be surprised."

    show anon neutral

    F "Heh."
    
    F "Race you the rest of the way!"

    show fang very happy flip:
        easein .2 yalign 0.5
        easein .2 yalign 0.1

    pause .5

    #Fang runs off stage right
    show fang very happy flip: 
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

    #Fade to black
    scene black with Dissolve(1)
    pause 1
    hide fang
    hide anon

    scene dw_sidewalk
    
    show anon grin:
        xcenter 0.5 ycenter 0.5 zoom 0.8
        easein 10.0 zoom 0.0 alpha 0.0 ycenter 0.6
    show fang happy:
        xcenter 0.55 ycenter 0.5 zoom 0.8
        easein 10.0 zoom 0.0 alpha 0.0 ycenter 0.6
    
    
    with Dissolve(1)
        
    F "Last one there pays for drinks!"

    A "No fair! You got a headstart!"

    F "Less whining, more running!"

    A "*grumble*"

    play music DW + "audio/music/sh2.ogg" fadein 1.0
    scene dw_reedHouse with Dissolve(1)

    show fang very happy:
        xcenter -.5 yoffset 108
        parallel:
            easein 1.4 xcenter 0.3
        parallel:
                easein 0.1 yalign .075
                easein 0.1 yalign .09
                repeat 7
        easein 0.1 yalign .1
    
    F "I win!"

    pause .5

    show fang happy

    pause 1
    show reed neutral flip:
        xcenter 1.5 yalign 0.1 yoffset 108
        easein 2 xcenter 0.7

    Re "Whatcha win?"

    F "Twenty kilos."

    show reed happy flip

    Re "No shit, gonna share?"

    F "Already snorted."

    show reed neutral flip

    pause 0.5

    show trish smile flip:
        xcenter 1.5 yalign 0.1 yoffset 108
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
        xcenter -.15 yalign 0.1 yoffset 108
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
            easein 1 yalign 0.12
            easeout 1 yalign 0.1
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

    F "For real, and it was barely half a mile, don't be such a baby."

    A "{i}I never had the makings of a varsity athlete...{/i}"

    show fang neutral flip:
        easein 1 xcenter 0.45
    
    pause 0.5

    show fang neutral

    pause 0.5 

    Re "Y'all ready to rip?"

    play sound "audio/effects/anonGardenFall.ogg"
    hide anon concerned with easeoutbottom
    
    
    show fang surprised

    pause 1

    show reed happy flip

    Re "I'll take that as a yes!"

    # As we fade to black Fang moves down to "pick up" anon and he rises back up with her as all three move off the right side
    show fang surprised flip
     
    #Play the reed van track and fade it out and in as needed. ***

    scene black with Dissolve(2)
    pause 2
    hide fang
    hide anon
    hide trish
    hide reed

    # Add video background footage
    scene dw_suburbRoad
    show dw_reedVan
    show anon dw vanNeutral behind fang,reed,trish
    show fang dw vanNeutral
    show reed dw vanNeutral
    show trish dw vanNeutral
    with Dissolve (2)

    show reed dw vanSpeaking

    Re "So first I gotta stop by a place downtown and meet a friend about some music equipment."

    Re "But other than that we have the whole day for whatever. What's the move muchachos?"

    show reed dw vanNeutral
    show fang dw vanSpeaking

    F "Depends on what we want to do tonight."

    show fang dw vanNeutral
    show anon dw vanSpeaking

    A "Rager at Fang's?"

    show anon dw vanNeutral
    show fang dw vanSpeaking

    F "Sure, if you'll break the news to Dad."

    show anon dw vanSad
    show fang dw vanNeutral

    A "..."

    show fang dw vanSpeaking 

    F "Yeah that's what I thought."

    # Around here we will see car will turn onto the road behind them and start to follow about a length behind. 
    # It'll be apart of a video file playing in the background layer since the start
    scene dw_suburbRoadCar

    show dw_reedVan
    show anon dw vanNeutral 
    show fang dw vanNeutral
    show reed dw vanSpeaking
    show trish dw vanNeutral
    
    Re "We don't need to do anything crazy, besides Stell's already gonna be throwing a wild party for Halloween at her boyfriend's new place."

    show reed dw vanNeutral
    show fang dw vanSpeaking

    F "Agreed, let's keep things simple, go pick up some snacks and watch a movie or something."

    show fang dw vanNeutral
    show reed dw vanSpeaking

    Re "Sounds good. I'll see if I've got anything special for the occasion."

    Re "Speaking of which, anyone want a hit?"

    show reed dw vanSmile

    "Reed holds out his pipe in hospitality."

    show reed dw vanSpeaking
    stop music fadeout 3.0
    Re "How bout you Anon?"

    show reed dw vanSmile
    play music DW + "audio/music/sun_araw.ogg" fadein 1.0
    menu:
        "{i}To hit or not to hit, that is the question.{/i}"

        "{i}Absolutely not{/i}": #Option 1
            show anon dw vanSpeaking

            A "Thanks man, but I don't know what's been in that bowl."

            show anon dw vanNeutral
            show reed dw vanSpeaking

            Re "Anyone else?"

            show reed dw vanNeutral

            "{w=1}.{w=1}.{w=1}."
            
            pause 0.25

            show reed dw vanSpeaking

            Re "Alright, more for me then."

            show reed dw vanSmile
        
        "{i}Absolutely{/i}": #Option 2
            show anon dw vanSpeaking

            A "Fuck it."

            "Anon snatches the pipe and lights up."

            show anon dw vanNeutral
            show trish dw vanSpeaking

            T "Oh Shit."

            show trish dw vanNeutral
            show fang dw vanSpeaking

            F "Don't smoke that retard!"

            show fang dw vanNeutral

            "Anon blows out a thick cloud into the front row."

            show anon dw vanSpeaking

            A "Too late."

            show anon dw vanNeutral 

            pause 2

            show anon dw vanSad with Dissolve(1)

            A "Oh damn, this isn't weed..."

            pause 1

            play sound "audio/effects/anonDumbassFall.ogg"

            hide anon

            scene black with Dissolve(2)
            hide fang
            hide reed
            hide trish

            F "Reed what did you pack in that!?"

            Re "Relax."

            Re "It's just salvia."

            F "{b}WHAT!?{/b}" # Add text shaking

            F "{b}Reed, stop the car. Where's the NARCAN?{/b}" 

            Re "Calm down amigo, it's not that serious. You can't OD on Psyches."

            Re "{cps=20}{size=*.5}I don't think anyway...{/size}" #Make text small and slower wps

            scene dw_trippin with dissolve

            Re "How we doing back there?"

            pause 1

            F "God dammit Anon, say something!"

            # hard cut to Gmod image of the inside of the van from the viewpoint of anon sitting in the back of vehicle, with fang trish and reed models in front. 
            # Fang is looking back at POV(anon) throw some effects and filters in for good measure, and anything else you feel moved to include I trust ya : )

            # Idk what this is referring to ***

            A "Whrmmuhwhssgon"

            Re "See? He's fine. Give him a few minutes and he'll snap out of it."
            scene black with Dissolve(2)

            # hard cut to few minutes later clip 
            # Idk the syntax for this ***

            # hard cut to same anon face cg just now with a thick red filter and maybe a fish eye lens effect, 
            # along with anything you can think of to emphasize how fucked up he is. 
            # If you can find the materials it would also be funny to overlay the top layer with a transparent giygas final form image scroll on the 
            # top layer and it's music from earthbound. Not mandatory though.
            scene dw_trippin
            camera:
                linear 0.5 matrixcolor HueMatrix(60)
                linear 0.5 matrixcolor HueMatrix(120)
                linear 0.5 matrixcolor HueMatrix(180)
                linear 0.5 matrixcolor HueMatrix(240)
                linear 0.5 matrixcolor HueMatrix(300)
                linear 0.5 matrixcolor HueMatrix(360)
                repeat
            
            pause 5

            Re "Annnnnnnny minute now."

            camera:
                linear 0.5 matrixcolor HueMatrix(0)
            
            #hard cut to a little longer than a few minutes later clip, then hard cut back to main van shot
            # Idk the syntax for this ***
            scene black with dissolve #placeholder

            A "{i}Ughhhhh....{/i}"
            scene dw_suburbRoadCar
            show dw_reedVan
            show fang dw vanNeutral
            show reed dw vanNeutral
            show trish dw vanNeutral
            with Dissolve (2)

            pause 1
            show anon dw vanSad with Dissolve(2) # Need to change zorder so he's on the right layer
            pause 3

            show reed dw vanSpeaking
            Re "There he is! Have a good trip bud?"

            show reed dw vanSmile
            show anon dw vanSpeaking
            A "What's going on? What's life? Are we even real?"

            show anon dw vanNeutral
            show reed dw vanSpeaking

            Re "Who can say? How do you feel?"

            show reed dw vanNeutral
            show anon dw vanSpeaking

            A "Like a windows 92 PC that just got force restarted. That was fucking crazy. Can't say I'll be doing that again."

            show anon dw vanNeutral
            show fang dw vanSpeaking

            F "So what have we learned today?"

            show fang dw vanNeutral
            show trish dw vanSpeaking

            T "Anon's a total idiot."

            T "Though some of us knew that already."

            show trish dw vanNeutral
            show anon dw vanSpeaking

            A "{i}Fuck off trigger.{/i}"

            show anon dw vanNeutral
            show trish dw vanSpeaking

            T "{b}{size=*1.5}WHAT DID YOU SAY!?{/b}{/size}"
            
            show trish dw vanNeutral
            show reed dw vanSpeaking

            Re "{b}HEY!{/b} None of that in here ok?!"

            pause 1
            show anon dw vanSad
            show trish dw vanNeutral

            "Anon and Trish exchange quick glances of mutual distaste, silently agreeing to continue their feud at a later time."

            "After a few minutes, tensions fall back to normal and discussion resumes."
    # back to normal
    pause 2

    show trish dw vanSpeaking

    T "Well, I'm fine with whatever you guys want to do today, but I'm gonna need you to drop me off at my place in a few hours."

    show trish dw vanNeutral
    show fang dw vanSpeaking

    F "Aw, why?"

    show fang dw vanNeutral
    show trish dw vanSpeaking

    T "My siblings. School lets out at 3, so I've gotta get home before them and make sure nobody burns down the complex."

    show trish dw vanNeutral
    show reed dw vanSpeaking

    Re "You need help with anything?"

    show reed dw vanNeutral
    show trish dw vanSpeaking

    T "No, I can manage them just fine on my own."

    T "You guys have fun, and I'll be over after my mom gets off work."

    show trish dw vanNeutral
    show anon dw vanSpeaking

    A "Well I for one, appreciate your sacrifice to prevent the triggocalypse."

    A "We'll be sure to dedicate a plaque in your memory."

    show anon dw vanNeutral
    show trish dw vanSpeaking

    T "And I'll make one when we donate you to the zoo."

    show trish dw vanNeutral
    show fang dw vanSpeaking

    F "Alright you two, knock it off."

    F "Besides, I still need him, he owes us a case."

    show fang dw vanNeutral
    show anon dw vanSpeaking

    A "I'm not paying for shit."

    show anon dw vanNeutral
    show reed dw vanSpeaking

    Re "S'cool Anon. I got it covered."

    Re "I met this guy who runs a bodega down on the west side."

    Re "He's got the good stuff and won't card me for it."

    show reed dw vanSmile
    show anon dw vanSpeaking

    A "Oh fuck yeah."

    show anon dw vanNeutral
    show fang dw vanSpeaking

    F "Duuude, we should get some stuff to mix drinks with!"

    show fang dw vanNeutral
    show reed dw vanSpeaking

    Re "I'm down for that."

    Re "Actually, I've been working on a recipe, you guys should try it and tell me what you think!"

    show reed dw vanSmile
    show anon dw vanSpeaking

    A "What's in it?"

    show anon dw vanNeutral
    show reed dw vanSpeaking

    Re "Ok, so you start with some Everclear."

    Re "Then add some kool-aid powder. Dealer's choice."

    Re "Then top it off with mountain dew."

    Re "then stir in a full can of Bang."

    # about here the car following them will turn away or pull over/stop
    scene dw_suburbRoad

    show dw_reedVan
    show anon dw vanNeutral 
    show fang dw vanNeutral
    show reed dw vanSpeaking
    show trish dw vanNeutral

    Re "I call it the Tsar Bomba, what do you think?"

    show reed dw vanSmile

    "{w=1}.{w=1}.{w=1}."

    show reed dw vanNeutral
    show anon dw vanSpeaking

    A "Well, it certainly sounds radioactive."

    show anon dw vanNeutral
    show fang dw vanSpeaking

    F "Yeah that's fucking vile man."

    show anon dw vanNeutral
    show reed dw vanSpeaking

    Re "Trish?"

    show reed dw vanNeutral
    show trish dw vanSpeaking

    T "Sorry Reed, but I don't have health insurance."

    show trish dw vanNeutral
    show reed dw vanSpeaking

    Re "Meh, a true artist is never appreciated in their time."

    show reed dw vanNeutral
    show anon dw vanSpeaking

    A "I learned to make a half-decent martini at Moe's. We'll just see what we have to work with."

    # pause the background visuals, and have red and blue lights flash on top of the screen 
    # or outside the windshield depending on the direction facing. Anon switches to frown
    # ***
    
    show anon dw vanSad
    pause 1.5
    show anon dw vanSpeaking

    A "Did someone have an accident?"

    show anon dw vanSad
    show trish dw vanSpeaking

    T "Fang I think that's your dad over there."

    show trish dw vanNeutral
    show fang dw vanSpeaking
    show reed dw vanSpeaking

    # F&Re "Oh Shit!"
    # Couldnt find the syntax for this

    show fang dw vanNeutral
    show reed dw vanNeutral

    "Reed scrambles for an aerosol can in his glove compartment, and begins desperately trying to wipe out the smell of skunk." 
    play sound DW + "audio/sfx/spray.ogg"

    show fang dw vanSpeaking

    F "We don't have time for that!"

    F "Just pull over and I'll handle it."

    # BG video is paused. 
    show fang dw vanNeutral 

    pause 1

    hide fang
    play sound DW + "audio/sfx/car door.mp3"

    scene black with Dissolve(1)
    hide trish
    hide reed
    hide anon

    pause 1
    # Council here, I think it would honestly work better if it fades to black and then we hear the car door open and close. Fang disappearing from the seat all of the
    # sudden looks a bit jarring to me

    # Fang fades from image with a car door open/close sound, fade to black, then fade to a picture of a corner store/crime scene, 
    # might find something that can be edited to look broken into. 
    # Fang enters from one side to face ripley who's on the other and switching the direction he's facing repeatedly. 
    # Both are neutral but ripley switches to shocked when he sees fang. Maybe use the background crowd trick from wani to make it feel more busy?
    
    scene dw_crimeScene  
    show fangdad neutral:
        xcenter .3 yalign 0.1 yoffset 108
        block:
            xzoom -1
            pause 0.75
            xzoom 1
            pause 0.75
            repeat 3
    with Dissolve(1)

    pause 2.25

    show fang neutral flip:
        xcenter .7 yalign 0.1 yoffset 108
    with easeinright
    play music DW + "audio/music/sh1.ogg" fadein 1.0
    pause 1

    show fangdad dw shocked

    DW_Ri "Lucy!? What are you doing here?" #Maybe add slight text shake to "Lucy!?" with a small wait between it and the next sentence?

    F "Me and the guys were driving by. What's going on? I didn't think you responded to calls anymore?"

    show fangdad neutral

    DW_Ri "I don't. Just passed by on my commute and thought it prudent to see what the fuss was about."

    F "Was there a break in?"

    DW_Ri "Mhm. And they found the night clerk's body stuffed into a supply closet."

    show fang shocked flip

    F "Oh God."

    DW_Ri "Shouldn't say too much, but there's something about it that just doesn't sit right with me."

    show fang neutral flip

    F "What do you mean?"

    DW_Ri "There isn't much of a mess to speak of, which wouldn't be unusual for a situation like this."

    DW_Ri "Except that every speck of cash is still present and accounted for, same for all the other valuables."

    DW_Ri "The only things the owner is missing are some camping and cooking tools."

    DW_Ri "And a cheap Halloween mask. But who knows what's related."  #This line can be changed to fit whatever design we use.

    F "Yeah that's oddly specific. What would someone want any of that for?"

    DW_Ri "Not sure. At first I thought it was probably just some punks or a homeless fella,"

    DW_Ri "Maybe there was an accident during an altercation and they panicked. But something about this doesn't add up."

    DW_Ri "We discovered the security cam was offline for hours before the call was made, and no one can tell me why. So there must be more to it than we know."

    show fangdad unimpressed

    DW_Ri "I hate this damn holiday. Just an excuse for people to act up and give us more work to do. We've barely got enough men to spare as is."

    show fangdad neutral with dissolve

    DW_Ri "Anyway, You kids stay out of trouble ya hear?"

    F "We will."

    show fang considering with dissolve

    F "Actually since I've got you here, is it alright if I bring the guys over tonight?"

    show fangdad unimpressed

    DW_Ri "Hmmm."

    show fangdad neutral

    DW_Ri "Guess it couldn't hurt. I certainly don't like the idea of you being all alone over there."

    DW_Ri "Just don't do anything your mother wouldn't approve of."

    DW_Ri "And if I call to check in, I expect you to pick up by the second ring, understood?"

    F "Yes sir."

    DW_Ri "Good, then get out of here. Media will be here any minute, and I don't want any civilians thinking it's ok to loiter."

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

    show dw_reedVan
    show anon dw vanNeutral
    show reed dw vanNeutral
    show trish dw vanNeutral
    with Dissolve (2)

    pause 1

    play sound DW + "audio/sfx/car door.mp3"

    show fang dw vanNeutral with dissolve

    pause 0.5

    show trish dw vanSpeaking
    play music DW + "audio/music/sh2.ogg" fadein 1.0
    T "So what was that all about?"

    show trish dw vanNeutral
    show fang dw vanSpeaking

    F "Just some shoplifters."

    F "More importantly, we're in the clear for tonight."

    show fang dw vanNeutral
    show reed dw vanSpeaking
    stop music fadeout 1.0
    Re "Alright! Let's get this party started!"

    show reed dw vanSmile

    play sound DW + "audio/sfx/Car Start Sound.mp3"

    scene black with Dissolve(1)
    pause 1
    scene home fang outside night with Dissolve (1)

    queue sound DW + "audio/sfx/car door.mp3"

    # This part was giving me way too much trouble for some reason. May need to be redone entirely

    show reed neutral flip:
        xcenter 1.25 yalign 0.1 yoffset 108 matrixcolor BrightnessMatrix(-0.5)
        easein 2 xcenter 0.2

    pause 1

    show fang neutral flip:
        xcenter 1.25 yalign 0.1 yoffset 108 matrixcolor BrightnessMatrix(-0.5)
        easein 2 xcenter 0.45
    
    pause 2

    show fang neutral
    
    pause 0.5 

    #show reed neutral #Idk why he shifts to the side so much when I flip him around so rn this statement is commented out

    pause 2

    Re "You good man?"

    pause 1

    A "{cps=*0.5}Yeah,{nw}"
    
    play sound DW + "audio/sfx/glass_clink.ogg" 

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
   
    jump dw_slasher_2
    
    
    
    