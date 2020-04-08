import sys
# parser = argparse.ArgumentParser()
# parser.add_argument('--test_run', action='store_true')
# args = parser.parse_args()
# test_run = args.test_run
# print (test_run)
# if test_run:
#     print('test run!')
# else:
#     print('production run!')
# exit(0) means a clean exit without any errors / problems

try:
    sys.exit(1)
except:
    print('there is failure and airflow exit code is 1')
finally:
   print('finall')
   sys.exit(1)
