# -*- coding: utf-8 -*-
#! /usr/bin/env python
import requests
data ={
    '__EVENTARGUMENT':'',
    '__EVENTTARGET':'',
    '__EVENTVALIDATION':'/wEdAAUIqCk3Gcmu25zI9fQWqoC7hI6Xi65hwcQ8/QoQCF8JIahXufbhIqPmwKf992GTkd0wq1PKp6+/1yNGng6H71Uxop4oRunf14dz2Zt2+QKDEM3sbzJLySdZoy08+/dzW8VF2on0',
    '__VIEWSTATE':'	/wEPDwUKLTM1MjEzOTU2MGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFC2Noa1JlbWVtYmVy4b/ZXiH+8FthXlmKpjSEgi7XBNU=',
    '__VIEWSTATEGENERATOR':'	C2EE9ABB',
    'btnLogin':'	登 录',
    'tbPassword':'liwei123@asd',
    'tbUserName':'liwei123o0',
    'txtReturnUrl':'http://www.cnblogs.com/'
}
s =requests.session()
s.post(url='http://passport.cnblogs.com/login.aspx',data=data)

r=s.get('http://home.cnblogs.com/group/')
print r.text


# rep = urllib2.Request \
#         ('http://passport.cnblogs.com/login.aspx?ReturnUrl=http%3A%2F%2Fwww.cnblogs.com%2F')
# html = urllib2.urlopen(rep).read()
# print(html)