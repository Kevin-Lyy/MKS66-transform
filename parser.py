from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    with open(fname,"r") as r:
        filedata = r.read().split('\n')
    i = 0
    while i < len(filedata):

        if filedata[i] == "line":
            boi = [int(j) for j in filedata[i+1].split()]
            add_edge(points,boi[0],boi[1],boi[2],boi[3],boi[4],boi[5])
            i += 2

        elif filedata[i] == "ident":
            ident(transform)
            i += 1

        elif filedata[i] == "scale":
            boi = [int(j) for j in filedata[i+1].split()]
            scalematrix = make_scale(boi[0],boi[1],boi[2])
            matrix_mult(scalematrix,transform)
            i += 2

        elif filedata[i] == "move":
            boi = [int(j) for j in filedata[i+1].split()]
            translateboi = make_translate(boi[0],boi[1],boi[2])
            matrix_mult(translateboi,transform)
            i += 2

        elif filedata[i] == "rotate":
            boi = filedata[i+1].split(' ')
            axis = boi[0]
            angleboi = int(boi[1])

            if axis == "x":
                matrix_mult(make_rotX(angleboi), transform)
            elif axis == "y":
                matrix_mult(make_rotY(angleboi), transform)
            elif axis == "z":
                matrix_mult(make_rotZ(angleboi), transform)
            else:
                print("no")

            i += 2

        elif filedata[i] == "apply":
            matrix_mult(transform,points)
            rfix(points)
            #print(points)
            i += 1

        elif filedata[i] == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            i += 1

        elif filedata[i] == "save":
            screen = new_screen()
            draw_lines(points, screen, color)
            boi = filedata[i+1]
            save_extension(screen,boi)
            i += 2

        elif filedata[i] == "quit":
            i = len(filedata)

        else:
            i+= 1


    pass
