import tkinter as tk
import requests
from bs4 import BeautifulSoup as BS

city_check = {
    #  key: value
    'питер': 'sankt-peterburge',
    'москва': 'moskve',
    'шри - ланка': 'shryakh-dzhayavardenepure-kotte',
    'шри-ланка': 'shryakh-dzhayavardenepure-kotte',
    'шри -ланка': 'shryakh-dzhayavardenepure-kotte',
    'шриланка': 'shryakh-dzhayavardenepure-kotte',
    'новосибирск': 'novosibirske',
    'казань': 'kazani',
    'красноярск': 'krasnoyarske',
    'минск': 'minske',
    'лондон': 'londone/velikobritaniya',
    'нижний новгород': 'nizhnem-novgorode',
    'рим': 'rimini',
    'омск': 'omske',
    'Дубай': 'dubae',
    'анталья': 'antale',
    'Барселона': 'barselone',
    '': '',
}

def weather_checker():
    value = city_request.get()

    url = f'https://weather.rambler.ru/v-{city_check[value]}/now/?updated'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')

    information = soup.find('div', class_='RkHg').text
    degrees = soup.find('div', class_='HhSR GyfK').text
    wind = soup.find('span', class_='VaOz d2qU').text
    pressure = soup.find('div', class_='hjtR pressure HbwD aT_0').find('span', class_='VaOz d2qU').text
    moon_phase = soup.find('div', class_='hjtR HbwD aT_0').find('span', class_='VaOz d2qU').text
    sensation_of_temperature = soup.find('span', class_='_VDA ypY4 MMaW').text
    date = soup.find('div', class_='O6uR').text

    label2 = tk.Label(root, text=f'{information} -  {degrees}', background='#add8e6', font=('Arial', 18, 'bold'))
    label2.grid()

    label3 = tk.Label(root, text=f'Date - {date}', background='#add8e6', font=('Arial', 18, 'bold'))
    label3.grid()

    label4 = tk.Label(root, text=f'{wind}', background='#add8e6', font=('Arial', 18, 'bold'))
    label4.grid()

    label5 = tk.Label(root, text=f'{pressure}', background='#add8e6', font=('Arial', 18, 'bold'))
    label5.grid()

    label6 = tk.Label(root, text=f'{moon_phase}', background='#add8e6', font=('Arial', 18, 'bold'))
    label6.grid()

    label7 = tk.Label(root, text=f'{sensation_of_temperature}', background='#add8e6', font=('Arial', 18, 'bold'))
    label7.grid()

    label7 = tk.Label(root, text='---------------------------------', background='#add8e6', font=('Arial', 18, 'bold'))
    label7.grid()


root = tk.Tk()

logo = tk.PhotoImage(file='logo.png')
root.iconphoto(False, logo)
root.config(bg='#add8e6')
root.resizable(True, True)
root.title('WeatherChecker')
root.geometry('800x500+700+280')

tk.Label(root, text='Введите название города:').grid(row=0, column=0, stick='w')
city_request = tk.Entry(root)
city_request.grid(row=0, column=1)
root.grid_columnconfigure(0, minsize=100)
root.grid_columnconfigure(1, minsize=100)

button1 = tk.Button(root, text='Take information', command=weather_checker)
button1.grid()

root.mainloop()






