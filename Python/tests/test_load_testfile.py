from leetcodelib import load_testfile

def test_load_testfile():
    import glob, os
    if True:
        testfile = 'testfile.yaml'
        #testfile = 'hello'
    #for testfile in glob.glob('../*.yaml'):
        arg_orders, arguments, answers = load_testfile(testfile)
        print os.path.basename(testfile)
        print 'argument orders: %s' % arg_orders
        for i in xrange(len(arguments)):
            print 'Case %d:' % i
            for j in xrange(len(arg_orders)):
                print "{}: {}".format(arg_orders[j], arguments[i][j])
            print "answer: {}".format(answers[i])
        print
    print "Test load_testfile finished."

if __name__ == "__main__":
    test_load_testfile()
