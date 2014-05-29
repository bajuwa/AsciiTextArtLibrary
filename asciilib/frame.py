#File: frame_v1_2.py
#Created By: Kaylyn Garnett
#For use in ASCIIlib Version: 1.2

#Imports required:
from drawing import *


######################
###Classes - Border###
######################

#Purpose: A class to store information about a "border" and provide proper methods to modify the information
#Note: A border is a simple 1-char-width edge added to the outside of a drawing
class Border:
    #Note: Anything that starts with an _ should be treated as private
    
    #########
    #Members#
    #########
    
    _corners = [" ", " ", " ", " "]
    _borders = [" ", " ", " ", " "]  

    ########################
    #Methods - Init/Set/Get#
    ########################

    def __init__(self, arrayOfCorners, arrayOfBorders):
        self._corners = [" ", " ", " ", " "]
        self._borders = [" ", " ", " ", " "]
        #run through a check to make sure each array is formatted correctly and each entry is a char, not string
        if len(arrayOfCorners) == 4 and len(arrayOfBorders) == 4:
            for i in range(0, 4):
                if (type(arrayOfCorners[i]) is str) and (len(arrayOfCorners[i]) == 1) and \
                   (type(arrayOfBorders[i]) is str) and (len(arrayOfBorders[i]) == 1):
                    self._corners[i] = arrayOfCorners[i]
                    self._borders[i] = arrayOfBorders[i]

    def getCorners(self):
        return self._corners

    def setCorners(self, arrayOfCorners):
        self._corners = arrayOfCorners
        return 0
    
    def getBorders(self):
        return self._borders

    def setBorders(self, arrayOfBorders):
        self._borders = arrayOfBorders
        return 0





######################
###Classes - Frames###
######################

