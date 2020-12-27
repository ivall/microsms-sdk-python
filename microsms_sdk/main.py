import requests
import hashlib

from .utils import check_payment_status, validate_code


class Microsms:
    def __init__(self):
        self.base_url = 'https://microsms.pl/api/'

    def sms(self, user_id, service_id, code) -> bool:
        validate_code(code)

        url = self.base_url + f'check_multi.php?userid={user_id}&code={code}&serviceid={service_id}'

        r = requests.get(url)
        payment_status = r.text.strip()

        paid = check_payment_status(payment_status)
        return paid

    def bank_tansfer(self, shop_id, hash, amount, control=None, return_urlc=None, return_url=None, description=None):
        amount = format(float(amount), '.2f')
        signature = hashlib.md5(f'{shop_id}{hash}{amount}'.encode('utf-8')).hexdigest()

        payload = {
            'shopid': shop_id,
            'signature': signature,
            'amount': amount,
            'control': control,
            'return_urlc': return_urlc,
            'return_url': return_url,
            'description': description
        }

        r = requests.get('https://microsms.pl/api/bankTransfer', params=payload).url
        return r
