# apidocs-generator
基于django restframework，生成swagger格式的api文档


Quick start
-----------

1. 安装最新版django restframework

    git clone git+https://github.com/encode/django-rest-framework

2 安装api-generator

    git clone git+https://github.com/yang0/django_sqltools.git

3 配置django settings文件

    REST_FRAMEWORK = {
        ...
        'DEFAULT_SCHEMA_CLASS':'apidocs.makedocs.MakeSchema'
    }

4. 运行命令行

    python manage.py generateschema --urlconf=xxxxx.urls --url=/xxxxx --generator_class=apidocs.generator.ApiDocsGenerator

    把xxxxx替换成自己的路径