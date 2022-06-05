# Akilli Kilit Sistemleri
 Blynk Server ile IoT Uygulaması
# Blynk Server Kurulumu
 Blynk, IOT sistemler için tasarlanmış bir programdır. Bu programla donanımlarınızı uzaktan kontrol edebilir, sensör verileri alabilir, veri depolayabilir, bu verileri    görselleştirebilir ve bunun gibi birçok şeyi yapabilirsiniz.
 
![Blynk](https://github.com/ufukderin12/Akilli-Kilit-Sistemleri/blob/main/Ekran%20Al%C4%B1nt%C4%B1s%C4%B1.PNG)

# Blynk Kullanımı
 Widgetları kullanarak projeleriniz için bir kontrol arayüzü oluşturmanızı sağlar.
# Blynk Server
Telefonunuz ve kontrol edeceğiniz donanım arasındaki tüm iletişimden sorumludur. Bunu yaparken Blynk Cloud'u kullanabilir veya özel Blynk sunucunuzu yerel olarak çalıştırabilirsiniz. 
# Blynk Kütüphanesi
Tüm popüler donanım platformları için sunucu ile iletişimi etkinleştirip ve gelen ve giden komutları işlemenizi sağlar. <br/>
Blynk her uygulamamız için bize bir “Auth Token” tanımlıyor ve bunu mail adresimize gönderiyor. Auth Token sizin için üretilmiş özel bir imza ve haberleşme sağlanırken bu imzaların uygulama ve donanımla eşleşmesi gerekiyor. 
# Server Kurulumu için Gerekli Kodlar
### wget https://github.com/shivasiddharth/blynk-server/releases/download/v0.41.16/pi-local-server-setup.sh
### sudo chmod +x ./pi-local-server-setup.sh
### sudo ./pi-local-server-setup.sh
Autostart kurulumunu yaptığınız zaman raspberry her ayağa kalktığında serveri otomatik olarak başlatır.
### Do you wish to set the server to autostart on boot? y
Sistem başlatılır.
### sudo nano /etc/rc.local
Bu adımdan sonra raspberrynize Blynk isminde bir klasör oluşturulur ve klasör içerisindeki mail.properties düzenlenir. Admin sayfasına raspberryi üzerindeki tarayıcadan bağlanabilir ve tokenınıza bağlı projeleri görüp bu admin sayfası üzerinden yönetebilirsiniz. Bu adımlar başarıyla tamamlandıktan sonra Blynk Server başarılı bir şekilde kurulmuş olacaktır. 
## Uygulamayı dair daha geniş bilgiler için Wiki sayfasına bakınız.












