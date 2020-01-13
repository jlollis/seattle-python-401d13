# Django Starter

## Typical Steps to Start Django Project

- create project
- define app
  - add app to project
  - add views
  - add urlpatterns
  - add templates
  - add tests

## Details

Create Project

```bash
bash$ mkdir eggs_site
bash$ cd eggs_site
bash$ pipenv install django
bash$ pipenv shell
bash$ django-admin startproject eggs_project .
bash$ python manage.py startapp spam
bash$ python manage.py runserver
```

Edit `settings.py`

```python
'spam.apps.SpamConfig' # add to INSTALLED_APPS list
```

Edit `spam/views.py`

```python
class HomePageView(TemplateView):
    template_name='home.html'

class AboutPageView(TemplateView):
    template_name='about.html'
```

Create App urls

```bash
bash$ touch spam/urls.py
```

Edit `spam/urls.py`

```python
urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view, name='about')
]
```

Edit `eggs_project/urls.py`

```python
path('', include('spam.urls')) # add to urlpatterns
```

Edit `settings.py`

```python
os.path.join(BASE_DIR, 'templates') # add to TEMPLATES['DIRS']
```

Create Templates

```bash
bash$ mkdir templates
bash$ touch templates/base.html
bash$ touch templates/home.html
bash$ touch templates/about.html
```

Edit `base.html`

```html
<nav>
    <a href="{% url 'home' %}">
    |
    <a href="{% url 'about' %}">
</nav>
{% block content %}
<!-- child template content goes here -->
{% endblock content %}
```

Edit `home.html`

```html
{% extends 'base.html' %}

{% block content%}
<h1>Home Page</h1>
{% endblock content%}
```

Edit `about.html`

```html
{% extends 'base.html' %}

{% block content%}
<h1>Home Page</h1>
{% endblock content%}
```

Edit `spam/tests.py`

```python
class SpamTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_templete(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')
```
