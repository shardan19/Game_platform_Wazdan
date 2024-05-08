from flask import Flask, render_template,request,jsonify

from controllers.dataRefresher import DataRefresher
from controllers.mainController import MainState
import json

app = Flask(__name__)



@app.route("/")
def home():
    if main_state.get_maintanance()==0:
        return render_template('sites/home.html',data={"games":data_refresher.data})
    else:
        return render_template('sites/info.html',data={"info":"Web site is currently under maintanance"})

@app.route('/launch', methods=['GET', 'POST'])
def launch():
    if main_state.get_maintanance()==0:
        print("launching...")
        main_state.increment_requests()
        if request.method == 'POST':
            data=json.loads(request.get_data(as_text=True))
            print(data)
            game = data["game"]
            license = data["license"]
            token = data["token"]
            format = data["format"]
            id=data["id"]

        if not all([game, license, token]):
            return render_template('modules/errorInfo.html',data={"error":"Missing required parameters!"})

        if format == 'json':
            print("data---->>",data_refresher.data[3])
            return data_refresher.data[int(id)]
        elif not format:
            js_file=data_refresher.data[int(id)]['js_file']
            script_src = '/static/games/'+js_file
            return script_src
            
        elif format != 'json':
            return render_template('modules/errorInfo.html',data={"error":"Bad format!"})
        
    else:
        return render_template('sites/info.html',data={"info":"Web site is currently under maintanance: "})


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    main_state.increment_requests()
    if request.method == 'GET':
        return render_template('sites/admin.html',data={"info":"Maintanance mode is: "+str(main_state.get_maintanance())})
    elif request.method == 'POST':
        data=json.loads(request.get_data(as_text=True))
        print(data)
        print(request.form)
        maintenance =data['maintanance']
        print(maintenance)
        if maintenance == 0:
            main_state.change_maintanance_mode(0)
            return {"info":"Maintenance mode turned off"}
        elif maintenance == 1:
            main_state.change_maintanance_mode(1)
            return {"info":"Maintenance mode turned on"}

@app.route("/stats")
def stats(methods=['GET', 'POST']):
    if main_state.get_maintanance()==0:
        main_state.increment_requests()
        print(main_state.get_requests_counter_list())
        return render_template('sites/info.html',data={"info":"Current minute requests:"+str(main_state.get_requests_counter()) +"   Requests list (10min): "+str(main_state.get_requests_counter_list())})
    else:
        return render_template('sites/info.html',data={"info":"Web site is currently under maintanance"})
if __name__=="__main__":
    print("APP STARTING...")

    data_refresher = DataRefresher()
    data_refresher.start()

    main_state=MainState()
    

    app.run(debug=True)