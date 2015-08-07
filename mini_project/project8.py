# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
SCREEN = [WIDTH, HEIGHT]
LIFE_POS = [50, 50]
SCORE_POS = [50, 70]
time = 0
time2 = 0
started = False
ROCK_NUMBER = 12
# determine a circle around my ship that the rock won't spawn in it.
SAFE_RADIUS = 300

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.life = 3 # life initialization
        self.score = 0 # score initialization
    
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def draw(self,canvas):
        #draw score and life
        canvas.draw_text('life:' + str(self.life), LIFE_POS, 20, "White")
        canvas.draw_text('score:' + str(self.score), SCORE_POS, 20, "White")
        if self.thrust:
            ship_thrust_sound.set_volume(0.9)
            ship_thrust_sound.play()
            self.image_center = [135, 45]
            
        else:
            ship_thrust_sound.rewind()
            self.image_center = [45, 45]
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle )

    def update(self):

        forward_vector = angle_to_vector(self.angle)

        accele_constant = 1.0
        friction_constant = 0.04
        for dimen in range(2):
            self.pos[dimen] = (self.pos[dimen] + self.vel[dimen]) % SCREEN[dimen]
            if self.thrust:
                self.vel[dimen] = self.vel[dimen] * (1 - friction_constant) + forward_vector[dimen] * accele_constant
            else:
                self.vel[dimen] = self.vel[dimen] * (1 - friction_constant)
        self.angle += self.angle_vel
    
    def keydown_handler(self, key):
        if key == simplegui.KEY_MAP['up']:
            self.thrust = True
        elif key == simplegui.KEY_MAP['left']:
            self.angle_vel = -0.05
        elif key == simplegui.KEY_MAP['right']:
            self.angle_vel = 0.05
        elif key == simplegui.KEY_MAP['space']:
        #launch missile
            self.shoot()
        else:
            pass
    def keyup_handler(self, key):
        if key == simplegui.KEY_MAP['up']:
            self.thrust = False
        elif key == simplegui.KEY_MAP['left']:
            self.angle_vel = 0.0
        elif key == simplegui.KEY_MAP['right']:
            self.angle_vel = 0.0
        elif key == simplegui.KEY_MAP['space']:
            pass
        else:
            self.thrust = False
            self.angle_vel = 0
            
    def shoot(self):
        forward_vector = angle_to_vector(self.angle)
        missile_constant = 4
        vel_x = self.vel[0] + forward_vector[0] * missile_constant
        vel_y = self.vel[1] + forward_vector[1] * missile_constant
        pos_x = self.pos[0] + forward_vector[0] * self.radius
        pos_y = self.pos[1] + forward_vector[1] * self.radius
        missile = Sprite([pos_x, pos_y], [vel_x, vel_y], 0, 0, missile_image, missile_info, sound = missile_sound)
        missile_group.add(missile)
        
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
    
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def draw(self, canvas):
        if self.animated:
            global time2
            current_index = (time2 % 24) // 1
            current_center = [self.image_center[0] + current_index * self.image_size[0], self.image_center[1]]
            canvas.draw_image(self.image, current_center, self.image_size, self.pos, self.image_size, self.angle)
            time2 += 1
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        for dimen in range(2):
            self.pos[dimen] = (self.pos[dimen] + self.vel[dimen]) % SCREEN[dimen]
        self.angle += self.angle_vel
        
        self.age += 1
        if self.age >= self.lifespan:
            return True
        else:
            return False
    
    def collide(self, other_object):
        distance = dist(self.get_position(), other_object.get_position())
        if distance >= self.get_radius() + other_object.get_radius():
            return False
        else:
            return True
    
    
           
def draw(canvas):
    global time, started
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
        return    
    
    # draw and update ship
    my_ship.draw(canvas)
    my_ship.update()

    # draw and update rock group
    process_sprite_group(canvas, rock_group)
    
    # draw and update missile group
    process_sprite_group(canvas, missile_group)
    
    # process collision between ship and rock group
    collision = group_collide(rock_group, my_ship)
    if collision:
        my_ship.life -= 1
    
    # process collision between rock_group and missile_group
    number_rock_destroy = group_group_collide(rock_group, missile_group)
    
    # draw and update explosion group
    process_sprite_group(canvas, explosion_group)
    
    # update my ship's score
    my_ship.score += number_rock_destroy * 100
    
    if my_ship.life <= 0:
        new_game()
    
# take a set and a canvas and call the update and draw methods for each sprite in the group
def process_sprite_group(canvas, sprite_group):
    for sprite in list(sprite_group):
        sprite.draw(canvas)
        #if the sprite's age exceed its lifespan
        go_dead = sprite.update()
        if go_dead:
            sprite_group.remove(sprite)
            
# take a set group and a other_object and check for collision between other_object and 
# elements of the group. Remove item from group if it collide with other_object.
# At last, return whether there is a collision occur.
def group_collide(group, other_object):
    collision = False
    for item in list(group):
        if item.collide(other_object):
            group.remove(item)
            collision = True
            explosion = Sprite(other_object.get_position(), [0, 0], 0, 0, explosion_image, explosion_info, explosion_sound)
            explosion_group.add(explosion)
    return collision 

# check collision between two groups
def group_group_collide(group, other_group):
    # number of item collided in first group
    number_collide = 0
    for item in list(group):
        if group_collide(other_group, item):
            group.remove(item)
            number_collide += 1
    return number_collide

# timer handler that spawns a rock    
def rock_spawner():
    if len(rock_group) + 1>= ROCK_NUMBER:
        return
    pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    while dist(pos, my_ship.get_position()) < SAFE_RADIUS:
        pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    # the velocity of rock is basing on the current score of my ship
    vel = [random.randrange(-5, 5) / 10.0 + my_ship.score / 2000.0, random.randrange(-5, 5) / 10.0 + my_ship.score / 2000.0]
    ang = random.randrange(0, 628) / 100.0 
    ang_vel = random.randrange(0, 10)/100.0
    rock = Sprite(pos, vel, ang, ang_vel, asteroid_image, asteroid_info)
    rock_group.add(rock)
    
# keydown handler
def keydown(key):
    my_ship.keydown_handler(key)

# keyup handler
def keyup(key):
    my_ship.keyup_handler(key)
    
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        soundtrack.rewind()
        soundtrack.play()

# start a new game
def new_game():
    global my_ship, rock_group, missile_group, time, started
    my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
    rock_group = set()
    missile_group = set()
    explosion_group = set()
    time = 0
    started = False
    soundtrack.pause()
        
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set()
missile_group = set()
explosion_group = set()

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
