
from shutil import copyfile

def copy_and_format_file(filename, file_type, indentation = 4):

    # Cleanup file name
    new_name = filename.replace("/", "_").replace("-", "_")
    new_location = "_includes/{0}".format(new_name)

    # Copy file to docs/_includes directory
    copyfile("../{0}".format(filename) , new_location)

    # Prepare indentation str based on params
    identation_str = ""
    for x in range(0, indentation):
        identation_str += " "

    ## Add indentation to all lines
    with open(new_location, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            newline = "{0}{1}".format(identation_str,line)
            f.write(newline)

    ## Add Type on top
    with open(new_location, 'r+') as f:
        content = f.read()
        line = ".. code-block:: {0}".format(file_type)
        f.seek(0, 0)
        f.write( '\n' + line.rstrip('\r\n') + '\n\n\n' + content)
