
# استفاده از نسخه سبک پایتون
FROM python:3.11-slim

# نصب کتابخانه‌های سیستمی که Playwright بهشون نیاز داره
RUN apt-get update && \
    apt-get install -y wget gnupg curl libnss3 libatk-bridge2.0-0 libxkbcommon0 libgtk-3-0 libasound2 && \
    rm -rf /var/lib/apt/lists/*

# کپی و نصب کتابخانه‌های پایتون که در requirements.txt لیست شدن
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# دانلود و نصب مرورگر Chromium برای Playwright
# با تنظیم این متغیر، مرورگرها در مسیر مشخصی نصب می‌شن تا خطای "Executable doesn't exist" رخ نده [citation:2][citation:9][citation:10]
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
RUN python -m playwright install --with-deps chromium

# کپی کردن تمام کدهای پروژه به داخل کانتینر
WORKDIR /opt/render/project/src
COPY . .

# پورتی که اپلیکیشن شما روش اجرا میشه (Render این رو به طور خودکار تنظیم میکنه)
EXPOSE 10000

# دستور اجرای اپلیکیشن شما (مثال برای FastAPI)
# اگر فریمورک دیگه‌ای مثل Flask دارید، این بخش رو تغییر بدید
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
