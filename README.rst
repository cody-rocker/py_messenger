py_messenger
============
*This project is in the process of undergoing a full rewrite to include a complete python module as well as a command line tool. Original files can be found in py_messenger_old directory.*

:Developer:
  `Cody Rocker <mailto:cody.rocker.83@gmail.com>`_
:Date:
  2016

Example CLI usage:
--------------

**>> Config**

.. code-block:: bash

  # Run complete program configuration (first-run)
  py_messenger config

  # or set properties individually from the command line
  py_messenger config --set-user example@gmail.com

**>> SMTP (default)**

.. code-block:: bash

  py_messenger -d example@gmail.com -m "message body"

**>> SMS**

.. code-block:: bash

  py_messenger send -t SMS -d 1234567890 -m "message body"

**>> MMS**

  Not yet implemented

------------

Questions, comments, ideas are welcome.
