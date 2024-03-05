from flask import Flask, request, render_template
import openai
import config

# Initialize OpenAI client with your API key
openai.api_key = config.API_KEY

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code = request.form["code"]
        error = request.form["error"]

        # Construct prompt for explaining the error
        prompt = f"Explain the error in this code without fixing it:\n\n{code}\n\nError:\n\n{error}"

        # Retrieve explanation from OpenAI
        explanation = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",  # or engine="davinci-codex" depending on your openai version
            prompt=prompt,
            max_tokens=1024
        ).choices[0].text

        # Construct prompt for fixing the code
        fixed_code_prompt = f"Fix this code: \n\n{code}\n\nError:\n\n{error}. \n Respond only with the fixed code."

        # Retrieve fixed code from OpenAI
        fixed_code = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",  # or engine="davinci-codex" depending on your openai version
            prompt=fixed_code_prompt,
            max_tokens=1024
        ).choices[0].text

        return render_template("index.html",
                               explanation=explanation,
                               fixed_code=fixed_code)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
''''
try code import numpy as np
 a = [1,2,3,4,5]
 b = [6,7,8,9,10]

c = numpy.array( a + b)



'''