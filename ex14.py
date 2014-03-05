from sys import argv

script,user_name=argv
my_prompt='>>>'

print "Hi %s,I'm the %s script." %(user_name,script)
print "I'd like to ask you a few questions."
print "Do you lie me %s?" %user_name
likes=raw_input(my_prompt)

print "Where do you live %s?" %user_name
lives=raw_input(my_prompt)

print "What kind of computer do you have?"
computer=raw_input(my_prompt)

print '''
Alright,so you said %r about liking me.
You live in %r.Not sure where that is.
And you have a %r computer.Nice.
''' %(likes,lives,computer)