from flask import Flask, render_template_string
import os
from utils import SCORES_FILE_NAME

SUCCESS_TEMPLATE = """
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>The score is:</h1>
        <div id="score">{{ score }}</div>
    </body>
</html>
"""

ERROR_TEMPLATE = """
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>ERROR:</h1>
        <div id="score" style="color:red">{{ error }}</div>
    </body>
</html>
"""

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as file:
                score = int(file.read().strip())
            return render_template_string(SUCCESS_TEMPLATE, score=score)
        else:
            raise FileNotFoundError("Scores file not found.")
    except Exception as e:
        return render_template_string(ERROR_TEMPLATE, error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
