module Main (main) where 

import System.IO (getContents)

main :: IO()
main = do 
  input <- getContents
  let lineCount = length (lines input)
      charCount = length input 
  putStrLn ("lines: " ++ show lineCount)
  putStrLn("char: " ++ show charCount)
