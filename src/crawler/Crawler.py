#encoding=UTF-8

import urllib2
import urllib

class Crawler:
    
    m_tempResult = ""
    
    def __init__(self):
        pass;
    
#   从这里开始爬
    def run(self, url):
        # 伪装成浏览器
        
        pass
    
    
    
    def __login(self, url):
        '''
        简单登陆
        '''
        self.m_tempResult = urllib2.urlopen('http://XXXX').read()
        
        pass
    
    
    def __advanceLogin(self, url, username, password):
        '''
        高级登陆设置
        '''
        postdata=urllib.urlencode({
                                   'username':'XXXXX',    
                                   'password':'XXXXX',   
                                   'continueURI':'http://www.verycd.com/',
                                   'fk':'fk',    
                                   'login_submit':'登录'})
        
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib2.Request('http://secure.verycd.com/signin/*/http://www.verycd.com/',
                              data = postdata,
                              headers=headers)
        self.m_tempResult = urllib2.urlopen(req).read()

#        self.m_tempContent = urllib.urlencode({'username':username,
#                           'password':password,
#                           'continue':'http://www.verycd.com/',
#                           'login_submit':u'登录'.encode('UTF-8'),
#                           'save_cookie':1, })
#       
#        self.opener.open(url, self.m_tempContent).read()
    
    
