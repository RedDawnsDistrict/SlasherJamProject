label shh_slasher_2:
    
    play music SHH +"audio/music/the_room.ogg" fadein 1.0
    
    scene shh_tv   
    
    show fang neutral:
        ycenter 0.75 xcenter 0.1 matrixcolor BrightnessMatrix(-1.0)
    
    show anon neutral:
        ycenter 0.75 xcenter 0.3 xzoom -1.0 matrixcolor BrightnessMatrix(-1.0)
    
    show reed neutral:
        ycenter 0.95 xcenter 0.8 matrixcolor BrightnessMatrix(-1.0) xzoom -1.0
    
    show shh_couch
    
    with Fade(0.5, 0.5, 0.5, color='#0000')
    
    F "Drinks, {w=0.2}popcorn, {w=0.2}blankets... {w=0.2}is there anything else we want before jumping in?"
    
    A "You guys want to take a wizz before we start?"

    F "Already did. {w=0.2}This stuff goes through you like nobodies business."

    "Reed is sitting on the floor with his laptop."
    
    "He connects it to the screen with an HDMI cord, {w=0.5}{nw}"
    
    show reed:
        ease 0.5 ycenter 0.75 
    
    extend "then fiddles with some settings before the image comes up."
    
    play sound "audio/ui/uiOptionOn.wav"
    
    show shh_nflix behind reed,fang,anon:
        blur 2.0
    
    show fang neutral:
        matrixcolor BrightnessMatrix(-0.5)
    
    show anon neutral:
        matrixcolor BrightnessMatrix(-0.5)
    
    show reed neutral:
        matrixcolor BrightnessMatrix(-0.5)
    
    with dissolve
    
    pause 0.5
    
    Re "So what do you guys want to watch?"
    
    show anon shrug with dissolve:
        xzoom 1.0
    
    A "Something festive, obviously."

    Re "Works for me, {w=0.2}any suggestions?"
    
    menu:
        "{s}Fang{/s} Friday the 13th":
           
           $ shh_cinema = "friday"
           
           A "How about 'Friday the 13th'? {w=0.2}It's a solid classic."
           
           Re "Which one?"
           
           show anon considering with dissolve
           A "Uh, {w=0.2}the first one I guess?"
           
           show fang considering
           F "Isn't that the one with Jason’s mom? {w}That sounds kinda lame."
           
           show anon neutral with dissolve:
               xzoom -1.0
           
           A "Nah, they did a really good job with it and is was a great twist for its time." 
           
           A "The last scene actually got me when I was a kid."
           
           pause 0.5
           show anon considering
           A "Plus, I think the plot works even better if you go into it expecting Jason."
           
           show fang happy  
           F "Alright, we can give it a shot."
           
           show anon neutral with dissolve:
               xzoom 1.0               
           
           extend " Fire it up Reed."
           
           show reed happy with dissolve
           
           Re "Aye aye, captain!"
           
           play sound "audio/ui/uiOptionOn.ogg"
           pause 0.5
           play music SHH +"audio/music/murder_house.ogg" fadein 1.0
           show reed neutral
           show anon neutral
           show fang neutral
           show shh_friday behind anon, reed:
               xcenter 0.517 ycenter 0.447 blur 4.0 alpha 0.95 zoom 1.01
           hide shh_nflix
        
        "Scream":
           
           $ shh_cinema = "scream"
           
           F "How about 'Scream'? {w}Think it's time we settle this debate once and for all."
           
           show anon neutral with dissolve:
               xzoom -1.0
           
           A "Agreed."
           
           Re "Oh? What’s this all about?"
           
           show anon neutral with dissolve:
               xzoom 1.0
           
           A "She seems to think I’m the Stu in this relationship."
           
           pause 1.0
           
           A "I disagree."
           
           pause 0.5
           show fang happy
           F "Care to weigh in Reed?"
           
           show reed considering
           
           Re "{cps=*0.25}Hmmmmm {/cps}{w=0.5}{nw}"
           
           show reed explanatory
           
           extend ", gonna have to side with her on this one. {w}She's more of a Billy than you are."
           
           show reed neutral
           show fang happy:
               xcenter 0.1
               easein 0.5 xcenter 0.2
               ease 0.5 xcenter 0.1
           
           F "HAHA GET FUCKED!"
           
           show anon shrug with dissolve
           A "Aw come on, what makes you say that?"
           
           show reed unimpressed
           
           Re "I just think between the two of you, she's more likely to rope you into something dangerous than you to her."
           
           show anon considering with dissolve
           A "Huh, never thought about it like that before."
           show anon neutral
           F "Just put the damn movie in, {w=0.2}traitor."
           
           show reed happy with dissolve
           Re "Aye aye, captain!"
           
           play sound "audio/ui/uiOptionOn.wav"
           pause 0.5
           play music SHH +"audio/music/murder_house.ogg" fadein 1.0
           show reed neutral
           show shh_scream behind anon, reed:
               xcenter 0.517 ycenter 0.447 blur 4.0 alpha 0.95 zoom 1.01
           hide shh_nflix
           
        "Anon's idea":
            
           $ shh_cinema = "halloween" 
            
           show anon grin with dissolve         
           
           A "I got something."
           
           show anon:
               xcenter 0.3
               easein 1.0 xcenter 0.7
           
           show reed unimpressed:
               ease 0.5 xcenter 0.95
           
           extend " Let me cast to the TV real quick and close your eyes."
           
           play sound "audio/ui/uiClick.wav"
           show shh_yt behind reed, anon:
               blur 2.0
           hide shh_nflix
           
           show fang considering
           F "Oh fuck, here we go."
              
           Re "What is it?"

           A "You'll just have to wait and see."

           A "It’s gonna scare the shit out of you, trust me."
           
           play sound "audio/ui/uiOptionOn.wav"
           pause 0.5
           play music SHH +"audio/music/fnaf.ogg" fadein 1.0
           show shh_scary behind anon, reed:
               xcenter 0.517 ycenter 0.447 blur 4.0 alpha 0.95 zoom 1.01
           hide shh_yt
           show reed neutral:
               xcenter 0.95
               ease 0.5 xcenter 0.8
           show anon:
               ease 1.0 xcenter 0.3
           pause 1.0
           
           
           show fang shocked
           F "The hell is this?!"

           A "HAHAHAHAHAHAHA!"

           A "What did I tell ya?"

           A "This horrifying or what?"
           show fang angry
           F "Goddammit Anon, why do you always pull this shit?"

           F "Reed cut him off please."

           A "You’re no fun."

           Re "I dunno, let’s give it a chance."

           F "Jeez, of course you would like this."

           F "This is why I need to have Trish around, you two drive me nuts."
           
           show fang neutral
           show anon neutral
           A "It’s cool Reed, I got what I wanted already."

           Re "You sure bro?"

           A "Yeah, you can put something normal on now."
           
           show reed happy with dissolve
           Re "Aye aye, captain!"
           
           play sound "audio/ui/uiOptionOn.wav"
           pause 0.5
           play music SHH +"audio/music/murder_house.ogg" fadein 1.0
           show shh_halloween behind anon, reed:
               xcenter 0.517 ycenter 0.447 blur 4.0 alpha 0.95 zoom 1.01
           hide shh_scary
           pause 1.0
           
        "I don't care":
           
           $ shh_cinema = "halloween"
           
           show anon neutral with dissolve
           
           F "I don't really care, just pick something you like."
           
           F "But no shock films, {w=0.2}I hate that stuff."
           
           show fang considering with dissolve
           
           F "{w=0.2}I still can't believe you got me to watch that centipede movie."
           
           pause 1.0
           
           show anon grin with dissolve:
               xzoom -1.0 
           
           A "I still can't believe you watched the second one."
           
           show fang flip off happy
           show anon grin behind fang
           with dissolve
           
           pause 0.5
           
           show anon neutral
           show fang happy
           show reed happy 
           with dissolve
           
           Re "No prob, I’ve got pretty much everything you can ask for."
           
           show anon shrug with dissolve:
               xzoom 1.0
           
           A "I'm pretty indifferent myself. {w=0.2}Surprise us."
           
           show anon neutral with dissolve
           
           Re "Aye aye, captain!"
           
           play sound "audio/ui/uiOptionOn.wav"
           pause 0.5
           play music SHH +"audio/music/murder_house.ogg" fadein 1.0 
           show shh_halloween behind anon, reed: 
               xcenter 0.517 ycenter 0.447 blur 4.0 alpha 0.95 zoom 1.01 
           hide shh_nflix
           show reed neutral
           
    pause 3.0
    
    show reed neutral:
        ease 0.5 ycenter 0.655
    
    Re "Actually before we get in too deep, I'm gonna take a smoke break."
    
    show fang considering
    F "Alright, but do it outside. {w}Dad's like a bloodhound and I don’t want to get in trouble."

    Re "No prob. {w=0.2}Think I'll check on Trish while I'm out."

    A "Want us to pause it for you?"

    Re "Nah, you're good. {w=0.2}I've seen this one before."
    
    show reed neutral with dissolve:
       xzoom 1.0 xcenter 0.75
    
    F "Don't get lost out there."
     
    show reed considering 
     
    Re "Heh, I'll try not to."
    
    show reed happy
    
    extend " Be right back."
    
    show reed:
        xcenter 0.75
        ease 1.5 xcenter 1.2
    
    show anon:
        ease 1.0 matrixcolor BrightnessMatrix(-1.0)
    show fang:    
        ease 1.0 matrixcolor BrightnessMatrix(-1.0)
    pause 2.0
    
    show anon with dissolve:
        xzoom -1.0
    
    A "Hey! Quit hogging all the popcorn!"

    F "I popped it bitch, {w=0.2}deal with it."
    
    play sound SHH +"audio/sfx/popcorn.ogg"
    
    show anon:
        xcenter 0.3
        easein 0.25 xcenter 0.2
        ease 0.25 xcenter 0.3 
        0.5
        repeat
    
    show fang:
        xcenter 0.1
        0.5
        easein 0.25 xcenter 0.2
        ease 0.25 xcenter 0.1 
        repeat
    
    pause 0.5
    
    stop music fadeout 3.0
    
    play ambient1 "audio/effects/outdoorLoop.ogg" fadein 3.0
    scene home fang outside night with Fade (1.0, 1.0, 1.0):
        zoom 1.5 xcenter 0.7 ycenter 0.2      
    
    pause 1.0
    
    show reed neutral: 
        xcenter 0.4 ycenter 0.655 xzoom 1.0 matrixcolor BrightnessMatrix(-0.5)
    with Dissolve(1)   
    
    show reed neutral:
        ease 0.5 xcenter 0.7 
    
    pause 0.5
    play sound SHH +"audio/sfx/van_open.ogg"
    
    "I open the door to my van and look around for my grinder."
    
    show reed:
        ease 0.5 xcenter 0.9 rotate 10
    
    "It was wedged between a pack of tissues in the storage box of the console."
    
    show reed:
        ease 0.5 xcenter 0.9 rotate 0
        
    pause 0.25
    
    play sound SHH +"audio/sfx/van_close.ogg"
    
    "I shut the door, {w=0.2}{nw}"
    
    show reed:
        xzoom -1.0 xcenter 0.95
        ease 0.5 ycenter 0.7
 
    extend "then lean against it while ripping a nice long toke for my efforts."
     
    play sound SHH +"audio/sfx/lighter.ogg" 
    show reed considering:
        ease 0.5 rotate 10
    pause 0.5    
    
    "Ahhhh." 

    pause 2.0

    show reed neutral

    play sound "<from 0 to 2>" + SHH +"audio/sfx/ringtone.ogg" #notorious/memetic Samsung ringtone, might not change
    
    pause 2.0

    play sound "audio/ui/uiClick.wav"    
    
    pause 1.0
    
    play music SHH +"audio/music/critters_for_sale.ogg" fadein 1.0
    
    show shh_trishhouse:
          xcenter -0.5 crop (960, 0.0, 1920, 1080)
          ease_bounce 1.0 xcenter 0.5     
    
    show trish neutral:
          xcenter -0.3 ycenter 0.655 matrixcolor BrightnessMatrix(-0.25)
          ease_bounce 1.0 xcenter 0.3 

    pause 0.5
    
    show trish explanatory
    T "Hey, what's up?"
    
    pause 0.5
    show trish neutral
    show reed explanatory
    
    Re "Nothing much, {w=0.2}just seeing what’s up with you."
    
    pause 0.5
    show reed neutral
    show trish surprised
     
    T "Oh! {w=0.5}{nw}"
    
    show trish considering
    extend "Well, same shit as always I guess."
    
    show trish explanatory
    T "Thought I’d try to get the house picked up a little."

    T "Then the bus came by and that lasted for all of 10 minutes."
    
    hide trish 
    show riley neutral:
        xcenter 0.3 ycenter 0.655 matrixcolor BrightnessMatrix(-0.25)
    with dissolve 
    T "Riley’s grounded after he got caught tagging with his friends again, so I’ve been trying to keep him contained to his room."
    
    hide riley
    show tana neutral:
        xcenter 0.3 ycenter 0.655 matrixcolor BrightnessMatrix(-0.25)
    with dissolve 
    T "Tana ignited a piece of bread on the stove trying to make toast, but I caught it before she started a housefire."
    
    hide tana
    show trish explanatory:
        xcenter 0.3 ycenter 0.655 matrixcolor BrightnessMatrix(-0.25)
    with dissolve
    T "The rest are in the living room watching a movie I put on, {w=0.2}so it’s unusually quiet right now."
    
    pause 0.5
    
    show trish considering
    T "What are you guys up too?"
    
    pause 0.5
    show trish neutral
    show reed explanatory
    
    Re "Not much. {w=0.2}They’re watching a movie too actually."
    
    pause 0.5
    show reed neutral
    show trish considering
    T "And you’re not?"
    
    pause 0.5
    show trish neutral
    show reed explanatory
    Re "I was, but I thought you might like some company."
    
    show reed neutral
    show trish happy
    with dissolve
    T "Aw, that’s sweet of you."
    
    show trish smile
    with dissolve
    T "Mom should be home soon, so I’ll be over before too much longer."
    
    stop music
    play sound "audio/effects/lockerSmash.ogg"
    show trish surprised 
    show reed shocked
    
    pause 0.5
    T "Hey what was that?"

    show reed considering:
        ease 0.5 xcenter .8 rotate 0
    pause 0.5   
    
    show reed shocked:
        xzoom -1.0
        0.5
        xzoom 1.0
        0.5
        xzoom -1.0
        0.5
        xzoom 1.0
        
    pause 1.0
    
    Re "I don’t know, I don't see anything."
    
    show reed explanatory:
        xzoom -1.0
    with dissolve
    
    Re "Probably a raccoon."
    
    show trish neutral
    play music SHH +"audio/music/critters_for_sale.ogg" fadein 1.0

    Re "Or maybe the lovebirds fighting inside."
    
    pause 0.5
    
    Re "Anyway, could you grab some pizza on the way over? {w=0.2}I'll cover ya when you get here."
    
    show reed neutral
    show trish explanatory
    T "That's fine, what do you want?" 
    
    show trish neutral
    show killer shh behind shh_trishhouse, reed:
        matrixcolor BrightnessMatrix(-1.0) xcenter 1.2 ycenter 0.655 xzoom -1.0
        ease_expo 2.0 xcenter 0.3
    
    show reed explanatory
    
    Re "Doesn't really matter. {w=0.2}As many drinks as they've put back, they'll probably eat anything you give them."
    
    Re "Just pick out something nice for yourself, {w=0.2}my treat."
    hide killer
    show reed neutral
    show trish surprised
    pause 0.5    
    
    T "Well thank you I-"
    
    play sound "audio/effects/anonDink.ogg"
    stop music fadeout 3.0
    show trish unimpressed
    
    T "Hey!{w=0.5}{nw}"
    
    show trish:
        zoom 1.0 alpha 1.0
        ease 2.0 zoom 0.5 alpha 0.0 
    
    extend " Knock it off you two!"

    T "Sorry Reed, I’ll see you soon."
    
    play sound SHH +"audio/sfx/end_call.ogg"
    hide shh_trishhouse
    with moveoutleft
    
    "I pocket the phone, {w=0.2}{nw}"
    
    show reed neutral:
        xzoom 1.0
        ease 0.5 xcenter 0.8
    
    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    
    extend "then dump out my ashes into the grass before putting everything back where I found it."
    
    scene black
    pause 2.0
    
    
    scene home fang outside night:
        zoom 1.2 ycenter 0.3
    show reed neutral:
        xzoom -1.0 xcenter 0.6 ycenter 0.7 zoom 0.35 matrixcolor BrightnessMatrix(-0.5)      
    with Dissolve(1)
    
    "I’ve been gone awhile, {w=0.2}probably should get back to them before they worry."
    
    show reed:
       ease 0.5 xcenter 0.45 matrixcolor BrightnessMatrix(-0.75)
       xzoom 1.0 xcenter 0.4
       easein 0.25 ycenter 0.6 
    
    pause 1.0
    
    stop ambient1 fadeout 10.0
    play sound SHH +"audio/sfx/locked_1.ogg"
     
    camera:
        zoom 1.0 xcenter 0.5 ycenter 0.5
        parallel:
            ease 12.5 zoom 4.0 xcenter 0.8 ycenter 0.6
        parallel:
            ease 0.5 yoffset 25
            0.5
            ease 0.5 yoffset 0
            0.5
            ease 0.5 yoffset -25 
            0.5
            ease 0.5 yoffset 0
            0.5
            ease 0.5 yoffset 25
            0.5
            ease 0.5 yoffset 0
            0.5
            ease 0.5 yoffset -25 
            0.5
            ease 0.5 yoffset 0
            0.5
            ease 0.5 yoffset 0
            0.5
            ease 0.5 yoffset 25
            0.5
            ease 0.5 yoffset 0
            
    Re "Hmm?{w=1}{nw}"
    
    play sound SHH +"audio/sfx/locked_2.ogg"
    
    $ renpy.pause(2.00, hard=True)
    
    play sound SHH +"audio/sfx/locked_3.ogg"
    $ renpy.pause(2.00, hard=True)
    
    show reed explanatory
    Re "Hey guys, {w=0.2}open the door!{w=1}{nw}"
    
    play sound SHH +"audio/sfx/locked_4.ogg"
    
    $ renpy.pause(2.00, hard=True)
    
    show reed angry
    
    Re "Come on, this isn't funny!{w=1}{nw}"
    
    $ renpy.pause(1.00, hard=True)
    
    show reed shh shocked
    
    camera:
        zoom 4.0 xcenter 0.8 ycenter 0.6 yoffset 0.0
    
    Re "Hey, who are-{w=0.5}{nw}"
    
    window hide
    
    play sound SHH +"audio/sfx/stinger.ogg"
    show arms shh with moveinbottom:
        zoom 0.35 xcenter 0.45 ycenter 0.45
    
    $ renpy.pause(0.25, hard=True)
    
    scene black #with Fade(0.5,0.5,0.5, color = "#ba0b0b")
    
    camera:
        zoom 1.0 xcenter 0.5 ycenter 0.5 rotate 0
    
    pause 5.0
    
    play music SHH +"audio/music/murder_house.ogg"
    scene shh_tv    
    show anon neutral:
        matrixcolor BrightnessMatrix(-1.0) ycenter 0.75 xcenter 0.3
    show fang neutral:
        matrixcolor BrightnessMatrix(-1.0) ycenter 0.75 xcenter 0.1
    show shh_couch
    show shh_current behind anon,fang:
        xcenter 0.517 ycenter 0.447 blur 4.0 alpha 0.95 zoom 1.01
    
    F "Was that Reed just now?"

    A "Hard to hear it over the sound system, {w=0.2}but I’m not sure who else it would be."

    F "Think he locked himself out?"
     
    A "Pft, that wouldn't surprise me. "
    
    show anon:
        ycenter 0.75
        ease 0.5 ycenter 0.655
    
    extend "I'll go check on him."

    $ renpy.music.set_pause(True)
    play ambient1 "audio/effects/hungryBeast.ogg" fadein 1.0
    
    scene shh_door_c with Fade(0.5,0.5,0.5)
    
    F "Is he out there?"
    
    A "Hold on."
    
    play sound SHH +"audio/sfx/unlocked.ogg" 
    
    scene shh_door_o with Dissolve(1)
    
    pause 1.0
    
    scene home fang outside night with Fade(0.5,0.5,0.5):
        zoom 3.5 xcenter 0.85 ycenter -0.2     
   
    pause 1.0
    
    show anon concerned:
        xcenter 0.35 ycenter 0.655 matrixcolor BrightnessMatrix(-0.75)        
    with dissolve
     
    "I don’t see him out here {w=0.5}{nw}"
    
    show anon:
        xzoom -1.0
        0.5
        xzoom 1.0
        0.5
        xzoom -1.0
        0.5 
        xzoom 1.0
    
    extend "or anything else really."

    "Where the fuck did he go?"

    pause 1

    "It's kinda creepy actually."

    stop ambient1 fadeout 1.0
    
    scene black with Dissolve(1)
    
    "Well I'll leave the door unlocked for him anyway."
    
    $ renpy.music.set_pause(False)
    scene shh_tv    
    show anon concerned:
        matrixcolor BrightnessMatrix(-0.5) ycenter 0.655 xcenter 0.8 xzoom -1.0
    show fang considering:
        matrixcolor BrightnessMatrix(-0.5) ycenter 0.75 xcenter 0.2
    show shh_couch
    show shh_current behind anon,fang:
        xcenter 0.517 ycenter 0.447 blur 4.0 alpha 0.95 zoom 1.01
    with Dissolve(1)
    
    F "What happened?"  
    
    pause 0.5
    show anon shrug
    
    A "I don’t know, {w=0.2}he wasn’t there."
    
    show anon concerned:
        ease 0.5 ycenter 0.75
    
    A "Let’s see if I can reach him."
    
    pause 1.0
    play sound SHH +"audio/sfx/tapping_1.ogg"
    
    A "{i}Hey man, didn’t see u outside."

    A "{i}Whered u go?"

    pause 1.0
    play sound SHH +"audio/sfx/message.ogg"
    pause 1.0
    
    Re "{i}Went out for a walk."

    Re "{i}I'll be back soon."
    
    show anon considering
    
    pause 0.5
    play sound SHH +"audio/sfx/tapping_2.ogg"
     
    A "{i}w/e man, just let us know when you get back I left the door unlocked."
    
    pause 1.0
    play sound SHH +"audio/sfx/message.ogg"
    pause 1.0 
     
    Re "{i}Thank you."
    
    Re "{i}I will."

    play sound "audio/ui/uiClick.wav"
    
    pause 0.5
    
    F "So what's up with him?"
    
    show anon shrug:
        ease 0.5 ycenter 0.655
    pause 0.5
    
    show fang neutral
    A "Nothin', {w=0.2}just said he'd be out for a bit." 
    
    show anon neutral:
        ease 1.0 xcenter 0.3
        
    show fang neutral:
        0.5
        ease 0.5 xcenter 0.1        
    
    extend " You know how he can be." 
     
    show anon neutral:
       xcenter 0.3 ycenter 0.655
       ease 0.5 ycenter 0.75
       xzoom 1.0
     
    show fang happy
    "Fang rolled her eyes."

    F "More than you'll ever know."
    
    pause 2.0
    stop music
    show shh_loading behind anon,fang:
        xcenter 0.517 ycenter 0.447 blur 4.0 alpha 0.95 zoom 1.01
    hide shh_current


    pause 1
    show fang shocked
    F "Dude, did you hit something?"
    
    show anon shrug:
        xzoom -1.0
    with dissolve
    
    A "No, how could I? The laptop is over there."
    
    show fang considering
    
    show anon sad
    with dissolve
    
    "Anon checks his phone and makes a face."
    
    A "Damn, looks like the internet’s out."
    
    pause 0.5
    show fang angry
    F "Uhhhhhhhhg."

    F "Captain Kush better not have broke something. " 
    
    show fang considering
    extend "I don’t know how to fix this shit."
    
    show anon considering
    A "Maybe he just tripped on the power chord on his way out, {w=0.2}I can go take a look."
    
    pause 0.5
    show anon neutral
    F "Eh don’t bother. {w}The movie’s almost over anyway."
    show anon considering
    A "You sure?"
    
    show fang shh grin
    with dissolve

    F "We finally have the place to ourselves now." 
    
    show killer shh:
        matrixcolor BrightnessMatrix (-1.0) ycenter 1.1 xcenter -0.2 
        ease 2.0 xcenter 1.2
    
    extend " Wouldn’t you rather take this upstairs?"
    
    show anon ohshit
    A "{cps=*0.25}Uhhh,{/cps}{w=0.2}{nw}"
    
    show fang behind anon
    show anon happy
    extend " yeah, sure!"
    
    hide killer shh
    
    show anon neutral with dissolve
    
    show fang happy:
        ycenter 0.75
        ease 0.5 ycenter 0.655

    F "Alright then, {w=0.5}{nw}"
    
    show fang:
        xcenter 0.1 ycenter 0.655
        ease 2.0 xcenter 1.2
    
    extend "get me a drink on the way up will ya?"
    
    show anon neutral:
        ycenter 0.75 xcenter 0.3 xzoom 1.0
        ease 0.5 ycenter 0.655
        0.25
        ease 2.0 xcenter 1.2


    scene black with Dissolve(2)

    hide shh_loading

    
    "I peel myself off the couch and stumble through the dark towards the kitchen."

    scene shh_kitchen with Dissolve(2)

    show anon neutral:
     ycenter 0.655 xcenter -0.2
     ease 5.0 xcenter 0.7

    "I don’t know where Mrs. Aaron keeps most of her things, but I’m not so drunk I can’t find the fridge."
    
    play sound SHH +"audio/sfx/open_fridge.ogg"
    
    play ambient1 SHH +"audio/sfx/fridge.ogg"

    scene black with dissolve
    
    scene shh_fridge_b with dissolve
    show shh_fridge_f with dissolve
    show anon neutral behind shh_fridge_f:
        xcenter 0.6 xzoom -1.0 ycenter 1.2 zoom 1.5
        
    with Dissolve(1)
    
    pause 1.0

    "Dammit, {w=0.2}I don’t remember what we stored it in now."

    pause 1.0
    
    play sound "audio/effects/anonBedRustle.ogg"
    "I think it was in something plastic?"
    
    show anon considering:
        xzoom 1.0
    with dissolve

    pause 1
    
    play sound "audio/effects/anonDink.ogg"
    "This thermos maybe?"
    
    pause 0.5
    
    show killer shh behind anon:
        matrixcolor BrightnessMatrix(-0.8) ycenter 0.7 zoom 1.25 xzoom -1.0 xcenter 0.65
    with Dissolve(1)    
    
    show anon unimpressed
    
    "This is too hard, {w=0.2}I’ll just grab one of Rip’s beers and we can replace it later."
   
    pause 0.5
    play sound SHH +"audio/sfx/pickup.ogg"
    pause 0.5
    
    show anon neutral:
        ycenter 1.2
        ease 0.5 ycenter 1.1
        
    "Here we go."
    
    stop ambient1 fadeout 0.5
    "Now I just have to-"
    
    play sound SHH +"audio/sfx/stinger_2.ogg"
    show killer shh:
        easein 1.0 matrixcolor BrightnessMatrix(0)        
    show anon ohshit
    
    pause 1.0
    play music SHH +"audio/sfx/stinger_perc.ogg"
    show anon neutral:
        zoom 1.5
        easein 0.25 zoom 0.9
        xzoom 1.0
        easein 0.5 xcenter 0.55 ycenter 0.2
        block:
            ease 0.25 xoffset 10
            0.25
            ease 0.25 xoffset 0
            0.25
            ease 0.25 xoffset -10
            0.25
            ease 0.25 xoffset 0
            0.25
            repeat
        
    show killer shh:
        0.25
        easein 0.25 xcenter 0.75
                 
    with vpunch

    pause 2
    
    A "{cps=*0.5}{size=*0.5}I...Can’t…"
    
    A "{cps=*0.5}{size=*0.5}...Fang..."
          
    window hide
    stop music fadeout 0.5

    pause 0.5
    
    play sound SHH +"audio/sfx/stab_2.ogg" 
    
    show anon shh held:
        ease 0.5 xoffset 0
    with vpunch
    
    pause 2
    
    scene black with Fade(0.5,0.5,0.5, color = "#ba0b0b")
        
    pause 5.0
    
    play music SHH +"audio/music/yume_nikki.ogg" fadein 1.0
    scene shh_fangroom with Fade (0.5,0.5,0.5)
    
    "I’m sitting on my bed, waiting for my prince passibly charming to show up as I grow impatient."

    F "God, {w=0.2}how long does it take to pick up a drink?"

    "Did he get lost?"

    "As I start to question if I should go check on him, {w=0.2}I hear the door open." 
    
    play sound "audio/effects/doorSlam.ogg"
    
    pause 1.0
    
    "I scramble back into position as quickly as I can."
    
    scene shh_cgfang1 with Dissolve(1)
    
    F "Come in ♥"

    F "Hey big boy, {w=0.2}you ready to play ♥"
    
    play sound "<from 18 to 19>" + SHH +"audio/sfx/footsteps.mp3"
    camera:
        zoom 1.0 xcenter 0.5 ycenter 0.5
        ease 0.25 zoom 1.1 yoffset 10 xcenter 0.525
        ease 0.25 zoom 1.2 yoffset 0 xcenter 0.55       
        
    scene shh_cgfang2 with dissolve

    F "Anon? What are you wearing?"

    F "Is this some stupid bit? Is that why you took so long?"
    
    play sound "<from 10 to 11.5>" + SHH +"audio/sfx/footsteps.mp3"
    camera:
        zoom 1.2 xcenter 0.55  
        ease 0.25 zoom 1.3 yoffset 10 xcenter 0.575
        ease 0.25 zoom 1.4 yoffset 0 xcenter 0.6    
        
    pause 0.5
    
    F "Come on Anon say something, this isn’t funny."

    play sound "<from 21 to 22.5>" + SHH +"audio/sfx/footsteps.mp3"
    camera:
        zoom 1.4 xcenter 0.6  
        ease 0.25 zoom 1.5 yoffset 10 xcenter 0.625
        ease 0.25 zoom 1.6 yoffset 0 xcenter 0.65       
        
    stop music fadeout 1.0
    
    scene shh_cgfang3 with dissolve
    
    F "Anon?"

    F "No, {w=0.2}you’re not..."
    
    play ambient1 SHH +"audio/sfx/stinger_3.ogg" noloop
    camera:
        zoom 1.6 xcenter 0.65
        easein 0.5 xcenter 0.75 zoom 2.0
    
    show knife shh with moveinbottom:
        zoom 0.6 xcenter 0.45 ycenter 0.5

    pause 0.5

    scene black

    play sound SHH +"audio/sfx/fang_scream.ogg"
    queue sound SHH +"audio/sfx/stab_1.ogg"

    #scene black with Fade(0.5,0.5,0.5, color="#ba0b0b")
    
    pause 5.0
    
    camera:
        zoom 1.0 ycenter 0.5 xcenter 0.5 yoffset 0 rotate 0
    play sound SHH +"audio/sfx/drive_away.ogg"
    
    pause 1.0
    scene home fang outside night  with Dissolve(2)
    
    show trish neutral:
        xcenter 0.6 xzoom -1.0 ycenter 0.655
        
    show tablesmashpizzas:
        crop (120, 0, 1800, 1080) xcenter 0.9 ycenter 0.6       
    
    with Dissolve(3)
    
    play ambient1 "audio/effects/nightLoop.ogg" fadein 3.0
    "After a long evening of dealing with the gremlins I call my family, {w=0.2}I finally make it to Fang's place for some much deserved R&R."
    
    show trish smile
    pause 0.5
    
    "Hope they haven’t passed out on me already."
    
    show trish neutral:
        xcenter 0.6 zoom 1.0 alpha 1.0 ycenter 0.655
        ease 1.0 xcenter 0.4 zoom 0.5 alpha 0.0
        
    show tablesmashpizzas: 
        crop (120, 0, 1800, 1080) xcenter 0.9 ycenter 0.6 alpha 1.0 zoom 1.0 
        ease 1.0 alpha 0.0 zoom 0.5 xcenter 0.55 ycenter 0.65
    
    show black with Dissolve(1)
    
    "I stroll over to the front door and find it unlocked, {w=0.2}guess that saves them the trouble."
    
    play sound SHH +"audio/sfx/door_open_close.mp3"
    
    pause 1.0
    stop ambient1 fadeout 0.5
    play music SHH +"audio/music/call_of_cthulhu.ogg" fadein 5.0
    scene home fang dim with Dissolve(1)

    "I lock the door behind me and look around"

    T "Hey guys I’m here! {w}I got it half veggies half meat lovers if that’s cool with everybody!"
    
    pause 0.5
    
    "There’s no response."

    "I lay the boxes down on the side table and take a look around."

    "I can see TV is on {w=0.2}and food trash is littered across the coffee table, {w=0.2}but otherwise no sign of life."
    
    pause 0.5
    
    "Are they playing a joke on me?"

    "I wouldn’t put it past Anon… but I get the feeling that’s not the case."

    "I’ll look around and see where they went."

    call screen shh_exploration

