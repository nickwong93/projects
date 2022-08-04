import pandas as pd
import numpy as np

data = pd.read_csv ('E:/00 NMQ Digital/AMEA Report/Week30/product_report_all_locales_31_07_2022_18_05.csv')

df = pd.DataFrame(data, columns = [
	'Locale', 
	'Step Id', 
	'Name (For SM or Model or SKU)', 
	'Type', 
	'Main or Child Product', 
	'GWT Live Status (Explanation)', 
	'Available In Store Date', 
	'Effective Sunrise Date (CADC + CLPC)', 
	'Permalink Live'
	])

###### To remove the unwanted content from Instore date and Sunrise date column #####
df['Available In Store Date'] = df['Available In Store Date'].str.slice(start=0, stop=10,step=1)

df['Effective Sunrise Date (CADC + CLPC)'] = df['Effective Sunrise Date (CADC + CLPC)'].str.slice(start=0, stop=10,step=1)

###### To filter AMEA locales only #####
AMEA = ['ar_XX', 'en_AP', 'en_AU', 'en_EG', 'en_ID', 'en_MY', 'en_NZ', 'en_PH', 'en_SG', 'en_TH', 'en_TW', 'en_XX', 'en_ZA', 'fr_XX', 'id_ID', 'ko_KR', 'pt_XX', 'ru_XX', 'th_TH', 'vi_VN', 'zh_TW']

#### .isin means to only include the locales that are in the AMEA list above. ####
df = df[df['Locale'].isin(AMEA)]


#### Change the In-store date and Sunrise Date based on the week that we are checking ####
in_store_start_date = df ['Available In Store Date'] >= "2022-07-25"
in_store_end_date = df ['Available In Store Date'] <= "2022-07-31"
impacted_instore_period = in_store_start_date & in_store_end_date

sunrise_start_date = df ['Effective Sunrise Date (CADC + CLPC)'] >= "2022-07-25"
sunrise_end_date = df ['Effective Sunrise Date (CADC + CLPC)'] <= "2022-07-31"
impacted_sunrise_period = sunrise_start_date & sunrise_end_date

####################################################
df = df.loc[impacted_instore_period | impacted_sunrise_period]

# def colouring_date(d):
# 	if d >= "2020-06-29" and  d <= "2020-07-05":
# 		color = 'red'
# 	return 'color: %s' % color

# df.style.apply(colouring_date, subset=['Available In Store Date','Effective Sunrise Date (CADC + CLPC)'])

#### Export output to Excel, index = False so that there is no indexing included ####
df.to_excel(r'E:/00 NMQ Digital/AMEA Report/Week30/AMEA Weekly Launch Report_Week30.xlsx', index = False)
