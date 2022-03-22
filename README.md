# imagestore

![Alt text](imagestore.webp?raw=true "Gitpod View")

A repo demonstrating the use of M databases as a native image store.

Uses **mg_python** to interface Python with YottaDB/GTM/Intersystems Cache and Iris

An image passed file location or a http link is passed. The image is then converted to a binary string and stored in an M database.

# imagestore.py

Running imagestore.py requires the Python libraries **request** and **wget** to be pre installed

It also requires an M database to be running on the network with a port exposed for incoming connections to the database (through mg_python)

Finally, two environmnetal variables need to be set:

**yottaadd** needs to be set to the address of the M database

**yottaport** needs to be set to the port of the database

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

# Gitpod Demo
 
1) Create a free/paid Gitpod account - https://www.gitpod.io/
2) Log into the account
3) Open a new browser tab and add **gitpod.io/#https://github.com/RamSailopal/imagestore** to the address - This will create a new Gitpod cloud instance.

Once everything has loaded, two image tabs will open. One will show the original cruise ship image via http link and the other will show the same images stored locally, created from the M database (see graphic above for more details)

# References

mg_python - https://github.com/chrisemunt/mg_python

