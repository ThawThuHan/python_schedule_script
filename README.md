# python_schedule_script

<p> 
<pre>
Usage: Schedule_delete_per_minute.py [options]

Options:
  -h, --help  show this help message and exit
  -n NUM      specify -n recurring time!
  -p PATH     specify file path!
None
</p>

<h1>To Run python script as a background Service </h1>

<p>run this command </p>

<p>nohup python3 -u /home/thawthuhan/Desktop/Schedule_delete_per_minute.py -n 2 -p [filePath] >> output.log &</p>
<p>don't forget & (end of command line) <p>
<p>and then you can check log in output.log and check process using ps aux | grep Schedule_delete_per_minute.py</p>
<p>to kill process using kill %PID</p>
