from json import dumps

from ..base import PAWTBase
from ..message_specials import Location
from ...const import API_PATH


class InlineQuery(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)
        self.id = data['id']
        self.user = tg.user(data=data['from'])
        self.from_ = self.user
        self.query = data['query']
        self.offset = data['offset']

        if data.get('location'):
            self.location = Location(tg, data['location'])
        else:
            self.location = None

    def __repr__(self):
        return '<InlineQuery {}>'.format(self.id)

    def __str__(self):
        return self.query

    def answer(self, results, cache_time=None, is_personal=None,
               next_offset=None, switch_pm_text=None, switch_pm_parameter=None):
        results = dumps([result.to_dict() for result in results])
        info = dict(inline_query_id=self.id, results=results)
        if cache_time is not None:
            info['cache_time'] = cache_time
        if is_personal:
            info['is_personal'] = is_personal
        if next_offset:
            info['next_offset'] = next_offset
        if switch_pm_text:
            info['switch_pm_text'] = switch_pm_text
        if switch_pm_parameter:
            info['switch_pm_parameter'] = switch_pm_parameter
        return self._tg.post(API_PATH['answer_inline_query'], data=info)
