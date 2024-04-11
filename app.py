from flask import Flask, request, Response

app = Flask(__name__)
PORT = 3000

@app.route('/call', methods=['POST'])
def handle_call():
    xml_response = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say>Hello. It has come to my attention that you are a scammer. I have decided to flood your phone lines to prevent you from scamming innocent people. I will not stop, until you stop. Stop being a criminal and I may consider ending the flood. This message will now repeat</Say>
    </Response>
    '''
    return Response(xml_response, mimetype='text/xml')

if __name__ == '__main__':
    print('Starting on port', PORT)
    app.run(port=PORT)

      ##Flask is a lightweight and versatile web framework for Python that allows developers to build web applications quickly and efficiently. 

      # future of the flask :-
                             #1) Enhanced Performance: 
                             #2) Modern Technology Integration
                             #3) Continued Development
                             #4) Community Support 