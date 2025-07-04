از خاطرات جوانی اسماعیل خان، می‌توان به درافتادن او با یک غولِ فیل‌صفت در جریان جنگ‌های چریکی سال ۱۹۷۸ اشاره کرد.

ماجرا از این قرار است که یک غول فیل‌صفت در خانه‌ی گوشه‌ی پایین سمت چپ یک صفحه‌ی شطرنج 
$8×8$ قرار دارد و می‌خواهد به خانه‌ی گوشه‌ی بالا سمت راست برود. سطرها را از پایین به بالا و ستون‌ها را از چپ به راست به ترتیب با اعداد ۱ تا ۸ شماره‌گذاری می‌کنیم. پس غول فیل‌صفت در خانه‌ی `(1,1)` قرار دارد و می‌خواهد به خانه‌ی `(8,8)` برود. همان‌طور که می‌دانید، غول‌های فیل‌صفت به صورت قطری حرکت می‌کند.

خانه‌ی اسماعیل در خانه‌ی `(8,8)` از صفحه‌ی شطرنج قرار دارد و اگر غول فیل‌صفت بتواند به خانه‌ی او برسد، روی آن نشسته و از آن‌جایی که غول است و سنگین، خانه خراب شده و اسماعیل خانه‌خراب می‌شود. از این رو اسماعیل می‌خواهد تعدادی از خانه‌های صفحه‌ی شطرنجی را ببندد تا غول فیل‌صفت نتواند به خانه‌ی اسماعیل برسد. غول نمی‌تواند به خانه‌های بسته شده برود یا حتی در مسیرش از آن‌ها رد شود. از طرفی چون اسماعیل تنبل است، می‌خواهد کمترین تعداد خانه را ببندد تا کمتر به زحمت بیفتد.

متاسفانه اسماعیل نمی‌داند که کدام خانه‌ها را باید ببندد تا به هدفش برسد؛ برای همین از شما کمک می‌خواهد. از طرفی سایر غول‌ها خانه‌ی `(x,y)` را در نظر گرفته‌اند و اگر اسماعیل بخواهد آن را ببندد، او را با شمشیر و جفتک لهِ له می‌کنند؛ پس اسماعیل نمی‌تواند خانه‌ی `(x,y)` را ببندد و شما باید موقع پیشنهاد دادن خانه‌ها، این را در نظر بگیرید؛ پس به این نکته دقت کنید که اسماعیل تمام خانه‌های صفحه‌ی شطرنج را می‌تواند ببندد، غیر از خانه‌ی `(1,1)`، `(8,8)` و خانه‌ی `(x,y)` که در ورودی به شما داده می‌شود.

### ورودی
در تنها سطر ورودی به ترتیب دو عدد $x$ و $y$ آمده است که مختصات خانه‌ای را از جدول نشان می‌دهد که اسماعیل نمی‌تواند آن را ببندد.

حداقل یکی از بین 
$x$ و $y$ برابر ۱ نیست و حداقل یکی از بین 
$x$ و $y$ برابر ۸ نیست.

### خروجی

خروجی بدین شکل است:
- در سطر اول خروجی باید یک عدد باشد که نمایانگر تعداد خانه‌هایی است که اسماعیل باید ببندد.
- سپس در سطر‌های بعدی، مختصات هر خانه را باید در دو خط نشان داد، به این صورت که شماره‌ی سطر خانه در خط اول و شماره‌ی ستون خانه در سطر دوم باشد.
مثال
ورودی نمونه ۱
```plaintext
4 4
```
خروجی نمونه ۱
```plaintext
1
7 7
```