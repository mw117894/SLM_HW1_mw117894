link <- "https://database.lichess.org/lichess_db_puzzle.csv.bz2"

filename <- "puzzles.csv.bz2"

header <- c("PuzzleId", "FEN", "Moves",
          "Rating", "RatingDeviation",
          "Popularity", "NbPlays",
          "Themes", "GameUrl")

decompressed_filename <- "puzzles.csv"

if (!file.exists(filename)){
  print(paste(filename, "hasn't been found. Downloading...",sep = " "))
  options(timeout = 300)
  download.file(link,destfile = filename)
  
} else{
  print(paste(filename," has been already downloaded"))
}

if (file.exists(decompressed_filename)){
  print(paste(decompressed_filename," has been already unpacked."))
  
}else{
  
  R.utils::bunzip2(filename, decompressed_filename, remove = F)  
}
data<- read.csv(decompressed_filename,header = F)
colnames(data) <- header
head(data)