label shh_slasher_fd:
    
    T "I can't leave now, I just got here. "
    
    call screen shh_exploration 
    
label shh_slasher_cel:
    
    if shh_cellar_seen == False:
    
      T "Over my dead body. {w}No one knows which dirty secrets Fang's dad is hiding there."
    
      pause 1.0
    
      T "Their laundry, perhaps."
      
      $ shh_cellar_seen = True
    
    else:
        
      T "No means no."  
    
    call screen shh_exploration
    

label shh_slasher_kit:
    
    if shh_kitchen_seen == False:
        scene shh_kitchen with pushright
    
        "I peak into the kitchen, but still no sign of anyone."
    
        "The fridge was left open. {w}Reed did say they were drinking, {w=0.2}but even the skinnie knows how to shut a door."

        pause 0.5
    
        "Something must have happened in a hurry."
    
        $ shh_kitchen_seen = True
        $ shh_new_location = "WHERE TO GO?"
    
        scene home fang dim with Dissolve(1)
    
    else:
        
        T "Nothing suspicious except that fridge."
    
    call screen shh_exploration
    
    
label shh_slasher_up:
    
    "Maybe they just went upstairs."
    
    play sound SHH +"audio/sfx/stairs.ogg"
    scene shh_hallway with pushdown
    
    $ shh_location = "sfloor_a"
    $ shh_new_location = "WHERE TO GO?"
    call screen shh_exploration
    

