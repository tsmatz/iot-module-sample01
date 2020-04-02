from flask import Flask
from azure.iot.device import IoTHubModuleClient
 
app = Flask(__name__)
module_client = IoTHubModuleClient.create_from_edge_environment()
module_client.connect()
 
@app.route("/")
def hello():
  return "Hello"
 
@app.route('/<message>')
def get_message(message):
  module_client.send_message_to_output(message, "output1")
  return "Proceeded - {}!".format(message)
 
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)