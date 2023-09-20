from flask import Flask, request
app = Flask(__name__)

@app.route('/story')
def story_template():
    return """
    <h1>Madlibs</h1>
    <form method="POST">
        <input type='text' placeholder='place' name='place'/>
        <input type='text' placeholder='noun' name='noun'/>
        <input type='text' placeholder='verb' name='verb'/>
        <input type='text' placeholder='adjective' name='adjective'/>
        <input type='text' placeholder='plural_noun' name='plural_noun'/>
        <button>Submit</button>
    </form>
    """

@app.route('/story', methods=["POST"])
def save_story():
    place = request.form["place"]
    noun = request.form["noun"]
    verb = request.form["verb"]
    adjective = request.form["adjective"]
    plural_noun = request.form["plural_noun"]
    return f"""
           <h2>Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}.
           It loved to {verb} {plural_noun}</h2> 
           """







