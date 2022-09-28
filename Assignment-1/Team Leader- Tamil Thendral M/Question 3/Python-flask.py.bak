from flask import Flask,request,json

app=Flask(__name__)

mobile_technology={"1":"Apple", "2":"Samsung", "3":"Google Pixel" ,"4":"iqoo" ,"5":"Xiaomi" ,"6":"OnePlus" }

@app.route('/data',methods=['GET','POST'])
def api():
    if request.method=='GET':
        return mobile_technology
    if request.method=='POST':
        data=request.json
        mobile_technology.update(data)
        return 'data got inserted'

@app.route("/data/<id>",methods=['PUT'])
def update(id):
    data=request.form['item']
    mobile_technology[str(id)]=data
    return 'data updated'

@app.route("/data/<id>",methods=["DELETE"])
def deleteoperation(id):
    mobile_technology.pop(str(id))
    return 'data deleted'

if __name__=='__main__':
    app.run(debug=True)