import pandas as pd
import requests
from flask import abort

class Data:
        
    def __init__(self, ctx):
        self.logger = ctx.logger

    def basic_headers(self):
        dict = {}
        return dict

    def parse(self, data):
        df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
        return df    

    def get_annotation(self, url):
        headers = self.basic_headers()
        try:
            response = requests.get(url, verify=False, headers=headers)
        except Exception as e:
            self.logger.error(f"failed to get annotation response: {repr(e)}")
            abort(500)
        else:
            try:
                data = response.json()
            except Exception as e:
                self.logger.error(f"failed to convert data to json: {repr(e)}")
                abort(500)
            else:
                return self.parse(data)