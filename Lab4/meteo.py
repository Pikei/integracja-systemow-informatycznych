import csv
import matplotlib.pyplot as plt
import requests


def meteo():
    weather_codes = {
        0: "czyste niebo",
        1: "głównie bezchmurnie",
        2: "częściowo pochmurno",
        3: "pochmurno",
        45: "mgła",
        48: "opadająca mgła szronowa",
        51: "mżawka lekka",
        53: "mżawka umiarkowana",
        55: "mżawka gęsta",
        56: "zamrażająca mżawka: lekka",
        57: "zamrażająca mżawka: gęsta intensywność",
        61: "deszcz słaby",
        63: "deszcz umiarkowany",
        65: "deszcz intensywny",
        66: "marznący deszcz: intensywność lekka",
        67: "marznący deszcz: intensywność ciężka",
        71: "opady śniegu: intensywność niewielka",
        73: "opady śniegu: intensywność umiarkowana",
        75: "opady śniegu: intensywność duża",
        77: "ziarna śniegu",
        80: "przelotne opady deszczu: słabe",
        81: "przelotne opady deszczu: umiarkowane",
        82: "przelotne opady deszczu: gwałtowne",
        85: "opady śniegu lekkie",
        86: "opady śniegu intensywne",
        95: "burza: Słaba lub umiarkowana",
        96: "burza z lekkim gradem",
        99: "burza z silnym gradem",
    }

    coordinates = {
        "Gdańsk": ("52.52", "13.41"),
    }

    place = "Gdańsk"
    weather_url = (f"https://api.open-meteo.com/v1/forecast"
                   f"?latitude={coordinates[place][0]}&longitude={coordinates[place][1]}"
                   f"&hourly=temperature_2m,rain,weather_code")

    # You can check data in the browser:
    print(f"Pogoda dla m. {place}: {weather_url}\n")
    gdansk_weather = requests.get(weather_url).json()

    # Pogoda na 7 dób - 168 wartości
    for key, value in gdansk_weather.items():
        if key != 'hourly':
            print(f"{key}: {value} \n")
        else:
            for key1, value1 in value.items():
                if key1 == 'time':
                    time = value1
                elif key1 == 'temperature_2m':
                    temperature = value1
                elif key1 == 'rain':
                    rain = value1
                elif key1 == 'weather_code':
                    weather = value1
                print(f"{key1}: {value1} \n")

            with open('Lab4/weather.csv', 'w', newline='', encoding='UTF8') as csvfile:
                fieldnames = ["Time", "Temperature[°C]", "Rain", "Overall"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for i in range(0, len(time)):
                    writer.writerow({
                        "Time":str(time[i]),
                        "Temperature[°C]":str(temperature[i]),
                        "Rain":str((int)((float)(rain[i])*100))+"%",
                        "Overall":str(weather_codes.get(weather[i]))}
                    )

    today = []
    temp = []
    hour = str(time[0])
    todaysDate = str(time[0][0:10])
    for i in range(0, len(time)):
        today.append(time[i][11::])
        temp.append(temperature[i])
        hour = str(time[i])
        if "23:00" in hour:
            today.append(time[i][11::])
            # today.append(time[i+1][11::])
            temp.append(temperature[i])
            # temp.append(temperature[i+1])
            break

    plt.figure(figsize=(11, 11))
    plt.plot(today,temp)
    plt.title(f"Temperature for:{todaysDate}")
    plt.xlabel("Time hourly for 7 days")
    plt.ylabel("Temperature[°C]")
    plt.xticks(rotation=90)
    plt.autoscale()
    plt.savefig("Forecast.png")
    plt.show()