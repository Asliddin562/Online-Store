🛒 Online Store API
Bu Django Rest Framework asosida yaratilgan online do‘kon API loyihasidir. Loyihada foydalanuvchi ro'yxatdan o'tadi, mahsulotlarni ko‘radi, savatga qo‘shadi va buyurtma beradi.

📦 Texnologiyalar
Python 3.11+
Django 4.x
Django REST Framework
PostgreSQL (yoki SQLite)
JWT Authentication
Docker (ixtiyoriy)
drf-spectacular (Swagger docs uchun)

🚀 Funksiyalar
✅ Ro'yxatdan o'tish / Login (telefon raqami orqali)
✅ Mahsulotlar ro‘yxati va filtrlash
✅ Savatchaga mahsulot qo‘shish / olib tashlash
✅ Buyurtma yaratish (Delivery / Pickup)
✅ JWT orqali autentifikatsiya
✅ Admin panel orqali mahsulot va buyurtmalarni boshqarish

🛠 O‘rnatish
git clone https://github.com/your-username/online-store-api.git
cd online-store-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
