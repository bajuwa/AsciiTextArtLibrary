#File: jigsaw_v1_2.py
#Created By: Kaylyn Garnett
#For use in ASCIIlib Version: 1.2

#Imports required:
from drawing_v1_2 import *


##############################
###Classes - Jigsaw Drawing###
##############################
#Purpose: Combines a Jigsaw Base and array of Jigsaw Pieces to create a complete (dynamic) Drawing Object
class Jigsaw(Drawing):
    #Note: Anything that starts with an _ should be treated as private
    
    #########
    #Members#
    #########
    #Note: remember it inherets _drawing and _original
    #_drawing/_original will be the useable "compiled" drawings so that they can use all the Drawing methods as well
    #Note: The following members are used by the class to compile the useable Drawing, and should not be displayed/modified as Drawings
    #Note: The index of the pieces array should correspond with the appropriate anchorpoint in base as to where it should be able to attach to
    _base = [] #type: JigsawBase
    _pieces = [] #type: Array of JigsawPieces

    ########################
    #Methods - Init/Set/Get#
    ########################

    def __init__(self, newBase, newPieces):
        if type(newBase) is not JigsawBase or \
           type(newPieces) is not list:
            print("Error: parameter type mismatch in Jigsaw.__init__()")
            self._base = JigsawBase("", [])
            self._pieces = []
            return 1
        for piece in newPieces:
            if type(piece) is not JigsawPiece:
                print("Error: parameter type mismatch in Jigsaw.__init__()")
                return 1
        self._base = copy.deepcopy(newBase)
        self._pieces = copy.deepcopy(newPieces)
        self.assembleJigsawDrawing()
        super().__init__(self.getDrawing())
        return

    def getBase(self):
        return self._base

    def getPieces(self):
        return self._pieces

    def setBase(self, newBase):
        if type(newBase) is not JigsawBase:
            print("Error: parameter type mismatch in Jigsaw.setBase()")
            return 1
        self._base = copy.deepcopy(newBase)

    def setPiece(self, singlePiece, index):
        if type(singlePiece) is not JigsawPiece or \
           type(index) is not int or \
           index >= len(self._pieces) or \
           index < 0:
            print("Error: parameter type mismatch in Jigsaw.setBase()")
            return 1
        self._pieces[index] = copy.deepcopy(singlePiece)
        
    #takes two pieces that were created as 'puzzle piece' and sticks them together
    #note: the first line of a 'puzzle piece' type drawing is a single char, this is where the joint between images will be
    #note: the second line of a pp drawing is a single char, denoting what the joint-char should be replaced with ("", " ", "/", etcc)
    #the first piece will be considered the base, and the second will be laid overtop
    def assembleJigsawDrawing(self):
        base = copy.deepcopy(self.getBase())

        for i in range(0, len(base.getAnchorPoints())):
            #prep both pieces
            overlay = copy.deepcopy(self.getPieces()[i])
            #make base big enough to accomodate the new piece
            base.bufferAlign("center", "center", base.getWidth()+(2*overlay.getWidth()), base.getHeight()+(2*overlay.getHeight()))

            #find overlays joint and make the mend 
            overlaysJointCoord = overlay.getCoordOfChar(overlay.getJoint(), 1)
            mendedOverlay = Drawing(overlay.getMendedDrawing())
            del overlay
            #find bases joint and record it for later
            basesJointCoord = base.getCoordOfChar(base.getAnchorPoints()[i], 1)

            #overlay the two pieces
            #must buffer the overlay so that it's joint is in the same column as the bases, without regard to overall width
            #  math:   length of original overlay + difference of the 2 column index * 2 <- x2 because it must add the difference to both side of the drawing
            mendedOverlay.bufferAlign("center", "center", mendedOverlay.getWidth()+(basesJointCoord[0]-overlaysJointCoord[0])*2, mendedOverlay.getHeight())
            # then buffer to base's width to remove excess on the overlays right side
            mendedOverlay.bufferAlign("left", "center", base.getWidth(), mendedOverlay.getHeight())

            #now find the area of the base that will need to be overlayed
            spliceRange = [basesJointCoord[1]-overlaysJointCoord[1], basesJointCoord[1]+mendedOverlay.getHeight()-overlaysJointCoord[1]]
            baseSplice = Drawing(base.getDrawing()[spliceRange[0]:spliceRange[1]])
            overlayedSplice = Drawing.overlayDrawings(baseSplice, mendedOverlay, " ", "center", "center")
            del mendedOverlay
            del baseSplice

            #put the now combined rows back into their proper place in the base
            fullDrawing = Drawing(base.getDrawing()[:spliceRange[0]] + overlayedSplice.getDrawing() + base.getDrawing()[spliceRange[1]:])
            #trim all excess whitespace before returning final product
            fullDrawing.trim()
            base.setDrawing(fullDrawing.getDrawing())
            del fullDrawing

        #Assign the new drawing to the _drawing variable
        self.setDrawing(base.getDrawing())
        return 0


