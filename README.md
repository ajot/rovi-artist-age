# What is "Rovi Artist Age"?
 
"Rovi Artist Age" is a fun little [Alfred](http://www.alfredapp.com/) extension built using Python, that allows you to find the age and date of birth of any music artist using their first or last name using Rovi's artist info API. No more guessing, madonna & britney's date of births at your finger tips!

## What is Alfred?
[Alfred](http://alfredapp.com) is an award-winning productivity application for Mac OS X, which aims to save you time in searching your local computer and the web. Whether it's maps, Amazon, eBay, Wikipedia, you can feed your web addiction quicker than ever.

The real power of Alfred lies in it's [powerpack](http://www.alfredapp.com/powerpack/) that allows you to create your very own Terminal shell scripts, AppleScripts, workflows, search filters and file groups to extend Alfred.

## Summary

Why? Cause it's easy, fun. Why open a browser when you can find madonna's age with just a keyboard shortcut? It obvious;y doesn't stop there. You can search for any artist by their first or last names. Think usher, britney!

## Requirements

1. [Alfred](http://www.alfredapp.com/) + [Alfred Powerpack](http://www.alfredapp.com/powerpack/)
2. [Rovi API Key](http://developer.rovicorp.com)
3. [Growl](http://growl.info)
4. [Nice and shiny Mac](http://www.youtube.com/results?search_query=get+a+mac) - Of course you have one!

## How to Use

1. Make sure Alfred is running. 

2. Just hit your Alfred keyboard shortcut. In my case I have it configured it as CMD + SPACE. (The default is probably ALT + SPACE)

	![Alfred Launch Bar](https://github.com/mashery/rovi-artist-age/raw/master/images/alfred_launch_bar.png)
	
3. Type the keyword **age** followed by the first or last name of the artist you want to find the date of birth for (You can change the keyword by editing the info.plist file)

	![Alfred Launch Bar](https://github.com/mashery/rovi-artist-age/raw/master/images/alfred_launch_bar_fill.png)	
	
4. You get a Growl notification with the date of birth and the age of the artist

	![Alfred Growl Notification](https://github.com/mashery/rovi-artist-age/raw/master/images/alfred_growl.png)


## Examples ##
	<pre>age britney</pre>
	<pre>age usher</pre>

## Installation

	
1. Grab the latest source
	<pre>git clone git://github.com/mashery/rovi-artist-age.git</pre>

2. Copy the directory you just downloaded to -
	<pre>~/Library/Application Support/Alfred/extensions/scripts</pre>

3. Rename this directory to say "Rovi Artist Age"	

4. Open the file "~/Library/Application Support/Alfred/extensions/scripts/Rovi Artist Age/rovi_auth.py" and type in your Rovi **API key** & **Shared Secret**. Get your Rovi (Metadata and Search) API Key [here](http://developer.rovicorp.com)

	![Type your Rovi API Key](https://github.com/mashery/rovi-artist-age/raw/master/images/rovi_api_key.png)

5. You're done. Just give Alfred a whirl now. Refer [How to Use](#how-to-use) above.

## Development

Be sure to follow the configuration steps above and use this step-by-step guide to tweak to your heart's content.

1. Grab the latest source
	<pre>git clone git://github.com/mashery/rovi-artist-age.git</pre>

2. All the Rovi search related action takes place in the file 'rovi\_search\_.py'

3. All the Rovi auth related action takes place in the file 'rovi_auth.py'

4. Tweak away


## About 

* No warranty expressed or implied.  Software is as is.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly created by [Mashery Dev](http://dev.mashery.com)