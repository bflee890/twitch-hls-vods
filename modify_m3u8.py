def correct_m3u8(m3u8_file, url, file_output):
    file = open(file_output, 'w')

    for line in m3u8_file:
        if line[0] != '#':
            file.write(url + line)
        else:
            file.write(line)
        
    m3u8_file.close()
    file.close()