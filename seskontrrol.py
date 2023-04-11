import cv2
import mediapipe as mp
import numpy as np
import pyautogui
x=y=x1=y1=0
cam=cv2.VideoCapture(0)
myhands=mp.solutions.hands
hansd=myhands.Hands()

mydraw=mp.solutions.drawing_utils

while 1:
    ret,frame=cam.read()
    frame=cv2.flip(frame,1)

    framergb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    outuput=hansd.process(framergb)
    print(outuput.multi_hand_landmarks)

    h,w,_=frame.shape
    if outuput.multi_hand_landmarks:
        for handlasmrk in outuput.multi_hand_landmarks:
            mydraw.draw_landmarks(frame, handlasmrk, myhands.HAND_CONNECTIONS)
            for num ,landmarksi in enumerate(handlasmrk.landmark):
                positionx,positony=int(landmarksi.x*w),int(landmarksi.y*h)

                if num==8:
                    cv2.circle(frame,(positionx,positony),10,(255,168,175),-1)
                    x=positionx
                    y=positony
                if num == 4:
                    cv2.circle(frame, (positionx, positony), 10, (189, 168, 175), -1)
                    x1=positionx
                    y1=positony

        cx,cy=(x+x1)//2,(y + y1) // 2
        cv2.circle(frame,(cx,cy),10,(255,0,0),5)
        dist=((x1-x)**2+(y1-y)**2)**(0.5)//4
        #print(dist)
        cv2.line(frame,(x,y),(x1,y1),(0,255,186),10)

        if dist>35:
             pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

    cv2.imshow("kamera",frame)


    if cv2.waitKey(1) & 0XFF==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()