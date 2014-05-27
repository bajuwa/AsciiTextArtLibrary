# asciilib test file

# make sure to import the proper library for testing
# use from/* to avoid having to change the test file for each new version
from frame_v1_2 import *
from text_v1_2 import *
from drawings import *

# Test Cases

###################
### Test Case 0 ###
###################
# set up samples to initiate TextField for a range of different scenarios

properSampleText = ["Hello.", 
                    "My name is Kaylyn.",
                    "I am testing out my python library",
                    "It can help ASCII text artists manage and use their art in different ways.",
                    "Python programmers can also use it to format their command-line style programs.",
                    "Hope it passes all it's tests though...."
                    ]

properTitleText = ["Testing my titles all day long~"]

defectSampleNonStringList = [1, 4, properSampleText, "Muahaha"]

defectSampleEmptyList = []

defectSampleListOfEmptyLists = [[],[], []]

defectSampleString = "Muahahaha"

# proper test:
properTextField = TextField(properSampleText)
properTitleTextField = TextField(properTitleText)
# defect test: (make sure to comment these out once tested as they cause crashes)
#defectSampleNonStringListTextField = TextField(defectSampleNonStringList)
#defectSampleEmptyListTextField = TextField(defectSampleEmptyList)
#defectSampleListOfEmptyListsTextField = TextField(defectSampleListOfEmptyLists)
#defectSampleStringTextField = TextField(defectSampleString)









########################################
### Test Case B1 - addFrameToDrawing ###
########################################
# checks by printing it's result

print("Test Case B1 - addFrameToDrawing")
input()

print("Test using properties:")
print("top: right kitty")
print("left: right mouse")
print("right: left mouse")
print("bottom: left kitty")
input()
frame = Frame(Drawing(dRightKitty), Drawing(dMiniMouse), Drawing.flipHorizontally(Drawing(dMiniMouse)), Drawing.flipHorizontally(Drawing(dRightKitty)))
framedBulletted = Frame.addFrameToDrawing(Drawing(dDragon), frame, "left", "top", 3)
framedBulletted.draw()
##frame._topDrawing.draw()
##frame._leftDrawing.draw()
##frame._rightDrawing.draw()
##frame._bottomDrawing.draw()
input()

print("left-right repeats set to True")
input()
frame.setRepeats(False, True, True, False)
framedBulletted = Frame.addFrameToDrawing(Drawing(dDragon), frame, "left", "top", 3)
framedBulletted.draw()
input()

print("top-bottom aligns set to left-right")
input()
frame.setAlignments("left", "top", "bottom", "right")
framedBulletted = Frame.addFrameToDrawing(Drawing(dDragon), frame, "left", "top", 3)
framedBulletted.draw()
input()

