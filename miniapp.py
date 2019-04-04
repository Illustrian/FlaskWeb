{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, flash, request\n",
    "from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField\n",
    " \n",
    "# App config.\n",
    "DEBUG = True\n",
    "app = Flask(__name__)\n",
    "app.config.from_object(__name__)\n",
    "app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'\n",
    " \n",
    "class ReusableForm(Form):\n",
    "    name = TextField('Name:', validators=[validators.DataRequired()])\n",
    " \n",
    "    @app.route(\"/\", methods=['GET', 'POST'])\n",
    "    \n",
    "\n",
    "    def hello():\n",
    "    \n",
    "        form = ReusableForm(request.form)\n",
    "\n",
    "        print (form.errors)\n",
    "        if request.method == 'POST':\n",
    "            name=request.form['name']\n",
    "            print (name)\n",
    "\n",
    "        if form.validate():\n",
    "            # Save the comment here.\n",
    "            flash('Hello ' + name)\n",
    "        else:\n",
    "            flash('All the form fields are required. ')\n",
    "\n",
    "        return render_template('hello.html', form=form)\n",
    "\n",
    "        if __name__ == \"__main__\":\n",
    "            app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
