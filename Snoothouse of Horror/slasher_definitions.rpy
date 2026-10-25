#for next novels I suggest making another document, this would be harder to navigate through without a search feature

init:
    $ SHH = "mods/Snoothouse of Horror/assets/"

#Misc
define config.mouse = {"hover":[(SHH + "images/cursor_move.png", 0, 0)], "prompt": [(SHH + "images/cursor_hit.png", 0, 0)]}
define base = Character (ctc="ctc_end_marker", ctc_pause="ctc_mid_marker", ctc_timedpause=Null(), ctc_position="nestled-close")
define SHH_Ri = Character (_("Ripley"), base, color="#D8A09A", who_outlines=[(gui.name_text_thickness, '#461B1F')])
define SHH_FR = Character(_('Fang and Reed'), base, color="#42DFA8", who_outlines=[(gui.name_text_thickness, '#183623')])
default shh_cinema = "null"
default shh_new_location = "WHERE TO GO?"
default shh_cellar_seen = False
default shh_naser_seen = False
default shh_knife_obtained = False
default shh_parents_seen = False
default shh_location = "living_a"
default shh_hit_number = 0
default shh_kitchen_seen = False
default shh_zoom = 1.5
# default shh_word = "DEATH"

#Sprites
image killer shh = SHH + "images/sprites/slasher_neutral.png"
image killer shh weapon = SHH + "images/sprites/slasher_slash.png"
image killer shh shoulder = SHH + "images/sprites/shoulder.png"
image killer shh front = SHH + "images/sprites/killergrab.png"
image arms shh = SHH + "images/sprites/slasher_arms.png"
image knife shh = SHH + "images/sprites/fangroom_night_knife.png"
image reed shh shocked = SHH + "images/sprites/reed shockedPOV.webp"
image fang shh grin = SHH + "images/sprites/fang grin.png"
image anon shh held = SHH + "images/sprites/anon held.png"
image fangdad shh angry = SHH + "images/sprites/ripley angry.webp"
image fangdad shh sad = SHH + "images/sprites/ripley sad.png"
image fangdad shh shocked = SHH + "images/sprites/ripley shocked.webp"
image fangmom shh concerned = SHH + "images/sprites/fangmom concerned.webp"
image trish shh dejected = SHH + "images/sprites/trish dejected.png"

#BGs
image shh_tv = SHH + "images/bg/tv_scene/tv.png"
image shh_couch = SHH + "images/bg/tv_scene/couch.png"
image shh_nflix = SHH + "images/bg/tv_scene/N.png"
image shh_current = ConditionSwitch ('shh_cinema == \'scream\'', 'shh_scream', 'shh_cinema == \'halloween\'', 'shh_halloween', 'shh_cinema == \'friday\'', 'shh_friday', 'shh_cinema == \'lambs\'', 'shh_lambs')
image shh_scream = Movie(play=SHH + "images/bg/tv_scene/ghostface.webm")
image shh_friday = Movie(play=SHH + "images/bg/tv_scene/jason.webm")
image shh_scary = Movie(play=SHH + "images/bg/tv_scene/scary.webm")
image shh_lambs = Movie(play=SHH + "images/bg/tv_scene/chris_chan.webm")
image shh_halloween = Movie(play=SHH + "images/bg/tv_scene/myers.webm")
image shh_loading = Movie(play=SHH + "images/bg/tv_scene/loading.webm")
image shh_Timecard1 = Movie(play=SHH + "images/bg/tv_scene/Timecard1.webm")
image shh_Timecard2 = Movie(play=SHH + "images/bg/tv_scene/Timecard2.webm")
image shh_yt = SHH + "images/bg/tv_scene/yt.png"

