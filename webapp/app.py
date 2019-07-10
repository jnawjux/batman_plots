import gpt_2_simple as gpt2
from flask import Flask, request, render_template, jsonify

# gpt2.load_gpt2(sess, run_name='batman_66')

app = Flask(__name__, static_url_path="")

@app.route('/')
def index():
    """Return the main page."""
    return render_template('indexy.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Generate new sentences and add to origianl sentence."""
    data = request.json
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='batman_66')
    gen_text = gpt2.generate(sess,
                             length=100,
                             temperature=.25,
                             prefix=data['user_input'],
                             return_as_list=True)[0]
    sentences = " ".join([sentence + "."  for sentence in gen_text.split(".")][:-1])

    return jsonify(sentences)