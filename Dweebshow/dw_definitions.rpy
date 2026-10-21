init:
    $ DW = "mods/Dweebshow/assets/"

define config.mouse = {"dw_hover":[(DW + "images/cursor.png", 0, 0)]}
define base = Character (ctc="ctc_end_marker", ctc_pause="ctc_mid_marker", ctc_timedpause=Null(), ctc_position="nestled-close")
define DW_Ri = Character (_("Ripley"), base, color="#D8A09A", who_outlines=[(gui.name_text_thickness, '#461B1F')])

default dw_cinema = "null"
default dw_new_location = "WHERE TO GO?"
default dw_cellar_seen = False
default dw_naser_seen = False
default dw_knife_obtained = False
default dw_parents_seen = False
default dw_location = "living_a"
default dw_word = "DEATH"

image killer dw = DW + "images/sprites/slasher_neutral.png"
image killer dw weapon = DW + "images/sprites/slasher_slash.png"
image killer dw front = DW + "images/sprites/killergrab.png"
image killer dw shoulder = DW + "images/sprites/shoulder.png"
image arms dw = DW + "images/sprites/slasher_arms.png"
image knife dw = DW + "images/sprites/fangroom_night_knife.png"
image reed dw shocked = DW + "images/sprites/reed shockedPOV.webp"
image fang dw grin = DW + "images/sprites/fang grin.png"
image anon dw held = DW + "images/sprites/anon held.png"
image fangdad dw angry = DW + "images/sprites/ripley angry.webp"
image fangdad dw sad = DW + "images/sprites/ripley sad.png"
image fangdad dw shocked = DW + "images/sprites/ripley shocked.webp"

image dw_tv = DW + "images/bg/tv_scene/tv.png"
image dw_couch = DW + "images/bg/tv_scene/couch.png"
image dw_nflix = DW + "images/bg/tv_scene/N.png"
image dw_current = ConditionSwitch ('dw_cinema == \'scream\'', 'dw_scream', 'dw_cinema == \'halloween\'', 'dw_halloween', 'dw_cinema == \'friday\'', 'dw_friday', 'dw_cinema == \'lambs\'', 'dw_lambs')
image dw_scream = Movie(play=DW + "images/bg/tv_scene/ghostface.webm")
image dw_friday = Movie(play=DW + "images/bg/tv_scene/jason.webm")
image dw_scary = Movie(play=DW + "images/bg/tv_scene/scary.webm")
image dw_lambs = Movie(play=DW + "images/bg/tv_scene/chris_chan.webm")
image dw_halloween = Movie(play=DW + "images/bg/tv_scene/myers.webm")
image dw_loading = Movie(play=DW + "images/bg/tv_scene/loading.webm")
image dw_yt = DW + "images/bg/tv_scene/yt.png"
image dw_door_c = DW + "images/bg/door closed.jpg"
image dw_door_o = DW + "images/bg/door wide open.jpg"
image dw_fridge_f = DW + "images/bg/fridge1.png"
image dw_fridge_b = DW + "images/bg/fridge2.jpg"
image dw_kitchen = DW + "images/bg/kitchen_night.png"
image dw_trishhouse = DW + "images/bg/trishhome_evening.png"
image dw_fangroom = DW + "images/bg/fangroom_sntr.png"
image dw_hallway = DW + "images/bg/hallway light.jpg"
image dw_hallway_e =  DW + "images/bg/hallway edit.jpeg"
image dw_naserroom = DW + "images/bg/naserroom.png"
image dw_door_e = DW + "images/bg/door wide open empty.jpg"
image dw_neighborhood = DW + "images/bg/neighborhood.png"
image dw_reedHouse = DW + "images/bg/reedHouse.jpg"
image dw_crimeScene = DW + "images/bg/crimeScene.jpg"
image dw_suburbRoad = DW + "images/bg/suburb.jpg"
image dw_suburbRoadCar = DW + "images/bg/suburbWithCar.jpg"
image dw_cityRoad = DW + "images/bg/city.jpg"
image dw_cityRoadCar = DW + "images/bg/cityWithCar.jpg"
image dw_mystery = DW + "images/bg/wherehego.png"
image dw_sidewalk = DW + "images/bg/sidewalkEdit.png"

