# Pytest
import pytest

# Owns
from chat_app.models import Message

# Allow Access to DB
@pytest.mark.django_db
def test_messages():
    message = Message.objects.create(
        username = 'luis',
        room = 'roomRD',
        content = 'klk',
    )

    assert message.username == 'luis'
    assert message.room == 'roomRD'
    assert message.content == 'klk'