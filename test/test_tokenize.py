from multilingual_sentence_tokenizer import sentence_tokenizer

string_panjabi = '''ਪਰ ਦੋਵੇਂ ਭਾਈਚਾਰਿਆਂ ਵਿਚਕਾਰ ਤਰੇੜ ਪਹਿਲਾਂ ਤੋਂ ਜ਼ਿਆਦਾ ਗਹਿਰੀ ਹੁੰਦੀ ਦਿਖ ਰਹੀ ਹੈ, ਜਿਸ ਦੇ ਪਿੱਛੇ ਰੋਜ਼-ਰੋਜ਼ ਉਛਾਲੇ ਜਾਣ ਵਾਲੇ ਅਜਿਹੇ ਮੁੱਦੇ ਹਨ ਜਿਨ੍ਹਾਂ ਦਾ ਸਿੱਧਾ ਸਬੰਧ ਦੇਸ਼ ਦੇ ਮੁਸਲਮਾਨਾਂ ਨਾਲ ਹੈ। ਇੱਥੇ ਅਸੀਂ ਉਨ੍ਹਾਂ ਮੁੱਦਿਆਂ 'ਤੇ ਨਜ਼ਰ ਮਾਰ ਰਹੇ ਹਾਂ ਜੋ ਦਰਾੜ ਨੂੰ ਭਰਨ ਦੀ ਜਗ੍ਹਾ ਉਸ ਨੂੰ ਹੋਰ ਗਹਿਰਾ ਕਰਦੇ ਜਾ ਰਹੇ ਹਨ। ਅਜਿਹਾ ਨਹੀਂ ਹੈ ਕਿ ਇਹ ਸਾਰੇ ਬਿਆਨ ਕੇਵਲ ਸਿਆਸੀ ਤਬਕੇ ਤੋਂ ਆ ਰਹੇ ਹਨ, ਬਲਕਿ ਸਮਾਜ ਦੇ ਹਰ ਹਿੱਸੇ ਵਿੱਚੋਂ ਆ ਰਹੇ ਹਨ। ਸੋਸ਼ਲ ਮੀਡੀਆ 'ਤੇ, ਪਾਰਟੀਆਂ ਦੇ ਬੁਲਾਰਿਆਂ ਤੋਂ ਲੈ ਕੇ ਵੱਟਸਐਪ ਗਰੁੱਪ ਦੇ ਰਿਸ਼ਤੇਦਾਰਾਂ ਵਿਚਕਾਰ ਹਿੰਦੂ-ਮੁਸਲਮਾਨ ਤਕਰਾਰ ਨਾਲ ਜੁੜੇ ਮੁੱਦਿਆਂ 'ਤੇ ਬਹਿਸ ਅਤੇ ਵਿਵਾਦ ਲਗਾਤਾਰ ਜਾਰੀ ਹੈ। ਕਦੇ ਧਰਮ-ਸੰਸਦ ਦੇ ਨਾਮ 'ਤੇ, ਤਾਂ ਕਦੇ ਭੜਕਾਊ ਭਾਸ਼ਣ ਦੇ ਕੇ, ਕਦੇ ਮਾਸ ਦੀਆਂ ਦੁਕਾਨਾਂ ਨੂੰ ਲੈ ਕੇ, ਕਦੇ ਪਾਰਕ-ਮਾਲ ਵਿੱਚ ਨਮਾਜ਼ ਪੜ੍ਹਨ ਨੂੰ ਲੈ ਕੇ।'''
def test_tokenize_punjabi():
    res = sentence_tokenizer.tokenize(string_panjabi,language='pa')
    assert len(res) == 5

