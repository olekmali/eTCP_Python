""" uPython for ESP* parse URL library """

""" (C)2018 DrAM http://olek.matthewm.com.pl/
    - MIT License
    - use at your own risk
    - nothing guaranteed
    - give due credits respectively
"""

def parse_url(request):
    values = {}
    try:        # if request.find{'?')>=0:
        file, params = request.split('?', 1)
        if params.find('&')>=0:
            for x in params.split('&'):
                k, v = x.split('=', 1)
                values[k] = v
        else:
            k, v = params.split('=', 1)
            values[k] = v
    except:     # else:
        file   = request
        params = ''
        values = {}
    # print('url_lib debug: ', file, params, values)
    return(file, values)