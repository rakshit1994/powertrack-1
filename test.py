import os,json
from flask import Flask, jsonify, render_template, redirect, url_for, request
from urllib import urlopen

app = Flask(__name__)

def keywords(term):
    keyword = term
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
    z=""
    if request.method == 'POST':
        term=request.form['keywords']
        contxt=request.form['context']
        excl=request.form['excludes']
        x = str(keywords(term))
        xx = str(context(contxt))
        y = str(exclude(excl))
        z = "-is:retweet"
        final = "{\"value\":\""+x+" "+xx+" "+y+" "+z+"\"},"

    return render_template('index.html',final=final)



port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port),debug=True)