def test(number):

            print('---test---')
            def test_in(num):
                        print('---test_in---')
                        num += number
                        return num

            return test_in

result = test(100)
print(result(100))


