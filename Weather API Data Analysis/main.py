# تحلیل داده‌های API (دریافت دمای ساعت به ساعت از Open-Meteo)

# وارد کردن کتابخانه مورد نیاز برای ارسال درخواست HTTP
import requests

# تابعی برای دریافت داده‌های دمایی از API Open-Meteo
def get_weather_data(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    try:
        # ارسال درخواست به API
        response = requests.get(url)
        
        # بررسی کد وضعیت پاسخ
        if response.status_code == 200:
            # بازگشت داده‌ها به صورت JSON
            return response.json()
        else:
            print(f"Error: Status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# تابعی برای نمایش داده‌های دما
def display_weather_data(weather_data):
    if weather_data:
        # استخراج داده‌های دما
        hourly_temperatures = weather_data['hourly']['temperature_2m']
        
        print("\nHourly Temperature Data:")
        for hour, temp in enumerate(hourly_temperatures):
            print(f"Hour {hour}: {temp}°C")
    else:
        print("Error retrieving weather data.")

# مختصات جغرافیایی تهران
latitude = 35.6944
longitude = 51.4215

# دریافت داده‌های دمایی
weather_data = get_weather_data(latitude, longitude)

# نمایش داده‌های دما
display_weather_data(weather_data)
