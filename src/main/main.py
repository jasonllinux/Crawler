#encoding=UTF-8

from crawler import Crawler


if __name__ == '__main__':
    
    url = "http://www.baidu.com"
    c = Crawler();
    c.run(url);
    
    print "testing..."