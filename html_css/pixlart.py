# from PIL import Image

# # فتح الصورة
# img = Image.open("logo.png")

# # تقليل الحجم إلى عدد صغير من البكسلات
# small = img.resize((32, 32), resample=Image.NEAREST)

# # تكبيرها مرة ثانية لتظهر البكسلات بوضوح
# pixel_art = small.resize(img.size, Image.NEAREST)

# # حفظ النتيجة
# pixel_art.save("pixel_art.png")

# --------------------------------------------------------

from PIL import Image

# فتح الصورة الأصلية
img = Image.open(r"C:\Users\roaas\Downloads\IMG_20231119_140709.jpg")

# ⿡ تقليل الحجم (عدد البكسلات)
small = img.resize((64, 64), resample=Image.NEAREST)

# ⿢ تقليل عدد الألوان (مثلاً إلى 32 لون فقط)
small = small.convert("P", palette=Image.ADAPTIVE, colors=32)

# ⿣ تكبير الصورة مرة ثانية إلى حجمها الأصلي بالبكسلات الكبيرة
pixel_art = small.resize(img.size, Image.NEAREST)

# ⿤ حفظ النتيجة
pixel_art.save("pixel_art.png")

print("✅ تم إنشاء صورة Pixel Art جميلة باسم pixel_art.png")

# ---------------------------------------------------------------

# from PIL import Image

# # فتح الصورة الأصلية
# img = Image.open(r"C:\Users\roaas\Downloads\IMG-20210205-WA0009.jpg").convert("RGBA")

# # 🔹 تحديد اللون الذي سنعتبره "خلفية"
# # (نأخذ لون أول بكسل في الصورة عادةً)
# bg_color = img.getpixel((0, 0))

# # 🔹 تحويل البكسلات الشفافة
# datas = img.getdata()
# new_data = []
# for item in datas:
#     # إذا كان لون البكسل قريبًا من لون الخلفية، نجعله شفافًا
#     if abs(item[0]-bg_color[0]) < 20 and abs(item[1]-bg_color[1]) < 20 and abs(item[2]-bg_color[2]) < 20:
#         new_data.append((255, 255, 255, 0))  # شفاف
#     else:
#         new_data.append(item)

# img.putdata(new_data)

# # ⿡ تقليل الحجم إلى شكل بيكسل
# small = img.resize((16, 16), resample=Image.NEAREST)

# # ⿢ تقليل عدد الألوان (اختياري — يعطي مظهر 8bit)
# small = small.convert("P", palette=Image.ADAPTIVE, colors=32)

# # ⿣ تكبير الصورة مرة أخرى بنفس الأسلوب
# pixel_art = small.resize((img.width * 2, img.height * 2), Image.NEAREST)

# # ⿤ حفظ النتيجة بصيغة تدعم الشفافية (PNG)
# pixel_art.save("pixel_art_transparent.png", format="PNG")

# print("✅ Done Pixel Art file name is pixel_art_transparent.png")