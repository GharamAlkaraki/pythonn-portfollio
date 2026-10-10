# int_research.py
# Researching which string formats can be converted using int() in Python.
#Documentation Source: https://docs.python.org/3/builtins/stdtypes.html#numeric-types-int-float-complex

#تنجح , لأن بايثون يتجاهل تلقائياً المسافات الفارغة  المحيطة بالنص قبل التحويل.
print (int(" 22 "),type(int(" 22 ")))
# تنجح لأن علامة الموجب + تعتبر إشارة رياضية مقبولة لتحديد الأعداد الموجبة
print (int("+22"),type(int("+22")))
# تنجح لأن علامة الموجب + تعتبر إشارة رياضية مقبولة لتحديد الأعداد الموجبة
print (int("0022"),type(int("0022")))
# تنجح لأن الشرطة السفلية _ تُستخدم في بايثون كمحدد اختياري لقراءة الأرقام الكبيرة بشكل أسهل وتُحذف عند التحويل.
print (int("2_2"),type(int("2_2")))
