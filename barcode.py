import cv2, time
from pyzbar.pyzbar import decode
from pydub import AudioSegment
from pydub.playback import play


# capture webcam 
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success,frame = cap.read()
    # flip the image like mirror image 
    frame  = cv2.flip(frame,1)
    detectedBarcode = decode(frame)
    if not detectedBarcode:
        print("No Barcodes Detected")
    else:
        for barcode in detectedBarcode:
            if barcode.data != "":
                print(barcode)
                cv2.putText(frame,str(barcode.data),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)

    # time.sleep(1)
    cv2.imshow('scanner' , frame)
    if cv2.waitKey(1) == ord('q'):
        break