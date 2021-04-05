from graphviz import render
import graphviz
from tkinter import *
def generar(image, filename,color):
    file = open(filename,'w')
    file.write("digraph G {\n\ta0 [shape=plaintext,label=<\n <TABLE border=\"10\" cellspacing=\"10\" cellpadding=\"10\" style=\"rounded\" bgcolor=\"" + color + "\">\n")
    temp = image.head
    file.write("<TR>\n<TD border=\"3\"></TD>\n")
    temp_ = temp.next
    while(temp_ != None):
        file.write("<TD border=\"3\" >" + str(temp_.id + 1) +"</TD>\n")
        temp_ = temp_.next
    file.write("</TR>")
    temp = temp.prev
    while(temp != None):
        file.write("<TR><TD border=\"3\" >" + str(temp.id + 1) +"</TD>\n")
        temp_ = temp.nodeAccess
        while(temp_ != None):
            file.write("<TD border=\"3\" >" + str(temp_.data) +"</TD>\n")
            temp_ = temp_.right
        file.write("\n</TR>")
        temp = temp.prev
    file.write("  \n</TABLE>>];\n\n}")
    file.close()
    render('dot','png',filename)