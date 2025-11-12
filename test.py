class Test:
    def test(self, str):
        # for s in str:
        #     print(ord(s))
        val = sum([ord(s) for s in str])
        print(val)

if __name__ == '__main__':
    s = Test()
    s.test("abc")
