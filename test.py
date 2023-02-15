from ToolAutoFB import Login_2fa, Multi_process
import random
import json
import os
import time
from ultils import *
from threading import Thread
def autofb4multile(username, password, fa):
    #_______________________________
    print(frame("Login vào " + username, 1, 3))
    auto = Login_2fa(username=username, password=password, fa=fa)
    driver = auto.open_profile()
    code = auto.get_2facode()
    try:
        auto.login_2facode(code)
        time.sleep(5)
        driver.close()
    except:
        driver.close()
    
    
    

def main():
    acc_clones = [ '100087528783646|NhoamT7HeF28s|TDJWRSIRTHP4BB6ZXTJY57WOO5BHXTCA',
'100087370715950|NhosLGitiz2IZ|QEZ4QRR4H256QAWAXYZDQC5O7Y32FKIP',
'100087637812783|NhouLlDVM2UKF|II6A2B36TTFPSVQ2TC3VF6SGFS6W74HU']
    # auto = Multi_process(acc_clones=acc_clones, num_threads=2, action= autofb4multile)
    # auto.start_multi()
    
    threads = []
    session = []
    leng_session = (len(acc_clones) // 2) + 1 if len(acc_clones)%2 !=0 else len(acc_clones)/2
    print(leng_session)
    for _ in range(int(leng_session)):
        session.append(acc_clones[:2])
        acc_clones = acc_clones[2:]
        
    for list_acc_clone in session:
        for i in range(len(list_acc_clone)):
            username , password, fa = list_acc_clone[i].split("|")
            print(username, password, fa)
            threads.append(Thread(target=autofb4multile, args=(username,
                                                            password,fa,)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
if __name__ == "__main__":
    main()