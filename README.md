# fastapi-quickstart
## Basic
 - install
```

pip install fastapi

```
 - run

```

uvicorn main:app --reload

```

## Advance
 - 以下是一个由浅入深的FastAPI常用能力的教程提纲:

## 一、FastAPI基础
1. FastAPI简介
2. 第一个FastAPI应用
3. 请求方法
   - GET请求
   - POST请求 
   - PUT请求
   - DELETE请求
4. 路径参数
5. 查询参数

## 二、请求参数校验
1. 基本数据类型校验
   - 路径参数类型校验
   - 查询参数类型校验
2. 高级参数校验
   - 必填/可选参数
   - 参数默认值
   - 参数限制(如gt, lt, ge, le等)
   - 参数正则匹配
3. 请求体参数校验
   - 基于Pydantic模型的单一参数校验
   - 多个请求体参数
   - 嵌套模型参数
4. 表单参数校验
5. 文件上传校验

## 三、响应处理
1. 返回JSON响应
2. 返回模型对象
3. 自定义响应
   - 返回文本、HTML等
   - 自定义状态码
   - 添加响应头
   - Cookie设置
4. 响应模型
   - include/exclude响应字段
   - 嵌套响应模型
5. 错误处理
   - HTTP异常处理
   - 自定义异常

## 四、数据库操作
1. 数据库连接配置
2. 基于SQLAlchemy的ORM操作
   - 定义ORM模型
   - CRUD操作
3. 多数据库支持

## 五、认证与安全
1. HTTP基本认证
2. JWT认证
3. OAuth2认证
4. 权限控制
5. CORS设置

## 六、中间件
1. 访问日志中间件
2. 异常处理中间件
3. CORS中间件
4. GZip压缩中间件

## 七、后台任务
1. 使用BackgroundTasks
2. 基于Celery的异步任务

## 八、测试
1. 接口测试
2. 单元测试
3. 依赖注入
4. 测试用例参数化

## 九、部署
1. Uvicorn部署
2. Gunicorn部署
3. Docker部署
4. Kubernetes部署

## 十、项目实战
1. 构建RESTfulAPI
2. 项目结构最佳实践
3. 大型项目的目录组织
4. 集成Swagger UI
5. 对接前端

 - 以上提纲涵盖了FastAPI的主要功能和常见应用场景，由浅入深，循序渐进。通过这些内容的学习，可以全面掌握FastAPI的使用，并能够应用到实际项目的开发中。在实战部分，还可以结合具体的项目需求，学习如何使用FastAPI构建完整的Web应用。

# 应用场景

1. **构建RESTful API**

 - FastAPI最常见的应用场景就是快速构建RESTful API。它提供了自动数据验证、序列化/反序列化、交互式API文档等功能,大大简化了API开发的流程。

2. **数据处理管道**

 - FastAPI可以用于构建数据处理管道,比如从数据源获取数据、进行转换处理、存储结果等。利用FastAPI的异步特性,可以高效地处理大量数据。

3. **微服务**

 - 由于FastAPI性能出色、轻量级,非常适合构建微服务架构中的服务组件。可以用它开发各种小型的专用服务。

4. **机器学习模型服务**

 - 将训练好的机器学习模型通过API的形式提供服务时,FastAPI是一个不错的选择。它可以方便地对请求数据进行验证,并返回模型预测结果。

5. **事件驱动应用** 

 - FastAPI支持WebSockets,可以用于构建事件驱动的实时应用,如实时数据推送、在线聊天室等。

6. **文件共享服务**

 - 利用FastAPI可以快速开发一个本地或网络文件共享服务,支持文件上传、下载等功能。

7. **任务调度系统**

 - FastAPI可以集成Celery等分布式任务队列,构建一个高效的任务调度和执行系统。

8. **数据库操作**

 - FastAPI可以通过ORM与关系数据库进行交互,支持CRUD等常见数据库操作。

 - 总的来说,FastAPI是一个全能的Python Web框架,可以应用于构建各种API服务、数据处理系统、微服务等多种场景。

## 参考链接
 - https://www.perplexity.ai/search/fastapi-eCkQt20oR2WpsUQDHVX7Pw