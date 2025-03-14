import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler #mesleği ve yaşı 0-1 olarak degistirmek icin
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error #dogrulugu olcmek ıcın


#veri cekme

df = pd.read_excel("veri_on_isleme_ve_ozellik_muhendisligi.xlsx")

df.fillna(df["Gelir"].mean(),inplace=True)


#cinsiyet ve meslek sütunlarını sayısal hale getirelim
#bu sütunlar harflerden olustugu icin üstlerinde matematiksel işlemler yapamıyoruz bu yüzden 

le = LabelEncoder()
df["Cinsiyet"] = le.fit_transform(df["Cinsiyet"])
df["Meslek"] = le.fit_transform(df["Meslek"])



#giriş ve çıktı verilerini girelim

X  = df[["Yaş","Meslek","Cinsiyet"]]
y = df["Gelir"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2 ,random_state=42)


#Ölçeklendirme yapıyorum: tüm özellikleri ortalaması 0, standart sapması 1 olacak şekilde dönüştür
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


#modeli olustur ve egit
linear_model = LinearRegression()
linear_model.fit(X_train,y_train)


#modeli test et
linear_accuracy = linear_model.score(X_test,y_test)
print(f"Model doğruluk oranı : %{linear_accuracy *100:.2f}")


#daha karmaşık bir moodel kullan
rf_model  = RandomForestRegressor(n_estimators=68,random_state=1) #100 karar agacı
rf_model.fit(X_train,y_train)

rf_accuracy = rf_model.score(X_test,y_test)
print(f"Model doğruluk oranı : %{rf_accuracy *100:.2f}")




# Kullanıcıdan veri alalım
print("Lütfen tahmin için aşağıdaki bilgileri giriniz.")
yas = int(input("Yaş: "))
meslek = input("Meslek (Mühendis, Doktor, Öğretmen, Avukat):")
cinsiyet = input("Cinsiyet (Erkek, Kadın): ")


#kullanıcıdan alınan mesleği kodlayalım(LABEL ENCODING)
if cinsiyet == "Erkek":
    cinsiyet_kod = 1
elif cinsiyet == "Kadın":
    cinsiyet_kod = 0
else:
    raise ValueError("Geçersiz cinsiyet değeri")

meslek_kod = le.transform([meslek])[0] 


#yeni DataFrame
yeni_veri = pd.DataFrame([[yas,meslek_kod,cinsiyet_kod]], columns=["Yaş","Meslek","Cinsiyet"])

#Öğrenilen kuralları kullanarak yeni veriyi dönüştür.
yeni_veri_scaled = scaler.transform(yeni_veri)


tahmin = rf_model.predict(yeni_veri_scaled)

print(f"Tahmini Ortalama Maaş : {tahmin[0]:.2f}")