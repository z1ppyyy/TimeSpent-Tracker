from flask import Flask, render_template, request
from tracker import sync_spent_tracker

app = Flask('Tracker')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/tracker', methods=['POST'])
def tracker():
    username = request.form.get('username')
    month = request.form.get('month')

    if not username:
        return render_template('index.html', error='Invalid Name! Please try again.')
    
    response = sync_spent_tracker(username, month)

    return render_template('index.html', result=f'Your Time Spent for {month.capitalize()} is {response} hours')


if __name__ == '__main__':
    app.run()