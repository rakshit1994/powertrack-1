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
xx=""
y=""

def keywords(term):
    keyword = term
    if keyword == "":
        return ""

    final=""
    ekeyword = keyword
    nkeyword = ekeyword.split(',')

    for i in range(0,len(nkeyword)):
        if i == 0:
            nkeyword[i] = "\\\\\"" + nkeyword[i] + "\\\\\""
        else:
            nkeyword[i] = " OR "+"\\\\\"" + nkeyword[i] + "\\\\\""

    for i in range(0,len(nkeyword)):
        final+=nkeyword[i]

    final = "(" + final + ")"

    return final

def context(contxt):
    keyword = contxt
    if keyword == "":
        return ""

    final=""
    ekeyword = keyword
    nkeyword = ekeyword.splitlines()

    for i in range(0,len(nkeyword)):
        if i == 0:
            nkeyword[i] = "\\\\\"" + nkeyword[i] + "\\\\\""
        else:
            nkeyword[i] = " OR "+"\\\\\"" + nkeyword[i] + "\\\\\""

    for i in range(0,len(nkeyword)):
        final+=nkeyword[i]

    final = "(" + final + ")"

    return final

def exclude(excl):
    keyword = excl
    if keyword == "":
        return ""

    final=""
    ekeyword = keyword
    nkeyword = ekeyword.splitlines()

    for i in range(0,len(nkeyword)):
        if i == 0:
            nkeyword[i] = "\\\\\"" + nkeyword[i] + "\\\\\""
        else:
            nkeyword[i] = " OR "+"\\\\\"" + nkeyword[i] + "\\\\\""

    for i in range(0,len(nkeyword)):
        final+=nkeyword[i]

    final = "-(" + final + ")"

    return final

@app.route('/',methods = ['GET','POST'])
def Query():
    x=""
    xx=""
    y=""
    final=""
    if request.method == 'POST':
        if request.form['keywords']:
            term=request.form['keywords']
            contxt=request.form['context']
            excl=request.form['excludes']
            x = str(keywords(term))
            xx = str(context(contxt))
            y = str(exclude(excl))
            final = "{\"value\":\""+x+" "+xx+" "+y+"\"},"

    return render_template('index.html',final=final)




port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port),debug=True)
