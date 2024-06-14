#include <LiquidCrystal_I2C.h>
#include <DHT.h>
#include <WiFi.h>
#include <HTTPClient.h>

#define DHTTYPE DHT22
#define DHTPIN 19

DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(0x27, 16, 2);

const char *ssid = "Wokwi-GUEST";
const char *password = "";
const char *serverUrl = "https://5306834c-ed47-4644-8556-c8f65f3b8cdd-00-10wylyig7w2kr.sisko.replit.dev/sensor/data";

void setup()
{
    Serial.begin(115200);
    dht.begin();
    lcd.init();
    lcd.backlight();
    konfigurasiWiFi(ssid, password);
}

void loop()
{
    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();

    if (isnan(humidity) || isnan(temperature))
    {
        Serial.println("Failed to read from DHT sensor!");
        lcd.setCursor(0, 0);
        lcd.print("Sensor Error");
        return;
    }

    lcd.setCursor(0, 0);
    lcd.print("Temp: ");
    lcd.print(temperature);
    lcd.print(" C");

    lcd.setCursor(0, 1);
    lcd.print("Hum: ");
    lcd.print(humidity);
    lcd.print(" %");
    Serial.println(humidity);

    kirimKeAPI(temperature, humidity);

    Serial.println("=========================");
    delay(2000);
}

void konfigurasiWiFi(const char *ssid, const char *password)
{
    WiFi.mode(WIFI_STA);
    Serial.print("Menghubungkan ke WiFi...");
    WiFi.begin(ssid, password);
    int timeout = 0;
    while (WiFi.status() != WL_CONNECTED && timeout < 10)
    {
        delay(5000);
        Serial.print(".");
        timeout++;
    }
    if (WiFi.status() == WL_CONNECTED)
    {
        Serial.println("");
        Serial.println("WiFi tersambung");
        Serial.println("IP address: " + WiFi.localIP().toString());
    }
    else
    {
        Serial.println("Gagal terhubung ke Wi-Fi");
    }
}

void kirimKeAPI(float temperature, float humidity)
{
    if (WiFi.status() == WL_CONNECTED)
    {
        HTTPClient httpClient;
        httpClient.begin(serverUrl);

        httpClient.addHeader("Content-Type", "application/json");
        String jsonPayload = "{\"temperature\":" + String(temperature) + ", \"humidity\":" + String(humidity) + "}";
        int httpCode = httpClient.POST(jsonPayload);

        if (httpCode > 0)
        {
            String response = httpClient.getString();
            Serial.println("Data berhasil dikirim");
            Serial.println("HTTP Response code: " + String(httpCode));
            Serial.println("Response: " + response);
        }
        else
        {
            Serial.println("Gagal mengirim data");
            Serial.println("HTTP Response code: " + String(httpCode));
        }
        httpClient.end();
    }
    else
    {
        Serial.println("WiFi tidak terhubung");
    }
}