label shh_slasher_pr:
    
    if shh_parents_seen == False:
    
        "Not likely, but worth a shot I guess..."
        
        play sound SHH +"audio/sfx/locked_1.ogg"
        
        pause 0.5
        
        "Guess it's locked... {w}from the front?"

        "This bedroom door must be his own creation."
    
        $ shh_parents_seen = True
    
    else:
        
        "This lock and key puzzle is too dangerous to solve."
        
    call screen shh_exploration

label shh_slasher_nr:
    
    if shh_naser_seen == False:
    
        "Fang said Nas was out this weekend."
    
        pause 0.5
    
        "Guess it couldn't hurt to take a look."
    
        scene shh_naserroom with Dissolve(1)
        
        pause 0.5
        
        "Looks pretty vanilla.{w} It suits him, I guess."
        
        "I wonder if he really has a leopard mankini in his closet?"
        
        pause 0.5
        
        "Actually, {w=0.2}I don't want to know."
        
     #   T "That definitely not suits him. {w}Or anybody else, if you ask me."
        
        scene shh_hallway with Dissolve(1)
        
        $ shh_naser_seen = True
        
    else:
        
        "I've seen enough."
    
    call screen shh_exploration    


label shh_slasher_lr:
    
    "I'm already here now, no point in going back."
    
    call screen shh_exploration  
    
