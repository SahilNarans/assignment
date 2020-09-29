#!/usr/bin/env python
import os
import sys
import argparse
import requests

try:
    import json
except ImportError:
    import simplejson as json

class ExampleInventory(object):

    def _init_(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print(json.dumps(self.inventory));

    # Example inventory for testing.
    def example_inventory(self):
        env = os.environ['ENV']
        service = os.environ['SERVICE']
        try:
            app_inventory = requests.post('https://bjs.paytm.com/getinventory/', data = {'environment': env, 'microservice': service})
            if app_inventory.status_code == 200:
                return app_inventory.json()
        except:
          print('unable to get-inventory connect')
          return 404

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
ExampleInventory()
