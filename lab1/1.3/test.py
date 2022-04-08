import locale

cur_locale = locale.getlocale()

#locale.setlocale(locale.LC_NUMERIC, "es_ES")
locale.setlocale(locale.LC_NUMERIC, cur_locale)

num1 = "1,5"
num2 = "1.500,2"
num3 = "-1,5"
num4 = "-1.5"

print(locale.delocalize(num1))
print(locale.delocalize(num2))
print(locale.delocalize(num3))
print(locale.delocalize(num4))

print(float(""))