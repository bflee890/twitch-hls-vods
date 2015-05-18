import json
import urllib2

def get_twitch_file(vod_id):
    api_base = 'https://api.twitch.tv/api/vods/'
    usher_url_base = 'http://usher.twitch.tv/vod/'
    file_name = vod_id
    
    api_url = api_base + '%s/access_token' % (vod_id)
    response = urllib2.urlopen(api_url)
    access_token_json_blob = response.read()
    access_token = json.loads(access_token_json_blob)
   
    token = access_token['token']
    sig = access_token['sig']
    usher_url = usher_url_base + '%s?nauthsig=%s&nauth=%s' % (vod_id, sig, token)
    
    m3u_holder_file = urllib2.urlopen(usher_url)
   
    file_ = open(file_name, 'w')
    file_.write(m3u_holder_file.read())
    file_.close()
   
    m3u_holder_file.close()
    
    return file_name