from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meditation_times.settings') 

application = get_wsgi_application()