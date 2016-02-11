#!/usr/bin/python
# -*- coding: latin-1 -*-

MAXDEPTH = 300

def is_not_OoB(x, y):
    """return if not out of boundary (x and y between 0 and 19, included"""
    if x < 0 or y < 0 or x > 19 or y > 19:
        return False
    return True

def is_free(laby, x, y, xi, yi):
    """if not out of band, nor a wall nor a one-way"""

    dx = xi - x
    dy = yi - y
    direction = False

    # print str(xi) + " " + str(yi) + " " + str(is_not_OoB(xi, yi))
    if is_not_OoB(xi, yi):
        if laby[xi][yi] is "#":
            return False
    else:
        return False

    # if dx > 0:
    #     direction = True
    #     if laby[xi][yi] is "<":
    #         return False

    # if dy > 0:
    #     direction = True
    #     if laby[xi][yi] is "^":
    #         return False

    # if dx < 0:
    #     direction = True
    #     if laby[xi][yi] is ">":
    #         return False

    # if dy < 0:
    #     direction = True
    #     if laby[xi][yi] is "v":
    #         return False

    # if direction is False:
    #     print "error: can't guess direction"
    #     return -1

    return True


def ret_if_char(char):
    """
    return tile content only if upper case char, otherwise empty

    char -- character to return

    """

    if char >= "A" and char <= "Z":
        return char
    return ""

class Node(object):

    def expand(self, enig):
        """
        expand subnodes
        
        enig -- enigma instance to expand

        return 0 if ended
        return -1 if reached max depth
        return 1 if found exit

        """
        print "expanding self, my coordinates are: [" + str(self.x) + "," + str(self.y) + "]"
        if enig.labyrinth[self.x][self.y] is "+":
            print self.word_list
            del self
            return 1

        if self.depth + 1 > MAXDEPTH:
            del self
            return -1


        print "i am: " + str(self.x) + " " + str(self.y)
        if is_free(enig.labyrinth, self.x, self.y, self.x - 1, self.y) and is_not_OoB(self.x - 1, self.y):
            enig.node_list.append(Node(
                self.word_list + ret_if_char(enig.labyrinth[self.x][self.y]),
                self.x - 1, self.y,
                self.depth + 1)
            )
            print "adding: " + str(self.x - 1) + " " + str(self.y)
        if is_free(enig.labyrinth, self.x, self.y, self.x + 1, self.y) and is_not_OoB(self.x + 1, self.y):
            enig.node_list.append(Node(
                self.word_list + ret_if_char(enig.labyrinth[self.x][self.y]),
                self.x + 1, self.y,
                self.depth + 1)
            )
            print "adding: " + str(self.x + 1) + " " + str(self.y)
        if is_free(enig.labyrinth, self.x, self.y, self.x, self.y - 1) and is_not_OoB(self.x, self.y - 1):
            enig.node_list.append(Node(
                self.word_list + ret_if_char(enig.labyrinth[self.x][self.y]),
                self.x, self.y - 1,
                self.depth + 1)
            )
            print "adding: " + str(self.x) + " " + str(self.y - 1)
        if is_free(enig.labyrinth,self.x, self.y,  self.x -1, self.y) and is_not_OoB(self.x -1, self.y):
            enig.node_list.append(Node(
                self.word_list + ret_if_char(enig.labyrinth[self.x][self.y]),
                self.x, self.y + 1,
                self.depth + 1)
            )
            print "adding: " + str(self.x -1) + " " + str(self.y)

        return 0

    def __init__(self, word_list="", x=11, y=19, depth=0):
        """instanciate new node: if no value given, is root node"""
        self.x = x
        self.y = y

        self.depth = depth
        self.word_list = word_list

        return

class Enigma(object):
    
    def __init__(self):

        self.tree = Node()
        self.return_list = []
        self.node_list = []

        self.labyrinth = [
        ["0","0","0","A","0","0","0","0","<","0","#","#","0","0","0","0","0",">","0","0"],
        ["^","#","#","#","0","#","#","0","#","0","#","#","0","#","J","#","P","#","#","0"],
        ["0","#","0","0","0","0","0","T","0","0","<","B","0","O","0","0","0","0","#","0"],
        ["X","0","0","#","#","v","#","0","#","0","#","#","0","#","0","#","#","0","#","0"],
        ["0","#","0","<","0","0",">","0","<","0",">","0","0","0","0",">","0","0","0","0"],
        ["0","#","0","#","#","#","#","v","#","0","#","#","0","#","0","#","#","^","#","0"],
        ["0","#","J","#","#","0","<","0","0","0","L","0","0","<","0","0","0","0","0","0"],
        ["0","0","0","V","0","0","#","0","#","0","#","#","#","#","U","#","#","v","#","0"],
        ["0","#","0","#","#","0","#","0","#","0","0","0","0","<","0",">","0","0","#","E"],
        ["H","0","0","<","0","W",">","0","#","0","#","0","#","#","0","#","#","0","0","0"],
        ["0","#","^","#","#","0","#","0","0","0","#","0","M","0","0","0","0","F","#","0"],
        ["0","<","0","0","0","0","0","0","#","v","#","0","#","#","0","#","#","^","#","0"],
        ["#","#","0","#","#","0","#","#","#","0","#","D","0","<","0","D","0","0","0","0"],
        ["#","#","0","<","0","0","0","0","G","0","0","0","#","0","#","#","#","0","#","#"],
        ["0","0","0","#","K","#","#","#","#","U","#","E","0","0","J","0","0","0","0","0"],
        ["0","0","0","0","0","<","0","0","0","0",">","0","#","0","#","0","#","0","#","S"],
        ["0","#","0","#","#","#","0","#","0","#","#","0",">","0","0","E","0","0","<","0"],
        ["0","0","F","0","0","0","0","0","0","#","#","0","#","#","0","#","0","#","#","0"],
        ["0","#","0","#","^","#","0","#","0","#","#","0","<","0","F","#","0","#","#","0"],
        ["0","<","0","0","0","Y","0","#","+","#","#","-","#","#","0","#","0","I","0","0"],
        ]


    def __str__(self):
        ret_str = ""
        ret_str += "############################################\n"
        for x in self.labyrinth:
            ret_str += "##"
            for y in x:
                if y is "0":
                    ret_str += "  "
                elif y is "#":
                    ret_str += "##"
                else:
                    ret_str += " " + y

            ret_str += "##\n"

        ret_str += "##################  ####  ##################\n"

        return ret_str


    def expand_all(self):
        """expand nodes until all of them are either failed or a correct path"""

        self.node_list.append(Node())
        continue_ite = True
        end_string = ""
        numb_ite  = 0

        while continue_ite:
            numb_ite += 1
            print "expanding Node " + str(numb_ite) + "..." 
            if len(self.node_list) is 0:
                continue_ite = False
            for n in self.node_list:
                res = n.expand(self)
                if res is 1:
                    continue_ite = False
                    end_string = n.word_list
                    print end_string


        print "ended expansion"
        return


def main():
    e = Enigma()
    print str(e)    
    e.expand_all()

if __name__ == '__main__':
    main()