label shh_slasher_fr:
   
   stop music fadeout 2.0
   
   T "Here we go."
   
   scene shh_cgfang4 with Fade(0.5,0.5,0.5)
   
   pause 1.0
   
   show trish neutral:
       xcenter -0.2 ycenter 0.655
       easeout 0.5 xcenter 0.1
   
   pause 0.5
   play ambient1 "audio/effects/heartbeat.ogg" fadein 0.5
   show trish shock with dissolve

   "I step into Fang's room and what I see turns my blood to ice."

   "There she is, {w=0.2}draped across her bed like a ragdoll, {w=0.2}and bleeding from a wound on the chest."

   show trish surprised:
       xcenter 0.1 ycenter 0.655 zoom 1.0
       easeout 2.0 xcenter 0.6 zoom 0.5 ycenter 0.5
       xzoom -1.0
   
   pause 2.0
   
   show trish:
       xzoom -1.0 xcenter 0.6 zoom 0.5 ycenter 0.5
       easeout 1.0 xcenter 0.5
       easeout 1.0 rotate -10
   
   "With a trembling hand I reach out and feel for her pulse."
   
   pause 0.5
   
   "Nothing."

   show trish sad:
       easein 0.1 rotate 0
       easein 1.5 xcenter 0.8 ycenter 0.655 zoom 1.0 

   pause 1.0 
   "In my panic I stumble backwards, trying to make sense of what I’ve just seen."

   show trish sad:
       easein 0.5 xcenter 0.95
       xzoom 1.0
    
   play sound "audio/effects/anonHeadbutt.ogg"   
   pause 0.5

   stop ambient1 fadeout 1.0
   
   show trish surprised:
       xzoom 1.0
       easein 1.0 xcenter 0.5 
   
   queue sound "audio/effects/anonDumbassFall.ogg"
   
   show anon shh held:
       xcenter 1.2 ycenter 0.7 rotate 0 xzoom -1.0
       easein 2.0 xcenter 0.8 ycenter 1.2 rotate -90  
   with hpunch
   
   "I bump into Fangs closet, the door opens and another of our friends collapses onto the floor like a loose manikin."
   
   show trish shock with dissolve:
       easein 0.5 xcenter 0.4
   
   "I…{w=0.5}{nw}"
   
   show trish flip sad: 
       easein 0.5 xcenter 0.3       
   
   "I've got to get out of here!"
   
   play music SHH +"audio/music/clock_tower.ogg" fadein 0.5
   
   $ shh_location = "sfloor_b"
   $ shh_new_location = "BACK TO THE DOOR"
   scene shh_hallway_e with pushright  
   
   call screen shh_exploration
   