#Purpose: A class to store information about a "frame" and provide proper methods to modify the information
#Note: A frame is a more elaborate version of a border that makes use of other drawings instead of single chars
class Frame:
    #Note: Anything that starts with an _ should be treated as private
    
    #########
    #Members#
    #########
    
    _topDrawing = []
    _leftDrawing = []
    _rightDrawing = []
    _bottomDrawing = []
    _topAlign = "center"
    _leftAlign = "center"
    _rightAlign = "center"
    _bottomAlign = "center"
    _topRepeat = False
    _leftRepeat = False
    _rightRepeat = False
    _bottomRepeat = False

    ########################
    #Methods - Init/Set/Get#
    ########################

    def __init__(self, top, left, right, bottom):
        self._topDrawing = copy.deepcopy(top)
        self._leftDrawing = copy.deepcopy(left)
        self._rightDrawing = copy.deepcopy(right)
        self._bottomDrawing = copy.deepcopy(bottom)

    def getTop(self):
        return self._topDrawing

    def getLeft(self):
        return self._leftDrawing

    def getRight(self):
        return self._rightDrawing

    def getBottom(self):
        return self._bottomDrawing

    def getTopAlign(self):
        return self._topAlign

    def getLeftAlign(self):
        return self._leftAlign

    def getRightAlign(self):
        return self._rightAlign

    def getBottomAlign(self):
        return self._bottomAlign

    def getTopRepeat(self):
        return self._topRepeat

    def getLeftRepeat(self):
        return self._leftRepeat

    def getRightRepeat(self):
        return self._rightRepeat

    def getBottomRepeat(self):
        return self._bottomRepeat

    def setTop(self, drawing):
        _topDrawing = copy.deepcopy(drawing)
        return 0

    def setLeft(self, drawing):
        _leftDrawing = copy.deepcopy(drawing)
        return 0

    def setRight(self, drawing):
        _rightDrawing = copy.deepcopy(drawing)
        return 0

    def setBottom(self, drawing):
        _bottomDrawing = copy.deepcopy(drawing)
        return 0

    def setTopAlign(self, string):
        self._topAlign = string
        return 0

    def setLeftAlign(self, string):
        self._leftAlign = string
        return 0

    def setRightAlign(self, string):
        self._rightAlign = string
        return 0

    def setBottomAlign(self, string):
        self._bottomAlign = string
        return 0

    def setAlignments(self, top, left, right, bottom):
        self._topAlign = top
        self._leftAlign = left
        self._rightAlign = right
        self._bottomAlign = bottom
        return 0

    def setTopRepeat(self, boolean):
        self._topRepeat = boolean
        return 0

    def setLeftRepeat(self, boolean):
        self._leftRepeat = boolean
        return 0

    def setRightRepeat(self, boolean):
        self._rightRepeat = boolean
        return 0

    def setBottomRepeat(self, boolean):
        self._bottomRepeat = boolean
        return 0

    def setRepeats(self, top, left, right, bottom):
        self._topRepeat = top
        self._leftRepeat = left
        self._rightRepeat = right
        self._bottomRepeat = bottom
        return 0
        
    ##########################################
    #Methods - Instance Methods - Generators #
    ##########################################
    #These methods call upon the instance info to generate parts of the Frame for the final piece
   
    #Purpose: Generates the left border drawing by taking into account repetition and alignment
    def generateLeftBorder(self, targetHeight):
        if type(targetHeight) is int and targetHeight > 0:
            #Calculate the number of side-frames are required to fully enclose the image, if border repeats
            if self.getLeftRepeat() == True:
                #Note: the [1] is to grab the returning value that corresponds to the height value (check howManyCanFit method)
                #Note: +2 will ensure that when buffered, if center-aligned, it won't create weird images if they fit perfectly to begin with
                numOfLeftBorders = self.getLeft().howManyCanFit(self.getLeft().getWidth(), targetHeight)[1]+2

                #Now create the side borders, and buffer those with the center to create a row
                leftBorder = Drawing.combineIntoColumn([self.getLeft()]*numOfLeftBorders, "center", 0)
                leftBorder.bufferAlign("center", self.getLeftAlign(), leftBorder.getWidth(), targetHeight)
            else:
                leftBorder = copy.deepcopy(self.getLeft())
                leftBorder.bufferAlign("center", self.getLeftAlign(), self.getLeft().getWidth(), targetHeight)
            return leftBorder
        else:
            return Drawing([""])
        
    #Purpose: Generates the right border drawing by taking into account repetition and alignment
    def generateRightBorder(self, targetHeight):
        if type(targetHeight) is int and targetHeight > 0:
            #Calculate the number of side-frames are required to fully enclose the image, if border repeats
            if self.getRightRepeat() == True:
                #Note: the [1] is to grab the returning value that corresponds to the height value (check howManyCanFit method)
                #Note: +2 will ensure that when buffered, if center-aligned, it won't create weird images if they fit perfectly to begin with
                numOfRightBorders = self.getRight().howManyCanFit(self.getRight().getWidth(), targetHeight)[1]+2

                #Now create the side borders, and buffer those with the center to create a row
                rightBorder = Drawing.combineIntoColumn([self.getRight()]*numOfRightBorders, "center", 0)
                rightBorder.bufferAlign("center", self.getRightAlign(), rightBorder.getWidth(), targetHeight)
            else:
                rightBorder = copy.deepcopy(self.getRight())
                rightBorder.bufferAlign("center", self.getRightAlign(), self.getRight().getWidth(), targetHeight)
            return rightBorder
        else:
            return Drawing([""])
        
    #Purpose: Generates the left border drawing by taking into account repetition and alignment
    def generateTopBorder(self, targetWidth):
        if type(targetWidth) is int:
            #Calculate the number of side-frames are required to fully enclose the image, if border repeats
            if self.getTopRepeat() == True:
                #Note: the [1] is to grab the returning value that corresponds to the height value (check howManyCanFit method)
                #Note: +2 will ensure that when buffered, if center-aligned, it won't create weird images if they fit perfectly to begin with
                numOfTopBorders = self.getTop().howManyCanFit(targetWidth, self.getTop().getHeight())[0]+2

                #Now create the side borders, and buffer those with the center to create a row
                topBorder = Drawing.combineIntoRow([self.getTop()]*numOfTopBorders, "center", 0)
                topBorder.bufferAlign("center", self.getTopAlign(), targetWidth, topBorder.getHeight())
            else:
                topBorder = copy.deepcopy(self.getTop())
                topBorder.bufferAlign(self.getTopAlign(), "center", targetWidth, self.getTop().getHeight())
            return topBorder
        else:
            return Drawing([""])
        
    #Purpose: Generates the left border drawing by taking into account repetition and alignment
    def generateBottomBorder(self, targetWidth):
        if type(targetWidth) is int:
            #Calculate the number of side-frames are required to fully enclose the image, if border repeats
            if self.getBottomRepeat() == True:
                #Note: the [1] is to grab the returning value that corresponds to the height value (check howManyCanFit method)
                #Note: +2 will ensure that when buffered, if center-aligned, it won't create weird images if they fit perfectly to begin with
                numOfBottomBorders = self.getBottom().howManyCanFit(targetWidth, self.getBottom().getHeight())[0]+2

                #Now create the side borders, and buffer those with the center to create a row
                bottomBorder = Drawing.combineIntoRow([self.getBottom()]*numOfBottomBorders, "center", 0)
                bottomBorder.bufferAlign("center", self.getBottomAlign(), targetWidth, bottomBorder.getHeight())
            else:
                bottomBorder = copy.deepcopy(self.getBottom())
                bottomBorder.bufferAlign(self.getBottomAlign(), "center", targetWidth, self.getBottom().getHeight())
            return bottomBorder
        else:
            return Drawing([""])



    #########################
    #Methods - Class Methods#
    #########################
    #These classes are meant to be used to return new values/drawings, and should not be called by an object instance
    
    #Purpose: Frames a drawing with a given Frame object, with a certain amount of padding in between the two
    #Note: This is a class method as opposed to instance method because it is not as easy to reverse as a regular Border
    def addFrameToDrawing(drawing, frame, LRAlign, TBAlign, padding):        
        #Buffer the center image to account for padding
        center = copy.deepcopy(drawing)
        center.bufferAlign("center", "center", center.getWidth()+(padding*2), center.getHeight()+(padding*2))

        #Get each of the Individual drawings of the frame
        centerDrawingBasedWidth = center.getWidth() + frame.getLeft().getWidth()+ frame.getRight().getWidth()
        frameBasedWidth = max([frame.getTop().getWidth(), frame.getBottom().getWidth()])
        minimumWidth = max([centerDrawingBasedWidth, frameBasedWidth])
        top = frame.generateTopBorder(minimumWidth)
        left = frame.generateLeftBorder(center.getHeight())
        right = frame.generateRightBorder(center.getHeight())
        bottom = frame.generateBottomBorder(minimumWidth)
        
        #Calculate how much space needs to be added (if any) to the sides of the center image to balance the width of the final image
        extraSpace = minimumWidth - (center.getWidth() + left.getWidth() + right.getWidth())
        if extraSpace > 0:
            center.bufferAlign(LRAlign, TBAlign, center.getWidth()+extraSpace, center.getHeight())


        #Now create the side borders, and buffer those with the center to create a row
        middleSection = Drawing.combineIntoRow([left, center, right], TBAlign, 0)

        #Finally add all three pieces together
        return Drawing.combineIntoColumn([top, middleSection, bottom], "center", 0)
