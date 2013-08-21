<h1>Awesome-Wallpaper</h1>
<p>
AwesomeWallpaper downloads the best pictures every day for your desktop wallpaper to keep it interesting.  It is a script made to work with a cron job (scheduled execution) to download new photos every day.
</p>

<h1>Setting up AwesomeWallpaper is easy!</h1>
<p>
1:  Ensure Python is installed.  It probably already is, but to check, go into terminal and type "python" and see if it responds.<br/>
2:  Open terminal and enter<b>*</b>: rm ~/Library/Preferences/com.apple.Desktop.plist
3:  Make a directory for your wallpapers, it can be anywhere<br/>
4:  In settings, point your wallpaper directory to that directory, make sure it allows multiple wallpapers as well as timed switching<br/>
5:  Download <b>~get_todays_wallpapers.py</b> and put it in the same wallpapers directory<br/>
6:  Create a cron job to run <b>~get_todays_wallpapers.py</b> at the interval you choose<b>**</b>
</p>
<p>
<b>*</b>All this does is make it so that Mac OS doesn't switch your wallpaper back to the default when you restart your computer.<br/><br/>
<b>**</b>How to create CRON jobs:<br/>
<a href="http://benr75.com/pages/using_crontab_mac_os_x_unix_linux">Here</a> is a good tutorial for creating cron jobs on a *nix system with Crontab.<br/>
If that scares you, I recommend using Google's free software <a href="https://code.google.com/p/cronnix/">CronniX</a> to schedule cron jobs (only Mac OSX).
</p>
