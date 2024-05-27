# Sanal Mouse Kontrol Programı / Virtual Mouse Control Program

## Açıklama / Description

Bu Python programı, el hareketlerinizi kullanarak fare imlecinizi kontrol etmenizi sağlar. Webcam üzerinden el hareketlerinizi izler ve işaret parmağı ile baş parmağınızı belirli bir mesafede tuttuğunuzda fareyi hareket ettirir. Ayrıca, parmaklarınızın belirli hareketleriyle sol tıklama ve sağ tıklama yapmanızı sağlar.

This Python program allows you to control your mouse cursor using hand movements. It tracks your hand movements through the webcam and moves the mouse when you hold your index finger and thumb at a specific distance. Additionally, it enables left and right clicking based on specific finger gestures.

## Gereksinimler / Requirements

- Python 3.x
- OpenCV
- Mediapipe
- PyAutoGUI

## Nasıl Çalışır / How It Works
İşaret parmağınız ve baş parmağınız arasındaki mesafe 30 piksel ile 60 piksel arasında olduğunda, mouse imleci hareket eder.

İşaret parmağınız ve baş parmağınız arasındaki mesafe 30 pikselin altına düştüğünde, sol tıklama yapılır.

İşaret parmağınız ve orta parmağınız arasındaki mesafe 30 pikselin altına düştüğünde, sağ tıklama yapılır.

The mouse cursor moves when the distance between your index finger and thumb is between 30 pixels and 60 pixels.

A left click is triggered when the distance between your index finger and thumb falls below 30 pixels.

A right click is triggered when the distance between your index finger and middle finger falls below 30 pixels.

## Amaç / Purpose
Bu program, el hareketlerinizi kullanarak bilgisayarınızı kontrol etmenizi sağlar. Özellikle ellerini kullanarak bilgisayarla etkileşimde bulunmak isteyenler için faydalıdır.

This program allows you to control your computer using hand movements. It is particularly useful for those who want to interact with their computer using gestures.

## Lisans / License
Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.

This project is licensed under the MIT License. See the LICENSE file for more details.
