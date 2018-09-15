import simplegui
import random
 
CANVAS_SIZE = (800,800)
CANVAS_BACKGROUND = "Black"
score = 0
highscore = 0
STEP = 20
BALL_WIDTH = 10
ballstart = [CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/6]
ballstart1 = [CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/6]
ball_velocity = [0,0]
ball_velocity1 = [0,0]
pulldown = 0.5
pulldown1 = 0.05
iR = False
iL = False
Lose = False
line1 = [300,600]
line2 = [500,600]
img = simplegui.load_image("http://i296.photobucket.com/albums/mm182/CodeH4x0r/explosion17.png")
sp_width = 320
sp_height = 320
sp_columns = 5
sp_rows = 5
frameWidth = sp_width/sp_columns
frameHeight = sp_height/sp_rows 
frameCentreX = frameWidth/2
frameCentreY = frameHeight/2
frameIndex = (0,0)
check = 0

def welcome(canvas):
    canvas.draw_text('Welcome To Ball Blaster!', (CANVAS_SIZE[0]/8, CANVAS_SIZE[1]/8), 60, 'Red')
    canvas.draw_text('Aim: Collect the red and green balls and get the highest score!', (CANVAS_SIZE[0]/20, CANVAS_SIZE[1]/2.5), 30, 'White')
    canvas.draw_text('REMEMBER: YOU HAVE TO COLLECT THE', (CANVAS_SIZE[0]/25, CANVAS_SIZE[1]/1.75), 37, 'Green')
    canvas.draw_text('GREEN BALL OR YOU AUTOMATICALLY LOSE ', (CANVAS_SIZE[0]/50, CANVAS_SIZE[1]/1.6), 35, 'Green')
    canvas.draw_text('Use left and right arrow keys to move horizontal platform', (CANVAS_SIZE[0]/7, CANVAS_SIZE[1]/2.25), 25, 'White')
    
def start():
    reset()
    frame.set_draw_handler(draw)
    
def start_handler():
    start()
       
def scoreatend(canvas):
    canvas.draw_text('Score: ' + str(score), (CANVAS_SIZE[0]/4, CANVAS_SIZE[1]/2), 140, 'Red')
    canvas.draw_text('HighScore: ' + str(highscore), (CANVAS_SIZE[0]/3, CANVAS_SIZE[1]/8), 60, 'Red')
    
def ballstartingplace():
    global ballstart, ball_velocity
    ballstart = random.choice([[100,CANVAS_SIZE[1]/6], [200, CANVAS_SIZE[1]/6] , [300,CANVAS_SIZE[1]/6], [400,CANVAS_SIZE[1]/6], [500,CANVAS_SIZE[1]/6], [600,CANVAS_SIZE[1]/6],[700,CANVAS_SIZE[1]/6] ])
    ball_velocity = [0,0]
    
def specialballstartingplace(): 
    global ballstart1, ball_velocity1
    ballstart1 = random.choice([[100,CANVAS_SIZE[1]/6], [200, CANVAS_SIZE[1]/6] , [300,CANVAS_SIZE[1]/6], [400,CANVAS_SIZE[1]/6], [500,CANVAS_SIZE[1]/6], [600,CANVAS_SIZE[1]/6],[700,CANVAS_SIZE[1]/6]])
    ball_velocity1 = [0,0]    
        
def startnewgreen():
    global score
    score = 0
    ballstartingplace()
    specialballstartingplace()
    
def startnewred():
    ballstartingplace()
    specialballstartingplace()
    
def nextball():
    ballstartingplace()
    
def nextballred():
    specialballstartingplace()
    
def collision():
    global ballstart
    if ballstart[1] <= 700:
        y_test = ballstart[1] + BALL_WIDTH > line1[1]
        x_test_1 = line1[0] < ballstart[0] + BALL_WIDTH
        x_test_2 = line2[0] > ballstart[0] - BALL_WIDTH
        return x_test_1 and x_test_2 and y_test

def collisionred():
    global ballstart1
    if ballstart1[1] <= 700:
        y_test = ballstart1[1] + BALL_WIDTH > line1[1]
        x_test_1 = line1[0] < ballstart1[0] + BALL_WIDTH
        x_test_2 = line2[0] > ballstart1[0] - BALL_WIDTH
        return x_test_1 and x_test_2 and y_test
    
