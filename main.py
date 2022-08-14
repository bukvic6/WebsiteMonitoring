import time
import hashlib
import smtplib


from urllib.request import urlopen, Request


url = Request('https://www.decathlon.rs/disk-tegovi/7278-8967-teg-od-livenog-gvozda-28-mm.html#/demodelcolor-1042303/demodelsize-2325_kg?queryID=3a0a346b7ab1d5d5584fcdd9d9e5f297&objectID=969885',headers={'User-Agent': 'Mozilla/5.0'})

response = urlopen(url).read()

curHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(10)
while True:
    try:
        response = urlopen(url).read()
        
        curHash = hashlib.sha224(response).hexdigest()
        
        time.sleep(30)
        
        response = urlopen(url).read()

        newHash = hashlib.sha224(response).hexdigest()
        
        if newHash == curHash:
            continue
    
        else:            
            try:
                to = 'bukvic6@gmail.com'
                me = 'bukvic6@gmail.com'
                passv = 'pass'
                email = smtplib.SMTP("smtp.gmail.com",587)
                email.ehlo()
                email.starttls()
                email.ehlo()
                email.login(me,passv)
                header = 'To:' + to + '\n' + 'From: ' + me + '\n' + 'Subject:Decathlon \n'
                print(header)
                msg = header + '\n Dumbbell has arrived!!\n\n'

                
                email.sendmail(to,me,msg)
                print("done")
            except Exception as e:
                print(e)
            finally:
                email.quit()

            response = urlopen(url).read()
            curHash = hashlib.sha224(response).hexdigest()
            time.sleep(30)
            continue
    
    except Exception as e:
        print("error")