###########################
###Classes - Jigsaw Base###
###########################
#Purpose: Acts as the base to the jigsaw drawing and stores info for attaching pieces
class JigsawBase(Drawing):
    #Note: Anything that starts with an _ should be treated as private
    
    #########
    #Members#
    #########
    #Note: remember it inherets _drawing and _original
    #_drawing/_original will be the useable "base" components for this class
    _arrayOfAnchorPoints = [] #Each anchor point is a single-element string that denotes what character in the drawing should be used to attach a JigsawPiece

    ########################
    #Methods - Init/Set/Get#
    ########################

    #Note: Will default the init method if any of the anchor points appear more/less than once in a given base
    def __init__(self, basePseudoDrawing, anchorPoints):
        if type(basePseudoDrawing) is not list or\
           type(anchorPoints) is not list:
            print("Error: parameter type mismatch in JigsawBase __init__()")
            return 1
        for anchor in anchorPoints:
            if type(anchor) is not str or\
               len(anchor) != 1:
                print("Error: parameter type mismatch in JigsawBase __init__()")
                return 1
        #Calculate how many of each anchor point are in the pseudodrawing, and only procede if there is only 1 of each anchor point    
        count = [0] * len(anchorPoints) #each element in count refers to the relative element in anchor points
        for row in basePseudoDrawing:
            for character in row:
                for i in range(0, len(anchorPoints)):
                    if character == anchorPoints[i]:
                        count[i] += 1
        #now check to make sure each element in count is 1
        for element in count:
            if element != 1:
                print("Error: Incorrect number of instances of an anchor point (only 1 instance allowed)")
                return 1

        super().__init__(basePseudoDrawing)
        self._arrayOfAnchorPoints = copy.deepcopy(anchorPoints)

    #Purpose: Act as secondary constructor for formatted drawings where first element is the anchorPoints array, and rest is the drawing
    def initFromFormattedJBDrawing(formattedDrawing):
        if type(formattedDrawing) is not list or \
           type(formattedDrawing[0]) is not list:
            print("Error: parameter type mismatch in JigsawBase.initFromFormattedJBDrawing")
            return 1
        for anchor in formattedDrawing[0]:
            if type(anchor) is not str or\
               len(anchor) != 1:
                print("Error: parameter type mismatch in JigsawBase.initFromFormattedJBDrawing")
                return 1
        return JigsawBase(formattedDrawing[1:], formattedDrawing[0])
        
    def getAnchorPoints(self):
        return self._arrayOfAnchorPoints

    def setAnchorPoints(self, anchors):
        if type(anchors) is not list:
            print("Error: parameter type mismatch in JigsawBase.setAnchorPoints()")
            return 1
        for a in anchors:
            if type(a) is not str or \
               len(a) != 1:
                print("Error: parameter type mismatch in JigsawBase.setAnchorPoints()")
                return 1
        self._arrayOfAnchorPoints = anchors


############################
###Classes - Jigsaw Piece###
############################
#Purpose: Acts as a single piece to the jigsaw drawing and stores info for joints and mends
class JigsawPiece(Drawing):
    #Note: Anything that starts with an _ should be treated as private
    
    #########
    #Members#
    #########
    #Note: remember it inherets _drawing and _original
    #_drawing/_original will be the useable "base" components for this class
    _joint = "" #the single char string that shows where the piece should be attached
    _mend = "" #the single char string that replaces the _joint after being attached
    _attachToBaseIndexNum = -1 #Used for pieces that can only be attached to a certain anchor index of a JigsawBase

    ########################
    #Methods - Init/Set/Get#
    ########################

    def __init__(self, pseudoDrawing, joint, mend):
        if type(pseudoDrawing) is not list or\
           type(joint) is not str or \
           len(joint) != 1 or \
           type(mend) is not str or \
           len(mend) != 1:
            print("Error: parameter type mismatch in JigsawPiece.__init__()")
            return 1
        for row in pseudoDrawing:
            if type(row) is not str:
                print("Error: parameter type mismatch in JigsawPiece.__init__()")
                return 1
        self._joint = joint
        self._mend = mend
        super().__init__(pseudoDrawing)

    #Purpose: Act as secondary constructor for a formatted drawings where first element is the anchor/joint, second is the mend, and rest is the drawing
    def initFromFormattedJPDrawing(formattedDrawing):
        if type(formattedDrawing) is not list or\
           len(formattedDrawing) < 3 or \
           type(formattedDrawing[0]) is not str or \
           len(formattedDrawing[0]) != 1 or \
           type(formattedDrawing[1]) is not str or \
           len(formattedDrawing[1]) != 1:
            print("Error: parameter type mismatch in JigsawPiece.initFromFormattedJPDrawing")
            return 1
        for row in formattedDrawing:
            if type(row) is not str:
                print("Error: parameter type mismatch in JigsawPiece.initFromFormattedJPDrawing")
                return 1
        return JigsawPiece(formattedDrawing[2:], formattedDrawing[0], formattedDrawing[1])

    def getJoint(self):
        return self._joint

    def getMend(self):
        return self._mend

    #Purpose: returns the pseudo-drawing after the mend has replaced the joint char on the JP drawing
    def getMendedDrawing(self):
        tempDrawing = copy.deepcopy(self.getDrawing())
        for i in range(0, len(tempDrawing)): #iterate over rows
            tempRow = tempDrawing[i]
            for j in range(0, len(tempRow)): #iterate over chars in row
                if tempRow[j] == self.getJoint():
                    tempRow = tempRow[:j] + self.getMend() + tempRow[j+1:]
                    return (tempDrawing[:i] + [tempRow] + tempDrawing[i+1:])
        return 1 #getting here means the mend was not found/fixed, so return error

    def setPrefferedAnchorIndex(self, anchorIndex):
        if type(anchorIndex) is not int:
            print("Error: parameter type mismatch in JigsawPiece.setPrefferedAnchorIndex")
            return 1
        self._attachToBaseIndexNum = anchorIndex
        return
        
    def getPrefferedAnchorIndex(self):
        return self._attachToBaseIndexNum
            
