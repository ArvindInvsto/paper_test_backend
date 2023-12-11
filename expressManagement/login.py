from express.brokerage import Brokerage
from credentialManagement import saveToken


def loginPaper(brokerage):
    bro = Brokerage(broker_name=brokerage)
    return bro

def loginExpress(cred):
    # Broker Object
    bro=Brokerage(broker_name=cred.brokerage)
    if cred.token==None:
        # Login
        ret = {}
        if cred.brokerage == "paperbrokerage":
            # user = paperAuth(brokerage_user_id=cred.brokerage_user_id, password=cred.password,
            #     factor2=cred.factor2, vc=cred.vc,
            #     api_key=cred.api_key, imei=cred.imei)
            # if not user["exists"]:
            # ret=bro.login(user_id=cred.brokerage_user_id, password=cred.password, factor2=cred.factor2, vc=cred.vc, api_key=cred.api_key, imei=cred.imei)
            pass
        else:
            ret=bro.login(user_id=cred.brokerage_user_id, password=cred.password,
                factor2=cred.factor2, vc=cred.vc,
                api_key=cred.api_key, imei=cred.imei)
        # Save Token
        token=ret['token']
        saveToken(brokerage_user_id=cred.brokerage_user_id, token=token)
        
    elif (cred.token)!=None:
        # Set Session
        token=cred.token
        ret=bro.set_session(user_id=cred.brokerage_user_id, password=cred.password, token=token)
        # If error in set session
        if ret==None:
            # Login
            if cred.brokerage == "paperbrokerage":
                # user = paperAuth(user_id=cred.brokerage_user_id, password=cred.password,
                # factor2=cred.factor2, vc=cred.vc,
                # api_key=cred.api_key, imei=cred.imei)
                # # if not user["exists"]:
                # ret=bro.login(user_id=cred.brokerage_user_id, password=cred.password,
                # factor2=cred.factor2, vc=cred.vc,
                # api_key=cred.api_key, imei=cred.imei)
                pass
            else:
                ret=bro.login(user_id=cred.brokerage_setting_id, password=cred.password,
                    factor2=cred.factor2, vc=cred.vc,
                    api_key=cred.api_key, imei=cred.imei)
            # Save Token
            token=ret['token']
            saveToken(brokerage_user_id=cred.brokerage_user_id, token=token)
    print("brokerage login: ",bro)
    print("token: ", token)
    return bro