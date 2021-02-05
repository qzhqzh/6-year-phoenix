# 配置文件

class BaseConfig:
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = '465'
    MAIL_USERNAME = '@qq.com'
    MAIL_PASSWORD = ''

    MAIL_DEFAULT_SENDER = '@qq.com'
    MAIL_USE_SSL = True

class DevConfig(BaseConfig):
    DB = '127.0.0.1'