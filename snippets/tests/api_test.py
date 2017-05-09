import pytest
import factory

from django.contrib.auth.models import User

from pytest_factoryboy import register


@register
class AdminFactory(factory.Factory):
    class Meta:
        model = User

    username = 'admin'
    password = 'passwd'
    first_name = 'Luke'
    last_name = 'Skywalker'
    email = 'luke@skywalker.com'


@pytest.fixture
def admin_user(user):
    user.save()
    return user


@pytest.mark.django_db
def test_create_snippet(admin_user):
    # Using the standard RequestFactory API to create a form POST request
    # factory = APIRequestFactory()
    # request = factory.post('/snippets/', {'title': 'new idea'}, format='json')
    #
    assert User.objects.count()
    user = User.objects.get(username='admin')
    # force_authenticate(request, user=user)

    assert user
