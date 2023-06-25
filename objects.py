import pygame

class Ball:
    # constructor
    def __init__(self, x, y, radius, dx, dy, ball_color):
        self.x = x
        self.y = y
        self.raidus = radius
        self.dx = dx
        self.dy = dy
        self.ball_color = ball_color

    # Draw the ball attribute as surface, (color value), (x, y), ball raidus)
    def draw(self, surface):
        pygame.draw.circle(surface, self.ball_color, (self.x, self.y), self.raidus)

    # 
    def update_new_pos(self):
        self.x += self.dx
        self.y += self.dy

    # get obj rect (left, top, width, height)
    def get_rect(self):
        return pygame.Rect(self.x - self.raidus, self.y - self.raidus, self.raidus * 2, self.raidus * 2)

    # check if self collide base on the given obj
    def colliderect(self, obj):
        # create a self rect first, and the obj that got pass in also should be a rect
        if self.get_rect().colliderect(obj.get_rect()):
            return True
        else:
            return False
        
    def change_dir(self, dy):
        self.dx *= -1
        # dy change is based on the angle

class Paddle:
    def __init__(self, x, y, width, height, speed, color, disp_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.display_height = disp_height
        self.velocity_y = 0
        self.prev_paddle_y = self.y
        self.clock = pygame.time.Clock()


    # Draw paddle (srface, (color), (x, y, width, height))
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    # update new postion base on event
    def update_newpos(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key]:
            if self.y - self.speed > 0:
                self.y -= self.speed
            else:
                self.y = 0
                
        if keys[down_key]:
            if self.y + self.speed < self.display_height - self.height:
                self.y += self.speed
            else:
                self.y = (self.display_height - self.height)

    # return a self obj (left, top, width, height)
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def colliderect(self, obj):
        # create a self rect first, and the obj that got pass in also should be a rect
        # promblem that some time the ball can stuck inside padle and it will
        # glitch in and out we need to make a dection of the new pos is still in
        # collide range if it is we need to disalbe changing direciont
        max_speed = 7
        collide_direction_factor = 1.5
        if self.get_rect().colliderect(obj.get_rect()):
            if obj.x < self.x:
                obj.x = self.x - obj.raidus - 1
            else:
                obj.x = self.x + self.width + obj.raidus + 1
             #   obj.x = self.x + self.width + obj.radius + 1  # Move the ball outside the paddle to the right
            obj.dx *= -1 
            new_dy = obj.dy + self.velocity_y * collide_direction_factor
            print(new_dy)
            # Update dy based on the direction of ball movement
            if obj.dy <= 0:  # Ball moving upwards
                print(new_dy)
                print(max(new_dy, -max_speed))
                obj.dy = max(new_dy, -max_speed)  # Limit the maximum upward velocity
            else:  # Ball moving downwards
                obj.dy = min(new_dy, max_speed)  # Limit the maximum downwards velocity

    def cal_velocity(self, cons_time):
        delta_y = self.y - self.prev_paddle_y
        self.velocity_y = delta_y / cons_time
        self.prev_paddle_y = self.y
        





        


class Wall:
    def __init__(self, x, y, width, height, color, disp_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.display_height = disp_height

    # Draw paddle (srface, (color), (x, y, width, height))
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    # return a self obj (left, top, width, height)
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def colliderect(self, obj):
        # create a self rect first, and the obj that got pass in also should be a rect
        self_rect = self.get_rect()
        obj_rect = obj.get_rect()
        #collide side 0 = no hit, 1 = topm 2 = right, 3 = bot, 4 = left
        if self_rect.colliderect(obj_rect):
            # in this case that means is top collision
            if obj_rect.top <= self_rect.bottom or obj_rect.bottom >= self_rect.top:
                # only change y direction 
                obj.dy *= -1
            elif obj_rect.right >= self_rect.left:
                # only change z direction
                obj.dx *= -1


