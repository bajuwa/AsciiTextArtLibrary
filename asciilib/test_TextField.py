# asciilib test file

# make sure to import the proper library for testing
# use from/* to avoid having to change the test file for each new version
from text import *
from stored_drawings import *

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




###################################
# Test Case A1 - addIndentation ###
###################################
# checks by printing it's return value (0 or 1) and printing it's effects

print("Test Case A1 - addIndentation")

print("numOfSpacesToIndent: "+str(0))
input()
print("returns: "+str(properTextField.addIndentation(0)))
print("properTextField.draw():")
properTextField.draw()
input()

print("numOfSpacesToIndent: "+str(1))
input()
print("returns: "+str(properTextField.addIndentation(1)))
print("properTextField.draw():")
properTextField.draw()
input()

print("numOfSpacesToIndent: "+str(4))
input()
print("returns: "+str(properTextField.addIndentation(4)))
print("properTextField.draw():")
properTextField.draw()
input()

######################################
# Test Case A2 - removeIndentation ###
######################################
# checks by printing it's return value (0 or 1) and printing it's effects

print("Test Case A2 - removeIndentation")

print("returns: "+str(properTextField.removeIndentation()))
print("properTextField.draw():")
input()
properTextField.draw()
input()

print("returns: "+str(properTextField.removeIndentation()))
print("properTextField.draw():")
input()
properTextField.draw()
input()

####################################
# Test Case A3 - addBasicBullets ###
####################################
# checks by printing it's return value (0 or 1) and printing it's effects

print("Test Case A3 - addBasicBullets")

print("bulletChar: *")
print("indentationBetweenNumAndText: 0")
print("returns: "+str(properTextField.addBasicBullets("*", 0)))
print("properTextField.draw():")
input()
properTextField.draw()
input()

print("removing the bullet char")
print("returns: "+str(properTextField.removeBasicBullets()))
print("properTextField.draw():")
input()
properTextField.draw()
input()

print("bulletChar: -")
print("indentationBetweenNumAndText: 2")
print("returns: "+str(properTextField.addBasicBullets("-", 2)))
print("properTextField.draw():")
input()
properTextField.draw()
input()

print("removing the bullet char")
print("returns: "+str(properTextField.removeBasicBullets()))
print("properTextField.draw():")
input()
properTextField.draw()
input()

#################################
# Test Case A4 - addNumbering ###
#################################
# checks by printing it's return value (0 or 1) and printing it's effects

print("Test Case A4 - addNumbering")

print("range(0,3)")
print("bulletChar: .")
print("indentationBetweenNumAndText: 0")
print("returns: "+str(properTextField.addNumbering(range(0,3), ".", 0)))
print("properTextField.draw():")
input()
properTextField.draw()
input()

print("removing the numbering")
print("returns: "+str(properTextField.removeNumbering()))
print("properTextField.draw():")
input()
properTextField.draw()
input()

print("range(1,len(properTextField._paragraphs)+1)")
print("bulletChar: )")
print("indentationBetweenNumAndText: 2")
print("returns: "+str(properTextField.addNumbering(range(1,len(properTextField._paragraphs)+1), ")", 2)))
print("properTextField.draw():")
input()
properTextField.draw()
input()

print("removing the numbering")
print("returns: "+str(properTextField.removeNumbering()))
print("properTextField.draw():")
input()
properTextField.draw()
input()


####################################
# Test Case B1 - formatParagraph ###
####################################
# checks by printing it's result

# check the results of different widths
input("Test Case B1 - formatParagraph")
print()
input("Width: 100")
formattedParagraph100Left = TextField.formatParagraph(properTextField, 100, "left")
formattedParagraph100Left.draw()
print()
formattedParagraph100Right = TextField.formatParagraph(properTextField, 100, "right")
formattedParagraph100Right.draw()
print()
formattedParagraph100Center = TextField.formatParagraph(properTextField, 100, "center")
formattedParagraph100Center.draw()

