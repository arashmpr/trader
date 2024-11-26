import talib as ta

class TechnicalAnalysis:
    def set_data(self, data):
        self.data = data
    
    def compute(self):
        self._add_macd()
        return self.data
    
    def _add_macd(self):
        macd, macd_signal, macd_hist = ta.MACD(self.data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

        self.data['MACD'] = macd
        self.data['MACD_Signal'] = macd_signal
        self.data['MACD_Hist'] = macd_hist

        self.data['MACD_Trade_Signal'] = 0 #neutral
        self.data['MACD_Trade_Signal'][macd > macd_signal] = 1
        self.data['MACD_Trade_Signal'][macd < macd_signal] = -1
