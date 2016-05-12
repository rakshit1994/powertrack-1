# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os,json
from flask import Flask, jsonify, render_template, redirect, url_for, request
from urllib import urlopen

app = Flask(__name__)
count = 0
final=""
x=""
y=""
z=""

def bio_location(bio_loc):
    flag=0
    if bio_loc == "":
        return ""

    if bio_loc[0] == "-":
        flag =1
        bio_loc=bio_loc.replace(bio_loc[0],'')

    final=""
    ebio_loc = bio_loc
    nbio_loc = ebio_loc.split(',')

    for i in range(0,len(nbio_loc)):
        index = nbio_loc[i].find(' ')
        if index==-1:
            nbio_loc[i] = nbio_loc[i]
        else:
            nbio_loc[i]= "\\\\\"" + nbio_loc[i] + "\\\\\""

    for i in range(0,len(nbio_loc)):
        if i == 0:
            nbio_loc[i] = "bio_location:" + nbio_loc[i]
        else:
            nbio_loc[i] = " OR bio_location:" + nbio_loc[i]

    for i in range(0,len(nbio_loc)):
        final+=nbio_loc[i]

    if flag == 1:
        final = "-(" + final + ")"
    else:
        final = "(" + final + ")"
    return final

def bio_contains_pos(bio_con):
    flag=0
    if bio_con == "":
        return ""

    final=""
    ebio_loc = bio_con
    nbio_loc = ebio_loc.split(',')

    for i in range(0,len(nbio_loc)):
        index = nbio_loc[i].find(' ')
        if index==-1:
            nbio_loc[i] = nbio_loc[i]
        else:
            nbio_loc[i]= "\\\\\"" + nbio_loc[i] + "\\\\\""

    for i in range(0,len(nbio_loc)):
        if i == 0:
            nbio_loc[i] = "bio_contains:" + nbio_loc[i]
        else:
            nbio_loc[i] = " OR bio_contains:" + nbio_loc[i]

    for i in range(0,len(nbio_loc)):
        final+=nbio_loc[i]

    final = "(" + final + ")"
    return final

def bio_contains_neg(bio_con):
    flag=0
    if bio_con == "":
        return ""

    final=""
    ebio_loc = bio_con
    nbio_loc = ebio_loc.split(',')

    for i in range(0,len(nbio_loc)):
        index = nbio_loc[i].find(' ')
        if index==-1:
            nbio_loc[i] = nbio_loc[i]
        else:
            nbio_loc[i]= "\\\\\"" + nbio_loc[i] + "\\\\\""

    for i in range(0,len(nbio_loc)):
        if i == 0:
            nbio_loc[i] = "bio_contains:" + nbio_loc[i]
        else:
            nbio_loc[i] = " OR bio_contains:" + nbio_loc[i]

    for i in range(0,len(nbio_loc)):
        final+=nbio_loc[i]

    final = "-(" + final + ")"
    return final

def place_contains(place_con):
    flag=0
    if place_con == "":
        return ""
    if place_con[0] == "-":
        flag =1
        place_con=place_con.replace(place_con[0],'')

    final=""
    ebio_loc = place_con
    nbio_loc = ebio_loc.split(',')

    for i in range(0,len(nbio_loc)):
        index = nbio_loc[i].find(' ')
        if index==-1:
            nbio_loc[i] = nbio_loc[i]
        else:
            nbio_loc[i]= "\\\\\"" + nbio_loc[i] + "\\\\\""

    for i in range(0,len(nbio_loc)):
        if i == 0:
            nbio_loc[i] = "place_contains:" + nbio_loc[i]
        else:
            nbio_loc[i] = " OR place_contains:" + nbio_loc[i]

    for i in range(0,len(nbio_loc)):
        final+=nbio_loc[i]

    if flag == 1:
        final = "-(" + final + ")"
    else:
        final = "(" + final + ")"
    return final

def handlefn(handle1):
    flag=0
    if handle1 == "":
        return ""

    if handle1[0] == "-":
        flag =1
        handle1=handle1.replace(handle1[0],'')

    final=""
    t_handle=handle1
    t_handle=t_handle.split(',')

    for i in range(0,len(t_handle)):
        if i == 0:
            t_handle[i] = "from:" + t_handle[i]
        else:
            t_handle[i] = " OR from:" + t_handle[i]

    for i in range(0,len(t_handle)):
        final+=t_handle[i]

    if flag == 1:
        final = "-(" + final + ")"
    else:
        final = "(" + final + ")"

    return str(final)

def isretweet(retweets):
    if(retweets =="F"):
        return "-is:retweet" 
    else:
        return "is:retweet"


@app.route('/',methods = ['GET','POST'])
def Query():
    x=""
    xx=""
    y=""
    z=""
    rt=""
    pc=""
    final=""
    if request.method == 'POST':
        bio_con_pos=request.form['bio_con_pos']
        bio_con_neg=request.form['bio_con_neg']
        bio_loc=request.form['bio_loc']
        handle1=request.form['handle']
        place=request.form['place_con']
        retweets =request.form['retweet']
        x = str(bio_contains_pos(bio_con_pos))
        xx = str(bio_contains_neg(bio_con_neg))
        y = str(bio_location(bio_loc))
        z = handlefn(handle1)
        pc= place_contains(place)
        rt = isretweet(retweets)

        final = "{\"value\":\""+y+" "+pc+" "+x+" "+xx+" "+z+" "+rt+"\"},"
        print final
    return render_template('index.html',final=final)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port),debug=True)
