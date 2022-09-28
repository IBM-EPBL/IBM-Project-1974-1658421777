from flask import Flask,request,json

app=Flask(__name__)

mob_tech={"1":"Iphone", "2":"Samsung", "3":"Vivo" ,"4":"Realme" ,"5":"Xiaomi" ,"6":"Celkon" }

@app.route('/data',methods=['GET','POST'])
def api():
    if request.method=='GET':
        return mob_tech
    if request.method=='POST':
        data=request.json
        mob_tech.update(data)
        return 'data got inserted'

@app.route("/data/<id>",methods=['PUT'])
def update(id):
    data=request.form['item']
    mob_tech[str(id)]=data
    return 'data updated'

@app.route("/data/<id>",methods=["DELETE"])
def deleteoperation(id): 
    mob_tech.pop(str(id))
    return 'data deleted'

if __name__=='__main__':
    app.run(debug=True)