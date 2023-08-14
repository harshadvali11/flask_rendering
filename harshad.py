from flask import Flask,render_template

FAI=Flask(__name__)


@FAI.route('/wish')
def wish():
    return 'Hai How are You'

@FAI.route('/first')
def first():
    return render_template('first.html',name='harshad',age=27)


if __name__=='__main__':
    FAI.run(debug=True,host='192.168.1.150',port=5001)












