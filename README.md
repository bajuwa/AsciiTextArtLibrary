A python text art library that can help format text<br>
For examples of the formatted results, run any of the 'test_CLASSNAME.py' files which will go through unit tests that display the possibilities of each method within the CLASSNAME.py module.<br>
For a more extensive display of AsciiTextArtLibrary's capabilities, check out my game DragonSlayer at https://github.com/bajuwa/DragonSlayer<br>
<br>
<table>
  <tr>
    <td>Class/File Name</td>
    <td>Description/Purpose</td>
  </tr>
  <tr>
    <td>drawings.py</td>
    <td>This is a personal file that you can edit to contain your own personal Ascii art.  You can enter it manually so long as you conform to the string based format (see other examples in the file for the format).  If you are unfamiliar with writing python scripts or wish to avoid hardcoding your art, you can use drawings_v1_2.py's methods: <br>
    - use fileIntoDrawings to take a text file and convert it to a series of drawings objects<br>
    - then pass these drawings to saveMultipleDrawings in order to save them in to the drawings.py file
    </td>
  </tr>
  <tr>
    <td>drawing_v1_2.py</td>
    <td>the main module that deals with 'drawing' objects.  drawings are defined as a static piece of ascii art, meaning that there are no special qualities or meanings attached to it and can only perform simple manipulations.  Manipulations include:<br>
    - retrieve basic information such as height, width, etc<br>
    - adding/removing extra space around the edges of the drawing<br>
    - flipping images<br>
    - creating a tiled image from existing drawing<br>
    - combining drawings into a new drawing (horizontally and vertically)<br>
    - combine and compress drawings into a new drawing (same as combine, but also removes any extra whitespace from in between the combined drawings without distorting them)
    </td>
  </tr>
  <tr>
    <td>jigsaw_v1_2.py</td>
    <td>
      Extends the capabilities of the drawing but serves a very specific purpose of combining certain combinations of special drawings.  The Jigsaw Base would be considered the 'main' drawing with a series of 'anchor's incorporated into the drawing, and each anchor will be a placeholder when attaching Jigsaw Pieces.  For example, if you have a Jigsaw Base drawing of a person, with anchors at the head, hands, and feet; and you also have Jigsaw Pieces such as different helmet types for the head, gloves for the hands, and shoes for the feet; you can combine these inside a Jigsaw Drawing to create a person with interchangeable clothing.
    </td>
  </tr>
  <tr>
    <td>frame_v1_2.py</td>
    <td>
      A Frame is a series of drawings that will 'wrap' around another drawing to create a frame.  The frame itself will consist of four drawings (top, bottom, left, right), though you can reuse drawings in any part of the frame (for example the left and right sides of the frame can be the same image for consistency).
    </td>
  </tr>
  <tr>
    <td>text_v1_2.py</td>
    <td>
      A type of drawing that is interpretted and formatted for text.  Text formatting features include: <br>
      - indentation<br>
      - alignment<br>
      - bullets/numbering<br>
      - tables<br>
    </td>
  </tr>
</table>
<br>
To do:<br>
- Since this is an old project from my first couple years of programming, it needs to be refactored to clean up/remove unnecessary code.<br>
- Rename files to remove versions (residual evidence of pre-github manual version control)<br>
- Finish adding the 'Font' based features (where user can use textart to create a large font that they can type with)