def redvelocity():
    global ballstart1, ball_velocity1, pulldown1
    ballstart1[0] += ball_velocity1[0]
    ballstart1[1] += ball_velocity1[1]
    ball_velocity1[0] += 0
    ball_velocity1[1] += pulldown1
           
def reset():
    line1 = [300,600]
    line2 = [500,600]
    ballstartingplace()
    specialballstartingplace()
    startnewgreen()
    startnewred()
    nextball()
    nextballred()
    collision()
    collisionred()
    redvelocity()
        
def reset_handler():
    reset() 
        
def draw(canvas):
    global iR, iL, line1, line2, STEP, ball_velocity, ballstart, score, highscore, pulldown, frameIndex, check, ballstart1, Lose
    canvas.draw_circle([ballstart[0], ballstart[1]], 20, 20, 'Green', 'Yellow')
    canvas.draw_circle([ballstart1[0], ballstart1[1]], 15, 15, 'Red', 'Orange')
    canvas.draw_line(line1, line2, 20, 'Red')
    canvas.draw_text('Score: ' + str(score), (CANVAS_SIZE[0]/2.25, CANVAS_SIZE[1]/8), 50, 'Red')
    canvas.draw_text('HighScore: ' + str(highscore), (CANVAS_SIZE[0]/8, CANVAS_SIZE[1]/8), 30, 'White')
  
    check += 1
    if check % 8 == 0:
        canvas.draw_image(img, 
                        (frameWidth*frameIndex[0]+frameCentreX, 
                        frameHeight*frameIndex[1]+frameCentreY),
            (frameWidth, frameHeight),
            (CANVAS_SIZE[0] / 10, CANVAS_SIZE[1] / 9),
            (frameWidth / 2, frameHeight / 2))
        
        frameIndex = (
            (frameIndex[0] + 1) % sp_columns,
            (frameIndex[1] + 1) % sp_rows)
    elif check % 9 == 0:
        canvas.draw_image(img, 
                        (frameWidth*frameIndex[0]+frameCentreX, 
                        frameHeight*frameIndex[1]+frameCentreY),
            (frameWidth, frameHeight),
            (CANVAS_SIZE[0] / 2.5, CANVAS_SIZE[1] / 9),
            (frameWidth / 2, frameHeight / 2))
        
    else:
        canvas.draw_image(img, 
                        (frameWidth*frameIndex[0]+frameCentreX, 
                        frameHeight*frameIndex[1]+frameCentreY),
            (frameWidth, frameHeight),
            (CANVAS_SIZE[0] / 1.4, CANVAS_SIZE[1] / 9),
            (frameWidth / 2, frameHeight / 2))
   
    if iR:
        line1[0] += STEP
        line2[0] += STEP
    if iL:
        line1[0] -= STEP
        line2[0] -= STEP
    if iL:
        if line1 <= [-200,600]:
            line1 = [800,600]
            line2 = [1000,600]
    if iR:
        if line2 >= [1000,600]:
            line2 = [0,600]
            line1 = [-200,600]
   
    ballstart[0] += ball_velocity[0]
    ballstart[1] += ball_velocity[1]
    ball_velocity[0] += 0
    ball_velocity[1] += pulldown
    
    redvelocity()
    
    if collision():  
        ballstart = [2000,2000]
        score = score + 1
        nextball()
        
        if(score > highscore):
            highscore = score
        
    if collisionred():
        ballstart1 = [2000,2000]
        score = score + 2
        nextballred()
            
        if(score > highscore):
            highscore = score
            
    
    if ballstart[1] > 700:
        startnewgreen()
        
    if ballstart1[1] > 700:
        startnewred()

    if ((ballstart[1] > 660)):
        Lose = False
        frame.set_draw_handler(scoreatend)
        line1 = [300,600]
        line2 = [500,600]
        
    
def keydown(key):
    global  iR, iL
    if key == simplegui.KEY_MAP['right']:	
        iR = True
    if key == simplegui.KEY_MAP['left']:	
        iL = True

def keyup(key):
    global  iR, iL
    if key == simplegui.KEY_MAP['right']:	
        iR = False
    if key == simplegui.KEY_MAP['left']:	
        iL = False

frame = simplegui.create_frame("Ball Blaster", CANVAS_SIZE[0], CANVAS_SIZE[1])
frame.set_canvas_background("Black")
frame.set_draw_handler(draw)
frame.set_draw_handler(welcome)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Start", start_handler)
frame.add_button("Reset", reset_handler)

frame.start()
