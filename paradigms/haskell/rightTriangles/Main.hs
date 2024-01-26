--Dominic Woodruff

{-
Borrowed and modified from the Project 1 Main.hs

This code will calls the function 'RightTriangles' in the file
   RightTriangles.hs
This code will be run with 2 command line arguments and will
handle all input and output.  The RightTriangles function will
check if 2 integers are part of a right triangle
-}

module Main where
import RightTriangles
import System.Environment
import System.IO

{-
main is the entry point to the program.  Compile the code with command
     ghc --make Main.hs
then run the program with command
     ./Main in.txt out.txt
where in.txt is the name of the input file, out.txt is the name of the
output file
-}

main :: IO ()
main = do
  [inFile, outFile] <- getArgs
  input <- readFile inFile
  let output = checkTriangles input
  writeFile outFile output