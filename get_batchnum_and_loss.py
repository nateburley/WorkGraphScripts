import sys

#Gets the file used for writing and the file to store the results in
training_output_file = sys.argv[1]
batch_loss_ouput_file = sys.argv[2]
#For debugging
print("Input file: %s\n", training_output_file)
print("Output file: %s\n", batch_loss_ouput_file)

#Opens the files for reading and writing
infile = fopen(training_output_file, "r")
outfile = fopen(batch_loss_ouput_file, "w")

#Skips over the first 146 lines of the infile (Darknets setup crap)
counter = 0
line = " "
while (counter < 146):
    line = infile.realine()
#For debugging
print("\nCurrent line: %s\n", line)






#Closes the files
fclose(infile)
fclose(outfile)
