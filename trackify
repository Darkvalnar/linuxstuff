#! /bin/bash



# we create a function to grab the track title
function check_track(){ 

track="$(sp eval | grep SPOTIFY_TITLE)"
}

# we do the same for the artst
function check_artist(){ 

artname="$(sp eval | grep SPOTIFY_ARTIST)"
}


# we will run this until program termination
while : 
do
# we call the functions to get the track name and artist and trim them by removing unneccesary args
check_track
song=${track//"SPOTIFY_TITLE="/}

check_artist
artist=${artname//"SPOTIFY_ARTIST="/}

# now we assign the outputs of the track name check function to a variable
checkertrack = "$(check_track)"

#printing out the currently playing song:
echo "Now playing $song by $artist" 


# we will now compare whether or not the track stored within the variable is the same as the one we grab from the function
if $track = $checkertrack
then
return
# if the track changed, we will output the name of the artist and track again
else
clear
echo "Now playing $song by $artist"
fi
done
