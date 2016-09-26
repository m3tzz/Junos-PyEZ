from flask import Flask, render_template, json, request, session, redirect
from functools import wraps
#from flask_session import Session
from werkzeug import generate_password_hash, check_password_hash
#import backend_functions
import network_devices,PyEZ

app = Flask(__name__)

#### SESSION FOR LOGIN ######

#SESSION_TYPE = 'filesystem'
#PERMANENT_SESSION_LIFETIME = 180
#app.config.from_object(__name__)
#Session(app)

def isAuthed(func):
 @wraps(func)
 def decorated_function(*args, **kwargs):
   print "ENTREI NESTA MERDA"
   try:
      if "auth" not in session or session["auth"] != True:
        raise Exception("NOT AUTHORIZED")
      else:
        return func(*args, **kwargs)
   except:
        #OOPS
        redirect_to_index = redirect('/')
        response = app.make_response(redirect_to_index )
        return response

 return decorated_function

#### END SESSION FOR LOGIN ######


##### MAIN PAGE #####
@app.route('/')
def main():
    print "VAMOS EQUIPA CRL"
    #Return name of device according to IP address
    tmpRet = network_devices.list_switches()
    return render_template('index.html',nodes_info=tmpRet)

####### DISPLAY DEVICE INFO #######
@app.route('/display-device-info', methods=['POST'])
def display_device_info():
    #try:
        print "TUDO LA DENTRO!!"
        print request.form.get("ip")
        result = PyEZ.return_NetworkRequirements('10.40.23.52')
        return render_template('display-device-info.html' , output=result )
    #except:
    #     return render_template('display-device-info.html' , output="FODEU-SE")

####### DISPLAY FPC INFO #######
@app.route('/display-fpc-info', methods=['POST'])
def display_fpc_info():
    #try:
        print "TUDO LA DENTRO OH FPC!!"
        result_Chassis = PyEZ.return_FPC_Chassis_info('10.40.23.52')
        result_Status = PyEZ.return_FPC_Status_info('10.40.23.52')
        return render_template('display-fpc-info.html' , output=result_Chassis  , output2=result_Status )
    #except:
    #     return render_template('display-device-info.html' , output="FODEU-SE")


####### DISPLAY ALL CFG #######
@app.route('/display-all-cfg', methods=['POST'])
def display_all_cfg():
    #try:
        print "TUDO LA DENTRO OH CFG!!"
        result = PyEZ.return_all_config('10.40.23.52')
        return render_template('display-all-cfg.html' , output=result )
    #except:
    #     return ren

if __name__ == "__main__":
    app.run(debug=True)
