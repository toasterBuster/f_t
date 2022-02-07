import concurrent.futures as cf
from .models import MyUser
from django.core import serializers
import json

class Search():
    def single_search_queryset(db, **kwargs):
        return(MyUser.objects.query(**kwargs).using(db))

    # Includes db source name
    def single_search_json(db, **kwargs):
        res = serializers.serialize("json", Search.single_search_queryset(db, **kwargs))
        user_list = []
        for item in json.loads(res):
            single_user_dict = {
                "first_name": item["fields"]["first_name"],
                "last_name": item["fields"]["last_name"],
                "email": item["fields"]["email"],
                "data_source_name": db
            }
            user_list.append(single_user_dict)

        return user_list

    """
    Why multithreading? I'm assuming these operations would
    be called through a network connection for access to the
    databases. Multithreading does context switching when 
    waiting for a response and many threads can be created
    for many calls on databases. Multiprocessing is generaly
    used when dealing with CPU-intensive operations because
    it's the only way with Python (CPython) to bypass the global 
    interpreter lock, which is not necessary in this situation. 
    """
    def wide_search(**kwargs):
        database_list = ["bnc_users_db", "scotia_users_db", "acceo_users_db"]

        with cf.ThreadPoolExecutor(max_workers=len(database_list)) as executor:
            futures = []
            for db in database_list:
                futures.append(executor.submit(Search.single_search_json, db, **kwargs))
            res = []
            for future in cf.as_completed(futures):
                res += future.result()

        return res