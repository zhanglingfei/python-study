import re

def transferContent(content):
    string = ""
    for c in content:
        if c == '"':
            string += '\\\"'
        elif c == "'":
            string += "\\\'"
        elif c == "\\":
            string += "\\\\"
        else:
            string += c

    return string




def main():
    content=''' hello "" '' '''
    print(transferContent(content))

    print(re.escape(content))

if __name__ == '__main__':
    # when run in test_run mode, use python brand_monitor_service.py --test_run
    main()