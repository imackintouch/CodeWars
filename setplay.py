import os

def set_transform(output_data):
    output_list = output_data[:-1].split('\n') # Strip off the trailing \n as this is useles data
    return set([os.path.abspath(d) for d in output_list])    # Collapse any multiple slashes.

def main():
    # output_list = ['/bin//foo', '/foo//bar', '/foo/foo/bar']
    output_data = '/bin//foo\n/foo//bar\n/foo/foo/bar\n'
    output_set=set_transform(output_data)
    print(output_set)
    for s in output_set:
        print(s)

if __name__ == '__main__':
    main()