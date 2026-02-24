module Main (main) where 

import System.Environment (getArgs)
import Data.Char (toUpper)

main :: IO()
main = do 
  args <- getArgs
  case args of 
    ("--upper":rest) -> putStrLn(map toUpper (unwords rest))
    rest -> putStrLn (unwords rest)
