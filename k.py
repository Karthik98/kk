from flask import Flask,jsonify,request
app = Flask(__name__)

data = [
  {
    "name": "Captain America",
    "realname": "Steve Rogers",
    "team": "Avengers",
    "firstappearance": "1941",
    "createdby": "Joe Simon",
    "publisher": "Marvel Comics",
    "bio": "\r\n\t\tSteven Rogers was born in the Lower East Side of Manhattan, New York City, in 1925 to poor Irish immigrants, Sarah and Joseph Rogers.[54] Joseph died when Steve was a child, and Sarah died of pneumonia while Steve was a teen. By early 1940, before America's entry into World War II, Rogers is a tall, scrawny fine arts student specializing in illustration and a comic book writer and artist.\r\n\t\t"
  }
    ]
@app.route('/',methods=['GET'])
def test():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,port=8080)
