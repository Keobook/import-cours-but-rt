#!/usr/bin/env python3

# Example client for the RIS Live service <https://ris-live.ripe.net/>
# Asynchronous, it displays the current time periodically, to show
# that you can do something else while waiting for BGP news.

PERIOD = 300 # Seconds
TIMEFORMAT = '%Y-%m-%dT%H:%M:%SZ' #RFC 3339
ME='asynchronous-example-python-script-by-me' # Sent with the request https://ris-live.ripe.net/manual/#limits
ENDPOINT='wss://ris-live.ripe.net/v1/ws/?client=%s' % ME

import sys
import json
import time
import getopt
import asyncio

# https://websockets.readthedocs.io/
import websockets

class RISliveWebsocket():

    def __init__(self, verbose=False, router=None, allRouters=False, type=None, require=None, peer=None,
                 prefix=None, path=None, moreSpecific=None, lessSpecific=None):
        self.router = router
        self.allRouters = allRouters
        self.type = type # "UPDATE", "OPEN", "NOTIFICATION", "KEEPALIVE" or "RIS_PEER_STATE"
        self.require = require # "announcements" or "withdrawals"
        self.peer = peer
        self.prefix = prefix
        self.path = path
        self.moreSpecific = moreSpecific
        self.lessSpecific = lessSpecific
        self.verbose = verbose

    async def __aenter__(self):
        # TODO exception in _aenter_ are badly handled. Add an explicit handler?
        try:
            if not self.allRouters:
                request = {'type': 'ris_subscribe', 'data': {}}
                if self.router is not None:
                    request['data']['host'] = self.router
                if self.type is not None:
                    request['data']['type'] = self.type
                if self.require is not None:
                    request['data']['require'] = self.require
                if self.peer is not None:
                    request['data']['peer'] = self.peer
                if self.path is not None:
                    request['data']['path'] = self.path
                if self.prefix is not None:
                    request['data']['prefix'] = self.prefix
                if self.moreSpecific is not None:
                    request['data']['moreSpecific'] = self.moreSpecific
                if self.lessSpecific is not None:
                    request['data']['lessSpecific'] = self.lessSpecific
            else:
                request = {'type': 'request_rrc_list'}
            opening = json.dumps(request)
            if self.verbose:
                print("Trying to connect, to send %s" % opening)
        except Exception as e:
            print("Exception %s" % e)
            sys.exit(1)
        self._conn = await websockets.connect(ENDPOINT)
        await self._conn.send(opening)
        if self.verbose:
            print("Connected, %s sent" % opening)
        return self

    async def __aexit__(self, *args, **kwargs):
        if self.verbose:
            print("Goodbye")
        sys.exit(0) # TODO probably means the remote end closed the connection: find out if it is really the case?
        return self

    async def send(self, message):
        await self._conn.send(message)

    async def receive(self):
        if self.verbose:
            print("Trying to receive")
        return await self._conn.recv()

async def tick(routerList=False):
    if not routerList:
        while True:
            await asyncio.sleep(PERIOD)
            print("Waking up, it is %s" % time.strftime(TIMEFORMAT, time.gmtime(time.time())))
        
async def main(verbose, router, routerList, path):
    sock = RISliveWebsocket(verbose=verbose, router=router, allRouters=routerList, path=path)
    async with sock as feed:
        if routerList:
            print(await feed.receive())
        else:
            while True:
                print(await feed.receive())  # TODO better printing of messages

def usage(msg=None):
    if msg is not None:
        print(msg, file=sys.stderr)
    print('Usage: %s [-r RIS-router] [-p AS-path]' % sys.argv[0], file=sys.stderr)
    
if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hvlr:p:', ['help', 'verbose', 'router-list', 'router=', 'path='])
    except getopt.GetoptError as err:
        usage(err)
        sys.exit(2)
    routerList = False
    verbose = False
    router = None
    path = None
    for o, a in opts:
        if o in ('-v', '--verbose'):
            verbose = True
        elif o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('-l', '--router-list'):
            routerList = True
        elif o in ('-p', '--path'):
            path = a
        elif o in ('-r', '--router'):
            router = a
        else:
            assert False, "unknown option"
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait([main(verbose, router, routerList, path), tick(routerList)]))
    except KeyboardInterrupt:
        pass # Does not call __aexit__?
