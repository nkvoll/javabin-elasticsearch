import json
import requests

sessions_url = 'http://2014.javazone.no/api/sessions'

with open('sessions.bulk.json', 'w') as bulk_out:
    sessions = requests.get(sessions_url).json()
    print 'read {} sessions'.format(len(sessions))
    for session in sessions:
        details_url = None
        for link in session['links']:
            if link['rel'] == 'details':
                details_url = link['uri']
                break
        else:
            continue
        details = requests.get(details_url).json()
        session_id = details_url.split('/')[-1]
        bulk_out.write(json.dumps(dict(index=dict(_index='javazone',
_type='session', _id=session_id))))
        bulk_out.write('\r\n')
        bulk_out.write(json.dumps(details))
        bulk_out.write('\r\n')
        print 'wrote {}'.format(session_id)
