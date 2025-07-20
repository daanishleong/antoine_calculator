# chem_eng1
A Python toolkit aiming to help with calculating key variables required for solving vapor-liquid equilibira problems.

Overview:
This script is based of key fundamental concepts taught in thermodynamics such as Antoine's Equation and Raoult's Law to calculate out vapor pressures, 
composition of a binary mixture, bubble and dew pressures. The script aims to streamline the process of calculating variables needed for solving vapor-liquid equilibria problems by
minimising human error when cross-referencing data from a textbook/document. 

Features:
1. Calculates out vapor pressures, composition of a binary mixture, bubble and dew pressures
2. Supports multiple chemical species
3. Utilises an excel sheet to store key data making it scalable in the future

Language:
Python

Libraries:
pandas

Motivation:
I got really interested in programming after my intro to programming module back in Y1. I wanted to learn more about python and read online about how the best way to learn was to 
start creating small projects to solve problems that you encounter. When revising for my finals, I noticed I made many careless mistakes in my calculations that arose due to copying
wrong information when cross-referencing with data from physical textbooks/documents. I wanted to see if I can create a program that helps streamline this process and returns the 
necessary variables needed for calculations. 

When creating this script I encoutered a number of challenges. 
1. Errors when accessing data from .xlsx file:
    Data keyed into the .xlsx file was dirty and as such pandas could not recognise certain chemical species leading to errors. Had to learn how to clean up the data on both the
   .xlsx file ('ethanol' had a U+00A0 char which made accessing this species return an error; had to go into the .xlsx sheet to clean up and check if other species were affected)
   and the python script itself (standardising the process so that it becomes user-friendly)
2.  Change in project objectives due to limitations in current knowledge
     Originally, the script was supposed to be an all-in-one solver where upon calling the code and inputting global values for pressure, temperature and chemical species (A and B) the
    script would return all necessary data needed. However, when attempting to code that into the script, I realised that it was not possible as we would need to have new parameters
    to calculate out certain variables. For example, calculating bubble pressure would require knowledege of composition. However, to calculate out composition, we would need to know
    the bubble pressure. I realised that although the concepts were related to one another, they were not sequential. As such, I had to pivot over to a helper tool instead.

Learning outcomes:
I learnt more about the extensive libraries python has which can help aid in other projects. pandas for example is especially useful for automating data processing and cleaning 
especially for large datasets. Not only that, I reinforced my learning from my intro classes by applying it to a real project as well as strengthen my understanding of thermodynamic
concepts. Overall, the process of learning to write this program has enabled me to appreciate how programming can be useful for Chemical Engineering and enhance learning.
