# twitch-hls-vods
This script allows for one to retrieve the m3u8 file from Twitch's api.  Using 
this with ffmpeg to interpret said m3u8 file, you can download a VOD from 
twitch that has been streamed through HLS protocol

As of right now, this tool only works on VODs that have been streamed as HLS.  
You can tell which streams are through HLS by looking at the URL of the VOD
which should have a `/v/`

ex. `http://www.twitch.tv/nycfurby/v/5118926`

## Usage

If we use the above url as an example, here's an example of a command

`python download_m3u8.py -v 5118926 -q source`

The `-v` option specifices the video id of video you wish to download.  The 
`-q` option determines the quality of the option.  There's generally only 
source, high, medium, low, and mobile that are available.

The script will output a m3u8 file by the name of `{video_id}_{source}.m3u8`

## FFMPEG
It's worth noting that the FFMPEG command line program is able to take a M3U8 
file as a value for its input (-i) parameter, which will automatically download
 and concatenate the pieces together if, for example, run like this

`ffmpeg -i "input.m3u8" -c copy output.ts`

If all you want to do is upload to youtube, this should be more than enough.  Of
 course since it's ffmpeg, you can do alot more such as change the file type to 
 `mp4` and whatnot