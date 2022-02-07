# FinExpert Test - Toughts

I could not manage to make the data structure returned from wide_search read-only with @property. I realize I need to initialize attributes to the Search and then use a getter afterwards. My challenge was mostly with object relations and I understand my code is not optimal in that matter. I still decided to keep on going to be able to get the desired output.

I have populated three databases in SQLite with very basic user fields. To run this project in the django shell :

```
from users.db_ops import Search

# Filtering against user model on a single database 
Search.single_search_queryset(db, **kwargs) 

# Call against all databases using ThreadPoolExecutor
Search.wide_search(**kwargs)
```

Examples
```
Search.single_search_queryset("acceo_users_db", last_name="or") 
# Returns : <QuerySet [<MyUser: jade@or.com>, <MyUser: jemade@or.com>]>

Search.wide_search(last_name="or")
# Returns : [{'first_name': 'fortboy', 'last_name': 'or', 'email': 'fortboy@or.com', 'data_source_name': 'scotia_users_db'}, {'first_name': 'jade', 'last_name': 'or', 'email': 'jade@or.com', 'data_source_name': 'acceo_users_db'}, {'first_name': 'jemade', 'last_name': 'or', 'email': 'jemade@or.com', 'data_source_name': 'acceo_users_db'}]
```
