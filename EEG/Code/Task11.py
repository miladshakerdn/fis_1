import numpy as np
import matplotlib.pyplot as plt

# ---------------------------- Calculate W(t) ---------------------------
# TODO: Define the periodic function w(t) as specified
def w_func(t):
    """
    Calculates the value of the time-varying function w(t).
    """
    term1 = 120 * np.sin(8 * np.pi * t)
    term2 = 45 * np.sin(14 * np.pi * t)
    term3 = 30 * np.sin(20 * np.pi * t)
    term4 = 15 * np.sin(40 * np.pi * t)
    term5 = 5 * np.sin(80 * np.pi * t)
    return term1 + term2 + term3 + term4 + term5

# TODO: Create a time vector with 1000 samples over 2 seconds
# ایجاد بردار زمان برای ۲ ثانیه با فرکانس نمونه‌برداری ۱۰۰۰ هرتز (۲۰۰۰ نمونه)
t = np.linspace(0, 2, 2000, endpoint=False)

# TODO: Calculate w(t) values for each time point
# محاسبه مقادیر تابع w(t) در تمام نقاط زمانی
w_values = w_func(t)

# -------------- Calculate the time-varying potential at sensor 30  ------------
# TODO: Load the lead field matrix (or the potential vector from Task 10)
try:
    # بارگذاری فایل ذخیره شده از تسک ۱۰ که حاوی پتانسیل برای هر سنسور است
    data = np.load("EEG_Single_Dipole_Potential.npz")
    # این آرایه حاوی پتانسیل در هر یک از ۳۳ سنسور برای دوقطبی با قدرت واحد است
    L = data['V'] 
except FileNotFoundError:
    print("خطا: فایل EEG_Single_Dipole_Potential.npz یافت نشد. لطفاً ابتدا تسک ۱۰ را اجرا کنید.")
    # مقداردهی مقادیر پیش‌فرض برای جلوگیری از خطا در اجرای کد
    L = np.zeros(33)
    L[29] = 1e-6 # یک مقدار کوچک برای سنسور ۳۰

# TODO: Define the dipole orientation vector (informational)
# این متغیرها در این مرحله مستقیماً استفاده نمی‌شوند چون اثر آنها در L لحاظ شده است
# q = ...
# q1 = ...

# TODO: Calculate the constant electric potential at sensor 30
# پتانسیل ثابت در سنسور ۳۰ (اندیس ۲۹) همان مقدار میدان-راهنما است
V = L[29]

# TODO: Calculate the time-varying electric potential at sensor 30
# پتانسیل متغیر با زمان از ضرب مقدار ثابت در تابع متغیر w(t) به دست می‌آید
V_new = V * w_values


# -------------------------------------  Visiualize EEG Sensor Number 30 ------------------------------------------
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(13, 7))

# Plot w(t)
ax1.plot(t, w_values, label=r'w(t)', color='r')
ax1.set_title('Plot of w(t)')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Magnitude w(t)')
ax1.legend()
ax1.grid(True)

# Plot V (Constant Potential)
ax2.plot(t, np.full(t.shape, (V)), label=r'V (constant)')
ax2.set_title('Constant Potential at Sensor #30')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Voltage (V)')
ax2.legend()
ax2.grid(True)

# Plot V_new (Time-Varying Potential)
ax3.plot(t, V_new, label=r'V_new (time-varying)')
ax3.set_title('Time-Varying Potential at Sensor #30')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Voltage (V)')
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.show()