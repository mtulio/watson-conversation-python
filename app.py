import os

from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, send_from_directory, jsonify
from watson_developer_cloud import ConversationV1

load_dotenv(find_dotenv())

app = Flask (__name__,
    static_folder=os.environ.get('APP_PUBLIC_PATH') or 'YOUR PUBLIC STATIC DIR')
app.config.update (
        SERVER_NAME=os.environ.get('APP_SERVER_NAME') or '127.0.0.1:5000'
)

conversation = ConversationV1 (
    username=os.environ.get('CONVERSATION_USERNAME') or 'YOUR SERVICE NAME',
    password=os.environ.get('CONVERSATION_PASSWORD') or 'YOUR PASSWORD',
    version='2016-09-20')

@app.route('/api/message', methods=['POST'])
def send_api_message():
    """ Handle HTTP POST request to post new message."""
    try:
        req = request.get_json(silent=True, force=True)
    except:
        print "Unable to get HTTP Request. Unexpected error: ", sys.exc_info()[0]
        raise

    workspace = os.environ.get('WORKSPACE_ID') or '<workspace-id>'
    if not workspace or workspace == '<workspace-id>':
        output_message = {
            'output': {
            'text': 'The app has not been configured with a <b>WORKSPACE_ID</b> environment variable.'
            }
        }
        return jsonify(output_message), 404
    if 'context' not in req:
        req['context'] = {}
    if 'input' not in req:
        req['input'] = {}

    try:
        response = conversation.message(workspace_id=workspace,
            message_input=req['input'],
            context=req['context'])
    except:
        print "Unable to call Conversation API. Unexpected error: ", sys.exc_info()[0]
        raise

    print repr(response)
    return jsonify(response), 200

@app.route('/<path:filename>', methods=['GET'])
def send_root_file(filename):
    """ Handle HTTP GET file requests."""
    return app.send_static_file(filename)

@app.route('/', methods=['GET'])
def send_root():
    """ Handle HTTP root index request."""
    return app.send_static_file(os.environ.get('APP_INDEX_FILE'))

if __name__ == "__main__":
    app.run()
