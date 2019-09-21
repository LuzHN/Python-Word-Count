import sys

f = open("tweets.txt")
output = open("mapoutput.txt", "w+")

# Get input lines from stdin
for line in f:
	# Remove spaces from beginning and end of the line
	line = line.strip()
 
	# Split it into words
	words = line.split()
 
	# Output tuples on stdout
	for word in words:
		output.write(word + "\t1\n")