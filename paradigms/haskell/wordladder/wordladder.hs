--Dominic Woodruff
{-# OPTIONS_GHC -Wno-incomplete-patterns #-}

{-
Finds wordladders between 2 words, in this context a word ladder
is a list of words that belong to a dictonary all of which are
1 letter different from adjacent words, the ladder is a list of
such words that takes you from the start word to the end word.
_-}

import System.IO
import System.Environment
import Data.List

data Queue a = Queue [a] [a]

--Creates an empty queue
emptyQueue :: Queue a
emptyQueue = Queue [] []

--checks if queue is empty
isEmptyQueue :: Queue a -> Bool
isEmptyQueue (Queue [] []) = True
isEmptyQueue _ = False

--adds a value to the back of the queue
enqueue :: a -> Queue a -> Queue a
enqueue x (Queue front rear) = Queue front (x:rear)

--Take an element off of the front of the queue
dequeue :: Queue a -> (a, Queue a)
dequeue (Queue (x:xs) rear) = (x, Queue xs rear)
dequeue (Queue [] rear) = dequeue (Queue (reverse rear) [])


--Puts the queue in a readable format (reverses so wordladders output properly)
toList :: Queue a -> [a]
toList (Queue front rear) = front ++ reverse rear

--Driver, handles IO
main :: IO ()
main = do
    args <- getArgs
    if length args /= 3
        then putStrLn "Usage: program-name input-file start-word goal-word"
        else do
            let [inFile, startWord, goalWord] = args
            if length startWord /= length goalWord
                then putStrLn "Start word and goal word must be the same length."
                else do
                    input <- readFile inFile
                    let ladder = buildladder input startWord goalWord
                    putStrLn ladder


--Gets dictionary and starts the BFS
buildladder :: String -> String -> String -> String
buildladder input startWord goalWord =
    let words = lines input
        wordSet = filter (\w -> length w == length startWord && w /= startWord) words
        ladder = bfs (enqueue (startWord, [] ) emptyQueue) wordSet goalWord
    in case lookup goalWord ladder of
        Just path -> unwords (reverse path ++ [goalWord])
        Nothing -> "No ladder found"

--BFS/Breadth First Search
bfs :: Queue (String, [String]) -> [String] -> String -> [(String, [String])]
bfs queue dict goalWord
    | isEmptyQueue queue = []
    | goalReached (fst frontQueue) goalWord = toList queue
    | otherwise = bfs (enqueueAll newQueue queue) newDict goalWord
    where
        frontQueue = dequeue queue
        (word, path) = fst frontQueue
        neighbors = oneLetterDifferent word dict------Works up to at least here
        newPaths = map (\w -> (w, w:path)) neighbors
        newQueue = [(w, p) | (w, p) <- newPaths, w `elem` dict]
        newDict = dict \\ map fst newQueue
        enqueueAll xs q = foldr (\x acc -> enqueue x acc) q xs

--Checks if the goal was just added to the queue
goalReached :: (String, [String]) -> String -> Bool
goalReached (word, _) goalWord = word == goalWord

--Gets all of the words that are 1 letter different from the starting word
oneLetterDifferent :: String -> [String] -> [String]
oneLetterDifferent s1 = filter (\s2 -> countDiffs s1 s2 == 1)

--Counts how many letters are different between 2 words
countDiffs :: String -> String -> Int
countDiffs [] [] = 0
countDiffs (x:xs) (y:ys) = (if x == y then 0 else 1) + countDiffs xs ys


