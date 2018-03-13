CURRENCIES_JSON = 'https://core.telegram.org/bots/payments/currencies.json'


def format_currency(currency_name, total_amount, tg):
    currencies_json = tg.session.get(CURRENCIES_JSON).json()
    currency = currencies_json[currency_name]
    dec_count = currency['exp']

    # decimal operations
    whole_int = total_amount // (10 ** dec_count)
    decimal_int = total_amount % (10 ** dec_count)
    decimal = str(decimal_int).zfill(dec_count)

    # thousands operations
    thousands_parts_backwards = []
    while whole_int > 999:
        thousands_parts_backwards.append(str(whole_int % 1000).zfill(3))
        whole_int //= 1000
    thousands_parts_backwards.append(str(whole_int))
    sep = currency['thousands_sep']
    whole = sep.join(reversed(thousands_parts_backwards))

    # joining the whole number and the decimal
    if dec_count:
        value = whole + currency['decimal_sep'] + decimal
    else:
        value = whole

    # symbol processing
    symbol = currency['symbol']
    if currency['symbol_left']:
        if currency['space_between']:
            return symbol + ' ' + value
        else:
            return symbol + value
    else:
        if currency['space_between']:
            return value + ' ' + symbol
        else:
            return value + symbol
