from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 適切なセキュリティキーに変更してください

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    date = request.form['date']
    daily_items = request.form.getlist('daily_items')
    variable_items = request.form.getlist('variable_items')
    other_items = request.form['other_items']
    # セッションを使用して、後のリクエストでもデータを利用できるようにする
    session['daily_items'] = daily_items
    session['variable_items'] = variable_items
    session['other_items'] = other_items
    return render_template('result.html', date=date, daily_items=daily_items, variable_items=variable_items, other_items=other_items)

@app.route('/ready')
def ready():
    return render_template('ready.html')

@app.route('/incomplete')
def incomplete():
    return render_template('incomplete.html')

@app.route('/submit_ready', methods=['POST'])
def submit_ready():
    # セッションから情報を取得
    daily_items = session.get('daily_items', [])
    variable_items = session.get('variable_items', [])
    other_items = session.get('other_items', "")

    # フォームから選択されたアイテムを取得
    selected_daily_items = request.form.getlist('selected_daily_items')
    selected_variable_items = request.form.getlist('selected_variable_items')
    other_items_selected = request.form.get('other_items_selected', '')

    # すべてのアイテムが選択されているかを確認
    all_daily_selected = set(daily_items) == set(selected_daily_items)
    all_variable_selected = set(variable_items) == set(selected_variable_items)
    all_other_selected = bool(other_items_selected.strip())

    if all_daily_selected and all_variable_selected and all_other_selected:
        return redirect('/ready')
    else:
        return redirect('/incomplete')

if __name__ == '__main__':
    app.run(debug=True)
