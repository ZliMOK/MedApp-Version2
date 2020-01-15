#!flask/bin/python
# -*- coding: utf-8 -*
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/tip')
def root():
    tip = [
        {
            "tiptitle": "Drink some water, especially before meals",
            "contents": "Drinking enough water can have numerous benefits. Surprisingly, it can boost the number of calories you burn. Two studies note that it can increase metabolism by 24–30% over 1–1.5 hours. This can amount to 96 additional calories burned if you drink 8.4 cups (2 liters) of water per day. The optimal time to drink it is before meals. One study showed that downing 2.1 cups (500 ml) of water 30 minutes before each meal increased weight loss by 44%."
        },
    {
            "tiptitle": "Take vitamin D3 if you don’t get much sun exposure",
            "contents": "Sunlight is a great source of vitamin D. Yet, most people don’t get enough sun exposure. In fact, about 41.6% of the U.S. population is deficient in this critical vitamin. If you’re unable to get adequate sun exposure, vitamin D supplements are a good alternative. Their benefits include improved bone health, increased strength, reduced symptoms of depression, and a lower risk of cancer. Vitamin D may also help you live longer."
        },
    {
            "tiptitle": "Use plenty of herbs and spices",
            "contents": "Many incredibly healthy herbs and spices exist. For example, ginger and turmeric both have potent anti-inflammatory and antioxidant effects, leading to various health benefits. Due to their powerful benefits, you should try to include as many herbs and spices as possible in your die"
        },
    {
            "tiptitle": "Replace saturated with unsaturated fat",
            "contents": "Fats are important for good health and proper functioning of the body. However, too much of it can negatively affect our weight and cardiovascular health. Different kinds of fats have different health effects, and some of these tips could help us keep the balance right."
        }

    ]

    return jsonify(tip)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
