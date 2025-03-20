from telegram import Bot
import random
import json
import os
from datetime import datetime, timedelta
import time
import sys

# 1️⃣ توکن ربات و آیدی چت
TOKEN = "7949579672:AAGIdlRny3HrIVnGBCpJKhen5FLKXvV499o"
CHAT_ID = "5227052757"

# 2️⃣ مسیر فایل ذخیره‌سازی پیام‌ها
STATE_FILE = "messages_state.json"

# 3️⃣ لیست پیام‌ها (هر کدوم یک بار در چرخه ارسال می‌شه)
messages = [
    "دوستت دارم مبینا ❤️",
    "و خیلی خوشگلی ❤️",
    "باور دارم که فوق العاده‌ای ❤️",
    "تو خوشگل‌ترین و خوش‌قلب‌ترین دختر دنیایی ❤️",
    "عاشقتم مبینا ❤️",
    "خیلی خواستنی‌ای مبین ❤️",
    "واقعا خوشگلی امروز ❤️",
    "مبینا تو ماه کاملی ❤️",
    "خیلی دوستت دارم با همه‌ی قلبم ❤️",
    "همه‌ی آرزومی دخترم ❤️",
    "با بهترین آرزوها برای امروزت ❤️",
    "قشنگ‌ترین چشمای کل دنیا رو داری ❤️",
    "عاشق تک تک جزئیات صورت ماهتم ❤️",
    "با همه‌ی قلبم عاشقتم مبینا ❤️",
    "امروز واقعا بینهایت خوشگلی ❤️",
    "اونقد خوشگلی که دلم می‌خواد محو صورت ماهت بشم ❤️",
    "یادت نره واقعا خوشگلی ❤️"
]

# 4️⃣ تابع ارسال پیام
def send_message(text):
    bot.send_message(chat_id=CHAT_ID, text=text)
    print(f"پیام ارسال شد: {text}")

# 5️⃣ بارگذاری حالت از فایل
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as file:
            return json.load(file)
    return {"remaining": [], "used": []}

# 6️⃣ ذخیره‌سازی حالت به فایل
def save_state(state):
    with open(STATE_FILE, "w") as file:
        json.dump(state, file)

# 7️⃣ انتخاب پیام تصادفی از لیست
def get_random_message(state):
    if not state["remaining"]:
        state["remaining"] = messages[:]
        random.shuffle(state["remaining"])
        state["used"] = []

    message = state["remaining"].pop(0)
    state["used"].append(message)
    save_state(state)
    return message

# 8️⃣ محاسبه زمان تصادفی بین ۶ تا ۱۰ صبح
def get_random_time():
    hour = random.randint(6, 9)  # ساعت تصادفی بین ۶ تا ۹
    minute = random.randint(0, 59)  # دقیقه تصادفی
    return hour, minute

# 9️⃣ محاسبه مدت زمان انتظار تا زمان تصادفی
def wait_until_target_time(target_hour, target_minute):
    now = datetime.now()
    target_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
    if now > target_time:
        target_time += timedelta(days=1)
    wait_seconds = (target_time - now).total_seconds()
    print(f"انتظار تا ساعت {target_hour:02d}:{target_minute:02d} ({int(wait_seconds)} ثانیه)...")
    time.sleep(wait_seconds)

# 🔟 اجرای ربات
bot = Bot(token=TOKEN)
state = load_state()

# دریافت زمان تصادفی
hour, minute = get_random_time()
print(f"زمان انتخاب شده: {hour:02d}:{minute:02d}")
wait_until_target_time(hour, minute)

# ارسال پیام تصادفی
message = get_random_message(state)
send_message(message)

print("ربات خاموش شد.")
sys.exit()
