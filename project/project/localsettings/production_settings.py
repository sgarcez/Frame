DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pirata2012db',                     
        'USER': 'pirata',                   
        'PASSWORD': 'p1ratap1rata',              
        'HOST': 'pirata2012.cg2fof4liijb.eu-west-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}

DEBUG = True 

DEFAULT_FILE_STORAGE = 'project.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'project.s3utils.StaticRootS3BotoStorage'

AWS_ACCESS_KEY_ID = 'AKIAIZDES5WTEZ4SVM4Q'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'pirata'

S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL + 'static/'
MEDIA_URL = S3_URL + 'media/'

AWS_QUERYSTRING_AUTH = False
