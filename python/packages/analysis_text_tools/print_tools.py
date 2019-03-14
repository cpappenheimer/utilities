import os
import subprocess as sb
import sys


def getGitRepoVersion(absPathToGitRepo):
    gitFilePath = os.path.abspath(os.path.join(absPathToGitRepo, ".git"))
    getGitRepoVersionCmd = ("git --git-dir " + str(gitFilePath) + " log --pretty=\"%H\" -n1").split()
    return sb.check_output(getGitRepoVersionCmd).strip()
# end getGitRepoVersion


def printErr(msg):
    sys.stderr.write("\033[91m" + msg + "\033[0m")
# end printErr


def printWarning(msg):
    sys.stderr.write("\033[33m" + msg + "\033[0m")
# end printErr


def latexToROOTLATEX(s):
    rootStr = s.replace(r'$', '')
    rootStr = rootStr.replace(r'\mathcal', '') # TLatex doesn't have /mathcal implemented
    rootStr = rootStr.replace(r'\Re', 'Re') # TLatex doesn't have /Re and /Im implemented
    rootStr = rootStr.replace(r'\Im', 'Im')
    rootStr = rootStr.replace(r'\left(', '(') # the big parentheses look really weird and pixellated
    rootStr = rootStr.replace(r'\right)', ')') 
    rootStr = rootStr.replace(r'\mathrm', '#it') # no \mathrm in TLatex
    return rootStr.replace('\\', r'#') # must be last
# end latexToROOTFormat