print()
input("Width: 50")
formattedParagraph50Left = TextField.formatParagraph(properTextField, 50, "left")
formattedParagraph50Left.draw()
print()
formattedParagraph50Right = TextField.formatParagraph(properTextField, 50, "right")
formattedParagraph50Right.draw()
print()
formattedParagraph50Center = TextField.formatParagraph(properTextField, 50, "center")
formattedParagraph50Center.draw()
print()

print()
input("Width: 10")
formattedParagraph10Left = TextField.formatParagraph(properTextField, 10, "left")
formattedParagraph10Left.draw()
print()
formattedParagraph10Right = TextField.formatParagraph(properTextField, 10, "right")
formattedParagraph10Right.draw()
print()
formattedParagraph10Center = TextField.formatParagraph(properTextField, 10, "center")
formattedParagraph10Center.draw()
print()

##print()
##input("The following are supposed to cause errors/crashes, so will be commented out after testing")
##input("Width: 0")
##formattedParagraph0Left = TextField.formatParagraph(properTextField, 0, "left")
##formattedParagraph0Left.draw()
##print()
##input("Alignment: non-string")
##formattedParagraph00 = TextField.formatParagraph(properTextField, 0, 0)
##formattedParagraph00.draw()
##print()
##input("Alignment: not left/right/center")
##formattedParagraph0Justified = TextField.formatParagraph(properTextField, 0, "justified")
##formattedParagraph0Justified.draw()
##print()

print()


###############################################
# Test Case B2 - formatTableWithRowPriority ###
###############################################
# checks by printing it's result

print("Test Case B2 - formatTableWithRowPriority")

print("Test using properties:")
print("numOfColumns = 1")
print("targetWidth = 50")
print("LRAlign = 'left'")
print("cellPadding = 0")
input()
rowPriorityTable = TextField.formatTableWithRowPriority(properTextField, 1, 50, "left", 0)
rowPriorityTable.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()

print("Test using properties:")
print("numOfColumns = 5")
print("targetWidth = 50")
print("LRAlign = 'right'")
print("cellPadding = 1")
input()
rowPriorityTable = TextField.formatTableWithRowPriority(properTextField, 5, 50, "right", 1)
rowPriorityTable.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()

print("Test using properties:")
print("numOfColumns = 4")
print("targetWidth = 3")
print("LRAlign = 'center'")
print("cellPadding = 3")
input()
rowPriorityTable = TextField.formatTableWithRowPriority(properTextField, 4, 3, "center", 3)
rowPriorityTable.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()

##################################################
# Test Case B3 - formatTableWithColumnPriority ###
##################################################
# checks by printing it's result

print("Test Case B3 - formatTableWithColumnPriority")

print("Test using properties:")
print("numOfColumns = 1")
print("targetWidth = 50")
print("LRAlign = 'left'")
print("cellPadding = 0")
input()
columnPriorityTable = TextField.formatTableWithColumnPriority(properTextField, 1, 50, "left", 0)
columnPriorityTable.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()

print("Test using properties:")
print("numOfColumns = 5")
print("targetWidth = 50")
print("LRAlign = 'right'")
print("cellPadding = 1")
input()
columnPriorityTable = TextField.formatTableWithColumnPriority(properTextField, 5, 50, "right", 1)
columnPriorityTable.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()

print("Test using properties:")
print("numOfColumns = 4")
print("targetWidth = 3")
print("LRAlign = 'center'")
print("cellPadding = 3")
input()
columnPriorityTable = TextField.formatTableWithColumnPriority(properTextField, 4, 3, "center", 3)
columnPriorityTable.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()



########################################################
# Test Case B4 - formatTableWithRowPriorityWithTitle ###
########################################################
# checks by printing it's result

print("Test Case B4 - formatTableWithRowPriorityWithTitle")