label shh_slasher_kill:
   
   scene shh_door_c with pushdown
   
   stop music fadeout 3.0       
   T "I'm… {w=0.2}I'm sorry guys, {w=0.2}I promise I'll go get help!" 
   
   pause 1.0
   
   play sound SHH +"audio/sfx/door_knob.ogg" 
    
   scene shh_door_e with dissolve
   
   pause 0.5
   
   play sound SHH +"audio/sfx/stinger_final.ogg"
   show killer shh weapon:
       matrixcolor BrightnessMatrix(-1.0) xcenter 0.5 ycenter 0.655 zoom 0.5 xzoom -1.0
       0.5
       easein 0.5 matrixcolor BrightnessMatrix(0.0) zoom 1.5 ycenter 0.9
   
   pause 1.0
   
   hide killer shh weapon
   
   play ambient1 SHH +"audio/sfx/stinger_perc.ogg"
   
   $ shh_location = 'killer_door_a'
   $ shh_new_location = ""
   $ shh_hit_number = 0
   show shh_door_e:
       ease 0.5 blur 5.0
   
   call screen shh_exploration 
   
   
label shh_slasher_fd_gameover:   
   show killer shh front:
       zoom shh_zoom xcenter 0.5 ycenter 0.5
       easein 0.5 zoom 1.6
   stop ambient1
   play sound SHH +"audio/sfx/stab_2.ogg"
   queue sound SHH +"audio/sfx/trish_scream.ogg"
   scene black with Fade(0.5, 0.5, 0.5, color = "#ba0b0b")
   
   $ renpy.pause (3.0, hard=True)
     
   jump shh_slasher_kill

   # $ shh_word = renpy.input("What Trish has on her head to fight back?")
   # stop ambient1 fadeout 0.5
   
   # if shh_word == "HORNS":
     # jump shh_slasher_win   
   # elif shh_word == "Horns":
     # jump shh_slasher_win 
   # elif shh_word == "horns":
     # jump shh_slasher_win    
   # else:
     # play sound SHH +"audio/sfx/stab_2.ogg"
     # queue sound SHH +"audio/sfx/trish_scream.ogg"
     # scene black with Fade(0.5, 0.5, 0.5, color = "#ba0b0b")
     
     # pause 3.0
     
     # jump shh_slasher_kill


