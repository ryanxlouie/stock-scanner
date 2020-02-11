def bbandSignal(bbandData, dailyData, currentDate):
    middleBand = bbandData.loc[currentDate[0]]['Real Middle Band']
    lowerBand = bbandData.loc[currentDate[0]]['Real Lower Band']
    halfWay = (middleBand - lowerBand)/2
    # if (dailyData.loc[currentDate[0]]['1. open'] <= lowerBand+halfWay) and (dailyData.loc[currentDate[0]]['4. close'] < middleBand) and (dailyData.loc[currentDate[0]]['1. open'] < dailyData.loc[currentDate[0]]['4. close']):
    if (dailyData.loc[currentDate[0]]['1. open'] <= middleBand) and (dailyData.loc[currentDate[0]]['4. close'] < middleBand) and (dailyData.loc[currentDate[0]]['1. open'] < dailyData.loc[currentDate[0]]['4. close']):
        return(1)
    else:
        return(0)

def nineThirtyCrossover(emaData, wmaData, currentDate):
    if emaData.loc[currentDate[0]]['EMA'] < wmaData.loc[currentDate[0]]['WMA'] and emaData.loc[currentDate[1]]['EMA'] > wmaData.loc[currentDate[1]]['WMA']:
        return(1)
    else:
        return(0)

def fourRedsMACD(macdData, currentDate):
    now = macdData.loc[currentDate[0]]['MACD_Hist']
    if (now < 0):
        dm1 = macdData.loc[currentDate[1]]['MACD_Hist']
        dm2 = macdData.loc[currentDate[2]]['MACD_Hist']
        dm3 = macdData.loc[currentDate[3]]['MACD_Hist']
        dm4 = macdData.loc[currentDate[4]]['MACD_Hist']
        dm5 = macdData.loc[currentDate[5]]['MACD_Hist']
        if (now > dm1) and (dm1 < dm2) and (dm2 < dm3) and (dm3 < dm4) and (dm4 < dm5):
            return(1)
        else:
            return(0)
    else:
        return(0)

def diSignal(plusDIData, minusDIData, currentDate):
    if (plusDIData.loc[currentDate[1]]['PLUS_DI'] < plusDIData.loc[currentDate[0]]['PLUS_DI'] and minusDIData.loc[currentDate[1]]['MINUS_DI'] > minusDIData.loc[currentDate[0]]['MINUS_DI']):
        return(1)
    else:
        return(0)