# @Author: ASHISH SASMAL <ashishsasmal1>
# @Date:   15-09-2020
# @Last modified by:   ashish
# @Last modified time: 17-09-2020

# 408,93
# 549, 116

import cv2
import imutils
import sys
from image_align import alignImages
import pytesseract

img = cv2.imread("Test/"+sys.argv[1], cv2.IMREAD_COLOR)
temp = cv2.imread("Test/"+sys.argv[2], cv2.IMREAD_COLOR)

locs = {"accno":None,
            "amt":None,
            "name":None,
            "date":None
            }

value  = {"accno":None,
            "amt":None,
            "name":None,
            "date":None
            }

ROIS = cv2.selectROIs("Select Rois",temp)

confirm="n"
while confirm=="n":
    print(f"[ROIS selected : {len(ROIS)} ]")
    confirm = input("Confirm ROIs? [y/n] : ")
    if confirm!="n":
        break
    ROIS = cv2.selectROIs("Select Rois",temp)
# initBB = cv2.selectROI("Frame", temp, fromCenter=False,showCrosshair=True)

locs["accno"] = ROIS[0]
locs["amt"] = ROIS[1]
locs["name"] = ROIS[2]
locs["date"] = ROIS[3]

print("Aligning images ...")
aligned,H = alignImages(img, temp)
#


for i in locs:
    (x, y, w, h) = (locs[i][0], locs[i][1], locs[i][2] , locs[i][3])
    roi = temp[y:y+h, x:x+w]
    rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(rgb)
    print(f"[{i}: {text} ]")

cv2.imshow("Input", imutils.resize(img, width=700))
cv2.imshow("Output", imutils.resize(aligned, width=700))
cv2.waitKey(0)
