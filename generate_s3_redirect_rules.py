#!/usr/bin/env python3

import sys

CONDITION = "Condition"
REDIRECT = "Redirect"

KEYPREFIXEQUALS = "KeyPrefixEquals"
HTTOCODEEQUALS =  "HttpErrorCodeReturnedEquals"

PROTOCOL = "Protocol"
HOSTNAME = "HostName"

REPLACEKEYPREFIXWITH = "ReplaceKeyPrefixWith"

rules = [
    {
        CONDITION: {KEYPREFIXEQUALS: "index.php"},
        REDIRECT: {REPLACEKEYPREFIXWITH: "index.html"}
    },
    {
        CONDITION: {KEYPREFIXEQUALS: "otherStuff.php"},
        REDIRECT: {REPLACEKEYPREFIXWITH: "otherStuff.html"}
    },
    {
        CONDITION: {KEYPREFIXEQUALS: "privacy.php"},
        REDIRECT: {REPLACEKEYPREFIXWITH: "privacy.html"}
    },
    {
        CONDITION: {KEYPREFIXEQUALS: "genealogy.php"},
        REDIRECT: {REPLACEKEYPREFIXWITH: "genealogy.html"}
    },
    {
        CONDITION: {KEYPREFIXEQUALS: "projects/amplifier.php"},
        REDIRECT: {REPLACEKEYPREFIXWITH: "projects/amplifier.html"}
    },
    {
        CONDITION: {KEYPREFIXEQUALS: "projects/Valve%20Info.php"},
        REDIRECT: {REPLACEKEYPREFIXWITH: "projects/Valve%20Info.html"}
    },
    {
        CONDITION: {KEYPREFIXEQUALS: "projects/Cathamplifier.php"},
        REDIRECT: {REPLACEKEYPREFIXWITH: "projects/Cathamplifier.html"}
    },
    {
        CONDITION: {KEYPREFIXEQUALS: "projects/McPherson.php"},
        REDIRECT: {REPLACEKEYPREFIXWITH: "projects/McPherson.html"}
    },
    {
        CONDITION: {KEYPREFIXEQUALS: "projects/Williamson.php"},
        REDIRECT: {REPLACEKEYPREFIXWITH: "projects/Williamson.html"}
    },
    {
        CONDITION: {KEYPREFIXEQUALS: "projects/Selmer%20Organ.php"},
        REDIRECT: {REPLACEKEYPREFIXWITH: "projects/Selmer%20Organ.html"}
    },
    {
        CONDITION: {KEYPREFIXEQUALS: "projects/", HTTOCODEEQUALS: "404"},
        REDIRECT: {REPLACEKEYPREFIXWITH: "static/"}
    },
]

print("<RoutingRules>")

for rule in rules:
    print("{0}<RoutingRule>".format(' ' * 2))

    for rule_key, rule_value in rule.items():
        print("{0}<{1}>".format(' ' * 4, rule_key))

        for sub_rule_key, sub_rule_value in rule_value.items():
            print("{0}<{1}>{2}</{1}>".format(' ' * 6, sub_rule_key, sub_rule_value))

        # Force the redirect to be the correct protocol/domain as otherwise it's the S3 bucket
        if rule_key == REDIRECT:
            print("{0}<{1}>{2}</{1}>".format(' ' * 6, PROTOCOL, "https"))
            print("{0}<{1}>{2}</{1}>".format(' ' * 6, HOSTNAME, "dalmura.com.au"))

        print("{0}</{1}>".format(' ' * 4, rule_key))

    print("{0}</RoutingRule>".format(' ' * 2))

print("</RoutingRules>")
