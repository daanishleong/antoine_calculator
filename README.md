# antoine_calculator
A Python toolkit for aiding with calculating key variables required for solving vapor-liquid equilibira problems using thermodynamic concepts.

Overview:
This script is based of key fundamental concepts taught in thermodynamics such as Antoine's Equation and Raoult's Law to calculate out vapor pressures, 
composition of a binary mixture, bubble and dew pressures. The script aims to streamline the process of calculating variables needed for solving vapor-liquid equilibria problems by
minimising human error when cross-referencing data from a textbook/document. 

Features:
1. Calculates out vapor pressures, composition of a binary mixture, bubble and dew pressures
2. Supports multiple chemical species
3. Utilises an excel sheet to store Antoine Coefficient making it scalable in the future
4. Modular nature for easy integration and extension

Language:
Python

Libraries:
pandas

Motivation:
My interest in programming started when I took an intro to Python module. While revising for my thermodynamics finals, I noticed that many of my mistakes were owed due to manual
errors in copying data from textbooks. I wanted to build a toolkit that would help automate and simplify this process. Through this project, I aimed to showcase my understanding of
thermodynamic concepts as well as apply my Python skills.

When creating this script I encoutered a number of challenges. 
1. Errors when accessing data from .xlsx file:
    While trying to access data from the .xlsx file, I encountered a problem with "dirty" data where some chemical species, would return an error. For example, for "Ethanol" it had a
   U+00A0 character, which was invisible at first glance, causing lookups to fail. To solve this issue I had to:
        - Manually inspect and clean the Excel file
        - Standardise the input function to ensure user-friendliness in the Python script
   Key takeaways:
   I realised the importance of having clean data. I also need to research more on how I can utilise pandas or other libraries to clean up Excel sheets automatically. This is especially
   important when working with larger datasets where doing it manually would be inefficient.
   
2.  Change in project objectives due to limitations in current knowledge
     Originally, the script was supposed to be an all-in-one solver where upon calling the code and inputting global values for pressure, temperature and chemical species (A and B) the
    script would return all necessary data needed. However, when attempting to code that into the script, I realised that it was not possible as we would need to have new parameters
    to calculate out certain variables. For example, calculating bubble pressure would require knowledege of composition. However, to calculate out composition, we would need to know
    the bubble pressure. I realised that although the concepts were related to one another, they were not sequential. As such, I had to pivot over to a helper tool instead.

Learning outcomes:
- Gained hands-on experience with pandas for data access and manipulation
- Learned debugging skills when handling datasets (invisible characters, capitalisation, etc.)
- Applied thermodynamic concepts programmatically
- Learnt how to recognise limitations and scope of automation


