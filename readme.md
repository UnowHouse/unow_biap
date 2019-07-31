## 启动

自设定端口，默认端口8888
```sh
python3 server.py --port=8888
```
## 人数检测项目
如果可以，则把人数检测项目放置在**libs**目录下

## 植入人数检测函数需要修改的文件

- 进入handlers目录
- 编辑main_handlers.py文件，导入人数检测函数模块
- 在FaceCountHandler类里的 post函数里按照注释指示进行修改

## 测试
- 打开前端页面，如下地址
http://127.0.0.1/static/index.html

- 根据页面中的提示，进行测试