import csv
import urllib2
import urlparse

import os.path

class Media:
  
    def __init__(self, line_info):
        (ext_media, _not_used, info) = line_info.partition(':')
        line_reader = csv.reader(info.splitlines(1))
        dict = {}
        for row in line_reader:
            for info in row:
                if info:
                    qualifier , value = info.split('=')
                    value = value.strip('"')
                    dict[qualifier] = value
          
        self.type = dict['TYPE']
        self.group_id = dict['GROUP-ID']
        self.name = dict['NAME']
        self.auto_select = dict['AUTOSELECT']
        self.default = dict['DEFAULT']
    
class Stream:

    def __init__(self, line_info):
        (ext_media, _not_used, info) = line_info.partition(':')
        line_reader = csv.reader(info.splitlines(1), quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        dict = {}
        for row in line_reader:
            for info in row:
                tuple = info.split('=')
                if len(tuple) > 1:
                    qualifier, value = tuple
                    value = value.strip('"')
                    dict[qualifier] = value
          
        self.program_id = dict['PROGRAM-ID']
        self.bandwidth = dict['BANDWIDTH']
        self.codecs = dict['CODECS']
        self.video = dict['VIDEO']

class VideoStream:
  
    def __init__(self, line_1, line_2, line_3):
        self.media = Media(line_1)
        self.stream = Stream(line_2)
        self.m3u8_url = line_3
        
    def get_m3u8(self):
        return urllib2.urlopen(self.m3u8_url)
        
    def get_base_url(self):
        url = self.m3u8_url
        parsed_url = urlparse.urlparse(url)
        path = os.path.split(parsed_url.path)
        base_url = '%s://%s/%s/' % (parsed_url.scheme, parsed_url.netloc, path[0])
        
        return base_url
    
def parse(file_name):
    file = open(file_name)
    header = file.readline() # Just get rid of header since it's useless

    file_true = True
    video_streams = []
    while file_true:
        line_1 = file.readline()
        line_2 = file.readline()
        line_3 = file.readline()
        if line_1 and line_2 and line_3:
            video_streams.append(VideoStream(line_1, line_2, line_3))
        else:
            file_true = False

    return video_streams

def get_video_stream(video_streams, quality):
    for video_stream in video_streams:
        if video_stream.media.name.lower() == quality.lower():
            return video_stream
            
    # should be throwing an exception here
    return null