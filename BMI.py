from pip._vendor.distlib.compat import raw_input
import datetime

date = datetime.date.today()


print("Ile ważysz?\n")
masa=(raw_input())
masa = masa.replace(",",".")
masa = float(masa)
print("Ile masz wzrostu w cm")
wzrost=int(raw_input())
wzrost_w_m = float(wzrost/100)
print("\n")
BMI = masa/((wzrost_w_m)**2)
print("BMI=", BMI )

plik = open(r'C:\Users\Bartek\Desktop\BMI\BMI.txt','a')

plik.write("\n")
plik.write(str(date)+" | "+str(BMI))
#plik.write(str(BMI))
plik.close()










