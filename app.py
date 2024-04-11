# app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

@app.route('/', methods=['GET', 'POST'])
def palindrome_checker():
    if request.method == 'POST':
        user_input = request.form.get('input_string', '')
        if is_palindrome(user_input):
            result = f"'{user_input}' is a palindrome!"
        else:
            result = f"'{user_input}' is not a palindrome."
        return render_template_string(
            '''
            <h1>Palindrome Checker</h1>
            <form method="POST">
                <label for="input_string">Enter a string:</label><br>
                <input type="text" id="input_string" name="input_string" required><br><br>
                <input type="submit" value="Check">
            </form>
            <p>{{ result }}</p>
            ''',
            result=result
        )
    else:
        return render_template_string(
            '''
            <h1>Palindrome Checker</h1>
            <form method="POST">
                <label for="input_string">Enter a string:</label><br>
                <input type="text" id="input_string" name="input_string" required><br><br>
                <input type="submit" value="Check">
            </form>
            '''
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
