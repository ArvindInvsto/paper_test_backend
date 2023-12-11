from express.brokerage.brokerageUtils.brokers import brokersObjs

class Brokerage():
    def __init__(self, broker_name):
        '''
        broker (str): name of the broker
        '''
        self.brokerName=broker_name

        # Creating brokers object
        self.broker=brokersObjs[broker_name]()

    def login(self,
     user_id = None,
     password = None,
     factor2 = None,
     api_key = None,
     vc = None,
     imei =None,
     api_secret =None,
     auth_code=None):
     
        '''
        Login to the brokers api
        
        user_id (str): user_id/client_id for finvasia and samco
        password (str): password for finvasia and samco
        factor2 (str): factor2/yob for finvasia and samco
        api_key (str): api_key/secret_key for binance and finvasia
        api_secret (str): api_secret for binance
        vc (str): vc for finvasia
        imei (str): imei for finvasia
        auth_code: auth_code for fyers
        '''

        # Checking for broker and logining in
        if self.brokerName=='finvasia':
            if user_id != None and password!=None and factor2 !=None and vc!=None and api_key!=None and imei!=None:
                ret=self.broker.login(userId=user_id, password=password, factor2=factor2, vc=vc, api_key=api_key, imei=imei)
                return ret
            else:
                print("Please provides the correct login parameters!")

        if self.brokerName=='paperbrokerage':
            if user_id != None and password!=None and factor2 !=None and vc!=None and api_key!=None and imei!=None:
                ret=self.broker.login(userId=user_id, password=password, factor2=factor2, vc=vc, api_key=api_key, imei=imei)
                return ret
            else:
                print("Please provides the correct login parameters!")

    def set_session(self, user_id, password, token):
        '''
        To generate new session

        user_id (str): user_id/client_id for finvasia and samco
        password (str): password for finvasia and samco
        token (str): session token
        '''

        ret=self.broker.set_session(user_id, password, token)
        return ret

    def get_accountdetails(self):
        '''
        Get the account details of the broker
        '''
        ret=self.broker.get_accountdetails()
        return ret


    def get_order_book(self, instrument=None):
        '''
        Get the order histry of the broker

        instrument: instrument for the binance
        '''

        if self.brokerName=='binance':
            if instrument!=None:
                ret=self.broker.get_order_book(instrument=instrument)
                return ret           
            else:
                print("Please provide the correct parameter")
        else:
            ret=self.broker.get_order_book()
            return ret

    def get_position_data(self):
        '''
        Get positions(for finvasia, fyers and samco)
        '''
        ret=self.broker.get_position_data()
        return ret

    def get_holdings(self):
        '''
        Get Holdings(for finvasia, fyers and samco)
        '''
        ret=self.broker.get_holdings()
        return ret

    def get_order_detail(self, orderNumber):
        '''
        get Order detail
        '''
        ret=self.broker.get_order_detail(orderNumber)
        return ret

    def place_market_order(self,
     instrument,
     order_side,
     qty,
     product_type=None,
     validity=None,
     variety=None,
     exchange=None):
        '''
        To place market order

        instrument (str): name of the instrument
        order_side (str): order side (BUY, SELL)
        qty (int) : number of qty
        product_type (str): type of product (CNC, NRML, MIS)
        validity (str): order validity (DAY, IOC)
        variety (str): order variety (REGULAR, AMO)
        exchange (str): name of the exchange (NSE, BSE, NFO)
        '''

        if product_type!=None and validity!=None and variety!=None and exchange!=None:
            ret=self.broker.place_market_order(
                instrument=instrument,
                exchange=exchange,
                order_side=order_side,
                product_type=product_type,
                qty=qty,
                validity=validity,
                variety=variety)
            return ret
        else:
            print("Please provide the correct parameter")

    def place_limit_order(self,
     instrument,
     order_side,
     limit_price,
     qty,
     product_type=None,
     validity=None,
     variety=None,
     exchange=None):
        '''
        To place Limit order

        instrument (str): name of the instrument
        order_side (str): order side (BUY, SELL)
        limit_price (int): limit price
        qty (int) : number of qty
        product_type (str): type of product (CNC, NRML, MIS)
        validity (str): order validity (DAY, IOC)
        variety (str): order variety (REGULAR, AMO)
        exchange (str): name of the exchange (NSE, BSE, NFO)
        '''
        if product_type!=None and validity!=None and variety!=None and exchange!=None:
            ret=self.broker.place_limit_order(
                instrument=instrument,
                exchange=exchange,
                order_side=order_side,
                limit_price=limit_price,
                product_type=product_type,
                qty=qty,
                validity=validity,
                variety=variety)
            return ret
        else:
            print("Please provide the correct parameter")

    def place_sl_market_order(self,
     instrument,
     exchange,
     order_side,
     trigger_price,
     qty,
     validity,
     variety,
     product_type):
        '''
        To place SL market order for finvasia, fyers and samco

        instrument (str): name of the instrument
        order_side (str): order side (BUY, SELL)
        trigger_price (int): trigger price
        qty (int) : number of qty
        product_type (str): type of product (CNC, NRML, MIS)
        validity (str): order validity (DAY, IOC)
        variety (str): order variety (REGULAR, AMO)
        exchange (str): name of the exchange (NSE, BSE, NFO)
        '''
        cond = (
            type(instrument) == str and
            order_side in ['BUY', 'SELL'] and
            type(trigger_price) == int and
            type(qty) == int and qty > 0 and
            exchange in ['NSE', 'BSE', 'NFO', "MCX"] and
            validity in ['DAY', 'IOC'] and
            variety in ['REGULAR', 'AMO'] and
            product_type in ['CNC', 'NRML', 'MIS']
        )

        if cond:
            ret=self.broker.place_sl_market_order(
                instrument=instrument,
                exchange=exchange,
                order_side=order_side,
                product_type=product_type,
                trigger_price=trigger_price,
                qty=qty,
                validity=validity,
                variety=variety)
            
            return ret
        else:
            print("Please provide the correct parameter")


    def place_sl_limit_order(self,
     instrument,
     exchange,
     order_side,
     trigger_price,
     trigger_limit_price,
     qty,
     validity,
     variety,
     product_type):
        '''
        To place SL limit order

        instrument (str): name of the instrument
        order_side (str): order side (BUY, SELL)
        trigger_price (int): trigger price
        trigger_limit_price (int): trigger limit price
        qty (int) : number of qty
        product_type (str): type of product (CNC, NRML, MIS)
        validity (str): order validity (DAY, IOC)
        variety (str): order variety (REGULAR, AMO)
        exchange (str): name of the exchange (NSE, BSE, NFO)
        '''
        cond = (
            type(instrument) == str and
            order_side in ['BUY', 'SELL'] and
            type(trigger_price) == int and
            type(trigger_limit_price) == int and
            exchange in ['NSE', 'BSE', 'NFO', "MCX"] and
            type(qty) == int and qty > 0 and
            validity in ['DAY', 'IOC'] and
            variety in ['REGULAR', 'AMO'] and
            product_type in ['CNC', 'NRML', 'MIS']
        )

        if cond:
            ret=self.broker.place_sl_limit_order(
                instrument=instrument,
                exchange=exchange,
                order_side=order_side,
                product_type=product_type,
                trigger_price=trigger_price,
                trigger_limit_price=trigger_limit_price,
                qty=qty,
                validity=validity,
                variety=variety)
            return ret
        else:
            print("Please provide the correct parameter")

    def place_bracket_order(self,
     instrument,
     exchange,
     order_side,
     limit_price,
     sl_limit_price,
     sl_limit_trigger_price,
     take_profit_price,
     qty,
     validity,
     variety,
     product_type):
        '''
        To place bracket order

        instrument (str): name of the instrument
        order_side (str): order side (BUY, SELL)
        limit_price (int): limit price
        sl_limit_price (int): SL Limit price
        sl_limit_trigger_price (int): SL Limit trigger price
        take_profit_price (int): take profit price
        qty (int) : number of qty
        product_type (str): type of product (CNC, NRML, MIS)
        validity (str): order validity (DAY, IOC)
        variety (str): order variety (REGULAR, AMO)
        exchange (str): name of the exchange (NSE, BSE, NFO)

        return (tuple): (orderOne, orderTwo, orderThree)
        '''       
        cond = (
            type(instrument) == str and
            order_side in ['BUY', 'SELL'] and
            exchange in ['NSE', 'BSE', 'NFO', "MCX"] and
            type(limit_price) == int and
            type(sl_limit_price) == int and
            type(sl_limit_trigger_price) == int and
            type(take_profit_price) == int and
            type(qty) == int and qty > 0 and
            validity in ['DAY', 'IOC'] and
            variety in ['REGULAR', 'AMO'] and
            product_type in ['CNC', 'NRML', 'MIS']
        )

        # Placing order using class methods
        if cond:
            if order_side == 'BUY':

                orderOne=self.place_limit_order(
                    instrument=instrument,
                    exchange=exchange,
                    order_side='BUY',
                    qty=qty,
                    validity=validity,
                    variety=variety,
                    product_type=product_type,
                    limit_price=limit_price)

                OrderTwo=self.place_sl_limit_order(
                    instrument=instrument,
                    exchange=exchange,
                    order_side='SELL',
                    trigger_price=sl_limit_trigger_price,
                    trigger_limit_price=sl_limit_price,
                    qty=qty,
                    validity=validity,
                    variety=variety,
                    product_type=product_type)

                OrderThree=self.place_limit_order(
                    instrument=instrument,
                    exchange=exchange,
                    order_side='SELL',
                    qty=qty,
                    validity=validity,
                    variety=variety,
                    product_type=product_type,
                    limit_price=limit_price)

                return(orderOne, orderTwo, OrderThree)

            elif order_side == 'SELL':
                
                orderOne=self.place_limit_order( 
                    instrument=instrument,
                    exchange=exchange,
                    order_side='SELL',
                    qty=qty,
                    validity=validity,
                    variety=variety,
                    product_type=product_type,
                    limit_price=limit_price)

                orderTwo=self.place_sl_limit_order(
                    instrument=instrument,
                    exchange=exchange,
                    order_side='BUY',
                    trigger_price=sl_limit_trigger_price,
                    trigger_limit_price=sl_limit_price,
                    qty=qty,
                    validity=validity,
                    variety=variety,
                    product_type=product_type)

                orderThree=self.place_limit_order(
                    instrument=instrument,
                    exchange=exchange,
                    order_side='BUY',
                    qty=qty,
                    validity=validity,
                    variety=variety,
                    product_type=product_type,
                    limit_price=limit_price)
                
                return(orderOne, orderTwo, OrderThree)

        else:
            print("Please provide the correct parameter")

    def position_squareOff(self, orderno, product_type=None):
        '''
        Position squareOff for fyers

        orderno (str): order no
        product_type(str): product_type for finvasia
        '''
        cond = (orderno != None)
        if cond:
            if self.brokerName=='finvasia':
                ret=self.broker.position_squareOff(orderno=orderno, product_type=product_type)
            else:
                ret=self.broker.position_squareOff(id=orderno)
            return ret
        else:
            print("Please provide the correct parameter")

    def modify_order(self, 
        instrument, 
        exchange, 
        orderno, 
        newqty, 
        newprice_type, 
        newprice, 
        newtrigger_price=None):
        '''
        Modify Order

        instrument (str): name of the instrument
        exchange (str): name of the exchange
        orderno (str): order Number
        newprice (int): new price
        newtrigger_price (int): new trigger price for stoploss
        newprice_type (str): price type (MKT, SL-MKT, SL-LMT)
        newqty (int) : number of qty
        '''

        cond = (
            type(instrument) == str and
            exchange in ['NSE', 'BSE', 'NFO', "MCX"] and
            type(orderno) == str and
            type(newprice) == int and
            type(newtrigger_price) == int and
            type(newprice_type) == str and
            type(newqty) == int and newqty > 0 )

        if cond:
            ret=self.broker.modify_order(exchange=exchange, tradingsymbol=instrument,
                orderno=orderno, newquantity=newqty,
                newprice_type=newprice_type, newprice=newprice)
            
            return ret
        else:
            print("Please provide the correct parameter")


    def cancel_order(self, orderno):
        '''
        Cancel Order

        orderno (str): order no
        '''
        cond = (orderno != None)
        if cond:
            ret=self.broker.cancel_order(orderno=orderno)
            return ret
        else:
            print("Please provide the correct parameter")