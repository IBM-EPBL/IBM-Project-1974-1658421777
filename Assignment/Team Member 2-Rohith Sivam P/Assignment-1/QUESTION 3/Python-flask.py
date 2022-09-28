from flask import Flask,request,json

app=Flask(__name__)

car_companies={"1":"Maruti ", "2":"Honda", "3":"Tata" ,"4":"Kia" ,"5":"BMW" ,"6":"Audi" }

@app.route('/data',methods=['GET','POST'])
def api():
    if request.method=='GET':
        return car_companies
    if request.method=='POST':
        data=request.json
        car_companies.update(data)
        return 'data got inserted'

@app.route("/data/<id>",methods=['PUT'])
def update(id):
    data=request.form['item']
    car_companies[str(id)]=data
    return 'data updated'

@app.route("/data/<id>",methods=["DELETE"])
def deleteoperation(id):
    car_companies.pop(str(id))
    return 'data deleted'

if __name__=='__main__':
    app.run(debug=True)