import os
import datetime

class LOG:
    def __init__(self,file):
        #-------
        self.dir = file
        self.file = os.path.basename(file)
        self.YEAR = datetime.date.today().strftime("%Y")
        self.MONTH = datetime.date.today().strftime("%m")
        self.TODAY = datetime.date.today().strftime("%d")
        self.DATE = self.YEAR + "年" + self.MONTH + "月" + self.TODAY + "日"
        self.TIME = datetime.datetime.today().strftime("%H:%M:%S")
        self.log_text = "..\\LOG\\" + self.DATE + ".log"
        self.msg_num = 0
        self.msg_info = 0
        self.msg_err = 0
        self.msg_chk = 0
        #-------
        os.chdir(os.path.dirname(self.dir))
        if(os.path.isfile(self.log_text)):
            with open(self.log_text, mode='a') as f:
                logtext_msg = "LOG: " + self.TIME + ":" + str(self.file) + "よりログの出力が開始されます。\n"
                f.write(logtext_msg)
        else:
            with open(self.log_text, mode='w') as f:
                logtext_msg = "START: " + self.DATE + "の貴方の失敗と活動をお知らせします。\n"
                logtext_msg += "LOG: " + self.TIME + ":" + str(self.file) + "よりログの出力が開始されます。\n"
                f.write(logtext_msg)

    def msg(self, err_msg, type = 1):
        os.chdir(os.path.dirname(self.dir))
        self.TIME = datetime.datetime.today().strftime("%H:%M:%S")
        self.msg_num += 1
        self.msg_chk += 1
        self.err_msg = err_msg
        system_msg = ""
        time_msg = self.TIME + ", " +self.file + ", " + str(self.msg_num) +", "
        if(type==1):
            system_msg += time_msg
            system_msg += "[chk-" + str(self.msg_chk) + "], " + str(self.err_msg) + "\n"
        elif(type==2):
            system_msg += time_msg
            system_msg += "[chk-" + str(self.msg_chk) + "], " + str(self.err_msg) + "\n"
        else:
            self.msg_err += 1
            system_msg += time_msg
            system_msg += "[info-" + str(self.msg_num) + "] ,予期せぬエラーが起きている可能性があります。関連箇所を確認して下さい。\n"
        with open(self.log_text, mode='a') as f:
            f.write(system_msg)

    def err(self, err_msg):
        os.chdir(os.path.dirname(self.dir))
        self.TIME = datetime.datetime.today().strftime("%H:%M:%S")
        self.msg_num += 1
        self.err_msg = err_msg
        self.msg_err += 1
        time_msg = self.TIME + ", " +self.file + ", " + str(self.msg_num) +", "
        system_msg = time_msg
        system_msg += "[err-" + str(self.msg_err) + "]," + str(self.err_msg) + "\n"
        with open(self.log_text, mode='a') as f:
            f.write(system_msg)

    def info(self, err_msg):
        os.chdir(os.path.dirname(self.dir))
        self.TIME = datetime.datetime.today().strftime("%H:%M:%S")
        self.msg_num += 1
        self.err_msg = err_msg
        self.msg_info += 1
        time_msg = self.TIME + ", " +self.file + ", " + str(self.msg_num) +", "
        system_msg = time_msg
        system_msg += "[info-" + str(self.msg_err) + "], " + str(self.err_msg) + "\n"
        with open(self.log_text, mode='a') as f:
            f.write(system_msg)

    def SQL(self, err_msg):
        os.chdir(os.path.dirname(self.dir))
        self.TIME = datetime.datetime.today().strftime("%H:%M:%S")
        self.msg_num += 1
        self.err_msg = err_msg
        self.msg_info += 1
        time_msg = self.TIME + ", " +self.file + ", " + str(self.msg_num) +", "
        system_msg = time_msg
        system_msg += '[SQL:次のSQL文が実行ファイルにて実行]\n' 
        system_msg += str(self.err_msg) + "\n"
        with open(self.log_text, mode='a') as f:
            f.write(system_msg)
