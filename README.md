# terrarium

A digital terrarium written in MicroPython for a [Raspberry Pi Pico](https://shop.pimoroni.com/products/raspberry-pi-pico?variant=32402092294227) mounted with a [BreakoutColourLCD240x240](https://shop.pimoroni.com/products/1-3-spi-colour-lcd-240x240-breakout?variant=30250963632211&currency=GBP&utm_source=google&utm_medium=cpc&utm_campaign=google+shopping?utm_source=google&utm_medium=surfaces&utm_campaign=shopping&gclid=Cj0KCQjwwNWKBhDAARIsAJ8HkhfexBZbHZXHZKI0WixTnGqXf9Q40DyJy6te9mpHibEGymhLaVfnP_4aAhWKEALw_wcB). 

The code, written using the [Thonny](https://thonny.org) and based on [Pimorini's st7789](https://github.com/pimoroni/st7789-python) library, creates a simple nature scene. It will change in real-time, simulating the seasons alongside weather conditions, sunrises and sunsets.    


**Winter twilight**
![IMG_4597 | width = 100](https://user-images.githubusercontent.com/69108995/135408635-b0870e8d-d6d7-4be5-ac22-bb6ef2ade370.jpeg)


**Autumn evening**

![IMG_4598](https://user-images.githubusercontent.com/69108995/135408766-d3b60a5a-24d2-40de-a204-3079e85ff36f.jpeg)

**Spring sunrise**

![IMG_4599](https://user-images.githubusercontent.com/69108995/135408868-5e8680a5-8384-4ff7-91df-ea11f6ac4f6f.jpeg)

**Summer afternoon**
![IMG_4602](https://user-images.githubusercontent.com/69108995/135408938-6abc6198-10a6-4396-8501-8a16f4795e73.jpeg)


**Existing features**

(currently need to be manually implemented, ie they're not yet tied to the clock)

- snowfall
- basic sunrise, sunset and sky tones
- leaves, with seasonal colours

**In development**
- rainfall
- leafall
- leaf growth
- greater variation in branch shapes
- cloud cover
- greater variety in sky colours
- tie everything to the clock: ultimately the terrarium should use the date/time to generate a seasonal scene

