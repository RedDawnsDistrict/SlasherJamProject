init:
    $ DW = "mods/Dweebshow/assets/"


#There's a bunch of different narrators in the slasher arc, so I thought it would be less confusing to have character tags for'em
define base = Character (ctc="ctc_end_marker", ctc_pause="ctc_mid_marker", ctc_timedpause=Null(), ctc_position="nestled-close")
define DW_F = Character(_('Fang\'s Mind'), base, color="#B4D4CE", who_outlines=[(gui.name_text_thickness, '#0F3930')])
define DW_A = Character(_('Anon\'s Mind'), base, color="#36E12D", who_outlines=[(gui.name_text_thickness, '#0C300A')])
define DW_R = Character(_('Reed\'s Mind'), base, color="#ED4C5B", who_outlines=[(gui.name_text_thickness, '#421014')])
define DW_T = Character(_('Trish\'s Mind'), base, color="#B675E6", who_outlines=[(gui.name_text_thickness, '#3A0C5D')])

image killer dw = DW + "images/sprites/slasher_neutral.png"
image fc dw neutral = DW + "images/sprites/fc_neutral_slasher.png"
image fc dw listen = DW + "images/sprites/fc_listen_slasher.png"
image fc dw blush = DW + "images/sprites/fc_blush_blush.png"