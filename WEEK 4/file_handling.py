# This code opens a file named 'trial.text' in read mode, reads its content, prints it, and then closes the file.
file = open('trial.text', 'r')
text = file.read()
print(text)
file.close()

# This code opens a file named 'trial.text' in write mode, writes a new string to it, and then closes the file.
file = open('trial.text', 'w')
text = file.write("This is a modified version of the file.")
print(text)
file.close()
