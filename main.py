# Made by Pranshu Aggarwal

# Welcome to breakout for 2 players with NEW rules

# If one player looses the ball the match doesn't end but goes on. Just the player who lost receives a -2. The game is infinite. To stop and to know who won press "S"
# Use left and rigth arrows to move slider 2 and use "a" and "d" to move slider 1 


import pygame
import random

pygame.init()


dis = pygame.display.set_mode((400,500))

pygame.display.set_caption("Breakout")



# colors

red = [255,0,0]

blue = [0,0,255]
light_blue = [0,0,128]

green = [0,255,0]

white = [255,255,255]

# score

score_1 = 0
score_2 = 0

# text

font = pygame.font.Font('freesansbold.ttf', 15)
font2 = pygame.font.Font('freesansbold.ttf', 90) 
text = font.render('Player 1 score: '+str(score_1), True, red, blue)

textRect = text.get_rect()  
textRect.center = (110, 13)
dis.blit(text, textRect)

text2 = font2.render('Player 2 score: '+str(score_2), True, green, blue)
textrect = text2.get_rect()
textrect.center = (110, 450)
dis.blit(text2,textrect)




# slider_1
x_slider = 300

pygame.draw.rect(dis, green, [x_slider,460,90,15])



# slider_2
x_slider_2 = 300

pygame.draw.rect(dis, light_blue, [x_slider_2,60,90,15])


#defining the variables to remeber the old values of ball
x_ball_old = 0
y_ball_old = 0

# ball

x_list = []
y_list = []
for i in range(10, 390, 10):
    x_list.append(i)
for i in range(60,400,10):
    y_list.append(i)

x_ball = random.choice(x_list)
y_ball = random.choice(y_list)


pygame.draw.circle(dis, red, (x_ball,y_ball), 10, 0)

pygame.display.update()

#motion 

run = True

def mainloop(run, x_slider, x_slider_2, x_ball, y_ball, x_ball_old, y_ball_old, score_1, score_2, t):
    while run:
        pygame.time.delay(int(t))
        t -= 0.001
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        # motion of the slider_1
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x_slider >5:
            x_slider -= 10
        elif keys[pygame.K_RIGHT] and x_slider<310:
            x_slider += 10
            
        # motion of slider_2
        
        if keys[pygame.K_a] and x_slider_2 > 5:
            x_slider_2 -=10
        elif keys[pygame.K_d] and x_slider_2 < 310:
            x_slider_2 += 10

        # restart
        
        if keys[pygame.K_r]:
            mainloop(True, 300, 300, x_ball, 250, 0, 0, 0, 0, 40)


        # motion of ball vertically
    
        # hitting the striker_1
        if y_ball == 450 and x_ball>= x_slider and x_ball < x_slider + 90:
            y_ball_old = y_ball
            y_ball-=10
            score_2+=1
        # in between, going up
        elif y_ball<450  and y_ball > 50 and y_ball_old > y_ball:
            y_ball_old = y_ball
            y_ball-=10
        # in between, going down
        elif y_ball < 450  and y_ball > 50 and y_ball_old < y_ball:
            y_ball_old = y_ball
            y_ball+=10
            if x_ball_old < x_ball:
                x_ball+=10
            else:
                x_ball-=10
        # hitting the striker_2
        elif y_ball == 50 and x_ball>= x_slider_2 and x_ball < x_slider_2 + 90:
            y_ball_old = y_ball
            y_ball +=10
            score_1+=1
        # going below the striker_1
        elif y_ball_old < y_ball and y_ball >= 450:
            y_ball_old = y_ball
            y_ball+=10
            x_ball += (x_ball- x_ball_old)
            score_2 -= 1
        # going above the striker_2
        elif y_ball_old > y_ball and y_ball <= 50:
            y_ball_old = y_ball
            y_ball-=10
            score_1 -= 1
        
    

        # motion of the ball horizontally

        # hitting the left wall 
        if x_ball - 10 < 5:
            x_ball_old = x_ball
            x_ball+=10
        # hitting the right wall
        elif x_ball + 10 > 395:
            x_ball_old = x_ball
            x_ball -= 10
        # hitting the striker_1 while going right
        elif x_ball>= x_slider and x_ball <= x_slider + 90 and x_ball_old < x_ball:
            x_ball_old = x_ball
            x_ball +=10
        # hitting the striker_1 while going left
        elif x_ball>= x_slider and x_ball <= x_slider + 90 and x_ball_old > x_ball:
            x_ball_old = x_ball
            x_ball -=10
        # hitting the striker_2 while going right
        elif x_ball>= x_slider_2 and x_ball <= x_slider_2 + 90 and x_ball_old < x_ball:
            x_ball_old = x_ball
            x_ball +=10
        # hitting the striker_2 while going left
        elif x_ball>= x_slider_2 and x_ball <= x_slider_2 + 90 and x_ball_old > x_ball:
            x_ball_old = x_ball
            x_ball -=10
        # going left in between
        elif x_ball_old > x_ball:
            x_ball_old = x_ball
            x_ball -=10
        # going right in between
        elif x_ball_old < x_ball:
            x_ball_old = x_ball
            x_ball+=10
      
        
        if y_ball > 450:
            x_ball = 250
            y_ball = 250
        elif y_ball < 50:
            x_ball = x_ball
            y_ball = 250
    

    
        dis.fill(white)

 
    
        #ball
        pygame.draw.circle(dis, red, (x_ball,y_ball), 10, 0)
    
        # sliders
        pygame.draw.rect(dis, green, [x_slider,460,90,15])
        pygame.draw.rect(dis, light_blue, [x_slider_2, 30, 90, 15])


        # text
        font = pygame.font.Font('freesansbold.ttf', 15)
        text = font.render('Player 1 score: '+str(score_1), True, white, red)

        textRect = text.get_rect()  
        textRect.center = (110, 13)
        dis.blit(text, textRect)

        text2 = font.render('Player 2 score: '+str(score_2), True, white, red)
        textrect = text2.get_rect()
        textrect.center = (110, 490)
        dis.blit(text2,textrect)


    
        pygame.display.update()

        if keys[pygame.K_s]:

            dis.fill(white)

            if score_1> score_2:
                font = pygame.font.Font('freesansbold.ttf', 60)
                text = font.render('Player 1 Wins', True, white, red)

                textRect = text.get_rect()  
                textRect.center = (200, 130)
                dis.blit(text, textRect)
            elif score_1< score_2:
                font = pygame.font.Font('freesansbold.ttf', 60)
                text = font.render('Player 2 Wins', True, white, red)

                textRect = text.get_rect()  
                textRect.center = (200, 130)
                dis.blit(text, textRect)
            else:
                font = pygame.font.Font('freesansbold.ttf', 60)
                text = font.render('Tie', True, white, red)

                textRect = text.get_rect()  
                textRect.center = (200, 130)
                dis.blit(text, textRect)
                


            pygame.display.update()
            pygame.time.delay(1000)
            run = False

    pygame.quit()


mainloop(True, 300, 300, x_ball, 250, 0, 0, 0, 0, 40)

