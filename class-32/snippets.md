# Oh noes!
All these code snippets got jumbled up.
At least the spelling is correct.

```
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'postgres',
'USER':'postgres',
'PASSWORD': 'postgres',
'HOST': 'db',
'PORT': 5432
```

```
path('api-auth/', include('rest_framework.urls')),
```

```
'rest_framework.permissions.IsAuthenticated',
```

```
from .permissions import IsAuthorOrReadOnly

...

permission_classes = (IsAuthorOrReadOnly,)
```

```
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission:

    def has_object_permission(self, request, view, obj):
        # read only allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed for the author
        return obj.author == request.user
```

```
    depends_on:
        - db

  db:
    image: postgres:11
    volumes:
        - postgres_data:/var/lib/postgresql/data/

volumes:
    postgres_data:
```

```
psycopg2-binary = "*"
```
