#File: drawing_v1_2.py
#Created By: Kaylyn Garnett
#For use in ASCIIlib Version: 1.2

import copy
import math

#######################
###Classes - Drawing###
#######################
#Purpose: A class to store information about a "drawing" and provide proper methods to modify the drawing
#Note: A drawing is an array of strings, where each string is a row of the drawing

class Drawing:
    #Note: Anything that starts with an _ should be treated as private
    
    #########
    #Members#
    #########
    
    _original = []
    _drawing = []
    

    ########################
    #Methods - Init/Set/Get#
    ########################
    
    def __init__(self, arrayOfStrings):
        self._drawing = copy.deepcopy(arrayOfStrings)
        self._original = copy.deepcopy(arrayOfStrings)
        return

    def getDrawing(self):
        return self._drawing

    def getRow(self, rowIndex):
        return self._drawing[rowIndex]

    def getOriginal(self):
        return self._original

    def setDrawing(self, newDrawing):
        if type(newDrawing) is Drawing:
            self._drawing = copy.deepcopy(newDrawing.getDrawing())
        else:
            self._drawing = copy.deepcopy(newDrawing)
        return
            
    def resetDrawing(self):
        self.setDrawing(copy.deepcopy(self._original))
        return

    def setOriginal(self, newOriginal):
        if type(newOriginal) is Drawing:
            self._original = copy.deepcopy(newOriginal.getOriginal())
        else:
            self._original = copy.deepcopy(newOriginal)
        return

    def setRow(self, rowIndex, string):
        self._drawing[rowIndex] = string
        return


    ############################
    #Methods - Abstract Getters#
    ############################
    ## Getters that calculate information based on the drawing ##
        
    #Purpose: Draws the drawing to the screen as an image, not as an array
    def draw(self):
        for row in self._drawing:
            print(row)
        return
    
    #Purpose: Retrieves height by calculating the number of rows, aka the number of string elements in the array    
    def getHeight(self):
        return len(self._drawing)

    #Purpose: Retrieves the maximum width out of all the rows
    #Note: deals with the maximum to account for a non-buffered image with irregular width
    def getWidth(self):
        widthList = []
        for row in self._drawing:
            widthList.append(len(row))
        return max(widthList)
    
    #Purpose: returns a 2-element array specifying how many times the drawing can fit in a row of targetWidth and a column of targetHeight
    #Note: array is read: [how many can fit in a row of targetWidth, how many can fit in a column of targetHeight]
    def howManyCanFit(self, targetWidth, targetHeight):
        totalInRow = math.floor(targetWidth/len(self._drawing[0]))
        totalInColumn = math.floor(targetHeight/len(self._drawing))
        return [totalInRow, totalInColumn]

    #Purpose: Returns the number of instances of a certain char are found in a row, starting from the right
    def numOfCharsInRowFromRight(self, rowIndex, char):
        count = 0
        tempRow = self._drawing[rowIndex]
        for i in range(len(tempRow)-1, -1, -1): #iterate through chars in row, right to left
            if tempRow[i] == char:
                count += 1
            else:
                return count
        return count

    #Purpose: Returns the number of instances of a certain char are found in a row, starting from the right
    def numOfCharsInRowFromLeft(self, rowIndex, char):
        count = 0
        tempRow = self._drawing[rowIndex]
        for rowChar in tempRow: #iterate through chars in row, left to right
            if rowChar == char:
                count += 1
            else:
                return count
        return count

    #Purpose: Returns the number of instances of a certain char are found in a column, starting from the bottom
    def numOfCharsInColumnFromTop(self, columnIndex, char):
        count = 0
        for row in self._drawing: #iterate through rows, top to bottom
            if row[columnIndex] == char:
                count += 1
            else:
                return count
        return count

    #Purpose: Returns the number of instances of a certain char are found in a column, starting from the bottom
    def numOfCharsInColumnFromBottom(self, columnIndex, char):
        count = 0
        for i in range(len(self._drawing)-1, -1, -1): #iterate through rows, bottom to top, if char is right
            tempRow = self._drawing[i]
            if tempRow[columnIndex] == char:
                count += 1
            else:
                return count
        return count

    #Purpose: Returns boolean value based on whether the row is empty/whitespace or not
    def isRowEmpty(self, rowIndex):
        #If, by scanning through the row, it hits the end of the row before a non-whitespace character, it's an empty row
        tempRow = self._drawing[rowIndex]
        for char in tempRow:
            if char != " ":
                return False
        return True

    #Purpose: Returns the number of times an instance of parameter char occurs in a row of a drawing
    def numOfCharInRow(self, rowIndex, char):        
        count = 0
        for character in self._drawing[rowIndex]:
            if character == char:
                count += 1
        return count
        
    #Purpose: Returns the number of times an instance of parameter char occurs in a drawing
    def numOfCharInDrawing(self, char):
        count = 0
        for i in range(len(self._drawing)):
            count += self.numOfCharInRow(i, char)
        return count
    
    ##############################
    #Methods - Setters: Buffering#
    ##############################
    #Warning: These methods directly modify _drawing!

    ##TODO: turn alignment options in to enums

    #Purpose: Trims excess whitespace from edges so drawing is resized to smallest possible dimensions
    #Notes: As an example, it will take a buffered image and get rid of the whitespace that might have been added
    def trim(self):
        #make sure image is buffered to avoid errors
        self.bufferAlign("center", "center", self.getWidth(), self.getHeight())
        
        #trim tops and bottoms of empty rows
        while self.isRowEmpty(0) == True:
            self.setDrawing(self.getDrawing()[1:])
        while self.isRowEmpty(self.getHeight()-1) == True:
            self.setDrawing(self.getDrawing()[:-1])

        #then trim sides
        emptyRightSpace = []
        emptyLeftSpace = []
        for i in range(self.getHeight()):
            emptyRightSpace.append(self.numOfCharsInRowFromRight(i, " "))
            emptyLeftSpace.append(self.numOfCharsInRowFromLeft(i, " "))
        self.bufferAlign("left", "center", self.getWidth()-min(emptyRightSpace), self.getHeight())
        self.bufferAlign("right", "center", self.getWidth()-min(emptyLeftSpace), self.getHeight())

        return 0


    #Purpose: adds/removes rows/characters to fit a certain dimension and alignment
    #Note: RLalign refers to "left", "center", or "right"; TBalign refers to "top", "center", or "bottom"
    def bufferAlign(self, LRAlign, TBAlign, targetWidth, targetHeight):        #Make height changes
        differenceInHeights = targetHeight - len(self._drawing)
        topBuffer = math.ceil(differenceInHeights/2)
        bottomBuffer = math.floor(differenceInHeights/2)
        if TBAlign == "top":
            if differenceInHeights >= 0:
                self._drawing += [" "*self.getWidth()] * differenceInHeights
            else:
                self._drawing = self._drawing[:targetHeight]
        elif TBAlign == "center":
            if differenceInHeights >= 0:
                self._drawing = [" "] * topBuffer + self._drawing + [" "] * bottomBuffer
            else:
                self._drawing = self._drawing[-1*topBuffer:bottomBuffer]
        elif TBAlign == "bottom":
            if differenceInHeights >= 0:
                self._drawing = [" "*self.getWidth()] * differenceInHeights + self._drawing
            else:
                self._drawing = self._drawing[-targetHeight:]
        else:
            return 1 #signifies an error

        
        #Make width changes
        for i in range(len(self._drawing)):
            #calculate adjustments - if difference is odd, an extra space will be added to the right/top
            differenceInWidth = targetWidth - len(self._drawing[i])
            rightBuffer = math.ceil(differenceInWidth/2)
            leftBuffer = math.floor(differenceInWidth/2)
            tempRow = self._drawing[i]
            if LRAlign == "left":
                if differenceInWidth >= 0:
                    self._drawing[i] += " " * differenceInWidth
                else:
                    self._drawing[i] = tempRow[:targetWidth]   
            elif LRAlign == "center":
                if differenceInWidth >= 0:
                    self._drawing[i] = " "*leftBuffer + tempRow + " "*rightBuffer
                else:
                    self._drawing[i] = tempRow[-1*leftBuffer:rightBuffer]
            elif LRAlign == "right":
                if differenceInWidth >= 0:
                    self._drawing[i] = " " * differenceInWidth + self._drawing[i]
                else:
                    self._drawing[i] = tempRow[-targetWidth:]
            else:
                return 1 #signifies an error
                
        return 0
    #END BUFFERALIGN
    
    #Purpose: Adds a simple, 1-char width border around the edge of a drawing
    #Note: To remove the border, simply trim it to 2 less width/height
    def addBorder(self, border, padding):
        # set up and add the border around the edge of the drawing
        borderedDrawing = []
        height = self.getHeight()
        width = self.getWidth()
        arrayOfCorners = border.getCorners()
        arrayOfBorders = border.getBorders()
        # top of border
        borderedDrawing.append(arrayOfCorners[0] + arrayOfBorders[0] * (width+(padding*2)) + arrayOfCorners[1])
        borderedDrawing.extend([arrayOfBorders[3] + " "*(width+(padding*2)) + arrayOfBorders[1]]*padding)
        # attaches the contents of the display
        for i in range(height):
            sampleLine = self._drawing(i)
            # attaches the appropriate line of the objects from top to bottom
            borderedDrawing.append(arrayOfBorders[3] + " "*padding + sampleLine + " "*padding + arrayOfBorders[1])

        # attaches bottom of the border
        borderedDrawing.extend([arrayOfBorders[3] + " "*(width+(padding*2)) + arrayOfBorders[1]]*padding)
        borderedDrawing.append(arrayOfCorners[2] + arrayOfBorders[2] * (width+(padding*2)) + arrayOfCorners[3])
        self.setDrawing(borderedDrawing)
        return 0
    

    #########################
    #Methods - Class Methods#
    #########################
    #These classes are meant to be used to return new values/drawings, and should not be called by an object instance

    #Purpose: Return the max height of drawings given in an array of drawings
    def getMaxHeight(arrayOfDrawings):
        heightsOfDrawings = []
        for drawing in arrayOfDrawings:
            heightsOfDrawings.append(drawing.getHeight())
        return max(heightsOfDrawings)

    #Purpose: Return the max width of drawings given in an array of drawings
    def getMaxWidth(arrayOfDrawings):
        widthsOfDrawings = []
        for drawing in arrayOfDrawings:
            widthsOfDrawings.append(drawing.getWidth())
        return max(widthsOfDrawings)

    #Purpose: Returns a coordinate array corresponding to the n-th instance of char in the drawing
    def getCoordOfChar(self, char, nthInstance):
        count = 0
        for i in range(self.getHeight()): #iterate over rows
            tempRow = self._drawing[i]
            for j in range(self.getWidth()):  #iterate over characters in a row
                tempChar = tempRow[j]
                if tempChar == char:
                    count += 1
                    if count == nthInstance:
                        return [j, i]
        #if nthInstance was not found:
        return 0
        
    #Purpose: Turns a drawing into a tiled image within specific requirements of how many in a row/column
    #Notes: Padding refers to how much whitespace is in between each tile image
    def createTiledDrawingFromTileNums(drawing, numInRow, numInColumn, padding):
        singleRow = []
        for i in range(numInRow): #must iterate a deepcopy in order to avoid passing by reference
            singleRow.append(copy.deepcopy(drawing))
        singleRow = Drawing.combineIntoRow(singleRow, "center", padding)
        tiledImage = []
        for j in range(numInColumn):
            tiledImage.append(copy.deepcopy(singleRow))
        tiledImage = Drawing.combineIntoColumn([singleRow] * numInColumn, "center", padding)
        return tiledImage

    #Purpose: Turns a drawing into a tiled image within specific WxH dimensions
    #Notes: This image will cut off any excess characters outside the given dimensions
    def createTiledDrawingFromDimensions(drawing, targetWidth, targetHeight, padding):
        numInDimensions = drawing.howManyCanFit(targetWidth, targetHeight)
        tiledDrawing = Drawing.createTiledDrawingFromTileNums(drawing, numInDimensions[0]+1, numInDimensions[1]+1, padding)
        tiledDrawing.bufferAlign("center", "center", targetWidth, targetHeight)
        return tiledDrawing

    #Purpose: Takes 2 drawings, replaces the character on the first image with the characters from the second image, skipping any CHARs in the overlaying drawing
    #Note: Will only ignore the CHARs on the outside of the drawing, for example: if char = " ", then only whitespace outside the drawing will be ignored
    #Note: Although it will buffer each image to the same dimensions, its best to do that yourself before calling this function to make sure they align properly
    def overlayDrawings(baseDrawing, overlayDrawing, char, LRAlign, TBAlign):
        #make sure they are the same size
        copyDrawings = [copy.deepcopy(baseDrawing), copy.deepcopy(overlayDrawing)]
        copies = Drawing.bufferToSameHeight(copyDrawings, TBAlign, Drawing.getMaxHeight(copyDrawings))
        copies = Drawing.bufferToSameWidth(copies, LRAlign, Drawing.getMaxWidth(copies))
        baseCopy = copies[0]
        overlayCopy = copies[1]

        for i in range(len(baseCopy.getDrawing())): #iterate over rows
            for j in range(len(baseCopy.getRow(i))): #iterate over columns
                # use numOfChars to ensure that even intended spaces in the middle of a drawing get copied over
                if (j >= overlayCopy.numOfCharsInRowFromLeft(i, char)) and (j < (len(overlayCopy.getRow(i)) - overlayCopy.numOfCharsInRowFromRight(i, char))):
                    if (i >= overlayCopy.numOfCharsInColumnFromTop(j, char)) and (i < (overlayCopy.getHeight() - overlayCopy.numOfCharsInColumnFromBottom(j, char))):
                        baseCopy.setRow(i, baseCopy.getRow(i)[:j] + overlayCopy.getRow(i)[j] + baseCopy.getRow(i)[j+1:])
        return baseCopy

    #Purpose: Buffers each drawing of an array of drawings to the same height
    def bufferToSameHeight(arrayOfDrawings, TBAlign, targetHeight):
        copyDrawings = []
        for i in range(len(arrayOfDrawings)):
            copyDrawings.append(copy.deepcopy(arrayOfDrawings[i]))
            copyDrawings[i].bufferAlign("center", TBAlign, arrayOfDrawings[i].getWidth(), targetHeight)
        return copyDrawings
    
    #Purpose: Combine an array of drawings, in order, in a row, aligned as specified
    #Notes: combines them edge-to-edge, with a certain amount of padding between each image
    def combineIntoRow(arrayOfDrawings, TBAlign, padding):
        copyDrawings = []
        for drawing in arrayOfDrawings:
            copyDrawings.append(copy.deepcopy(drawing))
        copyDrawings = Drawing.bufferToSameHeight(copyDrawings, TBAlign, Drawing.getMaxHeight(arrayOfDrawings))
        rootPseudoDrawing = copyDrawings[0].getDrawing()  #takes the first image, and modifies it by extending the strings/rows with that of other drawings
        for k in range(len(rootPseudoDrawing)): #iterate over rows
            for l in range(1, len(copyDrawings)): #iterate over drawings
                #since we start at index 1, add befores before each image (this also prevents excess buffering at the end
                rootPseudoDrawing[k] += " " * padding
                samplePseudoDrawing = copyDrawings[l].getDrawing()
                rootPseudoDrawing[k] += samplePseudoDrawing[k]
        completeRowDrawing = Drawing(rootPseudoDrawing)
        return completeRowDrawing

    #Purpose: Buffers each drawing to be combined into a row of a specific width
    def combineIntoRowWidth(arrayOfDrawings, LRAlign, TBAlign, targetWidth):
        bufferedRow = copy.deepcopy(arrayOfDrawings) #make sure to copy to you're not modifying the original
        #calculate total width of combined drawings
        totalWidth = 0
        for drawing in bufferedRow:
            totalWidth += drawing.getWidth()
        differenceInWidth = targetWidth - totalWidth
        #calculate how much each drawing gets buffered
        individualBufferPadding = math.floor(differenceInWidth/len(bufferedRow))
        #buffer each image
        for drawing in bufferedRow:
            drawing.bufferAlign(LRAlign, TBAlign,
                                drawing.getWidth() + individualBufferPadding,
                                drawing.getHeight())
        #Note: padding = 0 because focus is on equally spaced images, not padding in between them
        #since individualBufferPadding was rounded down, make sure to return the image after it's been buffered to the correct width
        bufferedRow = Drawing.combineIntoRow(bufferedRow, TBAlign, 0)
        bufferedRow.bufferAlign(LRAlign, TBAlign, targetWidth, bufferedRow.getHeight())
        return bufferedRow

    #Purpose: Returns an array of drawings buffered to the same given width
    def bufferToSameWidth(arrayOfDrawings, LRAlign, targetWidth):
        copyDrawings = copy.deepcopy(arrayOfDrawings)
        maxWidth = Drawing.getMaxWidth(copyDrawings)
        #buffer each image to the same height
        for drawing in copyDrawings:
            #Note: Does not change height, so TBAlign is irrelevant and default to "center"
            drawing.bufferAlign(LRAlign, "center", maxWidth, drawing.getHeight()) 
        return copyDrawings

    #Purpose: Returns a drawing that is composed of 
    def combineIntoColumn(arrayOfDrawings, LRAlign, padding):
        copyDrawings = copy.deepcopy(arrayOfDrawings)
        maxWidth = Drawing.getMaxWidth(copyDrawings)
        bufferedColumn = []
        #Buffer each image and add it to the column
        for i in range(len(copyDrawings)):
            copyDrawings[i].bufferAlign(LRAlign, "center", maxWidth, copyDrawings[i].getHeight())
            bufferedColumn.extend(copyDrawings[i].getDrawing())
            if padding > 0 and i != len(copyDrawings)-1:
                bufferedColumn += [" " * maxWidth] * padding
        return Drawing(bufferedColumn)

    #Purpose: Returns a column with each drawing buffered be spread equally over a given height
    def combineIntoColumnHeight(arrayOfDrawings, LRAlign, TBAlign, targetHeight):
        copyDrawings = copy.deepcopy(arrayOfDrawings)
        #figure out the total height of all the drawings being combined
        totalHeight = 0
        for drawing in copyDrawings:
            totalHeight += drawing.getHeight()
        #calculate how much each drawing gets buffered to fit the total height
        #Note: use this method of individual buffers to ensure that even if a large image is combined with a smaller one,
        # they are edited according to their individual sizes, not to a general width
        differenceInHeight = targetHeight - totalHeight
        individualBufferPadding = differenceInHeight/len(copyDrawings)
        #buffer each image to appropriate heights
        for j in range(0, len(copyDrawings)):
            copyDrawings[j].bufferAlign(LRAlign, TBAlign, copyDrawings[j].getWidth(), copyDrawings[j].getHeight() + int(individualBufferPadding))
        columnDrawing = Drawing.combineIntoColumn(copyDrawings, LRAlign, 0)
        columnDrawing.bufferAlign(LRAlign, TBAlign, columnDrawing.getWidth(), targetHeight)
        return columnDrawing

    #Purpose: Compresses 2 drawings side by side while removing excess whitespace between drawings
    def compressHorizontally(leftDrawing, rightDrawing, TBAlign, padding, targetHeight):
        #create copy/base for the upcoming edits
        bufferedDrawings = Drawing.bufferToSameHeight([copy.deepcopy(leftDrawing), copy.deepcopy(rightDrawing)], TBAlign, targetHeight)
        tempLeft = bufferedDrawings[0]
        tempRight = bufferedDrawings[1]

        #use to store the amount of whitespace that's allowed to be removed
        excessWhitespace = len(tempLeft.getDrawing()[0]) + len(tempRight.getDrawing()[0]) #sets excess whitespace to max possible length

        #find out how much whitespace to trim out from between images
        for i in range(tempLeft.getHeight()):
            totalLinesWS = tempLeft.numOfCharsInRowFromRight(i, " ") + tempRight.numOfCharsInRowFromLeft(i, " ")
            if totalLinesWS < excessWhitespace:
                    excessWhitespace = totalLinesWS

        #now remove the excess whitespace from each image
        compressed = []
        for i in range(tempLeft.getHeight()):  #iterate through each row of the drawing, from top to bottom
            tempValue = 0
            leftLine = tempLeft._drawing[i]
            rightLine = tempRight._drawing[i]
            while (tempValue < excessWhitespace-padding) and (leftLine[-1] == " "):
                #first remove as much as possible from left drawing
                leftLine = leftLine[:-1]
                tempValue += 1
            #if more still needs to be removed, take it from right drawing
            while (tempValue < excessWhitespace-padding) and (rightLine[0] == " "):
                rightLine = rightLine[1:]
                tempValue += 1
            #then add each line to the new drawing
            compressed.append(leftLine + rightLine)

        return Drawing(compressed)

    #Purpose: Compresses an array of drawings into a row while deleting excess whitespace between drawings
    def compressIntoRow(arrayOfDrawings, TBAlign, padding):
        bufferedDrawings = Drawing.bufferToSameHeight(arrayOfDrawings, TBAlign, Drawing.getMaxHeight(arrayOfDrawings))
        while len(bufferedDrawings) > 2:
            bufferedDrawings = [Drawing.compressHorizontally(bufferedDrawings[0], bufferedDrawings[1]), \
                                TBAlign, padding, Drawing.getMaxHeight(bufferedDrawings)] \
                               + bufferedDrawings[2:]
        if len(bufferedDrawings) == 2:
            bufferedDrawings = Drawing.compressHorizontally(bufferedDrawings[0], bufferedDrawings[1], \
                                                            TBAlign, padding, Drawing.getMaxHeight(bufferedDrawings))
        return bufferedDrawings


    #Purpose: Compresses 2 drawings on top of eachother while removing excess whitespace between them
    #Note: BROKEN FOR NOW.  create overlaydrawings first
    def compressVertically(topDrawing, bottomDrawing, LRAlign, padding, targetWidth):
        #create copy/base for the upcoming edits
        bufferedDrawings = Drawing.bufferToSameWidth([copy.deepcopy(topDrawing), copy.deepcopy(bottomDrawing)], LRAlign, targetWidth)
        tempTop = bufferedDrawings[0]
        tempBottom = bufferedDrawings[1]

        #use to store the amount of whitespace that's allowed to be removed
        excessWhitespace = tempTop.getHeight() + tempBottom.getHeight() #sets excess whitespace to max possible length

        #find out how much whitespace to trim out from between images
        for i in range(tempTop.getWidth()): #iterate over columns
            totalColumnsWS = tempTop.numOfCharsInColumnFromBottom(i, " ") + tempBottom.numOfCharsInColumnFromTop(i, " ")
            if totalColumnsWS < excessWhitespace:
                    excessWhitespace = totalColumnsWS

        #now remove the excess whitespace from each image by overlaying the bottom image over the top
        #Note: uses center because they are set to same width, and compressed vertically, so it shouldn't influence the drawing
        if excessWhitespace > 0:
            overlappedRows = Drawing.overlayDrawings(Drawing(tempTop.getDrawing()[-excessWhitespace:]), \
                                                     Drawing(tempBottom.getDrawing()[:excessWhitespace]), \
                                                     " ", "center", "center")

            compressed = []
            compressed.extend(tempTop.getDrawing()[:-excessWhitespace])
            compressed.extend(overlappedRows.getDrawing())
            compressed.extend(tempBottom.getDrawing()[excessWhitespace:])
        else:
            compressed = tempTop.getDrawing() + tempBottom.getDrawing()

        return Drawing(compressed)

    #Purpose: Compresses a series of images on top of eachother, eliminating excess whitespace between images, and stacks them from bottom up
    def compressIntoColumnFromBottomUp(arrayOfDrawings, LRAlign, padding, targetWidth):
        bufferedDrawings = Drawing.bufferToSameWidth(arrayOfDrawings, LRAlign, targetWidth)
        while len(bufferedDrawings) > 2:
            bufferedDrawings = [Drawing.compressVertically(bufferedDrawings[1], bufferedDrawings[0], LRAlign, padding, targetWidth)]\
                               + bufferedDrawings[2:]
        if len(bufferedDrawings) == 2:
            bufferedDrawings = Drawing.compressVertically(bufferedDrawings[1], bufferedDrawings[0], LRAlign, padding, targetWidth)
        return bufferedDrawings

    #Purpose: Compresses a series of images on top of eachother, eliminating excess whitespace between images, and stacks them from bottom up
    def compressIntoColumnFromTopDown(arrayOfDrawings, LRAlign, padding, targetWidth):
        bufferedDrawings = Drawing.bufferToSameWidth(arrayOfDrawings, LRAlign, targetWidth)
        while len(bufferedDrawings) > 2:
            bufferedDrawings = [Drawing.compressVertically(bufferedDrawings[0], bufferedDrawings[1], LRAlign, padding, targetWidth)]\
                               + bufferedDrawings[2:]
        if len(bufferedDrawings) == 2:
            bufferedDrawings = Drawing.compressVertically(bufferedDrawings[0], bufferedDrawings[1], LRAlign, padding, targetWidth)
        return bufferedDrawings

    ##########################
    #Methods - Format Methods#
    ##########################
    #Methods related to the format required for the drawing.py file

    #Purpose: Takes a text file and converts it into a (series of) Drawings
    #Warning! For multiple drawings in a single file, make sure they are seperated by a simple new line with no other chars/whitespace
    #Warning! The txt file must be in the same directory as this library when used
    #Warning! Non-txt files are not supported
    def fileIntoDrawings(fileName):
        if fileName.split(".")[-1] != "txt":
            return 1

        ASCIIart = ""
        try:
            file = open(fileName, 'r')
        finally:
            try:
                ASCIIart = file.read()
            except:
                pass
            file.close()
        
        #Split file up into "rows"
        rowFormat = ASCIIart.split("\n")
        #trim the preceding/postceeding new lines
        while rowFormat[0] == "":
            rowFormat = rowFormat[1:]
        while rowFormat[len(rowFormat)-1] == "":
            rowFormat = rowFormat[:-1]

        
        #distinguish between seperate drawings, and add them to a drawing array
        arrayOfDrawings = []
        tempPseudoDrawing = []
        for i in range(len(rowFormat)):
            if rowFormat[i] == "":
                arrayOfDrawings.append(Drawing(tempPseudoDrawing))
                tempPseudoDrawing = []
            else:
                tempPseudoDrawing.append(rowFormat[i])
                
            if i == len(rowFormat)-1:
                arrayOfDrawings.append(Drawing(tempPseudoDrawing))
                tempPseudoDrawing = []
                
        for drawing in arrayOfDrawings:
            drawing.bufferAlign("left", "center", drawing.getWidth(), drawing.getHeight())
            drawing.trim()
            drawing.setOriginal(drawing.getDrawing())

        return arrayOfDrawings
    
    #Purpose: Takes a Drawing object and prints to screen the format required for the drawing file
    def returnInFormat(self, drawingName):
        #add the name and initial bracketting
        drawing = []
        drawing.append(str(drawingName) + " = [")

        #add string quotes around each ascii art line, complete with comma for the list
        for row in self._drawing:

            #add extra \'s to avoid trigger commands (dunno what they;re called)
            if row[-1] == "\\":
                row += "\\"
                    
            drawing.append('\t"' + row + '",')

        #remove the last comma from last element
        lastRow = drawing[len(drawing)-1]
        drawing[len(drawing)-1] = lastRow[:-1]

        #add final bracket, complete with a tab
        drawing.append("\t]")

        return drawing

    #Purpose: Saves multiple (or a single element list of) drawings onto the end of stored_drawings.py file
    #Note: If autoFormat is True, then it will automatically format it in proper "dCamelCaseName", where d stands for Drawing
    def saveMultipleDrawings(fileToAppendTo, arrayOfDrawings, nameOfDrawing, autoFormatBoolean):
        copyArray = copy.deepcopy(arrayOfDrawings)
        copyName = copy.deepcopy(nameOfDrawing)

        #format the name to make sure it can be used as a variable name
        if autoFormatBoolean:
            copyName = copyName.split()
            for i in range(len(copyName)):
                copyName[i] = copyName[i].capitalize()
            copyName = ["d"] + copyName
            copyName = "".join(copyName)

        #Remove non-variable friendly characters
        alpha = string.ascii_letters
        i = 0
        while i < len(copyName):
            if copyName[i] not in alpha:
                copyName = copyName[:i] + copyName[i+1:]
            else:
                i += 1

        #Format the drawings
        for j in range(len(copyArray)):
            copyArray[j] = copyArray[j].returnInFormat(copyName+str(j+1))
        
        #Open the file and save drawing
        file = open(fileToAppendTo, 'a')
        for k in range(len(copyArray)):
            tempDrawing = copyArray[k]
            for l in range(len(tempDrawing)):
                file.write(tempDrawing[l] + "\n")
            file.write("\n")

        file.close()
        return 0
        

    #Purpose: Takes a drawing, returns the drawing after being flipped horizontally
    #Warning! Best to save the new image after manually checking it first, as not all characters are flippable (D, G, 3, etc...)
    def flipHorizontally(drawing):
        #get the original image to be flipped
        flippedImage = copy.deepcopy(drawing.getDrawing())

        #iterate through each row, and then each char in row, and flip the characters and order
        for i in range(len(flippedImage)):
            flippedImage[i] = Drawing.flipRowHorizontally(flippedImage[i])

        #print the new drawing
        return Drawing(flippedImage)

    #Purpose: Takes a string (a row of a drawing), reverses the order and flips each image to a mirrored counterpart
    def flipRowHorizontally(string):
        flippedRow = ""
        #iterate through the original row, adding them to the final product in reverse order
        for i in range(len(string)-1, -1, -1):
            #uses flipChar to flip each individual character of the string
            flippedRow += Drawing.flipCharHorizontally(string[i])
        return flippedRow

    #Purpose: Takes a char, and returns the flipped version if it has one (if not, the original char is returned)
    def flipCharHorizontally(char):
        #use switch-case to find a reversable char
        if char == "/":
            return "\\"
        elif char == "\\":
            return "/"
        
        elif char == "(":
            return ")"
        elif char == ")":
            return "("
        
        elif char == "d":
            return "b"
        elif char == "b":
            return "d"
        
        elif char == "<":
            return ">"
        elif char == ">":
            return "<"
        
        elif char == "[":
            return "]"
        elif char == "]":
            return "["
        
        elif char == "{":
            return "}"
        elif char == "}":
            return "{"
        
        #if char was not reversable, return the original char
        return char
        

    #Purpose: Takes a drawing, returns the drawing after being flipped horizontally
    #Warning! Best to save the new image after manually checking it first, as not all characters are flippable (D, G, 3, etc...)
    def flipVertically(drawing):
        #get the original image to be flipped
        flippedImage = copy.deepcopy(drawing.getDrawing())

        #iterate through each row, and then each char in row, and flip the characters and order
        for i in range(len(flippedImage)):
            flippedImage[i] = Drawing.flipRowVertically(flippedImage[len(flippedImage)-i-1])

        #print the new drawing
        return Drawing(flippedImage)

    #Purpose: Takes a string (a row of a drawing), reverses the order and flips each image to a mirrored counterpart
    def flipRowVertically(string):
        flippedRow = ""
        #iterate through the original row, adding them to the final product in reverse order
        for char in string:
            #uses flipChar to flip each individual character of the string
            flippedRow += Drawing.flipCharVertically(char)
        return flippedRow

    #Purpose: Takes a char, and returns the flipped version if it has one (if not, the original char is returned)
    def flipCharVertically(char):
        #use switch-case to find a reversable char
        if char == "/":
            return "\\"
        elif char == "\\":
            return "/"
        
        elif char == "d":
            return "q"
        elif char == "b":
            return "p"

        elif char == "m":
            return "w"
        elif char == "w":
            return "m"
        
        elif char == "M":
            return "W"
        elif char == "W":
            return "M"

        elif char == "n":
            return "u"
        elif char == "u":
            return "n"

        elif char == "A":
            return "V"
        elif char == "V":
            return "A"

        elif char == "^":
            return "v"
        elif char == "v":
            return "^"

        elif char == "'":
            return ","
        elif char == ",":
            return "'"
        
        #if char was not reversable, return the original char
        return char
