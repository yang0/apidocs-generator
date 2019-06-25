=====
api-generator
=====

api-generator是基于最新版django restframework使用的

Quick start
-----------

1. 安装最新版django restframework

    pip install git+https://github.com/encode/django-rest-framework

2 安装api-generator

    pip install git+https://github.com/yang0/apidocs-generator.git

3 配置django settings文件

    REST_FRAMEWORK = {
        ...
        'DEFAULT_SCHEMA_CLASS':'apidocs.makedocs.MakeSchema'
    }

4. 运行命令行

    python manage.py generateschema --urlconf=xxxxx.urls --url=/xxxxx --generator_class=apidocs.generator.ApiDocsGenerator

    把xxxxx替换成自己的路径
