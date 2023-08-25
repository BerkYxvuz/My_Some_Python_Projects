from ursina import *
from ursina.prefabs.health_bar import HealthBar
from ursina.shaders import *
import pyautogui
screenWidth, screenHeight = pyautogui.size()
app = Ursina(size=(1366, 768))
global porksay
porksay = 0
porktext = Text(porksay, scale=2)
porktext.position = (-.59, .37, -.2)
camera.orthographic = True

camera.fov = 11
global player
player = Entity(model='quad',
                texture='Pan_Blue_Circle.png',
                position=(10, 10, -1),
                scale=(0.7, 0.7))
camera.position = (player.x, player.y)
uya = ""
uyari = Text(uya, color=color.red, scale=(2, 2), position=(-.15, .40))

terrain_width = 20
terrain_height = 20

for i in range(terrain_width * terrain_width):
    ihtimal = random.randint(90,100)
    if i % ihtimal == 0:
        cube = Entity(model='quad', texture='sulugrass', collider='box')
    else:
        cube = Entity(model='quad', texture='grass', collider='box')
    cube.x = floor(i / terrain_width)
    cube.y = floor(i % terrain_width)
    cube.z = 0

from ursina import *



aclik = HealthBar(bar_color = color.brown,
                  roundness=.5,
                  scale=(0.3, .04),
                  position=(-.85, -.30, -.1),
                  )

HB1 = HealthBar(bar_color=color.red,
                roundness=.5,
                scale=(0.3, .04),
                position=(-.85, -.40, -.1))
global Energy
Energy = HealthBar(bar_color=color.yellow,
                roundness=.5,
                scale=(0.3, .04),
                position=(-.85, -.35, -.1),
                text_color = color.black)

# Karakter Envanteri.
class Inventory(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(.4, .3),
            origin=(-.2, .5),
            position=(-.7, .4, -.1),
            texture='white_cube',
            texture_scale=(4, 3)
        )

class Craft(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(.3, .4),
            origin=(-.5, .5),
            position=(.5, .4),
            texture='white_cube',
            texture_scale=(3, 4),
            color=color.random_color()
            )
        self.item_parent = Entity(parent=self, scale=(1 / 5, 1 / 8))
global coalsay
coalsay = 0
coaltext_x = 45
coaltext_y = -13
coals = Text(coalsay, scale=2)
coals.position = (-.78, .37, -.2)

inventory = Inventory()
inventory.visible = False
coals.visible = False


craftingtable = Craft()

coalicon = Entity(
            parent=camera.ui,
            model='quad',
            scale=(.2, .2),
            origin=(.3 + 0.02, .5),
            position=(-.7, .5/1.12, -.1),
            texture='coal.png',
            texture_scale=(1, 1)
        )
def porkclick():
    global porksay
    if aclik.value < 100 and porksay > 0:
        aclik.value += 10
        porksay -= 1
        porktext.text = porksay

pork = Button(
            parent=camera.ui,
            model='quad',
            scale=(1/9, 1/9),
            origin=(.6, .9),
            position=(-.5, .5/1.12, -.1),
            texture='pork.png',
            color=color.white,
            on_click=porkclick
        )


porktext.visible = False
pork.visible = False
woodicon = Entity(
            parent=camera.ui,
            model='quad',
            scale=(.1/1.1, .1/1.1),
            origin=(.8, .9),
            position=(-.6, .5/1.15, -.1),
            texture='wood.png',
        )
woodicon.visible = False
coalicon.visible = False


craftingtable.visible = False
house = Button(model='quad' , origin=(.5, .5), texture='home.png', color=color.gray)
house.position = (.6, .4, -.2)
house.scale = (.1,.1)
house.visible = False
campfire = Button(model='quad', origin=(.5, .5), texture='campfire.png', color=color.gray)
campfire.position = (.7, .4, -.2)
campfire.scale = (.1,.1)
campfire.visible = False



def kampatesi():
    global coalsay
    global uya
    if x >= 5 and coalsay >= 3:
        PlayerCampFire_x = player.get_x()
        PlayerCampFire_y = player.get_y()
        PlayerCampFire = Entity(model='quad', texture='campfire.png',)
        PlayerCampFire.position = (PlayerCampFire_x, PlayerCampFire_y, -1)
        coalsay -= 3
        coals.text = coalsay
    else:
        uya="Kaynak Yeterli Değil."
        uyari.text = uya
        pass

campfire.on_click = kampatesi


global x
x = 0

woodstext_x = 45
woodstext_y = -13
woodshm = Text(x, scale=2)
woodshm.position = (-.69, .37, -.2)
woodshm.visible = False
def evyap():
    global x
    global PlayerHouse
    global PlayerHouse_x
    global PlayerHouse_y
    if x >= 15:
        PlayerHouse_x = player.get_x()
        PlayerHouse_y = player.get_y()
        PlayerHouse.position = (PlayerHouse_x, PlayerHouse_y, -1)
        x -= 15
        woodshm.text = x
    else:
        uya = "Kaynak Yeterli Değil."
        uyari.text = uya
        pass

