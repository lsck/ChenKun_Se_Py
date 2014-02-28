from sys import argv
script,filename=argv

print "We're going to erase %r." %filename
print "if you don't want that,hit Ctrl+C."
print "if you do want that,hit Enter."

raw_input("------->")

print "Opening the file..."
target=open(filename,'w')

print "Truncating the file.Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1=raw_input("line 1:")
line2=raw_input("line 2:")
line3=raw_input("line 3:")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()

txt=open(filename)
print "That's you write into %s is those:" %filename
for i in range(2):
    print txt.readline(),
print "And finally,we close it."
