import pygame
import time

pygame.init()

# Încărcare imagini pentru animație
walkRight = [pygame.image.load('img/R1.png'), pygame.image.load('img/R2.png'), pygame.image.load('img/R3.png'),
             pygame.image.load('img/R4.png'), pygame.image.load('img/R5.png'), pygame.image.load('img/R6.png'),
             pygame.image.load('img/R7.png'), pygame.image.load('img/R8.png'), pygame.image.load('img/R9.png')]
walkLeft = [pygame.image.load('img/L1.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'),
            pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'),
            pygame.image.load('img/L7.png'), pygame.image.load('img/L8.png'), pygame.image.load('img/L9.png')]
bg = pygame.image.load('img/map.png')
bg = pygame.transform.scale(bg, (1700, 900))

char = pygame.image.load('img/standing.png')

# Clasa Goblin (Inamic)
class Anamy(object):
    walkRight = [
        pygame.image.load('img/R1E.png'), pygame.image.load('img/R2E.png'), pygame.image.load('img/R3E.png'),
        pygame.image.load('img/R4E.png'), pygame.image.load('img/R5E.png'), pygame.image.load('img/R6E.png'),
        pygame.image.load('img/R7E.png'), pygame.image.load('img/R8E.png'), pygame.image.load('img/R9E.png'),
        pygame.image.load('img/R10E.png'), pygame.image.load('img/R11E.png')
    ]
    
    walkLeft = [
        pygame.image.load('img/L1E.png'), pygame.image.load('img/L2E.png'), pygame.image.load('img/L3E.png'),
        pygame.image.load('img/L4E.png'), pygame.image.load('img/L5E.png'), pygame.image.load('img/L6E.png'),
        pygame.image.load('img/L7E.png'), pygame.image.load('img/L8E.png'), pygame.image.load('img/L9E.png'),
        pygame.image.load('img/L10E.png'), pygame.image.load('img/L11E.png')
    ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkcount = 0
        self.val = 1.3  
        self.hitbox = (self.x + 17, self.y, 32, 70)
        self.direction = 1  
        self.path = [self.x, self.end]

    def draw(self, window, player):
        self.move(player)
        if self.walkcount + 1 >= 33:
            self.walkcount = 0
        if self.direction > 0:  
            window.blit(self.walkRight[self.walkcount // 3], (self.x, self.y))
        else: 
            window.blit(self.walkLeft[self.walkcount // 3], (self.x, self.y))
        self.walkcount += 1

       
        self.hitbox = (self.x + 17, self.y, 32, 70)
        pygame.draw.rect(window, (0, 0, 0), self.hitbox, 2)

    def draw_default(self, window):
        self.move_default()
        if self.walkcount + 1 >= 33:
            self.walkcount = 0
        if self.val > 0:
            window.blit(self.walkRight[self.walkcount // 3], (self.x, self.y))
            self.walkcount += 1
        else:
            window.blit(self.walkLeft[self.walkcount // 3], (self.x, self.y))
            self.walkcount += 1
        self.hitbox = (self.x + 17, self.y, 32, 70)  
        pygame.draw.rect(window, (0, 0, 0), self.hitbox, 2)  

    def move_default(self):
        if self.val > 0:
            if self.x + self.val < self.path[1]:
                self.x += self.val
            else:
                self.val *= -1
                self.walkcount = 0
        else:
            if self.x - self.val > self.path[0]:
                self.x += self.val
            else:
                self.val *= -1
                self.walkcount = 0        

    def move(self, player):
        
        if self.x < player.x:  
            self.x += self.val 
            self.direction = 1  
        elif self.x > player.x: 
            self.x -= self.val  
            self.direction = -1  

    def hit(self):
        print("hit")

# Clasa Jucător
class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.prev_y=0
        self.width = width
        self.height = height
        self.step = 5
        self.is_jump = False
        self.left = False
        self.right = False
        self.walk_count = 0
        self.jump_count=True
        self.jump_speed=0.15
        self.repause = True
        self.hitbox = (self.x + 17, self.y, 32, 70)
        self.platform=0

    
        
        
        
    def on_platform(self, platform_1, platform_2, platform_3, platform_4, platform_5,platform_6,platform_8,platform_7,platform_9,platform_11,platform_10,platform_13,platform_12):

        if self.platform==1:
              
           

            if self.x>platform_5.x+platform_5.width+100:

                self.x=platform_6.x
                self.platform=6
                return platform_6.y



        if self.platform==0:    
            if self.x > platform_1.x and self.x < platform_1.x + platform_1.width and self.y == 730:
                self.platform = platform_1.platform_number
                
                return platform_1.y
            
        if self.platform==0:
              if self.x > platform_2.x and self.x < platform_2.x + platform_2.width and self.y == 730:
                self.platform = platform_2.platform_number
                return platform_2.y

        if self.platform==0:
              if self.x > platform_4.x and self.y == 730:
                self.platform = platform_4.platform_number
                return platform_4.y

            
        if self.platform==1 or self.platform==2:    
              if self.x > platform_5.x and self.x < platform_5.x + platform_5.width and self.y==platform_1.y or self.y==platform_2.y :
                
                self.platform = platform_5.platform_number
                return platform_5.y
              
              

        if self.platform==5:    
              if self.x >= platform_8.x and self.x < platform_8.x + platform_8.width and self.y==platform_5.y  :
                
                self.platform = platform_8.platform_number
                return platform_8.y
              if self.x>platform_5.x+165 and self.x<=platform_5.x+platform_5.width/2+80:
                  self.x=platform_13.x+20
                  self.platform=platform_13.platform_number
                  return platform_13.y
        if self.platform==0:    
              if self.x>platform_3.x and self.x<platform_3.width+platform_3.x and self.y==730:

                self.platform=platform_3.platform_number
                return platform_3.y
        
        if self.platform==3:
            if self.x>platform_3.x and self.x < platform_3.x+40 and self.y==600:
                
                self.platform=8
                return platform_8.y
            #else:
                #return platform_3.y 
        if self.platform==6:

            if self.x>platform_6.x and self.x<platform_6.x+100:
                self.platform=8
                return platform_8.y           
        

        if self.platform==3 or self.platform==4:

            if self.x>platform_3.x+platform_3.width/2 and self.x<platform_3.x+platform_3.width:
                self.x=platform_7.x
                self.platform=7
                return platform_7.y
            if self.x>platform_4.x and self.x<platform_4.x+50 and self.y==platform_4.y:
                self.x=platform_7.x+platform_7.width-20
                self.platform=7
                return platform_7.y


        if self.platform==8:
                
            if self.x>platform_8.x+platform_8.width/2 and self.x<platform_8.x+platform_8.width and self.y==platform_8.y:
               
               
               self.x=platform_9.x+30
               self.platform=9
               return platform_9.y



        if self.platform==7:

            if self.x>platform_7.x+platform_7.width/2:
                self.platform=11
                return platform_11.y

        if self.platform==11:
            if self.x>platform_11.x and self.x<platform_11.x+platform_11.width/2 and self.y==platform_11.y:

                self.x=platform_10.x+platform_10.width
                self.platform=10
                return platform_10.y
        if self.platform==10:
             if self.x>platform_10.x+platform_10.width/2 and self.x<platform_10.x+platform_10.width and self.y==platform_10.y:
                self.x=platform_11.x
                self.platform=11
                return platform_11.y
        if self.platform==9:
            if self.x>platform_9.x+platform_9.width/2+20:
                self.x=platform_10.x+20
                self.platform=10
                return platform_10.y
            
        if self.platform==13:
            if self.x>platform_13.x and self.x<platform_13.x+50 and self.y==platform_13.y:
                self.platform=12
                self.x=platform_12.x+platform_12.width-10
                return platform_12.y 

        if self.platform==12:

            if self.x>platform_12.x+platform_12.width/2 and self.x<platform_12.x+platform_12.width and self.y==platform_12.y:
                
                self.x=platform_13.x+10
                self.platform=13
                return platform_13.y
              
        return self.y
    
          

    def fall(self, platform_1, platform_2, platform_3, platform_4, platform_5,platform_6,platform_8,platform_7,platform_9,platform_11,platform_10,platform_13,platform_12):
        if self.platform == 1:
            if self.x < platform_1.x or self.x > platform_1.x + platform_1.width and self.y == platform_1.y:
                self.platform=0
                return 730
            else:
                return platform_1.y
            


        if self.platform == 2:
            if  self.x > platform_2.x + platform_2.width and self.y == platform_2.y:
                self.platform=0
                return 730
            else:
                return platform_2.y
            
         
        
                
        if self.platform == 5:
            if  self.x > platform_5.x + platform_5.width and self.y == platform_5.y:
                self.platform=1
                return platform_1.y
            
            if self.x < platform_5.x and self.y == platform_5.y:
                self.platform=2
                return platform_2.y

            else:
                return platform_5.y
            
        if self.platform == 8:
            
            if  self.x > platform_8.x + platform_8.width and self.y == platform_8.y:
                
                self.platform=6
                return platform_6.y
           
            
            
            elif self.x < platform_8.x and self.y == platform_8.y:
                self.platform=5
                return platform_5.y

            else:
                return platform_8.y
        
        if self.platform==6:

            if self.x>(platform_6.x+platform_6.width) and self.y==platform_6.y:
                self.platform=3
                return platform_3.y
            elif self.x<platform_6.x and self.y==platform_6.y:
                self.platform=1
                self.x=platform_1.x+platform_1.width-50
                return platform_1.y
            else:
                return platform_6.y    
        if self.platform==3:

            if self.x<platform_3.x or self.x>platform_3.x+platform_3.width and self.y==600:
                
                self.platform=0
                return 730
            else:
                return platform_3.y 
        
       
        if self.platform==4:

            if self.x<platform_4.x and self.y==platform_4.y:
                self.platform=0
                return 730     
            else:
                return platform_4.y

        if self.platform==7:

            if self.x<platform_7.x and self.y==platform_7.y:
                self.x=platform_3.x+platform_3.width
                self.platform=3
                return platform_3.y    

            if self.x>platform_7.x+platform_7.width and self.y==platform_7.y:
               self.x=platform_4.x
               self.platform=4
               return platform_4.y     

        if self.platform==9:

            if self.x<platform_9.x and self.y==platform_9.y:

                self.platform=6
                self.x=platform_6.x+50
                return platform_6.y
                    
            elif self.x>platform_9.x+platform_9.width and self.y==platform_9.y:

                self.platform=3
                self.x=platform_3.x+50
                return platform_3.y

        if self.platform==11:
            if self.x<platform_11.x and self.y==platform_11.y:
                  self.platform=7
                  return platform_7.y
            
        if self.platform==10:
            
            if self.x>platform_10.x+platform_10.width and self.y==platform_10.y:
                self.platform=7
                return platform_7.y   
            
            if self.x<platform_10.x and self.y==platform_10.y:
                self.platform=3
                return platform_3.y
            

        if self.platform==13:

            if self.x>platform_13.x+platform_13.width and self.y==platform_13.y:
                self.platform=8
                return platform_8.y  

            if self.x<platform_13.x and self.y==platform_13.y:
                self.platform=5
                return platform_5.y  
            
        if self.platform==12:

            if self.x>platform_12.x+platform_12.width and self.y==platform_12.y:
                self.platform=5
                return platform_5.y



        return self.y

                       
       

  


    def draw(self, window):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not self.repause:
            if self.left:
                window.blit(walkLeft[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                window.blit(walkRight[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.left:
                window.blit(walkLeft[0], (self.x, self.y))
            else:
                window.blit(walkRight[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y, 32, 70)
        pygame.draw.rect(window, (0, 0, 0), self.hitbox, 2)

# Clasa Proiectil
class projectil(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

class Platrforms():
    def __init__(self, platform_number, x, y, width, height):
        self.platform_number = platform_number
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jump_force=10

    def draw(self, window, r, g, b):
        red_color = (r, g, b)  
        pygame.draw.rect(window, red_color, (self.x, self.y, self.width, self.height))

        










transparent_color = (245, 10, 225, 100) 
win_width = 1700
win_height = 900
window = pygame.display.set_mode((win_width, win_height))

jony = player(50, 730, 64, 64)
goblin = Anamy(100, 730, 64, 64, win_width-100)
goblin_2 = Anamy(10, 730, 64, 64, win_width-100)

platform_1 = Platrforms(1, 300, 600, 280, 50)
platform_2 = Platrforms(2, 0, 600, 100, 50)
platform_3 = Platrforms(3, 850, 600, 260, 50)
platform_4 = Platrforms(4, 1450, 600, 230, 50)
platform_5 = Platrforms(5, 90, 400, 320, 50)
platform_6 = Platrforms(6, 620, 420, 295, 50)
platform_7=Platrforms(7,1155,490,330,50)
platform_8 = Platrforms(8, 400, 310, 230, 50)
platform_9=Platrforms(9,700,230,230,50)
platform_10=Platrforms(10,1050,230,200,50)
platform_11=Platrforms(11,1350,310,330,50)
platform_12=Platrforms(12,30,170,185,50)
platform_13=Platrforms(13,290,100,325,50)





pygame.display.set_caption("My Game")

clock = pygame.time.Clock()
FPS = 60

# Funcție de re-desenare a ferestrei jocului
def redraw_game_window():
    window.blit(bg, (0, 0))
    jony.draw(window)
    goblin.draw(window, jony)
    goblin_2.draw_default(window)  # Goblinul urmărește jucătorul
    platform_12.draw(window, 242, 245, 66) 
    for bomb in bombs:
        bomb.draw(window)
    pygame.display.update()

# Bucla principală a jocului
run = True
bombs = []
is_on_nivel_0=True
is_on_nivel_1=False
is_on_nivel_2=False

ori=0
jump_cooldown = 200  
last_jump_time = 0

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bomb in bombs:
        if bomb.y - bomb.radius < goblin.hitbox[1] + goblin.hitbox[3] and bomb.y + bomb.radius > goblin.hitbox[1]:
            if bomb.x + bomb.radius > goblin.hitbox[0] and bomb.x - bomb.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                bombs.pop(bombs.index(bomb))

        if 0 < bomb.x < 1700:
            bomb.x += bomb.vel
        else:
            bombs.pop(bombs.index(bomb))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        facing = -1 if jony.left else 1
        if len(bombs) < 5:
            bombs.append(projectil(round(jony.x + jony.width // 2), round(jony.y + jony.height // 2), 5, (247, 120, 2), facing))

    if keys[pygame.K_LEFT] and jony.x > 0:
        jony.x -= jony.step
        jony.left = True
        jony.right = False
        jony.repause = False
        
    elif keys[pygame.K_RIGHT] and jony.x + jony.width < win_width:
        jony.x += jony.step
        jony.right = True
        jony.left = False
        jony.repause = False
        
    else:
        jony.repause = True
        jony.walk_count = 0

  
    current_time = pygame.time.get_ticks()

                   
    if keys[pygame.K_UP] and (current_time - last_jump_time > jump_cooldown):
                        
                        last_jump_time = current_time
                        jony.is_jump = True
                        jony.walk_count = 0

                        
                        
                        jony.y=jony.on_platform(platform_1,platform_2,platform_3,platform_4,platform_5,platform_6,platform_8,platform_7,platform_9,platform_11,platform_10,platform_13,platform_12)
                       
                        print("platform", jony.platform)
                   

                  
    jony.y=jony.fall(platform_1,platform_2,platform_3,platform_4,platform_5,platform_6,platform_8,platform_7,platform_9,platform_11,platform_10,platform_13,platform_12)           
   
    print("platform", jony.platform)
                  
                         
          
                
                
    
             
                

    #print("x=",jony.x)  
    # print("y=",jony.y)    
    redraw_game_window()

pygame.quit()
