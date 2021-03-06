from pawt.exceptions import BadArgument
from ..base import PAWTBase
from ..message_specials import OrderInfo, format_currency
from ...const import API_PATH


class PreCheckoutQuery(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)
        self.id = data["id"]
        self.user = tg.user(data=data["from"])
        self.from_ = self.user
        self.currency = data["currency"]
        self.total_amount = data["total_amount"]
        self.invoice_payload = data["invoice_payload"]
        self.shipping_option_id = data.get("shipping_option_id")
        self.order_info = None

        if data.get("order_info"):
            self.order_info = OrderInfo(tg, data=data["order_info"])

    def __repr__(self):
        return "<PreCheckoutQuery {}>".format(self.id)

    def format_amount(self):
        return format_currency(self.currency, self.total_amount, self._tg)

    def answer(self, ok, error_message=None):
        if bool(ok) == bool(error_message):
            raise BadArgument("error_message must be provided if and only if " "not ok")
        info = dict(pre_checkout_query_id=self.id, ok=ok)
        if not ok:
            info["error_message"] = error_message
        return self._tg.post(API_PATH["answer_pre_checkout_query"], data=info)