image dw_cgfang1 = DW + "images/bg/fangroom_night_1a.png"
image dw_cgfang2 = DW + "images/bg/fangroom_night_2a.png"
image dw_cgfang3 = DW + "images/bg/fangroom_night_3a.png"
image dw_cgfang4 = DW + "images/bg/fangroom_night_4a.png"
image dw_cgfang5 = DW + "images/bg/fangroom_night_5a.png"
image dw_cgkiller1 = DW + "images/bg/fangroom_night_2c.png"
image dw_cgkiller2 = DW + "images/bg/fangroom_night_3c.png"
image dw_trippin = DW + "images/bg/anonface.png"
image dw_credits = DW + "images/bg/credits large.png"

image anon dw vanNeutral = DW + "images/sprites/VanSprites/anon1.png"
image anon dw vanSpeaking = DW + "images/sprites/VanSprites/anon2.png"
image anon dw vanSad = DW + "images/sprites/VanSprites/anon3.png"
image fang dw vanNeutral = DW + "images/sprites/VanSprites/fang1.png"
image fang dw vanSpeaking = DW + "images/sprites/VanSprites/fang2.png"
image reed dw vanNeutral = DW + "images/sprites/VanSprites/reed2.png"
image reed dw vanSpeaking = DW + "images/sprites/VanSprites/reed3.png"
image reed dw vanSmile = DW + "images/sprites/VanSprites/reed1.png"
image trish dw lookLeft = DW + "images/sprites/VanSprites/trish1.png"
image trish dw lookRight = DW + "images/sprites/VanSprites/trish2.png"
image trish dw vanNeutral = DW + "images/sprites/VanSprites/trish3.png"
image trish dw vanSpeaking = DW + "images/sprites/VanSprites/trish4.png"
image dw_reedVan = DW + "images/sprites/VanSprites/vanBase.png"

# screen dw_inputcheck:
    # zorder 100
    # add "gui/button/menubuttons/template_full_idle.png" xcenter 0.4 ycenter 0.4 zoom 1.2
    # label _("ENTER THE WORD AND PRESS ENTER:") xcenter 0.8 ycenter 0.18 text_size 30 text_color "#FFFFFF" 
    # frame:
        # xcenter 0.85 ycenter 0.23
        # input value VariableInputValue('dw_word', default=True) length 5
    
    # if dw_knife_obtained == False:
      # label "HORNS >> " xcenter 0.75 ycenter 0.23  text_size 45 text_color "#FFFFFF"
    # else:   
      # label "KNIFE >> " xcenter 0.75 ycenter 0.23  text_size 45 text_color "#FFFFFF"

