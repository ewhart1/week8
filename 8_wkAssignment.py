#!/usr/bin/env python

# prints out a menu for the user to choose from in command line
print ("Choose an option (number) from the following menu")
option = input("(1) translate a protein-coding sequence of nucleotides into amino acid \n-or- (2) randomly draw nucleotides from a codon sequence: ")
# DB: Minor, but this seems easier to read if the options are on multiple lines.

# Nucleotide sequence input
dnaSeq = input("Enter desired nucleotide sequence: ")
dnaSeq = dnaSeq.upper()

# since we're translating to protein, we need to read from RNA. This will transcribe the DNA input into an RNA sequence
rnaSeq = dnaSeq.replace("T","U")

# RNA:Amino Acid  library that is referred to in order to convert sequence into amino acid
codons =	{"AAA":"Lys", "AAC":"Asn", "AAG":"Lys", "AAU":"Asn",
		"ACA":"Thr", "ACC":"Thr", "ACG":"Thr", "ACU":"Thr",
		"AGA":"Arg", "AGC":"Ser", "AGG":"Arg", "AGU":"Ser",
		"AUA":"Ile", "AUC":"Ile", "AUG":"Met", "AUU":"Ile",
		"CAA":"Gln", "CAC":"His", "CAG":"Gln", "CAU":"His",
		"CCA":"Pro", "CCC":"Pro", "CCG":"Pro", "CCU":"Pro",
		"CGA":"Arg", "CGC":"Arg", "CGG":"Arg", "CGU":"Arg",
		"CUA":"Leu", "CUC":"Leu", "CUG":"Leu", "CUU":"Leu",
		"GAA":"Glu", "GAC":"Asp", "GAG":"Glu", "GAU":"Asp",
		"GCA":"Ala", "GCC":"Ala", "GCG":"Ala", "GCU":"Ala",
		"GGA":"Gly", "GGC":"Gly", "GGG":"Gly", "GGU":"Gly",
		"GUA":"Val", "GUC":"Val", "GUG":"Val", "GUU":"Val",
		"UAA":"Stop", "UAC":"Tyr", "UAG":"Stop", "UAU":"Tyr",
		"UCA":"Ser", "UCC":"Ser", "UCG":"Ser", "UCU":"Ser",
		"UGA":"Stop", "UGC":"Cys", "UGG":"Trp", "UGU":"Cys",
		"UUA":"Leu", "UUC":"Phe", "UUG":"Leu", "UUU":"Phe"}

# if user selects option 1, this will print the corresponding amino acid name to their nucleotide sequence (assuming their characters entered are a multiple of 3)
if option == "1":
	AA  = ""
	for x in range(0, len(rnaSeq), 3):
		if rnaSeq[x:x+3] in codons:
			AA += codons[rnaSeq[x:x+3]]
	print ("Amino Acid sequence: ")
	print (AA)

# if user selects option 2, this will select a random sequence from the list the user enters and print that randomly selected codon back to the screen
elif option == "2":
	dnaSeq=dnaSeq.upper()  # DB: This is already done at the top, right?
	codons = [dnaSeq[y:y+3] for y in range(0, len(rnaSeq), 3)]
	print (codons)
	import random	# DB: Better to put this at the top of the script
	randomAA = random.choice(codons)
	print ("Randomly generated codon from the sequence entered: ")
	print (randomAA)

# DB: Overall, this looks good. I might recommend adding a few more comments that are specific
#     to lines whose function isn't necessarily obvious (often if statements and for loops).