def text_up(func):
    def wrap(text):
        res = func(text)
        text = res.upper()
        return text
    return wrap


@text_up
def get_text(text):
    text_str = ' '.join(text)
    return text_str


print(get_text(['Hello', 'world']))
