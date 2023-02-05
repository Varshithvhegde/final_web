# write the function to write the text into given filename if file is not there then create it
def write_into_file(filename, text):
    with open(filename, "a") as f:
        f.write(text)
        f.close()
        
# write the function to read the file and return the text
def read_file(filename):
    with open(filename, "r") as f:
        return f.read()
