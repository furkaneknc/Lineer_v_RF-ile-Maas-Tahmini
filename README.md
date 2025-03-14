Maaş Tahmin Modeli
Bu projede, yaş, cinsiyet ve meslek bilgilerine dayanarak bir bireyin maaşını tahmin eden bir makine öğrenmesi modeli geliştirilmiştir. 
Model, Lineer Regresyon ve Karar Ağaçları (Random Forest Regressor) kullanılarak eğitilmiştir.

Özellikler:
Veri Ön İşleme:
Eksik veriler, gelir sütununun ortalaması ile doldurulmuştur.

Kategorik veriler (Cinsiyet, Meslek) Label Encoding yöntemiyle sayısal verilere dönüştürülmüştür.
Veriler, ölçeklendirilmiştir (StandardScaler).

Modeller:
Lineer Regresyon: Basit bir model, tahmin için temel bir yaklaşım sunar.
Random Forest Regressor: Karar ağaçlarının birleşiminden oluşan, daha karmaşık ve yüksek doğruluk sağlayan bir modeldir.

Kullanıcı Girişi:
Kullanıcı, yaşını, mesleğini ve cinsiyetini girerek maaş tahmini alabilir.


Kullanım:
Kullanıcıdan yaş, meslek ve cinsiyet bilgileri alınarak tahmin yapılabilir. 
Modelin doğruluk oranı hem Lineer Regresyon hem de Rastgele Orman modeliyle ölçülmüştür.

Gelecekteki İyileştirmeler:
Daha fazla özellik eklenerek modelin doğruluğu artırılabilir.
Farklı makine öğrenmesi algoritmaları denenebilir.
Veri kümesine daha fazla özellik eklenebilir (örneğin, eğitim durumu, deneyim süresi).
