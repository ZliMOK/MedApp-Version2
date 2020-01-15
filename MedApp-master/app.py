#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    tasks = [
      {
          "medname": "Acetaminophen",
          "type": 0,
          "Dosage": "500mg",
          "Tablets": "100Capsules"
      },
      {
          "medname": "Adderall",
          "type": 0,
          "Dosage": "30mg",
          "Tablets": "100 Capsules"
      },
      {
          "medname": "Alprazolam",
          "type": 0,
          "Dosage": "1mg",
          "Tablets": "30 Tablets"
      },
      {
          "medname": "Amitriptyline",
          "type": 0,
          "Dosage": "10mg",
          "Tablets": "100 Tablets"
      },
      {
           "medname": "Amlodipine",
           "type": 0,
           "Dosage": "10mg",
           "Tablets": "20 Tablets"
       },
      {
           "medname": "Amoxicillin",
           "type": 0,
           "Dosage": "250mg",
           "Tablets": "21 Capsules"
       },
      {
           "medname": "Ativan",
           "type": 0,
           "Dosage": "1mg",
           "Tablets": "100 Tablets"
       },
      {
          "medname": "Atorvastatin",
          "type": 0,
          "Dosage": "20mg",
          "Tablets": "28 Film-coated Tablets"
      },
      {
          "medname": "Azithromycin",
          "type": 0,
          "Dosage": "500mg",
          "Tablets": "3 Film-coated Tablets"
      },
      {
          "medname": "Ciprofloxacin",
          "type": 0,
          "Dosage": "250mg",
          "Tablets": "100 Tablets"
      },
      {
          "medname": "Citalopram",
          "type": 0,
          "Dosage": "20mg",
          "Tablets": "28 Tablets"
      },
      {
          "medname": "Clindamycin",
          "type": 0,
          "Dosage": "75mg",
          "Tablets": "200 Capsules"
      },
      {
          "medname": "Clonazepam",
          "type": 0,
          "Dosage": "2mg",
          "Tablets": "30 Tablets"
      },
      {
          "medname": "Codeine",
          "type": 0,
          "Dosage": "6.25mg/5ml",
          "Tablets": "473ml"
      },
      {
          "medname": "Cyclobenzaprine",
          "type": 0,
          "Dosage": "5mg",
          "Tablets": "100 Tablets"
      },
      {
          "medname": "Cymbalta",
          "type": 0,
          "Dosage": "60mg",
          "Tablets": "7 Capsules"
      },
      {
          "medname": "Doxycycline",
          "type": 0,
          "Dosage": "100mg",
          "Tablets": "50 Capsules"
      },
      {
          "medname": "Gabapentin",
          "type": 0,
          "Dosage": "100mg",
          "Tablets": "100 Capsules"
      },
      {
          "medname": "Hydrochlorothiazide",
          "type": 0,
          "Dosage": "50mg",
          "Tablets": "100 Tablets"
      },
      {
          "medname": "Lbuprofen",
          "type": 0,
          "Dosage": "200mg",
          "Tablets": "100 Film-coated Tablets"
      },
      {
          "medname": "Lexapro",
          "type": 0,
          "Dosage": "10mg",
          "Tablets": "28 Tablets"
      },
      {
          "medname": "Lisinopril",
          "type": 0,
          "Dosage": "10mg",
          "Tablets": "100 Tablets"
      },
      {
          "medname": "Loratadine",
          "type": 0,
          "Dosage": "10mg",
          "Tablets": "300 Tablets"
      },
      {
          "medname": "Loarazepam",
          "type": 0,
          "Dosage": "1mg",
          "Tablets": "100 Tablets"
      },
      {
          "medname": "Losartan",
          "type": 0,
          "Dosage": "50mg",
          "Tablets": "3*10 Tablets"
      },
      {
          "medname": "Lyrica",
          "type": 0,
          "Dosage": "150mg",
          "Tablets": "56 Hard Capsules"
      },
      {
          "medname": "Meloxicam",
          "type": 0,
          "Dosage": "7.5mg",
          "Tablets": "100 Tablets"
      },
      {
          "medname": "Metformin",
          "type": 0,
          "Dosage": "500mg",
          "Tablets": "84 Film-coated Tablets"
      },
      {
          "medname": "Metoprolol",
          "type": 0,
          "Dosage": "100mg",
          "Tablets": "20 Tablets"
      },
      {
          "medname": "Naproxen",
          "type": 0,
          "Dosage": "220mg",
          "Tablets": "50 Tablets"
      },
      {
          "medname": "Omeprazole",
          "type": 0,
          "Dosage": "20mg",
          "Tablets": "42 Tablets"
      },
      {
          "medname": "Oxycodone",
          "type": 0,
          "Dosage": "10mg",
          "Tablets": "100 Tablets"
      },
      {
          "medname": "Pantoprazole",
          "type": 0,
          "Dosage": "40mg",
          "Tablets": "28 Film-coated Tablets"
      },
      {
          "medname": "Prednisone",
          "type": 0,
          "Dosage": "10mg",
          "Tablets": "100 Tablets"
      },
      {
          "medname": "Tramadol",
          "type": 0,
          "Dosage": "50mg",
          "Tablets": "20 Capsules"
      },
      {
          "medname": "Trazodone",
          "type": 0,
          "Dosage": "100mg",
          "Tablets": "100 Tablets"
      },
      {
          "medname": "Viagra",
          "type": 0,
          "Dosage": "100mg",
          "Tablets": "4 Film-coated Tablets"
      },
      {
          "medname": "Wellbutrin",
          "type": 0,
          "Dosage": "300mg",
          "Tablets": "30 Tablets"
      },
      {
          "medname": "Xanax",
          "type": 0,
          "Dosage": "0.5mg",
          "Tablets": "30 Tablets"
      },
      {
          "medname": "Zoloft",
          "type": 0,
          "Dosage": "20mg/ml",
          "Tablets": "60ml"
      },
      {
          "medname": "Zoloft",
          "type": 0,
          "Dosage": "20mg/ml",
          "Tablets": "60ml"
      },
      {
          "medname": "Advil",
          "type": 1,
          "usefor": 0,
          "Dosage": "200mg",
          "Tablets": "200 Coated Gel Caplets"
      },
      {
          "medname": "Aleve",
          "type": 1,
          "usefor": 1,
          "Dosage": "220mg",
          "Tablets": "50 Tablets"
      },
      {
          "medname": "Cepacol Antibacterial",
          "type": 1,
          "usefor": 1,
          "Dosage": "15mg/5ml",
          "Tablets": "500ml"
      },
      {
          "medname": "Childrens Dimetapp",
          "type": 1,
          "usefor": 0,
          "Dosage": "",
          "Tablets": "118ml"
      },
      {
          "medname": "Claritin",
          "type": 1,
          "usefor": 0,
          "Dosage": "5mg/5ml",
          "Tablets": "50 Chewable Tablets"
      },
      {
          "medname": "Colace",
          "type": 1,
          "usefor": 1,
          "Dosage": "100mg",
          "Tablets": "30 Tablets"
      },
      {
          "medname": "Cortaid",
          "type": 1,
          "usefor": 1,
          "Dosage": "",
          "Tablets": "1.33oz/37g"
      },
      {
          "medname": "Dulcolax",
          "type": 1,
          "usefor": 1,
          "Dosage": "5mg",
          "Tablets": "100 Comfort-coated Tablets"
      },
      {
          "medname": "Excedrin",
          "type": 1,
          "usefor": 1,
          "Dosage": "",
          "Tablets": "100 Caplets"
      },
      {
          "medname": "Gaviscon",
          "type": 1,
          "usefor": 1,
          "Dosage": "",
          "Tablets": "300ml/100 Chewable Tablets"
      },
      {
          "medname": "Lotrimin AF",
          "type": 1,
          "usefor": 1,
          "Dosage": "",
          "Tablets": "12g/0.42oz"
      },
      {
          "medname": "Maalox Antacid",
          "type": 1,
          "usefor": 1,
          "Dosage": "230mg",
          "Tablets": "250ml"
      },
      {
          "medname": "Midol",
          "type": 1,
          "usefor": 1,
          "Dosage": "",
          "Tablets": "24 Gelcaps/40 Caplets"
      },
      {
          "medname": "Motrin",
          "type": 1,
          "usefor": 0,
          "Dosage": "100mg/5ml",
          "Tablets": "1oz/30ml"
      },
      {
          "medname": "Orajel",
          "type": 1,
          "usefor": 1,
          "Dosage": "200mg",
          "Tablets": "0.45oz/13.3ml"
      },
      {
          "medname": "Pepto-Bismol",
          "type": 1,
          "usefor": 1,
          "Dosage": "",
          "Tablets": "12oz/354ml"
      },
      {
          "medname": "Rolaids",
          "type": 1,
          "usefor": 1,
          "Dosage": "",
          "Tablets": "60 Chewable Tablets"
      },
      {
          "medname": "Tagamet HB",
          "type": 1,
          "usefor": 1,
          "Dosage": "",
          "Tablets": "30 Tablets"
      },
      {
          "medname": "Tylenol",
          "type": 1,
          "usefor": 0,
          "Dosage": "16mg/5ml",
          "Tablets": "2oz/60ml"
      },
      {
          "medname": "Zantac",
          "type": 1,
          "usefor": 1,
          "Dosage": "150mg",
          "Tablets": "50 Tablets"
      },
      {
          "medname": "Children's Mucinex",
          "type": 1,
          "usefor": 0,
          "Dosage": "",
          "Tablets": "12 Granule Packets"
      },
      {
          "medname": "Pedialyte",
          "type": 1,
          "usefor": 0,
          "Dosage": "",
          "Tablets": "8 Powder Packs"
      },
      {
          "medname": "Little Remedies",
          "type": 1,
          "usefor": 0,
          "Dosage": "",
          "Tablets": "10 Pops"
      },
      {
          "medname": "Neosporin",
          "type": 1,
          "usefor": 0,
          "Dosage": "",
          "Tablets": "0.5oz/14.2g"
      },
      {
          "medname": "Dimetapp Cold an Cough",
          "type": 1,
          "usefor": 0,
          "Dosage": "",
          "Tablets": "8oz/237ml"
      },
      {
          "medname": "BabyRub",
          "type": 1,
          "usefor": 0,
          "Dosage": "",
          "Tablets": "1.76oz/50g"
      },
      {
          "medname": "Delsym",
          "type": 1,
          "usefor": 0,
          "Dosage": "",
          "Tablets": "3oz/89ml"
      },
      {
          "medname": "Benadryl",
          "type": 1,
          "usefor": 0,
          "Dosage": "1.5/5ml",
          "Tablets": "4oz/118ml"
      },
      {
          "medname": "Destin",
          "type": 1,
          "usefor": 0,
          "Dosage": "",
          "Tablets": "1oz/56g"
      }
    ]

    return jsonify(tasks)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