screen dw_exploration:   
    
    imagemap:
            if dw_location == "living_a":
                ground "images/backgrounds/home fang dim.webp"
                hotspot (0, 540, 400, 540) hovered SetVariable ('dw_new_location', 'KITCHEN') mouse 'dw_hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('dw_slasher_kit') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
                hotspot (400, 0, 350, 540) hovered SetVariable ('dw_new_location', 'UPSTAIRS') mouse 'dw_hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('dw_slasher_up') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
                hotspot (700, 350, 150, 300) hovered SetVariable ('dw_new_location', 'CELLAR') mouse 'dw_hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('dw_slasher_cel') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
                hotspot  (1800, 270, 200, 540) hovered SetVariable ('dw_new_location', 'FRONT DOOR') mouse 'dw_hover' action Play('sound', 'audio/ui/uiBack.wav'), Jump('dw_slasher_fd') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
            elif dw_location == "sfloor_a":
                ground DW + "images/bg/hallway light.jpg"
                hotspot (600, 100, 200, 800) hovered SetVariable ('dw_new_location', 'FANG\'S ROOM') mouse 'dw_hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('dw_slasher_fr') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
                hotspot (1000, 200, 200, 540) hovered SetVariable ('dw_new_location', 'PARENTS\' ROOM') mouse 'dw_hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('dw_slasher_pr') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
                hotspot (700, 150, 150, 600) hovered SetVariable ('dw_new_location', 'NASER\'S ROOM') mouse 'dw_hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('dw_slasher_nr') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
                hotspot (1300, 0, 320, 900) hovered SetVariable ('dw_new_location', 'LIVING ROOM') mouse 'dw_hover' action Play('sound', 'audio/ui/uiBack.wav'), Jump('dw_slasher_lr') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
            elif dw_location == "sfloor_b":
                ground DW + "images/bg/hallway edit.jpeg"
                hotspot (600, 100, 200, 800) hovered SetVariable ('dw_new_location', 'NO WAY I RETURN!') mouse 'dw_hover' action Play('sound', 'audio/ui/uiFail.wav') unhovered SetVariable('dw_new_location', 'BACK TO THE DOOR')
                hotspot (1000, 200, 200, 540) hovered SetVariable ('dw_new_location', 'DON\'T CARE') mouse 'dw_hover' action Play('sound', 'audio/ui/uiFail.wav') unhovered SetVariable('dw_new_location', 'BACK TO THE DOOR')
                hotspot (700, 150, 150, 600) hovered SetVariable ('dw_new_location', 'DOESN\'T MATTER') mouse 'dw_hover' action Play('sound', 'audio/ui/uiFail.wav') unhovered SetVariable('dw_new_location', 'BACK TO THE DOOR')
                hotspot (1300, 0, 320, 900) hovered SetVariable ('dw_new_location', 'YES, OVER HERE') mouse 'dw_hover' action Play('sound', 'audio/ui/uiBack.wav'), Jump('dw_slasher_kill') unhovered SetVariable('dw_new_location', 'BACK TO THE DOOR')              
            elif dw_location == "living_b":
                ground "images/backgrounds/home fang dim.webp"
                hotspot (0, 540, 400, 540) hovered SetVariable ('dw_new_location', 'KITCHEN') mouse 'dw_hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('dw_slasher_kit2') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
                hotspot (400, 0, 350, 540) hovered SetVariable ('dw_new_location', 'UPSTAIRS') mouse 'dw_hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('dw_slasher_up_fin') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
                hotspot (700, 350, 150, 300) hovered SetVariable ('dw_new_location', 'CELLAR') mouse 'dw_hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('dw_slasher_cel') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
                hotspot  (1800, 270, 200, 540) hovered SetVariable ('dw_new_location', 'FRONT DOOR') mouse 'dw_hover' action Play('sound', 'audio/ui/uiBack.wav'), Jump('dw_slasher_fd') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
            elif dw_location == "kitchen":
                ground DW + "images/bg/kitchen_night.png"
                hotspot (1400, 200, 100, 200) hovered SetVariable ('dw_new_location', 'THEY ARE HERE') mouse 'dw_hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('dw_slasher_kit3') unhovered SetVariable('dw_new_location', 'WHERE ARE KNIVES?')
            elif dw_location == "sfloor_c":
                ground DW + "images/bg/hallway edit.jpeg"
                hotspot (600, 100, 200, 800) hovered SetVariable ('dw_new_location', 'FANG\'S ROOM') mouse 'dw_hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('dw_slasher_fr_1') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
                hotspot (1000, 200, 200, 540) hovered SetVariable ('dw_new_location', 'PARENTS\' ROOM') mouse 'dw_hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('dw_slasher_pr') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
                hotspot (700, 150, 150, 600) hovered SetVariable ('dw_new_location', 'NASER\'S ROOM') mouse 'dw_hover' action Play('sound', 'audio/ui/uiClick.wav'), Jump('dw_slasher_nr_huh') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
                hotspot (1300, 0, 320, 900) hovered SetVariable ('dw_new_location', 'LIVING ROOM') mouse 'dw_hover' action Play('sound', 'audio/ui/uiBack.wav'), Jump('dw_slasher_lr_1') unhovered SetVariable('dw_new_location', 'WHERE TO GO?')
            
    add "gui/button/menubuttons/template_full_idle.png" xcenter 0.5 ycenter 0.8 zoom 1.5
    label "[dw_new_location!t]" xcenter 0.5 ycenter 0.8 text_size 80 text_color "#FFFFFF"
    
# walk cycle script
transform walking_cycle_aligned:
    easein 0.25 yalign .075
    easein 0.25 yalign .09
    repeat

# stop at current position
transform walking_cycle_stop:
    ease 0.15 yalign .1