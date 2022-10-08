"""
File: my_drawing
Name: Jason
----------------------
TODO: create my own figure by the GObejects.
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon, GArc, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constants control the size of circle
SIZE =20

# Global variable:
window = GWindow(width= 1000, height=800, title='My Idea~')
count = 1
hole = GOval(SIZE, SIZE)

def main():
    """
    Title: Disney V.S. Universal!
    Snowman and Minion are popular in each company!
    Snowman is like cold & winter and minion is like passionate & summer~
    It is funny to compare which one is loved by worldwide~

    In main function, there will be different:
    1. Add the string: 'Disney V.S. Universal'
    2. Add the string: 'Snowman'
    3. Draw a snowman in canvas
    4. Add the string: ' Minion'
    5. Draw a Minion.
    """
    # Disney V.S. Universal!
    ch = GLabel('Disney V.S. Universal')
    ch.font = '-80'
    ch.color = 'darksage'
    window.add(ch, x = window.width/2 -400, y = window.height/2 + window.height/3)

    #Add snowman in canvas
    snow_label = GLabel('Snowman', x =window.width/4- 150 , y= window.height/4 -100 )
    snow_label.font= '-50'
    window.add(snow_label)

    #Draw a snowman in canvas
    face = GOval(150,150)
    face.filled = False
    window.add(face, x = window.width/4 - face.width, y = window.height/4 - face.height/2 +14)

    body = GOval(150, 225)
    body.filled = False
    window.add(body, x = window.width/4 - body.width , y= window.height/2 - body.height/2)

    l_eye_brush = GArc(30,30 , 0, 180)
    l_eye_brush.filled= False
    window.add(l_eye_brush, x = window.width/4 - face.width +28, y = window.height/4 - face.height/2 +50)

    r_eye_brush = GArc(30, 30, 0, 180)
    r_eye_brush.filled = False
    window.add(r_eye_brush, x=window.width / 4 - 60, y=window.height / 4 - face.height / 2 + 50)

    l_eye = GOval(30,30)
    l_eye.filled = False
    window.add(l_eye, x = window.width/4 - face.width +28, y= window.height/4 - face.height/2 +60)

    r_eye = GOval(30,30)
    r_eye.filled = False
    window.add(r_eye, x = window.width / 4 - 60, y= window.height/4 - face.height/2 +60)

    l_eye_cent = GOval(15,15)
    l_eye_cent.filled = True
    window.add(l_eye_cent, x = window.width/4 - face.width +35 , y = window.height/4 - face.height/2 +60)

    r_eye_cent = GOval(15, 15)
    r_eye_cent.filled = True
    window.add(r_eye_cent, x = window.width / 4 - 50 , y = window.height/4 - face.height/2 +65)

    nose = GPolygon()
    nose.add_vertex((window.width/4 - face.width/2, window.height/4 +20))
    nose.add_vertex((window.width/4 - face.width/2,window.height/4 +30))
    nose.add_vertex((window.width / 4 - face.width / 2 + 80, window.height / 4 +25))
    nose.filled =True
    nose.fill_color = 'orange'
    window.add(nose)

    mouse = GOval(70, 30)
    mouse.filled =True
    mouse.fill_color = 'blue'
    window.add(mouse, x = window.width/4 - face.width+ face.width/3, y = window.height/4 - face.height/2 +face.height/2+face.height/4)

    teeth = GRect(30,20)
    teeth.filled = True
    teeth.fill_color = 'white'
    window.add(teeth, x = window.width/4 - face.width+ face.width/3 +18, y = window.height/4 - face.height/2 +face.height/2+face.height/4+3)

    dress = GOval(30,30)
    dress.filled = True
    window.add(dress, x = window.width/4 - body.width + body.width/2 -10 , y= window.height/2 - body.height/2 + body.height/3 - 40)

    dress_2 = GOval(30, 30)
    dress_2.filled = True
    window.add(dress_2, x=window.width / 4 - body.width + body.width / 2 - 10, y=window.height / 2 - body.height / 2 + body.height / 2- 13)

    dress_3 = GOval(30, 30)
    dress_3.filled = True
    window.add(dress_3, x=window.width / 4 - body.width + body.width / 2 - 10, y=window.height / 2 - body.height / 2 + body.height / 2 +50)

    head = GLine(window.width/4 - face.width+ face.width/2, window.height/4 - face.height/2 +14 , window.width/4 - face.width+ face.width/2, window.height/4 - face.height/2 - 15 )
    head.color = 'brown'
    window.add(head)

    head_2 = GLine(window.width / 4 - face.width + face.width / 2, window.height / 4 - face.height / 2 + 14, window.width / 4 - face.width + face.width / 2 -8, window.height / 4 - face.height / 2 - 10)
    head_2.color = 'brown'
    window.add(head_2)

    head_3 = GLine(window.width / 4 - face.width + face.width / 2, window.height / 4 - face.height / 2 + 14, window.width / 4 - face.width + face.width / 2 +8, window.height / 4 - face.height / 2 - 10)
    head_3.color = 'brown'
    window.add(head_3)

    l_hand = GLine(window.width/4 - body.width , window.height/2 - body.height/2 + body.height/2, window.width/4 - body.width - 30, window.height/2 - body.height/2 )
    l_hand.color = 'brown'
    window.add(l_hand)

    l_hand_finger = GLine(window.width/4 - body.width - 30 , window.height/2 - body.height/2 , window.width/4 - body.width - 30 - 10 , window.height/2 - body.height/2 -10)
    l_hand_finger.color = 'brown'
    window.add(l_hand_finger)

    l_hand_finger_2 = GLine(window.width/4 - body.width - 30 , window.height/2 - body.height/2 , window.width/4 - body.width - 30 + 10 , window.height/2 - body.height/2 - 10)
    l_hand_finger_2.color = 'brown'
    window.add(l_hand_finger_2)

    r_hand = GLine(window.width/4 - body.width + body.width , window.height/2 - body.height/2 + body.height/2, window.width/4 - body.width + body.width+ 90, window.height/2 - body.height/2 + body.height/2)
    r_hand.color = 'brown'
    window.add(r_hand)

    r_hand_finger = GLine(window.width/4 - body.width + body.width+ 90, window.height/2 - body.height/2 + body.height/2, window.width/4 - body.width + body.width+ 90 + 5, window.height/2 - body.height/2 + body.height/2- 10)
    r_hand_finger.color = 'brown'
    window.add(r_hand_finger)

    r_hand_finger_2 = GLine(window.width/4 - body.width + body.width+ 90, window.height/2 - body.height/2 + body.height/2, window.width/4 - body.width + body.width+ 90 + 5, window.height/2 - body.height/2 + body.height/2 + 10)
    r_hand_finger_2.color = 'brown'
    window.add(r_hand_finger_2)

    l_feet = GLine(window.width/4 - body.width + body.width/2 , window.height/2 - body.height/2 +body.height , window.width/4 - body.width + body.width/2 - 30   , window.height/2 - body.height/2 +body.height + 30)
    l_feet.color = 'brown'
    window.add(l_feet)

    r_feet = GLine(window.width/4 - body.width + body.width/2 , window.height/2 - body.height/2 +body.height , window.width/4 - body.width + body.width/2 + 30   , window.height/2 - body.height/2 +body.height + 30)
    r_feet.color = 'brown'
    window.add(r_feet)

    # Minion part
    # Add string 'Minion' in canvas
    minion = GLabel('Minion', x =window.width/2 + 140 , y= window.height/4 -100 )
    minion.font ='-50'
    window.add(minion)

    # Draw a minion
    m_head = GArc(180, 160, 0, 180)
    m_head.filled = True
    m_head.fill_color = 'yellow'
    m_head.color = 'yellow'
    window.add(m_head, x = window.width - 400, y = window.height/3 - m_head.height/2)

    body = GRect(180, 210)
    body.filled = True
    body.fill_color ='yellow'
    body.color = 'yellow'
    window.add(body, x = window.width - 400 , y = window.height/3)

    buttom = GArc(180,160, 180, 180)
    buttom.filled = True
    buttom.fill_color= 'blue'
    buttom.color = 'blue'
    window.add(buttom, x = window.width - 400 , y= window.height/3  + body.height- 39)

    eye = GOval(50,50)
    eye.filled = True
    eye.fill_color = 'white'
    window.add(eye, x = window.width - 400 + body.width/2 - 25, y = window.height/3 )

    eye_cent = GArc(30, 60, 180,180)
    eye_cent.filled = True
    window.add(eye_cent, x = window.width - 400 + body.width/2 - 25 + eye.width/3 -7 , y= window.height/3 + eye.height/3 -8 )

    m_eye_line = GLine(window.width - 400 +body.width/2 -25, window.height/3 +23, window.width - 400 +body.width/2 -25+50, window.height/3 +23  )
    window.add(m_eye_line)

    m_eye_left = GRect(65, 15)
    m_eye_left.filled=True
    window.add(m_eye_left , x= window.width - 400, y = window.height/3 +16 )

    m_eye_r = GRect(65,15)
    m_eye_r.filled =True
    window.add(m_eye_r, x= window.width- 400 + 115, y = window.height/3 +16)

    m_mouse = GArc(70, 100, 0, 180)
    m_mouse.filled= True
    window.add(m_mouse, x= window.width -400 + body.width/2 -33 , y = window.height/3 + body.height/2 +20 )

    m_l_hand = GRect(100, 10)
    m_l_hand.filled = True
    m_l_hand.color = 'yellow'
    m_l_hand.fill_color = 'yellow'
    window. add(m_l_hand, x = window.width - 400- body.width/4 - 50 , y = window.height/3+ body.height/2)

    m_l_finger = GOval(30,30)
    m_l_finger.filled = True
    window.add(m_l_finger, x = window.width - 400- body.width/5 - 60 , y = window.height/3+ body.height/2- 10)

    m_r_hand = GRect(70, 10)
    m_r_hand.filled = True
    m_r_hand.color = 'yellow'
    m_r_hand.fill_color = 'yellow'
    window. add(m_r_hand, x = window.width - 400 + body.width , y = window.height/3+ body.height/2)

    m_r_finger = GOval(30, 30)
    m_r_finger.filled = True
    window.add(m_r_finger, x=window.width - 400 + body.width + m_r_hand.width, y=window.height / 3 + body.height / 2 - 10)

    #open onmouseclicked to draw the line
    onmouseclicked(click)


def click(event):
    """
    In click function, I can draw infinite line before I close the window.
    """
    global count
    if count %2 != 0:
        hole.filled = False
        window.add(hole, x = event.x- SIZE/2, y= event.y- SIZE/2)
        count +=1
    else:
        count+= 1
        line = GLine(hole.x+SIZE/2, hole.y+SIZE/2, event.x, event.y)
        line.color = 'black'
        window.add(line)
        window.remove(hole)


if __name__ == '__main__':
    main()