image shh_slasher_title = SHH + "images/bg/slasher_titlecard.png"
image shh_door_c = SHH + "images/bg/door closed.jpg"
image shh_door_o = SHH + "images/bg/door wide open.jpg"
image shh_fridge_f = SHH + "images/bg/fridge1.png"
image shh_fridge_b = SHH + "images/bg/fridge2.jpg"
image shh_kitchen = SHH + "images/bg/kitchen_night.png"
image shh_trishhouse = SHH + "images/bg/trishhome_evening.png"
image shh_fangroom = SHH + "images/bg/fangroom_sntr.png"
image shh_hallway = SHH + "images/bg/hallway light.jpg"
image shh_hallway_e =  SHH + "images/bg/hallway edit.jpeg"
image shh_naserroom = SHH + "images/bg/naserroom.png"
image shh_door_e = SHH + "images/bg/door wide open empty.jpg"
image shh_neighborhood = SHH + "images/bg/neighborhood.png"
image shh_reedHouse = SHH + "images/bg/reedHouse.jpg"
image shh_crimeScene = SHH + "images/bg/crimeScene.jpg"
image shh_suburbRoad = SHH + "images/bg/suburb.jpg"
image shh_suburbRoadCar = SHH + "images/bg/suburbWithCar.jpg"
image shh_cityRoad = SHH + "images/bg/city.jpg"
image shh_cityRoadCar = SHH + "images/bg/cityWithCar.jpg"
image shh_mystery = SHH + "images/bg/wherehego.png"
image shh_sidewalk = SHH + "images/bg/sidewalkEdit.png"
image shh_curtain = SHH + "images/bg/Curtain.jpg"
image shh_sidewalk1 = SHH + "images/bg/sidewalk 1.png"
image shh_sidewalk2 = SHH + "images/bg/sidewalk 2.jpg"
image shh_sidewalk3 = SHH + "images/bg/sidewalk 3.jpg"
image shh_gmod = SHH + "images/bg/Trip.png"
image shh_police = SHH + "images/police.png"
image shh_cgfang1 = SHH + "images/bg/fangroom_night_1a.png"
image shh_cgfang2 = SHH + "images/bg/fangroom_night_2a.png"
image shh_cgfang3 = SHH + "images/bg/fangroom_night_3a.png"
image shh_cgfang4 = SHH + "images/bg/fangroom_night_4a.png"
image shh_cgfang5 = SHH + "images/bg/fangroom_night_5a.png"
image shh_cgkiller1 = SHH + "images/bg/fangroom_night_2c.png"
image shh_cgkiller2 = SHH + "images/bg/fangroom_night_3c.png"
image shh_trippin = SHH + "images/bg/anonface.png"
image shh_trippin2 = SHH + "images/bg/anonface2.png"
image shh_credits = SHH + "images/bg/credits large.png"

#Van stuff
image anon shh vanNeutral = SHH + "images/sprites/VanSprites/anon1.png"
image anon shh vanSpeaking = SHH + "images/sprites/VanSprites/anon2.png"
image anon shh vanSad = SHH + "images/sprites/VanSprites/anon3.png"
image fang shh vanNeutral = SHH + "images/sprites/VanSprites/fang1.png"
image fang shh vanSpeaking = SHH + "images/sprites/VanSprites/fang2.png"
image fang shh vanSmile = SHH + "images/sprites/VanSprites/fang3.png"
image fang shh vanScared = SHH + "images/sprites/VanSprites/fang4.png"
image reed shh vanNeutral = SHH + "images/sprites/VanSprites/reed2.png"
image reed shh vanSpeaking = SHH + "images/sprites/VanSprites/reed3.png"
image reed shh vanScared = SHH + "images/sprites/VanSprites/reed4.png"
image reed shh vanSmile = SHH + "images/sprites/VanSprites/reed1.png"
image trish shh lookLeft = SHH + "images/sprites/VanSprites/trish1.png"
image trish shh lookRight = SHH + "images/sprites/VanSprites/trish2.png"
image trish shh vanNeutral = SHH + "images/sprites/VanSprites/trish3.png"
image trish shh vanSpeaking = SHH + "images/sprites/VanSprites/trish4.png"
image trish shh vanScared = SHH + "images/sprites/VanSprites/trish5.png"
image shh_reedVan = SHH + "images/sprites/VanSprites/vanBase.png"

define Salvia_Text = WaveShader(amp = 0, melt="both", melt_params=(20,5.0,0.1))

