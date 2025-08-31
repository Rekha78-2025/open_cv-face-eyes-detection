import cv2 

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

capture = cv2.VideoCapture(0) 

while True: 
    isTrue, frame = capture.read() 
    
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    roi = face_detector.detectMultiScale(grey_frame, 1.2, 3) 
    # print(roi) 
    
    for x,y,w,h in roi:
        cv2.rectangle(frame, (x, y), (x+h, y+w), (10, 230, 1), 3)

    cv2.putText(frame, text = f"Numbers of persons: {len(roi)}", 
    org = (20,20), fontFace = 2, fontScale = 1.1,color = (20,240,90))
    
    cv2.imshow("Read faces", frame) 
    cv2.imshow("grey_faces", grey_frame) 
    
    if cv2.waitKey(20) & 0xff == ord("w"):
        break 
    
    