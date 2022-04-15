from flask import Flask, json, request, jsonify
import sys
from send_email import send_email

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def Message():
    content = request.get_json()
    content = content['userRequest']['utterance']
    content=content.replace("\n","")
    print(content)
    if content == u"컴퓨터 공지사항 크롤링":
        with open('./oneweek.txt', 'r') as f:
            f_read = f.read()
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : f_read 
                        }
                    }
                ]
            }
        }
    elif content == u"마일리지 공지사항 크롤링":
        send_email('11', '2')
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : u'수행완료'
                        }
                    }
                ]
            }
        }
    else:
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "error입니다."
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
