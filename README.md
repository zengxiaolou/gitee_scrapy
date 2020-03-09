![image](https://github.com/zengxiaolou/gitee_scrapy/blob/master/analyze/test.svg)

###简介
    该项目有用练手，通过scrapy-redis对等分布式爬取gitee网站[ www.gitee.com](http://www.google.com/)
    上开源的所有项目信息
    使用mongoDB作为数据库保存数据
    通过pandas、numpy、matplotlib等第三方库进行数据分析

### 安装
    将项目clone到本地，使用
    'pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/'
    快速安装依赖包

### 其他依赖
    redis、mongobd，请自行google 如何安装
    
### 运行

#### 爬虫
    进入myspider目录，
    ·scrapy crawl gitee——redis·
    启动爬虫脚本，脚本为分布式爬虫，需要向redis中放入启动url，方可开始
    strat_url
    'gitee_redis:start_urls gitee.com/explore'
    
#### 数据分析
    爬取完成后，运行analyze下的gitee.py 即可完成

    
