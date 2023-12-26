WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

# offset
HITBOX_OFFSET = {
    'player': -26,
    'object': -40,
    'grass': -10,
    'invisible': 0}

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'resources/images/graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general color
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui color
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15,'graphic':'resources/images/graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30,'graphic':'resources/images/graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic':'resources/images/graphics/weapons/axe/full.png'},
    'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'resources/images/graphics/weapons/rapier/full.png'},
    'sai':{'cooldown': 80, 'damage': 10, 'graphic':'resources/images/graphics/weapons/sai/full.png'}
}

# magic
magic_data = {
    'flame': {'strength': 15, 'cost': 20,
            'graphic': 'resources/images/graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10,
            'graphic': 'resources/images/graphics/particles/heal/heal.png'}

}

# enemy
monster_data = {
    'squid': {'health': 300, 'exp': 80, 'damage': 40, 'attack_type': 'slash', 'attack_sound': 'resources/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 800, 'exp': 1000, 'damage': 60, 'attack_type': 'claw', 'attack_sound': 'resources/audio/attack/claw.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 10, 'exp': 100, 'damage': 500, 'attack_type': 'thunder', 'attack_sound': 'resources/audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 150, 'exp': 80, 'damage': 21, 'attack_type': 'leaf_attack', 'attack_sound': 'resources/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}

}