label shh_slasher_win:       
     play sound "audio/effects/anonTheaterFall.ogg"
     stop ambient1
     show shh_door_e:
         easein_cubic 0.5 blur 0.0
     show killer shh weapon:
         matrixcolor BrightnessMatrix(0.0) zoom shh_zoom ycenter 0.9 xcenter 0.5 xzoom -1.0
         easein_cubic 0.5 matrixcolor BrightnessMatrix(-1.0) zoom 0.6 ycenter 0.5
     
     pause 0.5
     hide killer
     with vpunch
     
     "I manage to hurt him into the chest, {w=0.2}knocking him backwards through the front door."
     
     play sound "audio/effects/doorSlam.ogg"
     
     scene shh_door_c with vpunch
     
     play music SHH +"audio/music/clock_tower.ogg" fadein 5.0
     
     "I shut and lock the door as quickly as I can. {w}My mind racing on what to do."

     "I need to find something to defend myself for real, {w=0.2}preferably as sharp as my horns."
     
     "Even in dire conditions I don't want to break them apart."
     
     "After I have a weapon, I'll go find somewhere I can hide."

     "Trying to run now will probably get me killed. {w}All I can do is hope I can get him before he gets me."
     
     scene home fang dim with Dissolve(1)
     
     $ shh_location = "living_b" 
     $ shh_new_location = "WHERE TO GO?"
     call screen shh_exploration


