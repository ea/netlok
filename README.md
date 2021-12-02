# Simple Network Location swithing widget

I usually have a few aditional NICs on my mac and am constantly switching between different network confirugations. Network settings menu on macOS lets you define "locations" for which you can configure different settings for different interfaces. Once locations are set up the way you like them , switching between them doesn't requrie elevated privileges which means less password prompts!

This simple widget just uses `networksetup` to switch between different locations, shows the current one and displays external IP address if available. 
It uses `rumps` package and is otherwise pretty short and naive. 

Make it into an app via `py2app` by typing `make` and then you can add it to "login items" so it's run on startup. 

