import requests
from bs4 import BeautifulSoup

def floatChecker(i):
    try:
        float(i)
        return True
    except:
        return False

def bbc_scraper(bbcsoup):

    print("/// WEATHER SCRAPER ///\n")
    
    bbc_temp_low = 0
    bbc_temp_high = 0
    return_list = []
    
    for link in bbcsoup.find_all("a", {"id": "daylink-0"}):

        low_index = int(str(link.text).find("Low")) + 3
        if low_index == 2:
            bbc_temp_low = "N/A"
        else:
            bbc_temp_low = (str(link.text)[low_index])
            try:
                second_digit_low = int(str(link.text)[low_index+1])
                bbc_temp_low = bbc_temp_low + second_digit_low
            except:
                pass

        high_index = int(str(link.text).find("High")) + 4
        if high_index == 3:
            bbc_temp_high = "N/A"
        else:
            bbc_temp_high = (str(link.text)[high_index])
            try:
                second_digit_high = int(str(link.text)[high_index+1])
                bbc_temp_low = bbc_temp_low + second_digit_high
            except:
                pass
       
        print("BBC Low: " + bbc_temp_low + "\nBBC High: " + bbc_temp_high)

        return_list.append(bbc_temp_low)
        return_list.append(bbc_temp_high)
        return return_list

def met_scraper(metsoup):
    
    met_temp_reduced_high = ""
    met_temp_reduced_low = ""
    met_temp_list_high = []
    met_temp_list_low = []
    return_list = []

    for link in metsoup.find_all("span", {"class": "dayTemp"}):
        met_str_high_temp = str(link.text).replace("\n","")
        met_str_high_temp = met_str_high_temp.replace(" ","")
        if met_str_high_temp[1] != " " and met_str_high_temp[1] != "\n":
            met_temp_reduced_high = met_str_high_temp[0] + met_str_high_temp[1]
            met_temp_list_high.append(met_temp_reduced_high)
        else:
            met_temp_reduced_high = met_str_high_temp[0]
            met_temp_list_high.append(met_temp_reduced_high)

    for link in metsoup.find_all("span", {"class": "nightTemp"}):
        met_str_low_temp = str(link.text).replace("\n","")
        met_str_low_temp = met_str_low_temp.replace(" ","")
        if met_str_low_temp[1] != " ":
            met_temp_reduced_low = met_str_low_temp[0] + met_str_low_temp[1]
            met_temp_list_low.append(met_temp_reduced_low)
        else:
            met_temp_reduced_low = met_str_low_temp[0]
            met_temp_list_low.append(met_temp_reduced_low)
    
    print("\nMET Temperature Reading High: " + met_temp_list_high[0] + "\nMET Temperature Reading Low: " + met_temp_list_low[0])
    return_list.append(met_temp_list_high[0])
    return_list.append(met_temp_list_low[0])
    return return_list

#Place holder for the next weather site
#def new_scraper():

#----------------------------------------------------------------

def main():
    bbc_r = requests.get("https://www.bbc.co.uk/weather/2650628")
    bbcsoup = BeautifulSoup(bbc_r.content, "html.parser")
    met_s = requests.get("https://www.metoffice.gov.uk/public/weather/forecast/gcwzefp2c#?date=2018-10-27")
    metsoup = BeautifulSoup(met_s.content, "html.parser")

    all_temp = []

    for a in bbc_scraper(bbcsoup):
        all_temp.append(a)
    for a in met_scraper(metsoup):
        all_temp.append(a)

    average_temp = 0
    numbers_seen = 0

    for i in all_temp:
        if floatChecker(i):
            average_temp = average_temp + float(i)
            numbers_seen = numbers_seen + 1 
    average_temp = average_temp/numbers_seen

    print("Today's Average Temperature is: %.2f°C" % average_temp)

#These will trigger GPIO output when moved from the the terminal
    if average_temp >= 20.0:
        print("\nRed Light")
    elif average_temp < 20 and average_temp >= 17.5:
        print("\nOrange Light")
    elif average_temp < 17.5 and average_temp >= 15:
        print("\nOrange Light")
    elif average_temp < 15 and average_temp >= 12.5:
        print("\nOrange Light")
    elif average_temp < 12.5 and average_temp >= 10:
        print("\nOrange Light")
    elif average_temp < 10 and average_temp >= 7.5:
        print("\nOrange Light")
    elif average_temp < 7.5 and average_temp >= 5:
        print("\nOrange Light")
    elif average_temp < 5 and average_temp >= 2.5:
        print("\nOrange Light")
    elif average_temp < 2.5 and average_temp >= 0:
        print("\nOrange Light")
    else:
        print("\nYellow Light")

if __name__ == '__main__':
    main()

#Humidiy Check to-do
    
#This prints all the high temps for the week
    # if hightemp == "High":
    #   high_list.append(link.text[4])
#print(high_list)



