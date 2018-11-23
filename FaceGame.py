import cv2
import random
from timeit import default_timer as timer


face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')


cap = cv2.VideoCapture(0)
t = True
start = True
points = 0
diff = 50
box = [2000,2000]
start = timer()
time = 15
qu=False

def newRect(x, y, frame):
    print("new rect")

    a = random.randrange(100,1100)
    b = random.randrange(50,550)

    while(x>=a and x<=a+diff and y>=b and y<=b+diff):
        a = random.randrange(100, 1100)
        b = random.randrange(50, 550)

    color = (0, 0, 255)  # BGR not RGB
    stroke = 2
    cv2.rectangle(frame, (a, b), (a+diff, b+diff), color, stroke)
    return [a,b]


while(t):
    # capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)


    for (x, y, w, h) in faces:

        x2 =int((2*x+w)/2)
        y2 =int((2*y+h)/2)
        if (start):
            start = False
            print("new")
            box = newRect(x,y,frame)
        if (start):
            start = False
            print("new")
            box = newRect(x,y,frame)


        print(box[0],x2,box[0]+diff,box[1],y2,box[1]+diff)

        if (x2>box[0] and x2<box[0]+diff and y2>box[1] and y2<box[1]+diff):
            print("-"*100)
            points += 1
            box = newRect(x,y,frame)

        #print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        img_item = "my-img.png"
        cv2.imwrite(img_item, roi_color)
        # cv2.imshow('face', roi_color ) # shows faces in video

        # drawing rectangle around face
        color = (255, 0, 0)  # BGR not RGB
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y+h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y),color, stroke)



        cv2.circle(frame, (x2,y2),10, color, thickness=5)

    color2 = (0, 0, 255)
    cv2.rectangle(frame, (box[0], box[1]), (box[0]+diff, box[1]+diff),color2, 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, str(points), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), lineType=cv2.LINE_AA)
    cv2.putText(frame, str(time-int(timer())), (50,150), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), lineType=cv2.LINE_AA)
    # display the resulting  frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        qu = True
        break

    if timer() >= start+time:
        cv2.putText(frame, "GAME OVER", (200, 500), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0),
                    lineType=cv2.LINE_AA)
        break


if qu:
    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()
else:

    while (t):
        # capture frame-by-frame
        ret, frame = cap.read()

        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        cv2.putText(frame, "Game Over", (200,200), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), lineType=cv2.LINE_AA)

        cv2.putText(frame, "Final Score", (200,300), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), lineType=cv2.LINE_AA)
        cv2.putText(frame, str(points), (200,400), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), lineType=cv2.LINE_AA)

        color2 = (0, 0, 255)
        # display the resulting  frame
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()