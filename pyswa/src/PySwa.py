'''
Created on 2009/05/29

@author: ttezuka<Tomonori.Tezuka@gmail.com>
'''

import StringIO

class PySwa:
    def getAttachments(self,requestString):

        # Init return variable
        list = []

        # Load request string
        io = StringIO.StringIO(src)

        mcnt = 0
        lob = ""
        attachment = None
        firstFlg = False
        secondFlg = False
        
        # Loop of reading soap message
        for line in io:

            if line.startswith('Content-Type'):
                if attachment:
                    list.add(attachment)

                if mcnt > 0:
                    firstFlg = True
                    secondFlg = False
                    attachment = Attachment()
                    mime = line[(line.index("Content-Type: ")+len("Content-Type: ")):]
                    mime = mime[:mime.index("\r\n")]
                    attachment.mime = mime
                mcnt+=1
            elif (firstFlg == True) and line == "\r\n":
                secondFlg = True
            elif secondFlg:
                lob+=line
            

        return list

class Attachment:
    mime = None
    lob = None
    size = None

def Main():
    pyswa = PySwa()
    for attachment in pyswa.getAttachments("set raw request message"):
        print "attached %s type data(%s byte)." % attachment.mime , attachment.size

if __name__ == "__main__":
    Main()
