from flask import Flask,render_template,redirect,url_for,request
import requests





url = "https://aarmryzhnj.execute-api.us-east-1.amazonaws.com/first"

headers = {
  'X-Amz-Content-Sha256': 'beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3',
  'X-Amz-Date': '20201012T200352',
  'Authorization': 'AWS4-HMAC-SHA256 Credential=ASIAXI5D2F6WWMCLBASR/20201010/us-east-1/execute-api/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=c40374386a1e23b33a2fa7fb12075f0aa9f4ed32a5370a375c37daa025d6c9f3',
  'Content-Type': 'text/plain'
}



s=""

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        windspeed = str(float(request.form["Wind Speed"]))
        tpower =str(float(request.form["Theoretical_Power"]))
        wind_direction = str(float(request.form['Wind Direction']))
        s=windspeed+','+tpower+','+wind_direction

        payload = "{\r\n    \"data\" : \""+s+"\""+"\r\n}"
        

        
        response = requests.request("POST", url, headers=headers, data = payload)   

        r=response.text.encode('utf8')
        r=float()
        
        return render_template('htmlfile.html',content=r)
    else:
        return render_template('htmlfile.html')

if __name__ == "__main__":
    app.run(debug=True)