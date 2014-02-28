from sys import argv
from os.path import exists

script,from_file,to_file=argv

print "Copying from %s to %s" %(from_file,to_file)

# we could to these two on one line too,how?
in_file=open(from_file)
indata=in_file.read()

print "The input file is %d bytes long" %len(indata)

print "Does the output file exist? %r" %exists(to_file)
print "Ready,hit Enter to continue,Ctrl+C to abort."
raw_input()

out_file=open(to_file,'w')
out_file.write(indata)

print
print "All Right,All done."

out_file.close()
in_file.close()

txt=open(to_file)
print 'The file: %s is that:' % to_file
print
print txt.read()
out_file.close()
