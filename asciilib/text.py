#File: text_v1_2.py
#Created By: Kaylyn Garnett
#For use in ASCIIlib Version: 1.2

#Imports required:
from drawing import *

##########################
###Classes - Text Field###
##########################

#Purpose: A special type of drawing that accounts for text wrapping and alignment
class TextField(Drawing):
    #Note: Anything that starts with an _ should be treated as private
    
    #########
    #Members#
    #########

    _paragraphs = [] 
    _drawing = []  

    ########################
    #Methods - Init/Set/Get#
    ########################

    def __init__(self, arrayOfParagraphs):
        self._paragraphs = copy.deepcopy(arrayOfParagraphs)
        self._drawing = copy.deepcopy(arrayOfParagraphs)
        self._original = copy.deepcopy(arrayOfParagraphs)
        return

    def draw(self):
        self._drawing = self._paragraphs
        return super().draw()

    ##############################################
    #Methods - Instance Methods - Modifying Text #
    ##############################################
    #Directly modifies the paragraphs to simulate certain text effects

    #Purpose: Indents each paragraph by a certain number of spaces
    def addIndentation(self, numOfSpacesToIndent):
        for i in range(0, len(self._paragraphs)):
            self._paragraphs[i] = " "*numOfSpacesToIndent + self._paragraphs[i]
        return 0
        
    #Purpose: Removes indentation (no matter how many spaces it's been indented)
    def removeIndentation(self):
        for i in range(0, len(self._paragraphs)):
            self._paragraphs[i] = self._paragraphs[i].lstrip()
        return 0
    
    #Purpose: Add Basic single-char bullet points to each paragraph
    def addBasicBullets(self, bulletChar, indentationBetweenNumAndText):
        for i in range(0, len(self._paragraphs)):
            self._paragraphs[i] = bulletChar+" "*indentationBetweenNumAndText + self._paragraphs[i]
        return 0
        
        
    #Purpose: Removes basic single-char bullet points and all subsequent indentation before the paragraph
    def removeBasicBullets(self):
        for i in range(0, len(self._paragraphs)):
            self._paragraphs[i] = self._paragraphs[i][1:].lstrip()
        return 0

    #Purpose: Adds numbering to each paragraph, starting at a starting number, incrementing by a certain value each time, and followed by a char (possibly bracket or period) and indentation
    def addNumbering(self, rangeOfNumbers, charAfterNumber, indentationBetweenNumAndText):
        for i in range(0, len(self._paragraphs)):
            self._paragraphs[i] = str(rangeOfNumbers[i%len(rangeOfNumbers)])+charAfterNumber+" "*indentationBetweenNumAndText + self._paragraphs[i]
        return 0

    #Purpose: Removes the numbering from each paragraph
    #Warning! Will remove first 2 chars, then removes whitespace, regardless of what those 2 chars are
    def removeNumbering(self):
        for i in range(0, len(self._paragraphs)):
            if len(self._paragraphs[i]) > 2:
                self._paragraphs[i] = self._paragraphs[i][2:].lstrip()
        return 0
        
    #######################################
    #Methods - Class Methods - Formatting #
    #######################################

    #Purpose: Converts the paragraphs into Drawing object that's formatted with a certain alignment
    def formatParagraph(textField, targetWidth, LRAlign):
        #make sure to copy the original textField so you don't modify the original
        textField = copy.deepcopy(textField)
        
        formattedLines = []
        indexTracker = 0
        offset = 0

        #iterate through each paragraph in the array
        for paragraph in textField._paragraphs:
            indexTracker = 0
            offset = 0
            #provided the text is wider than the target width, start at targetWidth index, the decrement til a space is found
            while (len(paragraph)-indexTracker) > targetWidth:
                offset = 0 #use the offset to find the nearest break in the sentence to create a 'new line'
                #Note: indexTracker keeps the position of the start of the next new line in the original paragraph
                while paragraph[indexTracker+targetWidth-offset] != ' ':
                    offset += 1
                    # to avoid infinite loop, manually insert a breakpoint if you've hit the beginning of the row/line
                    if offset >= targetWidth:
                        offset = 0
                        paragraph = str(paragraph[:indexTracker+targetWidth-offset]+" "+paragraph[indexTracker+targetWidth-offset:])
                formattedLines.append(paragraph[indexTracker:indexTracker+targetWidth-offset])
                indexTracker += targetWidth-offset+1 #+1 to make sure the " " isn't added onto the front of the next line
            # take the left over bit and add it
            formattedLines.append(paragraph[indexTracker:])

        formattedLines = Drawing(formattedLines)
        formattedLines.bufferAlign(LRAlign, "center", formattedLines.getWidth(), formattedLines.getHeight())
        return formattedLines

    #Purpose: Converts the paragraphs into Drawing object that's formatted to appear as a table
    #           Priority goes to filling up an entire row before proceeding to next row
    def formatTableWithRowPriority(tableCells, numOfColumns, targetWidth, LRAlign, cellPadding):
        #make sure to copy the original tableCells so you don't modify the original
        tableCells = copy.deepcopy(tableCells)

        #make sure the total width isn't less than num of columns, taking in to account cell padding
        # note: minimum space for a single column is 1, so make sure the targetwidth can accomodate that
        if (numOfColumns+(cellPadding*(numOfColumns-1))) > targetWidth:
            targetWidth = numOfColumns+(cellPadding*(numOfColumns-1))
        
        # calculate the width of each column, taking in to account the amount of cell padding between them
        # note: cell padding does not apply to the outer edges of the table
        widthPerColumn = int((targetWidth-(cellPadding*(numOfColumns-1)))/numOfColumns)

        # add extra whitespace to accomodate empty cells
        if len(tableCells._paragraphs)%numOfColumns == 0:
            tableCells._paragraphs.extend([""]*(len(tableCells._paragraphs)%numOfColumns))
        else:
            tableCells._paragraphs.extend([""]*(numOfColumns-(len(tableCells._paragraphs)%numOfColumns)))

        # separate cells into appropriate rows
        rows = []
        currentRow = -1
        for i in range(len(tableCells._paragraphs)):
            # keep track of which row we're in
            if i%numOfColumns == 0:
                currentRow += 1
                rows.append([])
            # format each row, this step is required for text wrap and proper alignement
            formattedCell = TextField.formatParagraph(TextField([tableCells._paragraphs[i]]), widthPerColumn, LRAlign)
            formattedCell.bufferAlign(LRAlign, "top", widthPerColumn, formattedCell.getHeight())
            rows[currentRow].append(formattedCell)

        # buffer each cell to the max height of that row
        combinedRows = []
        for row in rows:
            combinedRows.append(Drawing.combineIntoRow(row, "top", cellPadding))

        #combine rows into the full table
        return Drawing.combineIntoColumn(combinedRows, "center", cellPadding)


    #Purpose: Converts the paragraphs into Drawing object that's formatted to appear as a table
    #           Priority goes to filling up an entire column before proceeding to next one
    #           Table is formatted to spread paragraphs/cells as evenly as possible over each column
    def formatTableWithColumnPriority(tableCells, numOfColumns, targetWidth, LRAlign, cellPadding):
        #make sure to copy the original tableCells so you don't modify the original
        tableCells = copy.deepcopy(tableCells)

        #make sure the total width isn't less than num of columns, taking in to account cell padding
        # note: minimum space for a single column is 1, so make sure the targetwidth can accomodate that
        if (numOfColumns+(cellPadding*(numOfColumns-1))) > targetWidth:
            targetWidth = numOfColumns+(cellPadding*(numOfColumns-1))
        
        # calculate the width of each column, taking in to account the amount of cell padding between them
        # note: cell padding does not apply to the outer edges of the table
        widthPerColumn = int((targetWidth-(cellPadding*(numOfColumns-1)))/numOfColumns)

        numOfCellsPerColumn = int(math.ceil(len(tableCells._paragraphs)/numOfColumns))

        # add extra whitespace to accomodate empty cells
        tableCells._paragraphs.extend([""]*((numOfCellsPerColumn*numOfColumns) - len(tableCells._paragraphs)))

        # separate cells into appropriate columns
        columns = []
        currentColumn = -1
        for i in range(len(tableCells._paragraphs)):
            # keep track of which column we're in
            if i%numOfCellsPerColumn == 0:
                currentColumn += 1
                columns.append([])
            # format each column, this step is required for text wrap and proper alignement
            formattedCell = TextField.formatParagraph(TextField([tableCells._paragraphs[i]]), widthPerColumn, LRAlign)
            formattedCell.bufferAlign(LRAlign, "top", widthPerColumn, formattedCell.getHeight())
            #TEST
            #formattedCell.draw()
            columns[currentColumn].append(formattedCell)

        # combine them into their respective rows (otherwise buffering will dis-align their column-row placement
        rows = []
        for i in range(0, numOfCellsPerColumn):
            row = []
            for j in range(0, numOfColumns):
                row.append(columns[j][i])
            rows.append(Drawing.combineIntoRow(row, "top", cellPadding))

        #combine rows into the full table
        return Drawing.combineIntoColumn(rows, LRAlign, cellPadding)

    #Purpose: implements formatOptionsIntoRows but with a title above the options
    def formatTableWithRowPriorityWithTitle(tableCells, numOfColumns, targetWidth, LRAlign, title, titleAlign, cellPadding):
        #make sure the total width isn't less than num of columns, taking in to account cell padding
        # note: minimum space for a single column is 1, so make sure the targetwidth can accomodate that
        # note: this should be done before formatting to make sure title isn't unnecessarily squished if targetWidth changes
        if (numOfColumns+(cellPadding*(numOfColumns-1))) > targetWidth:
            targetWidth = numOfColumns+(cellPadding*(numOfColumns-1))

        titleDrawing = TextField.formatParagraph(title, targetWidth, titleAlign)
        optionsDrawing = TextField.formatTableWithRowPriority(tableCells, numOfColumns, targetWidth, LRAlign, cellPadding)

        return Drawing.combineIntoColumn([titleDrawing, optionsDrawing], titleAlign, cellPadding)

    #Purpose: implements formatOptionsIntoRows but with a title above the options
    def formatTableWithColumnPriorityWithTitle(tableCells, numOfColumns, targetWidth, LRAlign, title, titleAlign, cellPadding):
        #make sure the total width isn't less than num of columns, taking in to account cell padding
        # note: minimum space for a single column is 1, so make sure the targetwidth can accomodate that
        # note: this should be done before formatting to make sure title isn't unnecessarily squished if targetWidth changes
        if (numOfColumns+(cellPadding*(numOfColumns-1))) > targetWidth:
            targetWidth = numOfColumns+(cellPadding*(numOfColumns-1))

        titleDrawing = TextField.formatParagraph(title, targetWidth, titleAlign)
        optionsDrawing = TextField.formatTableWithColumnPriority(tableCells, numOfColumns, targetWidth, LRAlign, cellPadding)

        return Drawing.combineIntoColumn([titleDrawing, optionsDrawing], titleAlign, cellPadding)
    
    #Purpose: Returns a Drawing that uses another drawing as a bullet point to each paragraph
    def formatWithDrawingBulletsOnLeft(textField, bulletDrawing, LRAlign, TBAlign, targetWidth, indentationBetweenBulletAndText, paddingBetweenBullets):
        # find out the width of the drawing in order to calculate how much space is left for the rest of the paragraph
        bulletWidth = bulletDrawing.getWidth()
        paragraphWidth = targetWidth - bulletWidth - indentationBetweenBulletAndText
        if paragraphWidth <= 0:
            paragraphWidth = 1

        # format each paragraph to appropriate size and alignment, then combine in with the bullet point
        listOfBullettedParagraphs = []
        for paragraph in textField._paragraphs:
            tempParagraph = TextField.formatParagraph(TextField([paragraph]), paragraphWidth, LRAlign)
            listOfBullettedParagraphs.append(Drawing.combineIntoRow([bulletDrawing, tempParagraph], TBAlign, indentationBetweenBulletAndText))
        
        # return the entire list after combining into a column
        return Drawing.combineIntoColumn(listOfBullettedParagraphs, LRAlign, paddingBetweenBullets)
    
    #Purpose: Returns a Drawing that uses another drawing as a bullet point to each paragraph
    def formatWithDrawingBulletsOnRight(textField, bulletDrawing, LRAlign, TBAlign, targetWidth, indentationBetweenBulletAndText, paddingBetweenBullets):
        # find out the width of the drawing in order to calculate how much space is left for the rest of the paragraph
        bulletWidth = bulletDrawing.getWidth()
        paragraphWidth = targetWidth - bulletWidth - indentationBetweenBulletAndText
        if paragraphWidth <= 0:
            paragraphWidth = 1

        # format each paragraph to appropriate size and alignment, then combine in with the bullet point
        listOfBullettedParagraphs = []
        for paragraph in textField._paragraphs:
            tempParagraph = TextField.formatParagraph(TextField([paragraph]), paragraphWidth, LRAlign)
            listOfBullettedParagraphs.append(Drawing.combineIntoRow([tempParagraph, bulletDrawing], TBAlign, indentationBetweenBulletAndText))
        
        # return the entire list after combining into a column
        return Drawing.combineIntoColumn(listOfBullettedParagraphs, LRAlign, paddingBetweenBullets)
