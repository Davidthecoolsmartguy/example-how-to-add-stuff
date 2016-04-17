from flask import Flask,request,url_for,render_template

from flask.ext.wtf import Form
from wtforms import TextField, FieldList,FormField, SubmitField,validators,IntegerField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'


class TelephoneForm(Form):
    item_description= IntegerField('des')
    quantity= IntegerField('Area Code/Exchange')
    price= TextField('Number')

class ContactForm(Form):
    item_list = FieldList(FormField(TelephoneForm))
  

    add_mobile = SubmitField('Add number')

@app.route('/',methods=["GET","POST"])
def index():
    form = ContactForm(request.form)
    if form.add_mobile.data:
    	#new_telephone is populated with appended entry
        new_telephone = form.item_list.append_entry()
    return render_template('testing.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)