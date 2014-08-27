#coding:utf-8

import urllib2
import json
import sys, codecs
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

def nico_search():
    url = 'http://api.search.nicovideo.jp/api/'
    req = urllib2.Request(url)
    req.add_header('content-type','application/json')

    params= json.dumps(
            {
                "query":u"サムネホイホイ",
                "service":[
                    "video"
                    ],
                "search":[
                    "tags"
                    ],
                "join":[
                    "thumbnail_url"
                    ],
                "filters":[
                    {
                        "type":"range",
                        "field":"view_counter",
                        "from":100
                        }],
                "from":0,
                "size":100,
                "sort_by":"view_counter",
                "issuer":"apiguide",
                "reason":"ma10"
                }
            )
    res = urllib2.urlopen(req, params)

    return res.readline()



def do_json(s):
    print type(s).__name__
    print json.loads(s)

if __name__ == '__main__':
    res_json = nico_search()
    do_json(res_json)
