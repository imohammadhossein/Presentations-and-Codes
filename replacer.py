# -*- coding: utf-8 -*-
import os
from shutil import copyfile


path = 'images/'
pathh = 'images1/'

counter = 0
for i in os.listdir(path):
    this  = i.split('_')[1]
    this = this.split('.')[0]
    # # this = ''.join([i for i in this if not i.isdigit()])
    # this = this.encode("utf-8") 
    for l in this :
        # print ("this is ", l ,"and this is the ascii : ",chr(64350))
        if (65252 < ord(l) <65257 ):
            this = this.replace(l,"n")
        elif(65200 < ord(l) < 65205):
            this = this.replace(l,"s")
        elif(65248 < ord(l) < 65253 ):
            this = this.replace(l,"m")
        elif(65172 < ord(l) < 65177):
            this = this.replace(l,"t")
        elif(65256 < ord(l) < 65261 ):
            this = this.replace(l,"h")
        elif(ord(l) == 65268 or ord(l) == 65265 or ord(l) == 64345 or ord(l) == 64345 or ord(l) == 65164 or ord(l) == 65162 or ord(l) == 65161 or ord(l) == 64510 or ord(l) == 64510 or ord(l) == 64511 or ord(l)==65266 or ord(l)==65267 or ord(l)==64344 or ord(l)==64509 or ord(l)==64508  or ord(l)==65163):
            this = this.replace(l,"y")
        elif(ord(l) == 65261 or ord(l) == 65262 or ord(l) == 65157 or ord(l) == 65158):
            this = this.replace(l,"o")
        elif(ord(l) == 65197 or ord(l) == 65198):
            this = this.replace(l,"r")
        elif(ord(l) == 65165 or ord(l) == 65166 or 65152 < ord(l) < 65157 or ord(l) == 65159 or ord(l) == 65160):
            this = this.replace(l,"a")
        elif(ord(l) == 65227 ):
            this = this.replace(l,"e")
        elif(ord(l) == 65195 ):
            this = this.replace(l,"v")
        elif(65240 <ord(l) <65245 or ord(l)==64401 or ord(l)==64400 or ord(l)==64399 or ord(l)==64398):
            this = this.replace(l,"k")
        elif(ord(l) == 65228 or ord(l)==65226 or ord(l)==65227 or ord(l)==65225):
            this = this.replace(l,"e")
        elif(ord(l) == 65170 or ord(l)==65169 or ord(l)==65168 or ord(l)==65167 or ord(l)==64340 or ord(l)==64341):
            this = this.replace(l,"b")
        elif(ord(l) == 65247 or ord(l)==65246 or ord(l)==65248 or ord(l)==65245):
            this = this.replace(l,"l")
        elif(ord(l) == 65194 or ord(l) == 65193 ):
            this = this.replace(l,"d")
        elif(ord(l) == 65208 or ord(l)==65207 or ord(l)==65206 or ord(l)==65205):
            this = this.replace(l,"x")
        elif(ord(l) == 65199 or ord(l) == 65200):
            this = this.replace(l,"z")
        elif(ord(l) == 64405 or ord(l)==64404 or ord(l)==64402 or ord(l)==64403):
            this = this.replace(l,"i")
        elif(ord(l) == 65235 or ord(l)==65233 or ord(l) == 65236 or ord(l) == 65234):
            this = this.replace(l,"f")
        elif(ord(l) == 65219 or ord(l)==65217 or ord(l)==65218 or ord(l)==65220):
            this = this.replace(l,"T")
        elif(ord(l) == 65187 or ord(l)==65186 or ord(l)==65188 or ord(l)==65185):
            this = this.replace(l,"H")
        elif(ord(l) == 65191 or ord(l) == 65192):
            this = this.replace(l,"u")
        elif(ord(l) == 65184 or ord(l) == 65181 or ord(l) == 65182 or ord(l) == 65183):
            this = this.replace(l,"g")
        elif(ord(l) == 65212 or ord(l)==65211 or ord(l)==65209 or ord(l)==65210):
            this = this.replace(l,"E")
        elif(ord(l) == 65239 or ord(l)==65240 or ord(l)==65238 or ord(l)==65237):
            this = this.replace(l,"G")
        elif(ord(l) == 64395 or ord(l)==64394):
            this = this.replace(l,"w")
        elif(ord(l) == 65231 or ord(l)==65229 or ord(l)==65230):
            this = this.replace(l,"q")
        elif(ord(l) == 65224 or ord(l) == 65222 or ord(l) == 65223):
            this = this.replace(l,"J")
        elif(ord(l) == 64380 ):
            this = this.replace(l,"j")
        elif(ord(l) == 65276 or ord(l) == 65275):
            this = this.replace(l,"LA")
        elif(ord(l) == 65180 or ord(l) == 65179 or ord(l)==64350):
            this = this.replace(l,"S")
        elif(64341 < ord(l) <64350 ):
            this = this.replace(l,"p")
    
    this = this.replace("گ", "i")
    this = this.replace("ا", "a")
    this = this.replace("ب", "b")
    this = this.replace("پ", "p")
    this = this.replace("ت", "t")
    this = this.replace("ث", "S")
    this = this.replace("ج", "g")
    this = this.replace("چ", "j")
    this = this.replace("ح", "H")
    this = this.replace("خ", "u")
    this = this.replace("د", "d")
    this = this.replace("ذ", "v")
    this = this.replace("ر", "r")
    this = this.replace("ز", "z")
    this = this.replace("ژ", "w")
    this = this.replace("س", "s")
    this = this.replace("ش", "x")
    this = this.replace("ص", "E")
    this = this.replace("ض", "Z")
    this = this.replace("ط", "T")
    this = this.replace("ظ", "J")
    this = this.replace("ع", "e")
    this = this.replace("غ", "q")
    this = this.replace("ک", "k")
    this = this.replace("گ", "i")
    this = this.replace("ف", "f")
    this = this.replace("ق", "G")
    this = this.replace("ل", "l")
    this = this.replace("م", "m")
    this = this.replace("ن", "n")
    this = this.replace("و", "o")
    this = this.replace("ه", "h")
    this = this.replace("ی", "y")
    # this = this.replace("0", "LLL")
    
    print(this)
    ex = i.split('.')[1]
    name  = repr(counter) + '_' +this+'_'+repr(counter)+'.'+ex
    counter = counter + 1
    #os.rename(path + i , pathh + name)
    copyfile(path + i , pathh + name)
    print(name)
    '''
    if len(this) > 5:
        counter =counter +1
    else :
        print(this)
    '''
    print(counter)
    