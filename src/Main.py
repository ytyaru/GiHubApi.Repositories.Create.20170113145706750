#!python3
#encoding:utf-8

import os
from pathlib import Path
from github import Repository
from github import Account

db_path = 'C:/GitHub.Accounts.sqlite3'
username = 'github_username'
repo_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
repo_description = 'repo desc.'
repo_homepage = 'http://repo'

account = Account.Account(db_path)
account.set_username(username)

r = Repository.Repository()
if (account.get_otp() is None):
    r.create(token=account.get_token(), name=repo_name, description=repo_description, homepage=repo_homepage)
else:
    r.create(otp=account.get_otp(), token=account.get_token(), name=repo_name, description=repo_description, homepage=repo_homepage)
