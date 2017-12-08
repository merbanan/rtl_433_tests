#
import re
import base64
from Crypto import Random
from Crypto.Cipher import AES
import binascii
import scipy
import os.path
import string
import sys
import math
from datetime import datetime
from binascii import unhexlify

def decode(file_path):
    try:
       try:
          par = sys.argv[2]
          if par.find("h") > -1:
             print "r per reverse,b per Binario,  e per Esadecimale, d per decimale, p per proporzione a 100"
       except:
          par = rbedp
       tipo1="-"
       tipo2="-"
       zero="-"
       bitStream=""
       f = scipy.fromfile(open(file_path), dtype=scipy.uint8)
       listBit=f.tolist()
       for i  in listBit:
           bitStream+=str(i)
       print "-------------------------------------------------------"
       SR_P_Ulei="C0000059A0"
       SR_P_Ulei = bin(int(SR_P_Ulei,16))[2:]

       bitStream = cleanData(bitStream)

       #print bitStream.find("010101010101001001001101")
       #reverse = reverseData(bitStream)
       #print reverse.find("010101010101001001001101")
       bitStream = preambleStrip(bitStream,"10")

       preUlei,hUlei,postUlei=ulei(bitStream,SR_P_Ulei)
       #printData(preUlei,"edpb")
       #printData(hUlei,"e")
       #printData(postUlei,"edpb")
       postSync,status = syncWordStrip(preUlei,"1101001110010001110100111001000100011100")
       #print status
       #print ("Dati tra SyncWord ed Ulei")
       #printData(postSync,par)
       #print ("Dati dopo Ulei")
       #printData(postUlei,par)
       #bitStream,sync = syncWordStrip(reverse,"01011000110111000101100011011101")
       #bitStream,tipo1=data1(bitStream,par)
       #bitStream,tipo2=data2(bitStream,par)
       #bitStream,zero = endTrans(bitStream)
       #wmBus(bitStream)
       if par.find("s") > -1:
          print sync
       printData(bitStream,par)
       #print tipo1,tipo2,zero,"------------------------------------------"
       if par.find("r") > -1:
          printData(reverse,par)
          if par.find("s") > -1:
             print rsync
          print "--------------------------------------------------------"
       #printData(reverse)
    except ValueError:
       print "Errore",ValueError

def ulei(bitStream,ulei):
    uleiStart=bitStream.find(ulei)
    postUlei = bitStream[uleiStart+len(ulei):]
    preUlei=bitStream[:uleiStart]
    #printData(preUlei,"e")
    #printData(ulei,"e")
    #printData(postUlei,"e")
    #print "Ulei Trovato a Posizione:",uleiStart
    return preUlei,ulei,postUlei

def cleanData(bitStream):
    recovered=""
    preambleBit=""
    preambleStart=bitStream.find("0")
    bitStream=bitStream[preambleStart:]
    stopByte=bitStream.find("111111111111111111111111")
    bitStream = bitStream[:stopByte]
    return bitStream


def preambleStrip(bitStream,preamble):
    count=""
    preambleByte = preamble * 4
    preambleStart = bitStream.find(preambleByte)
    bitStream = bitStream[preambleStart:]
    while bitStream[:2] == preamble:
          bitStream = bitStream[2:]
          count+=preamble
    #print count
    return bitStream

def syncWordStrip(bitStream,syncWord):
    syncWordStart=bitStream.find(syncWord)
    if syncWordStart > -1:
       status = "SyncWord "+syncWord+" Trovato"
       bitStream = bitStream[len(syncWord):]
    else:
       status = syncWord+" SyncWord NON trovato"
    return bitStream,status


def wmBus(bitStream):
    byte = ' '.join(bitStream[i:i+8] for i in range(0, len(bitStream), 8))
    output = ' '.join(hex(int(a, 2))[2:] for a in byte.split())
    #dataHex=output.replace(" ","")
    #data = dataHex.decode("hex")
    sByte = output.split(" ")
    i=0
    print "Length", sByte[0+i], "-->", int(sByte[0+i],16), "Bytes Totali"
    print "Control", sByte[1+i], "(Primary station?)"
    print "Manufacturer ID", sByte[2+i], sByte[3+i]
    print "Address:", sByte[7+i],sByte[6+i],sByte[5+i],sByte[4+i], "Type:",sByte[9+i], "Version:", sByte[8+i]
    print "CRC:", sByte[10+i],sByte[11+i]

def printData(bitStream,par):
    byte = ' '.join(bitStream[i:i+8] for i in range(0, len(bitStream), 8))
    if par.find("b") > -1:
       print "BIN:",byte
    #print "---------------------------------------------------------"
    output = ' '.join(hex(int(a, 2))[2:] for a in byte.split())
    outputList=output.split(" ")
    out = ""
    byteCount=output.split(" ")
    if par.find("c"):
       print "nB:",len(byteCount)
    for i in outputList:
        if len(i)==1:
           out+= "0"+i+" "
        else:
           out+=i+" "
    if par.find("e") > -1:
       print "HEX:",out
    out=""
    for d in outputList:
        #print int(d,16)
        out+=str(int(d,16))+" "
    if par.find("d") > -1:
       print "DEC:",out
    out=""
    for p in outputList:
        out+=str(int(p,16)*100/255)+" "
    if par.find("p") > -1:
       print "Prop:",out

def decrypt(bitStream,key):
    #key = bytes(key, "ascii")
    #byte = ' '.join(bitStream[i:i+8] for i in range(0, len(bitStream), 8))
    #output = ' '.join(hex(int(a, 2))[2:] for a in byte.split())
    #dataHex=output.replace(" ","")

    iv = '0000000000000000'
    iv = bytes(iv, 'ascii')
    aes = AES.new(key, AES.MODE_CBC, iv)
    dataHex = bytes.fromhex(dataHex)

    plain_text = aes.decrypt(dataHex)
    plain_text = plain_text.decode('utf-8')
    print plain_text


def endTrans(bitStream):
    rbitStream = bitStream[::-1]
    zero=0
    while rbitStream[:1]=="0":
          rbitStream=rbitStream[1:]
          zero+=1
    bitStream = rbitStream[::-1]
    while len(bitStream)%8!=0:
          bitStream+="0"
    return bitStream,zero



if __name__ == '__main__':
    if not os.path.exists(sys.argv[1]):
        print >> (sys.stderr, "The file doesn't exist.")
        sys.exit(1)
    decode(sys.argv[1])

