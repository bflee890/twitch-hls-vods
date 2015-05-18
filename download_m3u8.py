import hls_parser
import twitch_file_parser
import modify_m3u8
import sys, getopt

def main(argv):
    vod_id = 0
    quality = 'source'
    output = -1
    try:
        opts, args = getopt.getopt(argv,"hv:q:",["vod_id=", "quality="])
    except getopt.GetoptError:
        print 'download_m3u8.py -v <video_id>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'download_m3u8.py -v <video_id>'
            sys.exit()
        elif opt in ("-v", "--vod_file"):
            vod_id = arg
        elif opt in ("-q", "--quality"):
            quality = arg

    output = vod_id + '_' + quality + ".m3u8"
    
    file_name = hls_parser.get_twitch_file(vod_id)
    video_streams = twitch_file_parser.parse(file_name)
    video_stream = twitch_file_parser.get_video_stream(video_streams, quality)
    m3u8_file = video_stream.get_m3u8()
    
    base_url = video_stream.get_base_url()
    modify_m3u8.correct_m3u8(m3u8_file, base_url, output)
    
    
if __name__ == "__main__":
    main(sys.argv[1:])