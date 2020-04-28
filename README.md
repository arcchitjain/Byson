## BYSON - Bring your store online
Local shop owners are being hit hard by the current crisis.  While setting up a webshop offers them an opportunity to keep selling supplying their neighborhood, many of these stores struggle to shift their business online.  Our goal is to make it as easy as possible for shop owners to bring their store online and start offering their products to customers in the neighbourhood.  We want to connect them to local customers by offering a customised online experience that captures some of the flair of these unique stores and handle ordering, payment and facilitate the delivery of their products. By focusing on small stores and local business we want to make the experience of starting and running an online business as painless as possible.

Learn all about Byson in our 2 minute pitch:

[![Byson Pitch](https://img.youtube.com/vi/juLSdEGPbnc/0.jpg)](https://www.youtube.com/watch?v=juLSdEGPbnc)

### Progress
We have finished prototyping our theme generator, check out the video below:

[![Prototype theme color generator](https://img.youtube.com/vi/L4k8W7lPNec/0.jpg)](https://www.youtube.com/watch?v=L4k8W7lPNec)

### Running the local webserver

    pip install -e .
    cd byson
    python manage.py runserver

### Mockups

Creating personalized theme
    
    http://127.0.0.1:8000/shopmaker/tweak_layout

Importing product from image

    http://127.0.0.1:8000/shopmaker/import_products

### Proof of Concepts

Get a list of 4 dominant colors in the store image

    pip install ColorDetect
    pip install Pillow
    python get_dominant_colors.py

Read multiple barcodes from an image

    brew install zbar
    pip install pyzbar
    python get_barcodes.py

Build product hierarchy from food products based on barcode.

```python
pip install requests
pip install matplotlib
pip install networkx

python get_products.py
```

