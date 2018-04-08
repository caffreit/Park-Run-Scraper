import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np


option= webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path="C:\Users\Administrator\Documents\Python Scripts\chromedriver", chrome_options=option)

mala_data = np.zeros((1,11))


for i in range(2):
    run_num = i+1
    browser.get("http://www.parkrun.ie/malahide/results/weeklyresults/?runSeqNumber="+str(run_num))
    a = browser.page_source
    
    soup = BeautifulSoup(a,"html.parser")
    
    table = soup.find("table")
    
    rows = table.findAll("tr")
    text_data = []
    for tr in rows:
        cols = tr.findAll("td")
        for td in cols:
            text_data.append(td.get_text())
            
    labels = ["Position", "Name", "Time", "Age_Cat", "Age_Grade", "Gender", "Gen_Pos", "Club", "Note", "Total_Runs", "blank" ]
    myarray = np.asarray(text_data)
    data = myarray.reshape(-1,11)
    
    mala_data = np.vstack((mala_data,data))


df = pd.DataFrame(mala_data, columns = labels)

browser.close()

df.to_csv('parkscrape.csv', encoding='utf-8')
