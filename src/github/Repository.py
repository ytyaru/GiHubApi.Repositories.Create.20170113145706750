#!python3
#encoding:utf-8

import requests
import json
import urllib.parse

class Repository:
    def __init__(self):
        pass

    def create(self, username=None, password=None, otp=None, token=None, name=None, description=None, homepage=None):
        if (name is None):
            raise Exception('name is required.')
            return
        url = 'https://api.github.com/user/repos'
        data = self._get_post_data(name, description, homepage)
        headers = self._get_http_headers(otp, token)
        if not(username is None or password is None):
            r = requests.post(url, headers=headers, auth=(username, password), data=json.dumps(data))
        elif not(token is None):
            r = requests.post(url, headers=headers, data=json.dumps(data))
        else:
            raise Exception('Account information is required.')
            return
        
        if not(201 == r.status_code):
            print(r.status_code)
            print(r.text)
            raise Exception('Failed request.')
            return None
        
        res = json.loads(r.text)
        with open('GiHubApi.Repositories.Create.{0}.json'.format(res['id']), 'w') as f:
            f.write(r.text)
            print(r.text)
        return res

    def _get_http_headers(self, otp=None, token=None):
        headers = {'Time-Zone': 'Asia/Tokyo',
                    'Content-Type': 'application/json; charset=utf-8'}
        if not(otp is None):
            headers['X-GitHub-OTP'] = otp
        if not(token is None):
            headers['Authorization'] = 'token {0}'.format(token)
        print(headers)
        return headers

    def _get_post_data(self, name, description=None, homepage=None):
        data = {"name": name}
        if not(description is None):
            data["description"] = description
        if not(description is None):
            data["homepage"] = homepage
        print(data)
        print(json.dumps(data))
        return data
