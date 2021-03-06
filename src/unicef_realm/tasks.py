from celery.app import default_app

from unicef_realm.sync import load_business_area


@default_app.task()
def sync_business_area():
    load_business_area()
