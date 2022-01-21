import traceback

try:
    raise Exception('This is catz paw wilding on you for your naughty')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Traceback info was saved in error_log.txt')
