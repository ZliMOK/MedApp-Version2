#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/quiz')
def root():
    quiz = [
        {
            "question": "Vegetables contained ( ) can promote gastrointestinal motility, which is good for food digestion.",
            "option1": "Vitamins",
            "option2": "Cellulose",
            "option3": "Trace elements"
        },
    {
            "question": "In the natural world, ( ) is called the element of wisdom",
            "option1": "Iron",
            "option2": "Calcium",
            "option3": "Zinc"
        },
    {
            "question": "Which of the following foods is rich in trace element Iodine?",
            "option1": "Carrot",
            "option2": "Chocolate",
            "option3": "Kelp"
        },
    {
            "question": "Which hidden damage to the human body caused by long-term heavy drinking is the most serious?",
            "option1": "Heart",
            "option2": "Liver",
            "option3": "Kidney"
        }
    ]

    return jsonify(quiz)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
