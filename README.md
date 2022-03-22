# imagestore

![Alt text](imagestore.webp?raw=true "Gitpod View")

A repo demonstrating the use of M databases as a native image store.

Uses **mg_python** to interface Python with YottaDB/GTM/Intersystems Cache and Iris

An image passed file location or a http link is passed. The image is then converted to a binary string and stored in an M database.

# imagestore.py

Running imagestore.py requires the Python libraries **request** and **wget** to be pre installed

The main Python executable takes 3 commands:

**imgtobin** - Convert an image to a binary string to be stored in the database i.e.:

     ./imagestore.py imgtobin cruise https://image.shutterstock.com/image-photo/luxury-cruise-ship-sailing-port-600w-678153238.jpg
     
This will store the cruise ship image referenced from https://image.shutterstock.com/image-photo/luxury-cruise-ship-sailing-port-600w-678153238.jpg in an M database global called **IMAGES** under subscript **cruise**

**bintoimg** - Convert a binary entry in an M database to an image i.e.

     ./imagestore.py bintoimage cruise
     
This will take the binary strings stored in the cruise subscript of the global **IMAGES**, create one string and then create a **cruise.jpeg** image file

**delete** - Delete a global entry/image i.e.

     ./imagestore.py delete cruise
     
This will delete all binary strings associated with the **cruise** subscript in the M database global **IMAGES**

# References

mg_python - https://github.com/chrisemunt/mg_python

