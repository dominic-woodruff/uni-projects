--Dominic Woodruff

module RightTriangles where

import Data.Char (isDigit)
import System.IO
import System.Environment

checkTriangles :: String -> String
checkTriangles input = concatMap (++ "\n") (process2Ints (splitStringtoInts input))

--Split the input string into a list of ints
--works if more then 2 numbers are put on a line, it just parses 
--  ints from the entire file
splitStringtoInts :: String -> [Int]
splitStringtoInts str = take str []
  where
    --recursion likes putting things backwards so the list needs reversed
    take [] nums = reverse nums
    take (x:xs) nums
    --builds the ints by checking the string char by char, any non number is delimiter
      | isDigit x = let (word, rest) = span isDigit (x:xs)
                        num = read word
                    in take rest (num : nums)
      | otherwise = take xs nums

--Runs numbers through isRight 2 at a time
process2Ints :: [Int] -> [String]
process2Ints [] = []
process2Ints [_] = []
process2Ints (x:y:rest) = isRight x y : process2Ints rest

{-
Checks if inputs are a Pythagorean Triple by checking if any combination of them
as legs or hypotenuse when used in the Pythagorean Theorem make a number that when
rooted, rounded, then squared has the same value
-}
isRight :: Int -> Int -> String
isRight x y--x and y are the input integers/ sides of a triangle
  | x <= 0 || y <= 0 = "Invalid input"--Triangles must have positive dimensions
  --if the side can be square rooted, rounded, then squared into the same value
  --    it is a perfect square and completes the Pythagorean Triple
  | a2^2 == a = show x ++ ", " ++ show y ++ ", " ++ show a2 ++ " form a right triangle"
  | b2^2 == b = show x ++ ", " ++ show y ++ ", " ++ show b2 ++ " form a right triangle"
  | c2^2 == c = show x ++ ", " ++ show y ++ ", " ++ show c2 ++ " form a right triangle"
  --else the 3rd side does not generate a right triangle
  | otherwise = show x ++ ", " ++ show y ++ " do not form a right triangle"
  where a = x^2-y^2                         --if x is hypotenuse
        a2 = floor( sqrt( fromIntegral a))  --hypotenuse if above is true
        b = y^2-x^2                         --if y is hypotenuse
        b2 = floor( sqrt( fromIntegral b))  --hypotenuse if above is true
        c = x^2+y^2                         --if the 3rd side is the hypotennuse
        c2 = floor( sqrt( fromIntegral c))  --hypotenuse if above is true


