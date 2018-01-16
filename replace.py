'''
CREDITS
Kuldeep Singh Sidhu
Github: github/singhsidhukuldeep https://github.com/singhsidhukuldeep
Website: Kuldeep Singh Sidhu (Website) http://kuldeepsinghsidhu.com
LinkedIn: Kuldeep Singh Sidhu (LinkedIn) https://www.linkedin.com/in/kuldeep-singh-sidhu-96a67170/
Repository: github.com/singhsidhukuldeep/Keyword-Replacement
Language Used: Python 2.7
Compiler Used:
'''
credits = 'CREDITS\nKuldeep Singh Sidhu\n \nGithub:\t github/singhsidhukuldeep https://github.com/singhsidhukuldeep\nWebsite:\t Kuldeep Singh Sidhu (Website) http://kuldeepsinghsidhu.com\nLinkedIn:\t Kuldeep Singh Sidhu (LinkedIn) https://www.linkedin.com/in/kuldeep-singh-sidhu-96a67170/\nRepository:\t github.com/singhsidhukuldeep/Reddit-ChatBot\nLanguage Used:\t Python 3.6.1\nCompiler Used:\t\n\n'

print (credits)

#------------------------------------------------------

import os, fnmatch
from Tkinter import *
fields = 'Folder', 'Search', 'Replace', 'FilePattern'

def fetch(entvals):
#    print entvals
#    print ents
    entItems = entvals.items()
    for entItem in entItems:
        field = entItem[0]
        text  = entItem[1].get()
        print('%s: "%s"' % (field, text))

def findReplace(entvals):
#    print ents
    directory = entvals.get("Folder").get()
    find = entvals.get("Search").get()
    replace = entvals.get("Replace").get()
    filePattern = entvals.get("FilePattern").get()
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
        #for filename in files:
#            print filename
            filepath = os.path.join(path, filename)
            print filepath  # Can be commented out --  used for confirmation
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

def makeform(root, fields):
    entvals = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=17, text=field+": ", anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entvals[field] = ent
#        print ent
    return entvals

if __name__ == '__main__':
    root = Tk()
    root.title("Recursive S&R")
    ents = makeform(root, fields)
#    print ents
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Show', command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Execute', command=(lambda e=ents: findReplace(e)))
    b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Quit', command=root.quit)
    b3.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()