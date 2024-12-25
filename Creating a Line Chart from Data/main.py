# ایجاد نمودار خطی از داده‌ها

import matplotlib.pyplot as plt

# داده‌ها
years = [2010, 2011, 2012, 2013, 2014, 2015]
population = [2.5, 2.7, 3.0, 3.4, 3.6, 4.0]

# رسم نمودار خطی
plt.plot(years, population, marker='o', linestyle='-', color='green')

# تنظیمات نمودار
plt.title("Population Growth Over Years")
plt.xlabel("Year")
plt.ylabel("Population (in millions)")

# نمایش نمودار
plt.show()
