'''
Python conversion of AdobeHDS.php written by K-S-V
    original is available at https://github.com/K-S-V/Scripts
    
Initially this is intended to be a 1-1 conversion
'''
import argparse
import os.path
from pickle import FALSE
from _pyio import open


parser = argparse.ArgumentParser(description='Download a HTTP Dynamic Stream resource.')

# Command line switches (equivalent to Accepted[0] in php script - help is built in)
parser.add_argument('--debug', action='store_true', default=False, help='show debug output')
parser.add_argument('--delete', action='store_true', default=False, help='delete fragments after processing')
parser.add_argument('--fproxy', action='store_true', default=False, help='force proxy for downloading of fragments')
parser.add_argument('--play', action='store_true', default=False, help='dump stream to stdout for piping to media player')
parser.add_argument('--rename', action='store_true', default=False, help='rename fragments sequentially before processing')
parser.add_argument('--update', action='store_true', default=False, help='update the script to current git version')

# Command line arguments (equivalent to Accepted[1] in php script)
parser.add_argument('--auth', type=str, default='', help='authentication string for fragment requests')
parser.add_argument('--duration', type=int, default=0, help='stop recording after specified number of seconds')
parser.add_argument('--filesize', type=int, default=0, help='split output file in chunks of specified size (MB)')
parser.add_argument('--fragments', type=str, default='', help='base filename for fragments')
parser.add_argument('--manifest', type=str, default='', help='manifest file for downloading of fragments')
parser.add_argument('--outdir', type=str, default='', help='destination folder for output file')
parser.add_argument('--outfile', type=str, default='', help='filename to use for output file')
parser.add_argument('--parallel', type=int, default=0, help='number of fragments to download simultaneously')
parser.add_argument('--proxy', type=str, default='', help='proxy for downloading of manifest')
parser.add_argument('--quality', type=str, default='', help='selected quality level (low|medium|high) or exact bitrate')
parser.add_argument('--referrer', type=str, default='', help='Referer to use for emulation of browser requests')
parser.add_argument('--start', type=int, default=0, help='start from specified fragment')
parser.add_argument('--useragent', type=str, default='', help='User-Agent to use for emulation of browser requests')



args = parser.parse_args()

# CLI class not needed, Python argParse handles it for us
class CLI:
    def displayHelp(self):
        print 'Hello world'

# 
class cURL:
    def headers(self):
        headerVal = []
        headerVal.append('Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        headerVal.append('Connection: Keep-Alive')
        headerVal.append('Content-Type: application/x-www-form-urlencoded;charset=UTF-8')
        
        return headerVal
    
    def cookie(self, cookie_file):
        if (os.path.exists(cookie_file)):
            self.cookie_file = cookie_file
        else:
            try:
                open(cookie_file, mode, buffering, encoding, errors, newline, closefd)
                self.cookie_file = cookie_file
            except IOError as ex:
            

class F4F:
    def InitDecoder(self):
        pass


print args.debug