image Salvia:
    "mods/Snoothouse of Horror/assets/images/bg/Trip.png"
    xysize (1920,1080)
    function WaveShader(period=15, amp=5.0, speed=0.25, direction='x', double="x")

image shh_white = "#ffffff"
define shh_flash = Fade(.25, 3.0, .75, color="#fff")

screen shh_exploration:   
     
     imagemap:
            if shh_location == "living_a":
                ground "images/backgrounds/home fang dim.webp"
                hotspot (0, 540, 400, 540) hovered SetVariable ('shh_new_location', 'KITCHEN') mouse 'hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('shh_slasher_kit') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
                hotspot (400, 0, 350, 540) hovered SetVariable ('shh_new_location', 'UPSTAIRS') mouse 'hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('shh_slasher_up') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
                hotspot (700, 350, 150, 300) hovered SetVariable ('shh_new_location', 'CELLAR') mouse 'hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('shh_slasher_cel') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
                hotspot  (1800, 270, 200, 540) hovered SetVariable ('shh_new_location', 'FRONT DOOR') mouse 'hover' action Play('sound', 'audio/ui/uiBack.wav'), Jump('shh_slasher_fd') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
            elif shh_location == "sfloor_a":
                ground SHH + "images/bg/hallway light.jpg"
                hotspot (600, 100, 200, 800) hovered SetVariable ('shh_new_location', 'FANG\'S ROOM') mouse 'hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('shh_slasher_fr') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
                hotspot (1000, 200, 200, 540) hovered SetVariable ('shh_new_location', 'PARENTS\' ROOM') mouse 'hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('shh_slasher_pr') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
                hotspot (700, 150, 150, 600) hovered SetVariable ('shh_new_location', 'NASER\'S ROOM') mouse 'hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('shh_slasher_nr') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
                hotspot (1300, 0, 320, 900) hovered SetVariable ('shh_new_location', 'LIVING ROOM') mouse 'hover' action Play('sound', 'audio/ui/uiBack.wav'), Jump('shh_slasher_lr') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
            elif shh_location == "sfloor_b":
                ground SHH + "images/bg/hallway edit.jpeg"
                hotspot (600, 100, 200, 800) hovered SetVariable ('shh_new_location', 'NO WAY I RETURN!') mouse 'hover' action Play('sound', 'audio/ui/uiFail.wav') unhovered SetVariable('shh_new_location', 'BACK TO THE DOOR')
                hotspot (1000, 200, 200, 540) hovered SetVariable ('shh_new_location', 'DON\'T CARE') mouse 'hover' action Play('sound', 'audio/ui/uiFail.wav') unhovered SetVariable('shh_new_location', 'BACK TO THE DOOR')
                hotspot (700, 150, 150, 600) hovered SetVariable ('shh_new_location', 'DOESN\'T MATTER') mouse 'hover' action Play('sound', 'audio/ui/uiFail.wav') unhovered SetVariable('shh_new_location', 'BACK TO THE DOOR')
                hotspot (1300, 0, 320, 900) hovered SetVariable ('shh_new_location', 'YES, OVER THERE!') mouse 'hover' action Play('sound', 'audio/ui/uiBack.wav'), Jump('shh_slasher_kill') unhovered SetVariable('shh_new_location', 'BACK TO THE DOOR')              
            elif shh_location == "living_b":
                ground "images/backgrounds/home fang dim.webp"
                hotspot (0, 540, 400, 540) hovered SetVariable ('shh_new_location', 'KITCHEN') mouse 'hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('shh_slasher_kit2') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
                hotspot (400, 0, 350, 540) hovered SetVariable ('shh_new_location', 'UPSTAIRS') mouse 'hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('shh_slasher_up_fin') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
                hotspot (700, 350, 150, 300) hovered SetVariable ('shh_new_location', 'CELLAR') mouse 'hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('shh_slasher_cel') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
                hotspot  (1800, 270, 200, 540) hovered SetVariable ('shh_new_location', 'FRONT DOOR') mouse 'hover' action Play('sound', 'audio/ui/uiBack.wav'), Jump('shh_slasher_fd') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
            elif shh_location == "kitchen":
                ground SHH + "images/bg/kitchen_night.png"
                hotspot (1200, 200, 250, 250) hovered SetVariable ('shh_new_location', 'THEY ARE HERE!') mouse 'hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('shh_slasher_kit3') unhovered SetVariable('shh_new_location', 'WHERE ARE KNIVES?')
            elif shh_location == "sfloor_c":
                ground SHH + "images/bg/hallway edit.jpeg"
                hotspot (600, 100, 200, 800) hovered SetVariable ('shh_new_location', 'FANG\'S ROOM') mouse 'hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('shh_slasher_fr_1') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
                hotspot (1000, 200, 200, 540) hovered SetVariable ('shh_new_location', 'PARENTS\' ROOM') mouse 'hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('shh_slasher_pr') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
                hotspot (700, 150, 150, 600) hovered SetVariable ('shh_new_location', 'NASER\'S ROOM') mouse 'hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('shh_slasher_nr_huh') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
                hotspot (1300, 0, 320, 900) hovered SetVariable ('shh_new_location', 'LIVING ROOM') mouse 'hover' action Play('sound', 'audio/ui/uiBack.wav'), Jump('shh_slasher_lr_1') unhovered SetVariable('shh_new_location', 'WHERE TO GO?')
            elif shh_location == "killer_door_a": #probably better sound is needed
                ground SHH + "images/bg/door wide open empty.jpg"
                hotspot (500,300,700,780) hovered SetVariable ('shh_new_location', 'HIT HIM!'), SetVariable('shh_zoom', shh_zoom + 0.1) mouse 'prompt' action Play('sound', 'audio/effects/clap.ogg'), MouseMove(700,300, duration=0.1), If(shh_hit_number > 4, true=Jump("shh_slasher_win"), false=SetVariable("shh_hit_number", shh_hit_number + 1)), SetVariable('shh_zoom', shh_zoom - 0.05) unhovered SetVariable('shh_new_location', ''), SetVariable('shh_zoom', shh_zoom + 0.1)
                timer 3.0 action Jump('shh_slasher_fd_gameover')       
            elif shh_location == "killer_door_b":
                ground SHH + "images/bg/fangroom_night_2c.png"
                hotspot (1000,300,400,500) hovered SetVariable ('shh_new_location', 'STAB HIM!') mouse 'prompt' action Play('sound', SHH + "audio/sfx/stab_2.ogg"), Jump('shh_slasher_fr_fin') unhovered SetVariable('shh_new_location', '')
                timer 1.0 action Jump('shh_slasher_fr_gameover')
             
     if shh_location == "killer_door_a":
         add SHH + "images/sprites/killergrab.png" zoom shh_zoom xcenter 0.5 ycenter 0.5
             
     add "gui/button/menubuttons/template_full_idle.png" xcenter 0.5 ycenter 0.8 zoom 1.5
     label "[shh_new_location!t]" xcenter 0.5 ycenter 0.8 text_size 80 text_color "#FFFFFF"
    
transform walking_cycle_aligned:
    easein 0.25 ycenter 0.68
    easein 0.25 ycenter 0.655
    repeat

transform walking_cycle_stop:
    ease 0.15 ycenter 0.655

screen shh_curtain_enter:
    
    add SHH + "images/bg/Curtain.jpg"
    timer 2.0 action Jump('shh_main_2')
     
# screen shh_inputcheck: #this shit was broken, still why not have it as a legacy comment
    # zorder 100
    # add "gui/button/menubuttons/template_full_idle.png" xcenter 0.4 ycenter 0.4 zoom 1.2
    # label _("ENTER THE WORD AND PRESS ENTER:") xcenter 0.8 ycenter 0.18 text_size 30 text_color "#FFFFFF" 
    # frame:
        # xcenter 0.85 ycenter 0.23
        # input value VariableInputValue('shh_word', default=True) length 5
    
    # if shh_knife_obtained == False:
      # label "HORNS >> " xcenter 0.75 ycenter 0.23  text_size 45 text_color "#FFFFFF"
    # else:   
      # label "KNIFE >> " xcenter 0.75 ycenter 0.23  text_size 45 text_color "#FFFFFF"
