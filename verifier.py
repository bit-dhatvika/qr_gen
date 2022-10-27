import os

from generator import make_certi
def verify(sr):
        if os.path.exists("temp/cert/"+str(sr)+"cert.png"):
                return str(sr)+"cert.png"
        with open("data.txt", 'r') as f:
                lines = f.readlines()
                try :
                        line = lines[sr]
                        return make_certi(line.spli(","))
                except:
                        return None
