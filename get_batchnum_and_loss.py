import sys

#Gets the file used for writing and the file to store the results in
training_output_file = sys.argv[1]
input_file_length = int(sys.argv[2]) - 1
batch_loss_ouput_file = sys.argv[3]
#For debugging
print("Input file: {}".format(training_output_file))
print("Input file length: {}".format(input_file_length))
print("Output file: {}".format(batch_loss_ouput_file))

#Opens the files for reading and writing
infile = open(training_output_file, "r")
outfile = open(batch_loss_ouput_file, "w+")

#Variables for reading data in declared
counter = 0
line = " "

#Skips over the first 146 lines of the infile (Darknets setup crap)
while (counter < 147):
    line = infile.readline()
    #print(line)
    counter += 1

#Loops through the file one line at a time | 1818658
while (counter < input_file_length):
    line = infile.readline()
    first_entry = line.split(' ', 1)[0]
    second_item = line.split(', ')
    #If the first entry in the line is numeric, (a batch number) writes line to file
    if first_entry[0].isdigit():
        #Batch number extracted from line
        batch_number = first_entry[:-1]
        print("Batch number: {}".format(batch_number))

        #Loss rate extracted from line
        loss_rate = (second_item[1])[:-4]
        print("Loss rate: {}\n".format(loss_rate))

        #Output information written to file
        output_data = batch_number + ", " + loss_rate + "\n"
        #print(output_data)
        outfile.write(output_data)
    #Increments counter
    counter += 1

#Closes the files
infile.close()
outfile.close()
