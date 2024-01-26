--Dominic Woodruff

module DocTransformer where

import Data.Char (isAlpha, toLower, toUpper, isLower,)

--transformDoc function gets the final value by 
--passing all of the functions through eachother
--  replaceA -> changeCase -> 
--      splitString (args change from string to [string]) -> 
--      removeLen -> addNewLine
transformDoc :: String -> Int -> String
transformDoc str len = concat (addNewLine (removeLen (splitString (changeCase (replaceA str))) len))

--adds newline \n to the end of each string
addNewLine :: [String] -> [String]
addNewLine = map (++ "\n")

--Replace every 'a' and 'A' with '@'
replaceA :: String -> String
replaceA = map repl
    where
        repl 'a' = '@'
        repl 'A' = '@'
        repl other = other

--remove every string with length of input int
removeLen :: [String] -> Int -> [String]
removeLen strs len = filter (\string -> length string /= len) strs

--turns a string into a list of string with 
--  special character(without '@') as delimiters
splitString :: String -> [String]
splitString str = take str []
    where                                                                                                                                                                                                               
        take[] string = string
        take (x:xs) character
            | isAlpha x || x == '@' = let (word, rest) = span (\c -> isAlpha c || c == '@') (x:xs)
                in take rest(reverse  word : character)
            | otherwise = take xs character

--Make capital letters lowercase and vice-versa
changeCase :: String -> String
changeCase = map    (\character ->
                        if isLower character
                            then toUpper character
                        else toLower character
                    )
