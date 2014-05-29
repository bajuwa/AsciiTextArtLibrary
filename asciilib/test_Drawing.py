# asciilib test file

# make sure to import the proper library for testing
# use from/* to avoid having to change the test file for each new version
from drawing import *
from stored_drawings import *

# Test Cases
# A - init/set/get methods
# B - special generators/abstract getters/setter
# C - returns a new object based off a parameter object

############################
### Test Case A1  - init ###
############################

## NOTE: all samples are already imported from drawings
input("Test Case A1 - init")
rightKitty = Drawing(dRightKitty)
rightMouse = Drawing(dMiniMouse)
rightDragon = Drawing(dDragon)
bat = Drawing(dBat)
input("Done Test Case A1 - init")
print()


#################################
##### Test Case A2  - set/get ###
#################################

input("Test Case A2 - set/get")
print()

input("rightKitty.getDrawing()")
print(str(rightKitty.getDrawing()))
print()

input("rightKitty.draw()")
rightKitty.draw()
print()

input("rightKitty.getRow(0)")
print(str(rightKitty.getRow(0)))
print()

input("rightKitty.setDrawing(bat)")
rightKitty.setDrawing(bat)
print()

input("rightKitty.getDrawing()")
print(str(rightKitty.getDrawing()))
print()

input("rightKitty.draw()")
rightKitty.draw()
print()

input("rightKitty.getOriginal()")
print(str(rightKitty.getOriginal()))
print()

input("rightKitty.resetDrawing()")
rightKitty.resetDrawing()
print()

input("rightKitty.draw()")
rightKitty.draw()
print()

input("rightKitty.setOriginal(bat)")
rightKitty.setOriginal(bat)
print()

input("rightKitty.getOriginal()")
print(str(rightKitty.getOriginal()))
print()

input("rightKitty.draw()")
rightKitty.draw()
print()

input("rightKitty.resetDrawing()")
rightKitty.resetDrawing()
print()

input("rightKitty.draw()")
rightKitty.draw()
print()

input("rightKitty.setRow(2, 'bwahahaha')")
rightKitty.setRow(2, 'bwahahaha')
print()

input("rightKitty.draw()")
rightKitty.draw()
print()

input("rightKitty.setOriginal(dRightKitty)")
rightKitty.setOriginal(dRightKitty)
print()

input("rightKitty.resetDrawing()")
rightKitty.resetDrawing()
print()

input("rightKitty.draw()")
rightKitty.draw()
print()


########################################
### Test Case B1  - Abstract Getters ###
########################################

input("Test Case B1 - Abstract Getters")
print()

input("rightKitty.draw()")
rightKitty.draw()
print()

input("rightKitty.getHeight()")
print(str(rightKitty.getHeight()))
print()

input("rightKitty.getWidth()")
print(str(rightKitty.getWidth()))
print()

input("rightKitty.howManyCanFit(0, 0)")
print(str(rightKitty.howManyCanFit(0, 0)))
print()

input("rightKitty.howManyCanFit(5, 0)")
print(str(rightKitty.howManyCanFit(5, 0)))
print()

input("rightKitty.howManyCanFit(0, 6)")
print(str(rightKitty.howManyCanFit(0, 6)))
print()

input("rightKitty.howManyCanFit(20, 20)")
print(str(rightKitty.howManyCanFit(20, 20)))
print()

input("rightKitty.howManyCanFit(2000, 2000)")
print(str(rightKitty.howManyCanFit(2000, 2000)))
print()

input("rightKitty.numOfCharsInRowFromRight(0, ' ')")
print(str(rightKitty.numOfCharsInRowFromRight(0, " ")))
print()

input("rightKitty.numOfCharsInRowFromRight(5, 'g')")
print(str(rightKitty.numOfCharsInRowFromRight(5, "g")))
print()

input("rightKitty.numOfCharsInRowFromLeft(0, ' ')")
print(str(rightKitty.numOfCharsInRowFromLeft(0, " ")))
print()

input("rightKitty.numOfCharsInRowFromLeft(5, 'g')")
print(str(rightKitty.numOfCharsInRowFromLeft(5, "g")))
print()

input("rightKitty.numOfCharsInColumnFromTop(0, ' ')")
print(str(rightKitty.numOfCharsInColumnFromTop(0, " ")))
print()

input("rightKitty.numOfCharsInColumnFromTop(5, 'g')")
print(str(rightKitty.numOfCharsInColumnFromTop(5, "g")))
print()

input("rightKitty.numOfCharsInColumnFromBottom(0, ' ')")
print(str(rightKitty.numOfCharsInColumnFromBottom(0, " ")))
print()

input("rightKitty.numOfCharsInColumnFromBottom(5, 'g')")
print(str(rightKitty.numOfCharsInColumnFromBottom(5, "g")))
print()

input("rightKitty.isRowEmpty(0)")
print(str(rightKitty.isRowEmpty(0)))
print()

input("rightKitty.isRowEmpty(5)")
print(str(rightKitty.isRowEmpty(5)))
print()

input("rightKitty.numOfCharInRow(0, ' ')")
print(str(rightKitty.numOfCharInRow(0, " ")))
print()

input("rightKitty.numOfCharInRow(5, 'g')")
print(str(rightKitty.numOfCharInRow(5, "g")))
print()

input("rightKitty.numOfCharInDrawing('g')")
print(str(rightKitty.numOfCharInDrawing('g')))
print()

input("rightKitty.numOfCharInDrawing(' ')")
print(str(rightKitty.numOfCharInDrawing(" ")))
print()

input("rightKitty.numOfCharInDrawing('_')")
print(str(rightKitty.numOfCharInDrawing("_")))
print()

input("rightKitty.numOfCharInDrawing('/')")
print(str(rightKitty.numOfCharInDrawing('/')))
print()

input("rightKitty.numOfCharInDrawing('@')")
print(str(rightKitty.numOfCharInDrawing("@")))
print()


###############################
### Test Case B2  - Buffers ###
###############################

input("Test Case B2 - Abstract Setters")
print()

input("rightKitty.trim() + draw()")
rightKitty.trim()
rightKitty.draw()
print()

input("rightKitty.bufferAlign('center', 'center', 0, 0) + draw()")
rightKitty.bufferAlign('center', 'center', 0, 0)
rightKitty.draw()
print()

input("rightKitty.resetDrawing() + draw()")
rightKitty.resetDrawing()
rightKitty.draw()
print()

input("rightKitty.bufferAlign('left', 'bottom', 10, 10) + draw()")
rightKitty.bufferAlign('left', 'bottom', 10, 10)
rightKitty.draw()
print()

input("rightKitty.resetDrawing() + draw()")
rightKitty.resetDrawing()
rightKitty.draw()
print()

input("rightKitty.bufferAlign('right', 'top', 50, 50) + draw()")
rightKitty.bufferAlign('right', 'top', 50, 50)
rightKitty.draw()
print()

input("rightKitty.trim() + draw()")
rightKitty.trim()
rightKitty.draw()
print()

# test addBorder once Border Class has been tested


#####################################
### Test Case C1  - Group Getters ###
#####################################

##input("Test Case C1  - Group Getters")
##print()






