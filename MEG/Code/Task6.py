import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------- Calculate W(t) -------------------------------------------------

# TODO: Define the periodic function w(t) as specified
# تعریف تابع متناوب w(t) بر اساس فرمول داده شده
def w_func(t):
    # Sin() در مسئله با حروف بزرگ نوشته شده که معمولاً به معنی sin() است.
    term1 = 120 * np.sin(8 * np.pi * t)
    term2 = 45 * np.sin(14 * np.pi * t)
    term3 = 30 * np.sin(20 * np.pi * t)
    term4 = 15 * np.sin(40 * np.pi * t)
    term5 = 5 * np.sin(80 * np.pi * t)
    return term1 + term2 + term3 + term4 + term5

# TODO: Create a time vector with 1000 samples over 1 second
# صورت مسئله ۱ ثانیه داده با فرکانس ۱۰۰۰ هرتز خواسته است.
# (توجه: نمودار در فایل PDF برای ۲ ثانیه است، اما ما طبق متن عمل می‌کنیم)
t = np.linspace(0, 1, 1000, endpoint=False)

# TODO: Calculate w(t) values for each time point
# محاسبه مقادیر تابع w(t) در هر نقطه از زمان
w_values = w_func(t)


# ----------------------------- Calculate radial component of magnetic flux density for sensor 30  -------------------------------

# TODO: Load the lead field matrix (or the calculated field from Task 5)
# بارگذاری فایل ذخیره شده از تسک ۵ که حاوی میدان شعاعی برای هر سنسور است
try:
    data = np.load("MEG_Single_Dipole_Field.npz")
    # این آرایه حاوی میدان شعاعی در هر یک از ۳۳ سنسور برای دوقطبی واحد است
    Br_all_sensors = data['Br']
    # ما فقط به مقدار مربوط به سنسور شماره ۳۰ (اندیس ۲۹) نیاز داریم
    G_sensor30 = Br_all_sensors[29]
except FileNotFoundError:
    print("خطا: فایل MEG_Single_Dipole_Field.npz یافت نشد. لطفاً ابتدا تسک ۵ را اجرا کنید.")
    # مقداردهی یک مقدار پیش‌فرض برای جلوگیری از خطا در ادامه
    G_sensor30 = 1e-15 


# TODO: Define the dipole orientation vector
# این بردارها در محاسبه G_sensor30 در تسک ۵ استفاده شده‌اند و اینجا فقط برای کامل بودن ذکر می‌شوند
q = np.array([0, 0, 1])
# q1 = ... # این متغیر در مسئله تعریف نشده و نیازی به آن نیست

# TODO: Calculate the constant magnetic field at sensor 30
# این میدان ثابت، همان مقدار میدان-راهنما برای سنسور ۳۰ است (میدان برای دوقطبی با قدرت ۱)
B_r = G_sensor30

# TODO: Calculate the time-varying magnetic field at sensor 30
# میدان متغیر با زمان از ضرب مقدار ثابت میدان-راهنما در تابع متغیر w(t) به دست می‌آید
B_r_new = G_sensor30 * w_values


# -------------------------------------  Visiualize MEG Sensor Number 30 ------------------------------------------
# Plot
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(13, 7))

ax1.plot(t, w_values, label=r'w(t)', color='r')
ax1.set_title('Plot of w(t)')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Magnitude w(t)')
ax1.legend()
ax1.grid(True)

# Plot B_r
# برای نمایش خط ثابت، یک آرایه با طول t و مقدار ثابت B_r ایجاد می‌کنیم
ax2.plot(t, np.full(t.shape, B_r), label=r'B_r (constant)')
ax2.set_title('Constant Magnetic Field at Sensor #30')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('B (T)')
ax2.legend()
ax2.grid(True)


# Plot B_r_new
ax3.plot(t, B_r_new, label=r'B_r_new (time-varying)')
ax3.set_title('Time-Varying Magnetic Field at Sensor #30')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('B (T)')
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.show()


