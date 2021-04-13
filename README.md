# quittance-gen
Generate PDF rent receipt.

* Clone or fork the project

* Create a venv and activate it
```
python3 -m  venv venv
. venv/bin/activate
```

* Install python dependencies
```
pip install -r requirements.txt
```

* Add a image for the signature in static folder and call it signature.png

* Create data.json for user information
```
[
    {
        "id": {
            "lastname": "Toto",
            "firstname": "Tata"
        },
        "adresse": {
            "rue": "Boulevard des Capucines",
            "numero": "1",
            "code_postal": "00000",
            "ville": "City"
        },
        "loyer": {
            "ht": "220",
            "charge": "140",
            "total": "360"
        }
    }
]
```

* Launch the script, take care of the date format dd/mm/YYYY
```
python3 manage.py create_quittance :month/:year :date_of_payment
example : python3 manage.py create_quittance 01/2021 12/01/2021
```