# Packages
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import time

from config import *
import CustomTechIndicators

ti = TechIndicators(key='', output_format='pandas')
ts = TimeSeries(key='', output_format='pandas')

apiCalls = 0

##
bbandDataAll = []
for a in range (0, len(companyArray)):
    if (apiCalls == 5):
        print('Sleeping... BBand')
        time.sleep(60)
        apiCalls = 0
    bbandData, meta_data = ti.get_bbands(symbol=companyArray[a], interval='daily', time_period='20', series_type='close', nbdevup=2, nbdevdn=2, matype=0)
    bbandDataAll.append(bbandData)
    apiCalls += 1

##
emaDataAll = []
for a in range (0, len(companyArray)):
    if (apiCalls == 5):
        print('Sleeping... EMA')
        time.sleep(60)
        apiCalls = 0
    emaData, meta_data = ti.get_ema(symbol=companyArray[a], interval='daily', time_period='9', series_type='close')
    emaDataAll.append(emaData)
    apiCalls += 1

##
wmaDataAll = []
for a in range (0, len(companyArray)):
    if (apiCalls == 5):
        print('Sleeping... WMA')
        time.sleep(60)
        apiCalls = 0
    wmaData, meta_data = ti.get_wma(symbol=companyArray[a], interval='daily', time_period='30', series_type='close')
    wmaDataAll.append(wmaData)
    apiCalls += 1

##
macdDataAll = []
for a in range (0, len(companyArray)):
    if (apiCalls == 5):
        print('Sleeping... MACD')
        time.sleep(60)
        apiCalls = 0
    macdData, meta_data = ti.get_macd(symbol=companyArray[a], interval='daily', series_type='close')
    macdDataAll.append(macdData)
    apiCalls += 1

# plusDIData, meta_data = ti.get_plus_di(symbol=companyString, interval='daily', time_period='14')
# minusDIData, meta_data = ti.get_minus_di(symbol=companyString, interval='daily', time_period='14')

##
dailyDataAll = []
for a in range (0, len(companyArray)):
    if (apiCalls == 5):
        print('Sleeping... Daily Data')
        time.sleep(60)
        apiCalls = 0
    dailyData, meta_data = ts.get_daily(symbol=companyArray[a], outputsize='full')
    dailyDataAll.append(dailyData)
    apiCalls += 1

dateArray = dailyData.index.values
maxDateIndex = len(dateArray)

startDateIndex = maxDateIndex - startDay
endDateIndex = maxDateIndex - endDay
totalHits = 0

lastNineThirtyCrossover = []
for a in range(0, len(companyArray)):
    lastNineThirtyCrossover.append(100)

# firstTrigger = 100

for a in range(startDateIndex, endDateIndex):
    currentDate = [dateArray[a], dateArray[a-1], dateArray[a-2], dateArray[a-3], dateArray[a-4], dateArray[a-5], dateArray[a-6]]

    for b in range(0, len(companyArray)):
        bbandStatus = CustomTechIndicators.bbandSignal(bbandDataAll[b], dailyDataAll[b], currentDate)
        nineThirtyCrossoverStatus = CustomTechIndicators.nineThirtyCrossover(emaDataAll[b], wmaDataAll[b], currentDate)
        fourRedsMACDStatus = CustomTechIndicators.fourRedsMACD(macdDataAll[b], currentDate)
        if (nineThirtyCrossoverStatus == 1):
            lastNineThirtyCrossover[b] = 0
        if (fourRedsMACDStatus == 1) and (lastNineThirtyCrossover[b] <= 7) and (bbandStatus == 1):
            print(currentDate[0] + ' ' + companyArray[b])
            totalHits += 1
        lastNineThirtyCrossover[b] += 1

print('Start and End Dates')
print(dateArray[startDateIndex])
print(dateArray[endDateIndex-1])
print(totalHits)


## CODE FOR DI
# print(companyString)
# for a in range(startDateIndex, endDateIndex):
#     currentDate = [dateArray[a], dateArray[a-1], dateArray[a-2], dateArray[a-3], dateArray[a-4], dateArray[a-5], dateArray[a-6]]

#     if firstTrigger == 100:
#         bbandStatus = CustomTechIndicators.bbandSignal(bbandData, dailyData, currentDate)
#         nineThirtyCrossoverStatus = CustomTechIndicators.nineThirtyCrossover(emaData, wmaData, currentDate)
#         fourRedsMACDStatus = CustomTechIndicators.fourRedsMACD(macdData, currentDate)
#         if (nineThirtyCrossoverStatus == 1):
#             lastNineThirtyCrossover = 0
    
#         if (fourRedsMACDStatus == 1 and lastNineThirtyCrossover <= 7 and bbandStatus == 1):
#             firstTrigger = 0
#         lastNineThirtyCrossover += 1

#     if firstTrigger != 100:
#         diStatus = CustomTechIndicators.diSignal(plusDIData, minusDIData, currentDate)

#         if (diStatus == 1):
#             print(currentDate[0])
#             firstTrigger = 99
#         elif (firstTrigger == 10):
#             firstTrigger = 99
#         firstTrigger += 1
