Flash the ino file to Arduino UNO

Clone this repository on raspberry pi in location /home/pi
Run the python script on raspberry pi

To make the script run on startup follow the below instructions-


1. Create a launcher.sh file using the below command and enter the following instructions onto the file

    ``` nano launcher.sh ```

The above command creates a sh file and opens the content inside it which is currently empty. Add the below lines on to the file
```
#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/laserharp
sudo python bbt.py
cd /

```
What the above script in sh file will do is to navigate to the root directory, 
then to the laserharp directory, launch the Python script and then return to the root directory.\

We need to make the launcher script an executable, for which we do use this command

  ``` chmod 755 launcher.sh ```
Now test it, by typing in which should run your Python code.

  ```sh launcher.sh```

Now we need to make a directory for the any errors in crontab to go.Navigate back to your home directory by tryping the command

```cd```
To create a logs directory use the command-

```mkdir logs```

Now type in the command to access crontab window.

```sudo crontab -e```

Now, enter the line:

```@reboot sh /home/pi/laserharp/launcher.sh >/home/pi/logs/cronlog 2>&1```

This will execute the script upon start of raspberry pi.

Unplug the power or just type in:

```sudo reboot```

Wait for startup and see if your script automatically launches.If the script doesn't work, check out the log file:

```cd logs```

The following command will show you any errors that you might have.

```cat cronlog```



