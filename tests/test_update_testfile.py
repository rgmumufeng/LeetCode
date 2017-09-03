from solutions.leetcodelib import update_testfile

def test_update_testfile():
    import shutil, os
    shutil.copyfile('testfile.bak', 'testfile.yaml')
    arguments = [('apple', ['app', 'le']), ('aaa', ['a', 'b']), ('pearape', ['p', 'e', 'a'])]
    answers = [[0], [], [0, 4]]
    update_testfile('testfile.yaml', "s, words", arguments, answers, 'add', [2])
    
    os.remove('testfile_init.yaml')
    update_testfile('testfile_init.yaml', "s, words", arguments, answers, 'generate')

if __name__ == "__main__":
    test_update_testfile()