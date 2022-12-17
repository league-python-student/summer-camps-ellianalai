"""
Create a single player Pong game
"""
from Ball import Ball
from Paddle import Paddle

def setup():
    global started, score
    started = False
    score = 0
    
    # 1. Set the size of your window to at least width = 800, height = 600
    size(800, 600)
    
    # 2. Make a global ball variable
    global ball
    
    # 3. Initialize your ball variable to a new Ball(x)
    ball = Ball(width / 2)
    
    # 4. Make a global paddle variable
    global paddle
    # 5. Initialize your paddle variable to a new Paddle(x)
    paddle = Paddle(350)
    
def draw():
    global score
    if not started:
        textSize(32)
        fill(0)
        text("Press 's' to start", width/3, height/2)
        return
    
    # 6. Use the background() function to set the background color.
    #    background(0) will set a classic black background
    #    Do you see your background color?
    background(0)

    # 7. Call the ball object's update() and draw() methods.
    #    Do you see the ball moving on the screen?
    ball.update()
    ball.draw()

    # 8. Call the paddle object's update() and draw() methods.
    #    Do you see the paddle on the screen?
    paddle.update()
    paddle.draw()

    # 9. Finish the code in keyPressed() and keyReleased() first!
    
    # 12. Call the ball object's collision(paddle) method and pass the
    #     paddle object as an input variable.
    #     Does the ball bounce off the paddel?
    ball.collision(paddle)
    # 13. End the game when the ball goes below the bottom of the screen.
    #     You can use noLoop() to freeze the game and text() to print text
    #     on the screen.
    if ball.y>=height:
         noLoop()
         background('#FFE0F6')
         text("Game over", 400, 300)
         
    # 14. Figure out how to add a score to the game so every bounce off
    #     the paddle increases the player socre
    #     *HINT* use an if statement when checking the ball's collison
    #            with the paddle
    if ball.collision(paddle):
        score = text('0',400,400)
        score+=1
        fill('#FFE0F6')
        print(score)
    # *EXTRA*
    # Can you figure out how to make a 2 player pong game with paddles on
    # the left and right on the screen?

def keyPressed():
    if key == 's':
        global started
        started = True 
    elif key == CODED:
        pass        
        # 10. Change paddle.x_speed when the 'keyCode' variable is
        #     equal to LEFT or RIGHT.
        #     Does the paddle move?
        if keyCode == 39:
            paddle.x_speed +=1
        if keyCode == 37:
            paddle.x_speed -=1
            
    


def keyReleased():
    if key == CODED:
        pass
        # 11. Set paddle.x_speed to 0 when the LEFT or RIGHT arrow keys are released.
        #     Does the paddle stop when the keys are released?
        paddle.x_speed = 0
            
