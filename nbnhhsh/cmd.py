import sys
import argparse

from nbnhhsh import suo

def main():
    parser = argparse.ArgumentParser(description="一个转换缩写的工具")
    parser.add_argument("text")
    parser.parse_args()
    text = parser.parse_args().text
    print(suo(text))

if __name__ == '__main__':
    main()
