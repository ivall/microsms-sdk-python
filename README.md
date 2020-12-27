# microsms-sdk-python

## dokumentacja

#### Instalacja biblioteki
Bibliotekę instalujemy poprzez polecenie ```pip install git+https://github.com/ivall/lvlup-sdk-python#egg=lvluppayments```

#### Importowanie biblioteki
Aby skorzystać z biblioteki importujemy klasę Microsms.
```python
from microsms_sdk.main import Microsms
```
### Tworzenie instancji
Utworzenie instancji pozwoli na generowanie płatności.
```python
client = Microsms()
```
### Płatność SMS
Do sprwadzenia kodu SMS potrzebujemy 3 parametrów, które są opisane w dokumentacji microsms: https://microsms.pl/kernel/Mails/files/dokumentacja_techniczna_mirosms.pdf.
Przykład:
```python
sms_payment = client.sms(user_id, service_id, code)
```
Metoda sms zawsze zwraca boola, czyli True albo False.

### Płatność przelewem
```python
transfer_payment = client.bank_transfer(shop_id, hash, amount, control, return_urlc, return_url, description)
```
4 ostatnie parametry są opcjonalne, wymagane jest tylko shop_id, hash, amount.
Metoda bank_transfer zwraca string, link do płatności.
Dokumentacja microsms dotycząca przelewów: https://microsms.pl/documents/dokumentacja_przelewy_microsms.pdf