print("Test using properties:")
print("numOfColumns = 1")
print("targetWidth = 50")
print("LRAlign = 'left'")
print("title = "+str(properTitleTextField))
print("title align = left")
print("cellPadding = 0")
input()
rowPriorityTable = TextField.formatTableWithRowPriorityWithTitle(properTextField, 1, 50, "left", properTitleTextField, "left", 0)
rowPriorityTable.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()

print("Test using properties:")
print("numOfColumns = 5")
print("targetWidth = 50")
print("LRAlign = 'right'")
print("title = "+str(properTitleTextField))
print("title align = right")
print("cellPadding = 1")
input()
rowPriorityTable = TextField.formatTableWithRowPriorityWithTitle(properTextField, 5, 50, "right", properTitleTextField, "right", 1)
rowPriorityTable.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()

print("Test using properties:")
print("numOfColumns = 4")
print("targetWidth = 3")
print("LRAlign = 'center'")
print("title = "+str(properTitleTextField))
print("title align = center")
print("cellPadding = 3")
input()
rowPriorityTable = TextField.formatTableWithRowPriorityWithTitle(properTextField, 4, 3, "center", properTitleTextField, "center", 3)
rowPriorityTable.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()



###########################################################
# Test Case B5 - formatTableWithColumnPriorityWithTitle ###
###########################################################
# checks by printing it's result

print("Test Case B5 - formatTableWithColumnPriorityWithTitle")

print("Test using properties:")
print("numOfColumns = 1")
print("targetWidth = 50")
print("LRAlign = 'left'")
print("title = "+str(properTitleTextField))
print("title align = left")
print("cellPadding = 0")
input()
columnPriorityTable = TextField.formatTableWithColumnPriorityWithTitle(properTextField, 1, 50, "left", properTitleTextField, "left", 0)
columnPriorityTable.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()

print("Test using properties:")
print("numOfColumns = 5")
print("targetWidth = 50")
print("LRAlign = 'right'")
print("title = "+str(properTitleTextField))
print("title align = right")
print("cellPadding = 1")
input()
columnPriorityTable = TextField.formatTableWithColumnPriorityWithTitle(properTextField, 5, 50, "right", properTitleTextField, "right", 1)
columnPriorityTable.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()

print("Test using properties:")
print("numOfColumns = 3")
print("targetWidth = 3")
print("LRAlign = 'center'")
print("title = "+str(properTitleTextField))
print("title align = center")
print("cellPadding = 3")
input()
columnPriorityTable = TextField.formatTableWithColumnPriorityWithTitle(properTextField, 3, 3, "center", properTitleTextField, "center", 3)
columnPriorityTable.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()



###################################################
# Test Case B6 - formatWithDrawingBulletsOnLeft ###
###################################################
# checks by printing it's result

print("Test Case B6 - formatWithDrawingBulletsOnLeft")

print("Test using properties:")
print("drawing being used: dMiniMouse")
print("LRAlign = 'left'")
print("TBAlign = 'top'")
print("targetWidth = 30")
print("indentationBetweenBulletAndText = 1")
print("paddingBetweenBullets = 1")
input()
drawingBulletText1 = TextField.formatWithDrawingBulletsOnLeft(properTextField, Drawing(dMiniMouse), \
                                                            "left", "top", 30, 1, 1)
drawingBulletText1.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()


print("Test using properties:")
print("drawing being used: dMiniMouse")
print("LRAlign = 'right'")
print("TBAlign = 'bottom'")
print("targetWidth = 30")
print("indentationBetweenBulletAndText = 3")
print("paddingBetweenBullets = 3")
input()
drawingBulletText2 = TextField.formatWithDrawingBulletsOnRight(properTextField, Drawing.flipHorizontally(Drawing(dMiniMouse)), \
                                                            "right", "bottom", 30, 3, 3)
drawingBulletText2.draw()
input()
print("original text field paragraphs (check if remain untouched):")
print(str(properTextField._paragraphs))
input()

