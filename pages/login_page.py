

from typing import Self


class login ():

    def __init__(self, driver):
        self.driver = driver

    UserID = "//input[@id='strUsrAlias']"
    DealerCode = "//input[@id='strDealerID']"
    Password = "//tbody/tr[3]/td[3]/input[2]"
    Submit = "//input[@id='loginId']"


def login(self, userid, dealercode, password):
    send_text(self.UserID, userid)
    send_text(self.DealerCode, dealercode)
    send_text(self.Password, password)
    click(self.Submit)
