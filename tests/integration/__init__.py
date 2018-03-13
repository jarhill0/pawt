import os

from betamax import Betamax
from betamax_serializers.pretty_json import PrettyJSONSerializer
from requests import Session

from pawt import Telegram

token = os.environ.get('PAWT_TEST_TOKEN') or 'TOKENPLACEHOLDER'
user = os.environ.get('PAWT_TEST_USER') or '123'
# game should have animation
game = os.environ.get('PAWT_TEST_GAME') or 'GAMEPLACEHOLDER'
supergroup = os.environ.get('PAWT_TEST_SUPERGROUP') or '-123'

with Betamax.configure() as config:
    config.cassette_library_dir = os.path.join('tests', 'integration',
                                               'cassettes')
    config.define_cassette_placeholder('<TOKEN>', token)
    config.define_cassette_placeholder('<USER>', user)
    config.define_cassette_placeholder('<GAME SHORTNAME>', game)
    config.define_cassette_placeholder('<SUPERGROUP>', supergroup)

Betamax.register_serializer(PrettyJSONSerializer)

session = Session()
bm = Betamax(session, default_cassette_options={'serialize_with': 'prettyjson'})
tg = Telegram(token, session=session)