label shh_slasher_kit2:
   
   if shh_knife_obtained == False:
   
    T "Yup, the best place to find something like that."
    $ shh_location = "kitchen"
    $ shh_new_location = "WHERE ARE KNIVES?"
    $ shh_knife_obtained = True
    scene shh_kitchen with pushright
    
   else:   
    
    "I have my weapon. {w=0.2}It's time to hide somewhere else."   
   
   call screen shh_exploration
   
label shh_slasher_kit3:
    
   play sound SHH +"audio/sfx/knife.ogg"
   
   "I lightly run my finger against the edge of the blade. {w}Seems like Mrs. Aaron keeps her tools in good condition."

   T "This will work."
   
   pause 1.0
   
   "Now I need to hide somewhere. {w}Preferably, on the second floor."
   
   scene home fang dim with pushleft
   
   $ shh_location = "living_b"
   $ shh_new_location = "WHERE TO GO?"
   
   call screen shh_exploration
   
label shh_slasher_up_fin:
   play sound SHH +"audio/sfx/stairs.ogg"
   scene shh_hallway_e with pushdown
   $ shh_location = "sfloor_c"
   $ shh_new_location = "WHERE TO GO?"
   
   call screen shh_exploration 

label shh_slasher_nr_huh:
   
   play sound SHH +"audio/sfx/locked_2.ogg"
   T "The door doesn't budge."

   extend " What the hell is going on with it?"       
   
   call screen shh_exploration 
   
label shh_slasher_lr_b:
    
    if shh_knife_obtained:
        
       "But do I really need to go downstairs again?"
    
    else:
       play sound SHH +"audio/sfx/stairs.ogg"
       scene home fang dim with pushup       
       $ shh_new_location = "WHERE TO GO?"
       $ shh_location = "living_b"       
       
    call screen shh_exploration    
        
label shh_slasher_fr_1:
    
   "It seems I have no choice rather than going back there."  
   
   scene shh_cgfang4 
   show trish neutral:
       xcenter 0.3 ycenter 0.655
   with pushright
   pause 1.0
   
   "I guess this place is as good as any place to take cover."
   
   stop music fadeout 3.0
   play sound "audio/effects/rooftopDoorSmash.ogg"
   
   show trish surprised:
       xzoom -1.0
   with dissolve
   
   "I hear the sound of the front door being broken through. {w}It’s almost time."
   
   if shh_knife_obtained == False:
    
    show trish neutral:
      easein 0.5 xcenter 0.8
    
    "I have a sudden jolt of inspiration, and I bend over to feel through Anon’s clothes."

    "I pray with all my heart it's still there."
     
    play sound SHH +"audio/sfx/pocket_knife.ogg" 
    show trish smile with dissolve

    "Eventually I find what I’m looking for, and pull out a sharp pocket knife."
    
    pause 1.0

    show trish shh dejected with dissolve
    
    "I look back at the corpse wistfully."

    "I’m sorry, Anon."

    show trish neutral with dissolve

    "I know we didn’t always get along, {w=0.2}but I promise I won’t let that freak get away with this."

    
    $ shh_knife_obtained = True
   else:
       pass
    
   hide trish with dissolve
   
   "I stand there beside the door with my back against the wall, gripping the blade in my hand like my life depends on it."

   "Hmm, I guess it does."

   play sound "<from 5 to 11>" + SHH +"audio/sfx/footsteps.mp3"

   "I can just barely hear him make his way up the stairs and on the second floor, you think he’d make far more noise with his stature."

   queue sound SHH +"audio/sfx/door_knob.ogg"

   "Finally he comes to the door for my room."
   play ambient1 "audio/effects/heartbeat.ogg"
   play sound SHH +"audio/sfx/door creaking.mp3"
   
   scene shh_cgkiller1 with fade
   
   #T "The door begins to creak open."
   
   $ shh_location = 'killer_door_b'
   $ shh_new_location = ''
   "It’s time, {w}now or never."
   
   call screen shh_exploration
   
label shh_slasher_fr_gameover:
   stop ambient1
   scene shh_cgkiller2 with dissolve
   play sound SHH +"audio/sfx/stab_1.ogg"
   queue sound SHH +"audio/sfx/trish_scream.ogg"
       
   scene black with Fade(0.5,0.5,0.5, color="#ba0b0b")
       
   pause 4.0
       
   jump shh_slasher_fr_1

   
   # $ shh_word = renpy.input('You know your new weapon:')
   
   # if shh_word == 'Knife':
       # jump shh_slasher_fr_fin
   # elif shh_word == 'KNIFE':
       # jump shh_slasher_fr_fin
   # elif shh_word == 'knife':
       # jump shh_slasher_fr_fin
   
   # else:
       # stop ambient1
       # scene shh_cgkiller2 with dissolve
       
       # pause 1.0
       
       # play sound SHH +"audio/sfx/stab_1.ogg"
       # queue sound SHH +"audio/sfx/trish_scream.ogg"
       
       # scene black with Fade(0.5,0.5,0.5, color="#ba0b0b")
       
       # pause 4.0
       
       # jump shh_slasher_fr_1
   

