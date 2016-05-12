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
        if i == 0:
            nbio_loc[i] = "\\\\\"" + nbio_loc[i] + "\\\\\""
        else:
            nbio_loc[i] = " OR "+"\\\\\"" + nbio_loc[i] + "\\\\\""

    for i in range(0,len(nbio_loc)):
        final+=nbio_loc[i]

    final = "(" + final + ")"

    return final


def bio_contains_pos(bio_con):
    flag=0
    if bio_con == "":
        return ""

    final=""
    ebio_con = bio_con
    nbio_con = ebio_con.splitlines()

    for i in range(0,len(nbio_con)):
        if i == 0:
            nbio_con[i] = "\\\\\"" + nbio_con[i] + "\\\\\""
        else:
            nbio_con[i] = " OR "+"\\\\\"" + nbio_con[i] + "\\\\\""

    for i in range(0,len(nbio_con)):
        final+=nbio_con[i]

    final = "(" + final + ")"
    
    return final

def place_contains(place_con):
    flag=0
    if place_con == "":
        return ""

    final=""
    ebio_loc = place_con
    nbio_loc = ebio_loc.split(',')

    for i in range(0,len(nbio_loc)):
        if i == 0:
            nbio_loc[i] = "\\\\\"" + nbio_loc[i] + "\\\\\""
        else:
            nbio_loc[i] = " OR "+"\\\\\"" + nbio_loc[i] + "\\\\\""

    for i in range(0,len(nbio_loc)):
        final+=nbio_loc[i]


    final = "-(" + final + ")"

    return final



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
        if request.form['bio_loc']:
            bio_con=request.form['bio_con']
            bio_loc=request.form['bio_loc']
            place=request.form['place_con']
            x = str(bio_contains_pos(bio_con))
            y = str(bio_location(bio_loc))
            pc= place_contains(place)

            final = "{\"value\":\""+x+" "+y+" "+pc+"\"},"
            print final
    return render_template('index.html',final=final)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port),debug=True)