house.on_click=evyap
global evde
evde = False
def evegir():
    global evde
    global PlayerHouse_x
    global PlayerHouse_y
    global leaver
    evde = True
    if distance(player,PlayerHouse)<1:
        player.position = (PlayerHouse_x, PlayerHouse_y, 1)
        leaver = Button(model='quad', texture='exit.png', color=color.gray)
        leaver.position = (-.40, .40, -.1)
        leaver.scale = (.1, .1/2)
        leaver.on_click = cikis
    else:
        pass

def cikis():
    global leaver
    global evde
    player.position = (PlayerHouse_x, PlayerHouse_y, -1)
    leaver.hide()

    evde = False

PlayerHouse = Entity(model='quad', texture='home.png',collider='box', on_click=evegir,position=(0,0,2))
PlayerHouse.on_click = evegir

import random

class Domuz:
    def __init__(self):
        self.health = 5
        self.entity = Entity(model='quad', collider='sphere', texture='pig.png', z=-1)
        self.entity.position = (random.randint(0, 19), random.randint(0, 19), -.1)
        self.entity.scale = (0.7, 0.7)
        self.entity.on_click = self.damage


    def hareket(self):
        domuzsecenekler = ["W", "S", "A", "D"]
        self.secilen = random.choice(domuzsecenekler)
        if self.health != 0:
            if self.secilen == "W":
                self.entity.x += 0.1

            if self.secilen == "S":
                self.entity.y -= 0.1

            if self.secilen == "A":
                self.entity.x -= 0.1

            if self.secilen == "D":
                self.entity.x += 0.1


    def reset_color(self):
        self.entity.color = color.white
    def damage(self):
        if distance(player, self.entity) < 2:
            global porksay
            self.healthbar = HealthBar(bar_color=color.red,
                                       roundness=2,
                                       scale=(1, 0.3),
                                       position=(self.entity.position.x, self.entity.position.y + 1, -2))
            porksay += 1
            porktext.text = porksay
            self.health -= 1
            Energy.value -= 10
            self.entity.shake()
            self.entity.color = color.red
            invoke(self.reset_color, delay=0.5)
            if self.health == 0:
                destroy(self.entity)
class Atesett(Entity):
    def __init__(self, position, target):
        super().__init__(
            model='quad',
            texture='rock.png',
            collider='box',
            position=(player.x, player.y, -.1))
        self.animate_position(target)
        destroy(self, delay=2)
class iskelet:
    def __init__(self):
        self.health = 5
        self.entity = Entity(model='quad', collider='box', texture='iskelet.jpg', z=-1)
        self.entity.position = (random.randint(0, 19), random.randint(0, 19), -.1)
        self.entity.scale = (0.7, 0.7)
        self.entity.on_click = self.damage

    def iskelethareket(self):
        domuzsecenekler = ["W", "S", "A", "D"]
        self.secilen = random.choice(domuzsecenekler)
        if self.health != 0:
            if self.secilen == "W":
                self.entity.x += 0.1

            if self.secilen == "S":
                self.entity.y -= 0.1

            if self.secilen == "A":
                self.entity.x -= 0.1

            if self.secilen == "D":
                self.entity.x += 0.1

    def on_collision_enter(self, entity):
        if entity.name == 'Atesett':
            print('Atesett ile collision gerçekleşti!')
        else:
            print('Başka bir entity ile collision gerçekleşti!')
    def reset_color(self):
        self.entity.color = color.white
    def damage(self):
        if distance(player, self.entity) < 2:
            self.health -= 1
            Energy.value -= 10
            self.entity.shake()
            self.entity.color = color.red
            invoke(self.reset_color, delay=0.5)
            if self.health == 0:
                destroy(self.entity)
iskelet1 = iskelet()
class coal:
    def __init__(self):
        self.coalhealth = 0
        self.entity = Entity(model='quad', texture='coal.png', collider='box')
        self.entity.scale = (1, 1, 1)
        self.entity.position = (random.randint(0, 19), random.randint(0, 19), -1)
        self.entity.on_click = self.coalclick
    def coalclick(self):
        global coalsay
        if distance(player, self.entity) < 1 and Energy.value >= 5 and self.coalhealth < 10:
            coalsay += 1
            coals.text = coalsay
            Energy.value -= 5
            Energy.text = "Enerji: " + str(Energy.value)
            self.coalhealth += 1
            self.entity.shake()
        if self.coalhealth == 10:
            self.entity.hide()

class Tree:
    def __init__(self):
        self.health = 0
        self.entity = Entity(model='quad', texture='agac.png', collider='box')
        self.entity.scale = (0.7, 0.7, 0.7)
        self.entity.position = (random.randint(0, 19), random.randint(0, 19), -1)
        self.entity.on_click = self.click

    def click(self):
        global x
        if distance(player, self.entity) < 1 and Energy.value >= 5 and self.health < 5:
            x += 1
            self.health += 1
            woodshm.text = x
            Energy.value -= 5
            Energy.text = "Enerji: " + str(Energy.value)
            self.entity.shake()
        if self.health >= 5:
            self.entity.texture = 'kutuk.png'

#NESNELERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
tree1 = Tree()
tree2 = Tree()
tree3 = Tree()
tree4 = Tree()
tree5 = Tree()
tree6 = Tree()
tree7 = Tree()
tree8 = Tree()
coal1 = coal()
coal2 = coal()
coal3 = coal()
coal4 = coal()
coal5 = coal()
domuz1 = Domuz()
domuz2 = Domuz()

global zombiespawnval
global sayyy
global zombiespawned
zombiespawned = False
sayyy=0
gece = False
zombiespawnval = 0
global zombieq
zombie = Entity()
class Sword(Entity):
    def __init__(self, position, target):
        super().__init__(
            model='quad',
            texture='sword.png',
            position=(player.x, player.y, -1))
        self.animate_position(target)

def input(key):
    if key == 'q':
        global iskelet1
        mouse_position = mouse.world_point
        Atesett(
            position=(player.x, player.y, -.1),
            target=(mouse_position.x, mouse_position.y))

    if key == 'b':
        house.visible = not house.visible
        campfire.visible = not campfire.visible
        craftingtable.visible = not craftingtable.visible
    if key == 'tab':
        inventory.visible = not inventory.visible
        coals.visible = not coals.visible
        coalicon.visible = not coalicon.visible
        woodshm.visible = not woodshm.visible
        woodicon.visible = not woodicon.visible
        pork.visible = not pork.visible
        porktext.visible = not porktext.visible

zombieposy = random.randint(0, 10)
zombieposx = random.randint(0, 10)
zombihby = zombieposy + 1
zombihbx = zombieposx - 0.5
zombiehb = HealthBar(bar_color=color.red,
                             parent=zombie,
                             roundness=.2,
                             scale=(1, 0.3),
                             position=(zombihbx, zombihby, -.1))
if gece == False:
    zombiehb.visible = False
Ateset = None
def update():
    global domuz1, gece, evde ,zombie,Energy,sayyy,yas,zombiespawnval,zombiespawned,zombiex,zombiey,ateset
    sayyy += 1
    if sayyy % 100 == 0:
        domuz1.hareket()
        domuz2.hareket()
    if sayyy % 400 == 0:
        aclik.value -= 1
        aclik.text = "Açlık: " + str(aclik.value)

    if player.x > terrain_width:
        if held_keys["a"]:
            player.x += 1
        if held_keys["d"]:
            player.x -= 1
    if player.y > terrain_height:
        if held_keys["s"]:
            player.y += 1
        if held_keys["w"]:
            player.y -= 1
    if player.x < 0:
        player.x += 1
    if player.y < 0:
        player.y += 1
    if held_keys["w"] and evde == False:
        player.y += 0.1
        player_x = player.get_x()
        player_y = player.get_y()
        camera.position = (player_x, player_y)
    if held_keys["s"] and evde == False:
        player.y -= 0.1
        player_x = player.get_x()
        player_y = player.get_y()
        camera.position = (player_x, player_y)
    if held_keys["d"] and evde == False:
        player.x += 0.1
        player_x = player.get_x()
        player_y = player.get_y()
        camera.position = (player_x, player_y)
    if held_keys["a"] and evde == False:
        player.x -= 0.1
        player_x = player.get_x()
        player_y = player.get_y()
        camera.position = (player_x, player_y)
    if sayyy % 30 == 0:
        Energy.value += 1
    if sayyy % 80 == 0:
        uya=""
        uyari.text = uya
    if sayyy % 3000 == 0 and gece==False:
        camera.z = -2
        camera.shader = basic_lighting_shader
        gece = True
        zombiespawnval += 1
    if sayyy == 6000:
        sayyy -= 6000
        camera.shader = None
        gece = False

    if zombiespawnval == 1:
        global zombie
        zombiehb.visible = True
        zombie = Entity(model='quad', texture='zombie.jpg', scale=(0.7, 0.7), collider="sphere",)
        zombie.x = zombieposx
        zombie.y = zombieposy
        zombie.z = -1

        zombiespawned = True
        zombiespawnval += 1

    if zombiespawned == True:

        if distance(zombie,player) < 0.8:
            HB1.value -= 0.5
            HB1.text = "Can: " + str(HB1.value)
        if player.get_x() - zombie.get_x() < 0:
            zombie.x -= 0.01
            zombiehb.x -= 0.01
        if player.get_x() - zombie.get_x() > 0:
            zombie.x += 0.01
            zombiehb.x += 0.01
        if player.get_y() - zombie.get_y() < 0:
            zombie.y -= 0.01
            zombiehb.y -= 0.01
        if player.get_y() - zombie.get_y() > 0:
            zombie.y += 0.01
            zombiehb.y += 0.01
    if not held_keys["a"] and not held_keys["d"] and not held_keys["s"] and not held_keys["w"] and distance(player,zombie) > 1:
        HB1.value += 0.5
    if zombie.intersects(Atesett).hit:
        zombiehb.value -= 20
        zombie.shake()
        if zombiehb.value == 0:
            zombiespawned = False
            zombie.z = 1
        else:
            pass

app.run()