label shh_slasher_fr_fin:
   stop ambient1
   scene black with Fade(0.5,0.5,0.5, color="#ba0b0b")
   
   "Without a moment’s hesitation, {w=0.2}I jam the blade deep into the man’s neck."

   play sound SHH + "audio/sfx/thud.mp3"

   "He staggers forward, {w=0.2}and a moment later collapses into the floor."
   
   scene shh_cgfang4 
   
   show killer shh:
       xcenter 0.8 rotate 90 ycenter 1.0 xzoom -1.0
   
   show trish sad:
       xcenter 0.1 ycenter 0.655 xzoom 1.0
   
   with Dissolve(1)

   "It’s done."

   show trish sad:
       ycenter 0.655 xzoom -1.0
       ease 0.6 ycenter 0.75
   
   "I fall to the ground, {w=0.2}my legs no longer hold the strength to bear my weight."

   "All the feelings suppressed by the adrenaline rush burst through to the surface."
   
   "And I cry into my coat."
   
   pause 0.5
   
   "It's all{cps=*0.5}...{/cps}simply too much to process."
   
   pause 2.0
   
   play music SHH +"audio/music/clock_tower.ogg" fadein 1.0
   
   show killer shh weapon:
       easein 2.0 rotate 0 ycenter 0.75
       
   pause 2.5

   show killer shh weapon:
      easein_bounce 0.5 xcenter 0.6
      1.0
      easein_bounce 0.5 xcenter 0.45      
      1.0
      easein_bounce 0.5 xcenter 0.3     
   
   pause 3.0

   stop music 
   
   play sound "audio/effects/shotTinnitus.ogg"

   scene shh_cgfang4 
   show fangdad neutral:
       xcenter 0.3 ycenter 0.655
   show trish surprised:
       xcenter 0.1 ycenter 0.655
       4.5
       xzoom 1.0
   
   show killer shh:
       ycenter 0.75 xcenter 0.8 xzoom -1.0
       parallel:
           matrixcolor TintMatrix('#f7f7f7')
           1.0
           matrixcolor TintMatrix('#e0b6b6')
           1.0
           repeat  
       parallel:
           ease 0.25 xoffset 10 
           0.25
           ease 0.25 xoffset 0
           0.25
           ease 0.25 xoffset -10
           0.25
           ease 0.25 xoffset 0
           0.25
           repeat
           
   with Fade(0.5, 1.5, 0.5, color = "#fff")
   
   show fangdad neutral

   pause 3
       #xcenter 0.2
       #ease 1.5 xcenter 0.6
       
   "Ripley looks over at the remains of his daughter, then back to the man in front of him."
    
   show killer shh:
        ease 0.25 xoffset 0
    
   show fangdad shh angry
   with dissolve    

   "His face twisted by a look of intense hatred."
   
   show killer shh:
       easein 0.5 xcenter 0.5
       
   pause 0.4
   
   play sound "<from 0 to 2>" + "audio/effects/shotTinnitus.ogg"    
   
   
   show killer shh:
       xcenter 0.85
   with Fade (0.25,0.25,0.5,color = "#fff")
   
   play sound "<from 0 to 2>" + "audio/effects/shotTinnitus.ogg"           
   
   show fangdad shh angry
       
   show killer shh:
      xcenter 0.95 
   with Fade (0.25,0.25,0.5,color = "#fff")      

   play sound "<from 0 to 2>" + "audio/effects/shotTinnitus.ogg"
   scene white

   hide killer
   
   #show killer shh:
   #    easein 0.5 rotate 90 xcenter 1.0
   #    easein 0.5 xcenter 1.2 ycenter 0.8
   #pause 0.5
   
   queue sound SHH +"audio/sfx/Glass_breaking.ogg"
   
   pause 3.0
   
   scene shh_cgfang5
   
   show fangdad neutral:
        xcenter 0.3 ycenter 0.655       
   
   show trish surprised:
        xcenter 0.1 ycenter 0.655
   with hpunch
     
   pause 1.0
   queue sound "audio/effects/anonGardenFall.ogg"
   
   camera:
       ease 0.25 yoffset 20
       ease 0.25 yoffset 0
   
   pause 0.5
   
   queue sound SHH +"audio/sfx/trish_crying.ogg"
   show trish sad behind fangdad:
       ycenter 0.655
       easein 0.5 ycenter 0.75
   
   pause 0.5
   
   show fangdad neutral with dissolve:
       xzoom -1.0
       0.5
       ease 0.5 ycenter 0.75
   
   play music SHH +"audio/music/clock_tower_2.ogg" fadein 5.0
   
   SHH_Ri "Shhh, it’s ok. {w=0.5}It’s over now."
 
   T "{w=0.2}...Who was that?"

   SHH_Ri "…"
   
   show fangdad neutral
   
   SHH_Ri "I couldn’t say."
   
   pause 0.5
   
   SHH_Ri "Can you tell me what happened here?"

   T "I-I…"
  
   T "I'm not sure, {w=0.2}I got here later than they did."

   T "{cps=*0.5}Did...{/cps}did Reed at least?"

   show fangdad shh sad with dissolve

   SHH_Ri "...his body was in the vehicle out front."

   SHH_Ri "...I'm sorry."
   
   show trish shh dejected with dissolve
   
   pause 0.5
   
   T "Thank you..."

   SHH_Ri "It was nothing, {w=0.2}just a part of the job."

   T "…"

   T "How did you know he was…?"

   show fangdad neutral with dissolve

   SHH_Ri "I didn’t, but when I tried to call my daughter earlier, no one picked up."
    
   pause 0.5
   show fangdad unimpressed

   SHH_Ri "Frankly, {w=0.25}that’s not unusual."

   show fangdad neutral

   SHH_Ri "But then I called the boy and got the same response."

   SHH_Ri "That{w=0.5} has never happened."

   show fangdad shh sad with dissolve

   SHH_Ri "...I'm sorry I didn't get here sooner."

   SHH_Ri "This all could have been avoided if I just…"
   
   show trish sad notears with dissolve

   T "It's ok Mr. Aaron."

   T "There's nothing more you could have done."
   
   show fangdad neutral with dissolve:
       xzoom 1.0
       0.5
       ease 0.5 ycenter 0.655

   SHH_Ri "Well, that’s where you’re wrong."

   SHH_Ri "I’m gonna make a call into dispatch. Don’t touch anything."

   show fangdad:
       easeout 1.0 xcenter 0.8
   
   pause 1.0
   
   show fangdad shh shocked behind trish:
       easein 0.25 xcenter 0.7

   stop music fadeout 1.0  
   pause 2

   SHH_Ri  "No..."
   
   show trish surprised:
       easein 1.0 xcenter 0.6
       
   pause 2.0   
  
   show trish surprised   
   
   play music SHH + "audio/music/Halloween.mp3" fadein 4.0

   T "It can’t be..."
   
   scene shh_mystery with Dissolve(1)

   T "Where did he go?"

   SHH_Ri "…"

   SHH_Ri "I don’t know."

   T "You hit him didn’t you?"

   SHH_Ri "Of course I did, but…"
   
   stop ambient1 fadeout 3.0
   
   "With unsteady hands, Ripley reloads his weapon and takes a deep breath." 
   
   play sound SHH +"audio/sfx/reload.ogg"
   
   SHH_Ri "Looks like I’ve got a long night ahead of me."

   scene black with Dissolve(1)

   pause 4

   $ quick_menu = False
   scene shh_credits:
       ycenter 2.0 xcenter 0.5
       linear 35.0 ycenter -1.0
   with Fade(1.0,1.0,1.0)   
   
   pause 20.0
   
   scene black with Dissolve(1)
   stop music fadeout 5.0
   
   pause 1.0
  
   return #jump into the menu with the slasher disabled/scene where Samantha presenting next story or whatever
