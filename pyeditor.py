#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 1.2.2 $"
__date__ = "$Date: 2002/01/17 21:37 $"
__revision__ = "$Date: 2016/10/20 $"
__copyright__ = "Copyright (c) 2002-2016 Cedric Bonhomme"
__license__ = "GPLv3"

import os
from tkinter import *
import tkinter.filedialog

class Editor:
    def __init__(self, window_title):
        self.window_title = window_title

        self.root = Tk()
        self.root.title(self.window_title)
        self.root.minsize(width=500,height=500)
        self.root.configure(width=5000,height=5000)

        self.menubar = Menu(self.root)
        self.toolsbar = Frame(self.root, bd =1)
        self.toolsbar.pack(side=TOP,fill =X)
        self.statusbar = Label(self.root, text="", bd=1, relief=SUNKEN,
                               anchor=W)
        self.statusbar.pack(side=BOTTOM, fill=X)

        self.product_dir = os.getcwd()
        print("Working directory: " + self.product_dir)
        print(self.root.cget("width"))
        print(self.root.cget("height"))
        print("Default encoding: " + sys.getdefaultencoding())

        self.images =('./images/filenew','./images/closefile',
                      './images/fileopen','./images/filesave',
                      './images/editcut','./images/editcopy',
                      './images/editpaste','./images/undo',
                      './images/redo','./images/searchfind')
        self.textes =('Nouveau','Fermer,''Ouvrir','Sauver','Couper','Copier',
                      'Coller','Annuler','Refaire','Chercher')

        self.createmenubar()
        self.createtoolsbar()

        # ---- Définitions des formats de fichiers ----
        self.formats = [
        ('Format', '*.txt'),
        ('Tous', '*.*')
        ]

        self.root.mainloop()

    def close(self):
        self.root.quit()

    def createText(self):
        try:
            self.root.textboxFrame.destroy()
        except AttributeError:
            pass
        self.root.textboxFrame = textboxFrame = Frame(self.root)
        self.root.text = text = Text(textboxFrame, bg = "white")
        rightScrollbar = Scrollbar(textboxFrame, orient=VERTICAL,
                                   command=text.yview)
        text.configure(yscrollcommand = rightScrollbar.set)
        rightScrollbar.pack(side=RIGHT, fill=Y)

        text.focus_set()
        text.pack(side = TOP,expand=True,fill=BOTH)
        textboxFrame.pack(side=TOP,expand=True,fill=BOTH)
        text.config(wrap=WORD)

    def createmenubar(self):
        self.menubar = Menu(self.root)

        # menu Fichier
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Nouveau", command = self.nouveau)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Ouvrir...", command = self.ouvrir,)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Enregister", command = self.sauver)
        self.filemenu.add_command(label="Enregister sous...",
                                  command = self.sauver)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Imprimer...", command = self.imprimer)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Fermer", command = self.fermer)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quitter", command = self.root.quit)
        self.menubar.add_cascade(label="Fichier",menu=self.filemenu)

        # menu Edition
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Annuler")
        self.editmenu.add_command(label="Refaire")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Couper", command = self.couper)
        self.editmenu.add_command(label="Copier")
        self.editmenu.add_command(label="Coller")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Chercher", command = self.chercher)
        self.editmenu.add_command(label="Remplacer", command = self.remplacer)
        self.menubar.add_cascade(label="Edition", menu=self.editmenu)

        # menu Aide
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Aide")
        self.helpmenu.add_command(label="A propos de : Editeur de texte V1.0")
        self.menubar.add_cascade(label="Aide", menu=self.helpmenu)
        self.root.config(menu=self.menubar)

    def createtoolsbar(self):
        nBou = len(self.images)
        self.photoI =[None]*nBou
        for b in range(nBou):
            # Création de l'icône (objet PhotoImage Tkinter) :
            self.photoI[b] =PhotoImage(file = self.images[b] +'.gif')
            bou = Button(self.toolsbar, image =self.photoI[b], relief =GROOVE,
                         command = self.action(b))
            bou.pack(side =LEFT, padx=2, pady=2)

    def action(self, i):
        if i == 0:
            return self.nouveau
        if i == 1:
            return self.fermer
        if i == 2:
            return self.ouvrir
        if i == 3:
            return self.sauver
        if i == 4:
            return self.couper
        if i == 5:
            pass
        if i == 6:
            pass

    def chercher(self):
        aChercher = "bonjour"
        texte = self.root.text.get(1,0, END)
        resultat = texte.find(aChercher)
        if resultat >= 0:
            pass
            return resultat

    def remplacer(self,vieux,nouveau):
        texte = self.root.text.get(1,0, END)
        texte.replace(vieux, nouveau)

    def nouveau(self):
        self.createText()
        title = "Nouveau - pyEditeur"
        self.root.title(title)
        print("Nouveau fichier")

    def fermer(self):
        try:
            self.root.textboxFrame.destroy()
        except AttributeError:
            pass
        self.root.title(self.window_title)
        print("Fermeture de fichier")

    def imprimer(self):
        """ """

    def apropos(self):
        print("-= pyEditeur =-")
        print("Editeur de texte Python V 1.0")
        print("Auteur : Cedric Bonhomme")

    def sauver(self):
        file = tkinter.filedialog.asksaveasfile(parent=self.root,
                                          filetypes=self.formats,
                                          title="Enregistrer le fichier",
                                          mode='w')
        if file != None:
            texte = self.root.text.get(1.0, END)
            try:
                file.write('%s' % texte)
                file.close()
            except :
                print("Erreur d'ecriture !")
            (filepath, filename) = os.path.split(file.name)
            title = filename + " - pyEditeur"
            self.root.title(title)
            print("Sauvegarde dans %s" % file.name)

    def ouvrir(self):
        file = tkinter.filedialog.askopenfile(parent=self.root,
                                        filetypes=self.formats,
                                        mode='r',
                                        title='Ouvrir un document')
        if file != None:
            try:
                data = file.read()
                file.close()
            except:
                print("Erreur de lecture !")
            l = 0
            for lines in data:
                l = l+1
                try:
                    self.root.text.insert(str(l)+'.0', lines)
                except:
                    self.createText()
                    self.root.text.insert(str(l)+'.0', lines)
            (filepath, filename) = os.path.split(file.name)
            title = filename + " - pyEditeur"
            self.root.title(title)
            print("Ouverture de fichier ...")
            print("Octets lu du fichier %s : %d octets." % \
                    (filename, len(data)))
            print("Chemin : " + filepath)

    def couper(self):
        self.root.text.selection_clear()


if __name__ == '__main__':
    print("Python text editor - {version}".format(version=__revision__))
    print("Author : Cedric Bonhomme")
    f = Editor("pyEditor")