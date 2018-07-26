#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 09:23:58 2018

@author: guidomassaccesi
"""
import warnings
import csv, sys, random
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon
from Bio import SeqIO, BiopythonParserWarning, pairwise2 
'''
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
'''

class HCVProteinAnalyzer():
        
    def __init__(self):
        self.protein_sequences = []
        self.sequence_names = []
        self.file = "/Users/guidomassaccesi/Downloads/11108_fulllength_evolutionanalysis.gb"  
        self.peptide_file = "/Users/guidomassaccesi/Desktop/PeptidesToMatch.csv"
        self.peptides = []
        self.peptide_names = []
    
    def getFileName(self):
        return self.file
    
    def getPeptideFileName(self):
        return self.peptide_file
    
    def importSequences(self, file):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", BiopythonParserWarning) #ignore parsing errors from improper genebank files
            
            for record in SeqIO.parse(file, "genbank"):#parse through genebank file
                self.protein_sequences.append(record.seq) #append protein sequences
                self.sequence_names.append(record.name) #append sequence names
            print ("Sequences Imported Correctly!")
            
    def alignSequences(self, template, test):
            alignments=pairwise2.align.globalms(template, test ,1,0,-10,-0.2) #align sequences based on ClustalW Protein aligner parameters
            bole1a_aligned=alignments[0][0] #name and assign the main sequence
            compared_sequence=alignments[0][1] #name and assign the sequence to compare to the main sequence
            match_symbols=[] #initialize array that houses whether specific amino acids match consensus sequence with * applied when a mismatch occurs
            for i in range(len(bole1a_aligned)): #loop to populate match symbol list
                if bole1a_aligned[i]==compared_sequence[i]:
                    match_symbols.append("|")
                else:
                    match_symbols.append("*")
            match_symbols=("".join(match_symbols)) #trim list into string
            
            
            #print main sequence and compared sequence with 
            #match symbols in between 80 characters at a time so that console can output properly
            for i in range(0, len(bole1a_aligned), 80): 
                print ("{} {} {}".format(i+1, bole1a_aligned[i:i+80], i+80))
                print ("{} {} {}".format(i+1, match_symbols[i:i+80], i+80))
                print ("{} {} {}".format(i+1, compared_sequence[i:i+80], i+80))
                print ()
    
    def importPeptides(self, file):
        
         peptides_to_match=csv.reader(open(file, newline=''), delimiter=',', quotechar='|')
         for line in peptides_to_match:
                peptide_added=line[1].strip()
                self.peptides.append(peptide_added)
                self.peptide_names.append(line[0])
        
    
if __name__ == '__main__':
    app = HCVProteinAnalyzer()
    fileName=app.getFileName()
    peptideFile= app.getPeptideFileName()
    app.importSequences(fileName)
    app.alignSequences(app.protein_sequences[0], app.protein_sequences[1])
    app.importPeptides(peptideFile)
