# Scrapy_zol_wallpapers-scrapy-zol-
使用scrapy框架和内建ImagePipeline结合爬取代理池爬取zol高清壁纸，开启多进程可实现数十G数据爬取。

需要安装redis数据库，scrapy框架



建立project: 
  scrapy startproject zol_wallpapers desk.zol.com.cn
生成爬虫： 
  cd zol_wallpapers
  scrapy genspider wallpaper






使用方法：
  单进程： 
     scrapy crawl wallpaper
  
  
  
  
  
  
  多进程： 
    进入spider目录下，修改wallpaper.py start_request中实例变量start_urls为壁纸分类支链接，如http://desk.zol.com.cn/meinv/1366x768_p4/(美女)，       http://desk.zol.com.cn/dongman/1366x768_p4/（动漫）,同时可以修改壁纸分辨率为自己需要的分辨率。
    
    
    
    运行终端terminal 输入命令scrapy crawl wallpaper
    
    
    
    
    重复：修改支链接，打开新终端输入指令进行多进程爬取即可实现。
      
