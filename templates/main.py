import sys
input = sys.stdin.readline

def readint():
    return(int(input()))

def readlist():
    return(list(input().split()))

def readstring():
    return(input().strip())

def readintlist():
    return(list(map(int, input().split())))

def readstringlist():
    return(input().split())

def solve():
    pass

def main():
    t = readint()
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
