from flask import Flask, render_template, request

app = Flask(__name__)


# AI/Automation Logic: Simple keyword-based triage for NGO staff
def analyze_symptoms(text):
    text = text.lower()
    urgent_keywords = ['chest pain', 'breathing', 'heavy bleeding', 'unconscious', 'fracture']

    priority = "Normal"
    for word in urgent_keywords:
        if word in text:
            priority = "URGENT (Alert NGO Doctor)"
            break

    summary = f"Patient reported: '{text[:50]}...' | Auto-Priority: {priority}"
    return priority, summary


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        symptoms = request.form.get('symptoms')

        # Calling our automation function
        priority, summary = analyze_symptoms(symptoms)

        result = {
            "name": name,
            "priority": priority,
            "summary": summary
        }
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
