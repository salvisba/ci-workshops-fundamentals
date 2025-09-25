#!/usr/bin/env python3

from jsonrpclib import Server
import ssl
import pprint

ssl._create_default_https_context = ssl._create_unverified_context

switch = Server("https://arista:u7mn1wby11syhsdg@192.168.0.12/command-api")

response = switch.runCmds( 1, ["show version"] )

print(response)
pprint.pp("The switch model name is " + response[0]["modelName"] + " and it is running " + response[0]["version"])