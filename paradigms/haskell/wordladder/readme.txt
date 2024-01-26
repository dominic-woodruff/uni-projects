Supposed to be ran normally: 
ghc wordladder.hs
./wordladder [dictionary] [startword] [goalword]

I could not get the depth first search to not loop forever,
I narrowed the problem code to something in the second half of my search
but I could not figure out exactly was wrong,
I left a testing doc that shows all of my other functions (except 
buildladder and main which depend on this function) working and how I tested
them but this bug was not something I was able to solve
