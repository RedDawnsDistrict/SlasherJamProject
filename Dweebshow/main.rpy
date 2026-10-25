label shh_main_1:
    play music SHH + "audio/music/twin_peaks.ogg" fadein 3.0
        
    $ quick_menu = False
    call screen shh_curtain_enter with PushMove(2.0, mode='pushdown')
    
    
label shh_main_2:    
    scene shh_curtain with None
    show fangmom neutral:
        ycenter 0.655 xcenter 0.5
    with Dissolve(2)
    pause 0.5
    $ quick_menu = True
    FM "Hello, everyone."

    FM "You know, Halloween is a very strange holiday."

    show fangmom shh concerned with dissolve

    FM "Personally,{w=0.20} I don't understand it. {w=0.40}Kids worshipping ghosts,{w=0.20} pretending to be devils." 

    show fangmom unimpressed with dissolve

    FM "Things on TV that are {i}completely{/i} inappropriate for younger viewers."

    show fangmom neutral with dissolve
      
    FM "Things like the following half hour."

    FM "Now nothing seems to bother {i}my{/i} kids.{w=0.40} But tonight's show,{w=0.30} which I totally wash my hands of,{w=0.30} is reeeeally scary."
   
    show fangmom unimpressed with dissolve

    FM "At least I think so."

    show fangmom neutral with dissolve

    FM "So if you have sensitive children..."

    show fangmom unimpressed with dissolve

    FM "...or are one..."

    show fangmom unimpressed with dissolve

    FM "Maybe you should tuck them into bed early tonight instead of writing us angry letters tomorrow."

    FM "Thanks for your attention."
    
    hide fangmom with dissolve
    
    menu:
       "{space=400}{size=*2.0}Which story to play?"

       "{color=#b3b9f2}Just the Two of Us":
             $ quick_menu = False
             stop music fadeout 1.0
             play sound SHH + "audio/sfx/slasher_jingle.ogg"
             scene shh_slasher_title with Dissolve(2)   
             pause 5.0
             
             jump shh_slasher_1
           
       "{color=#e3b598}Second novel":
             $ renpy.open_url('https://www.youtube.com/watch?v=04qPdGNA_KM')
             return
             
       "{color=#b5f2b3}Third novel":
             $ renpy.open_url('https://www.youtube.com/watch?v=dBz2GJAdttw')
             return     