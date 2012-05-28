#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Wrapper which operates "ssgnc", Google N-gram search system
"""

__author__ = 'Yuta Hayashibe' 
__version__ = ""
__copyright__ = ""
__license__ = "GPL v3"


import subprocess

ORDER_OPTION = { "FLAG" : "--ssgnc-order",
                "UNORDERED" : "UNORDERED",
                "ORDERED" : "ORDERED",
                "PHRASE" : "PHRASE",
                "FIXED" : "FIXED",
                "DEFAULT" : "FIXED" }
RESULTS_OPTION = { "FLAG" : "--ssgnc-max-num-results",
                "DEFAULT" : "20" }
FLEQ_OPTION = { "FLAG" : "--ssgnc-min-freq",
                "DEFAULT" : "0" }
NGRAM_OPTION = { "FLAG" : "--ssgnc-num-tokens",
                "DEFAULT" : "1-7" }


class Ssgnc(object):
    def __init__(self, bin, index, option = [ORDER_OPTION['FLAG'], ORDER_OPTION['DEFAULT']]):
        assert isinstance(bin, unicode)
        assert isinstance(index, unicode)
        assert isinstance(option, (list, tuple))
        args = [bin, index] + option
        subproc_args = { 'stdin': subprocess.PIPE,
                         'stdout': subprocess.PIPE,
                         'stderr': subprocess.STDOUT,  # not subprocess.PIPE
                         'cwd': '.',
                         'close_fds' : True,          }
        try:
            self.p = subprocess.Popen(args, **subproc_args)
        except OSError:
            raise 
        (self.stdouterr, self.stdin) = (self.p.stdout, self.p.stdin)

    def __del__(self):
        self.p.stdin.close() #send EOF (This is not obligate)
        try:
            self.p.kill()
            self.p.wait()
        except OSError:
            # can't kill a dead proc
            pass

    def search(self, string):
        if type(string) is unicode:
            string = string.encode('utf_8')
        assert isinstance(string, str)
        self.p.stdin.write(string + '\r\n')
          
        result = []
        while True:
            line = self.stdouterr.readline()
            if not line.strip():
                break
            result.append(line.split())
            result[-1][-1] = int(result[-1][-1])
        return result
        
        
    def get_frequency(self, words):
        if type(words) is unicode:
            words = words.encode('utf_8')
        assert isinstance(words, str)

        l = self.search(words)
        if len(l)==0:
            return 0
        else:
            return l[0][-1]
        
        
if __name__ == '__main__':
    import corrcha.tool.setting
    BIN_PATH = corrcha.tool.setting.val['ssgnc']['bin']
    INDEX_PATH = corrcha.tool.setting.val['ssgnc']['index']

    import sys
    arglis = sys.argv[1:]
    ssgnc = Ssgnc(BIN_PATH, INDEX_PATH)
    
    while True:
        string = raw_input("Input query: ")
        
        if len(string)==0 :
            sys.exit()
        print ssgnc.get_frequency(string)


