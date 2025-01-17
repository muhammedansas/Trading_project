import pyotp
from smartapi import SmartConnect
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class AngelBrokingService:
    def __init__(self):
        self.settings = settings.ANGEL_BROKING
        self.api = None

    def generate_totp(self):
        totp = pyotp.TOTP(self.settings['TOTP_KEY'])
        return totp.now()

    def authenticate(self):
        try:
            self.api = SmartConnect(api_key=self.settings['API_KEY'])
            data = self.api.generateSession(
                self.settings['CLIENT_ID'],
                self.settings['MPIN'],
                self.generate_totp()
            )
            if data['status']:
                logger.info("Successfully authenticated with Angel Broking")
                return data
            else:
                raise Exception("Authentication failed")
        except Exception as e:
            logger.error(f"Authentication failed: {str(e)}")
            raise Exception(f"Authentication failed: {str(e)}")

    def get_balance(self):
        try:
            if not self.api:
                self.authenticate()
            balance_data = self.api.rmsLimit()
            if balance_data['status']:
                return balance_data['data']
            else:
                raise Exception("Failed to fetch balance")
        except Exception as e:
            logger.error(f"Failed to fetch balance: {str(e)}")
            raise Exception(f"Failed to fetch balance: {str(e)}")

    def get_ltp(self, stock_code):
        try:
            if not self.api:
                self.authenticate()
            ltp_data = self.api.ltpData("NSE", stock_code, "TOKEN")
            if ltp_data['status']:
                return ltp_data['data']
            else:
                raise Exception("Failed to fetch LTP")
        except Exception as e:
            logger.error(f"Failed to fetch LTP for {stock_code}: {str(e)}")
            raise Exception(f"Failed to fetch LTP: {str(e)}")