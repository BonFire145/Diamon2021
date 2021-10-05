from flask import request

# 여러개의 패러미터를 받아오는 방향으로 진행할 것.

@app.route('/predict', method=['POST'])
def predict():
    params = json.loads(request.get_data(), encoding='UTF-8')
    print('json.loads: {}'.format(params))
    if len(params) == 0:
        return 'Parameter Error! (Some Data is 0-length)'

    params_str = ''
    for key in params.keys():
        params_str += 'key: {}, value {}<br>'.format(key, params[key])
    print('params_str {}'.format(params_str))
    return params_str
