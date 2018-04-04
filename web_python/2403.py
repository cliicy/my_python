'''
   try:
        file.open('web_content.txt')
    except:
        print('fail to open file web_content.txt')
        exit(-1)
    try:
        print('succeed to open file web_content.txt')
    finally:
        file.close()
'''

class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def do_something(self):
        bar=1/0
        return bar+10

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("In __exit__()")


def get_sample():
        return Sample()


class Sample2:
    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print
        "type:", type
        print
        "value:", value
        print
        "trace:", trace

    def do_something(self):
        bar = 1 / 0
        return bar + 10


class div:
    try:
        a=1/2
        print(a)
     #   print(m)
        b=1/0
        print(b)
        c=2/1
        print(c)
    except NameError:
        print('Ops')
    except ZeroDivisionError:
        print('Wrong math!')
    except:
        print('Error')

if __name__ == '__main__':
    print('start')
    with get_sample() as sample:
        print("sample:",sample)

    with Sample2() as sample2:
        sample2.do_something()