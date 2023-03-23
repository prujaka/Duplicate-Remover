from DuplicateRemover import DuplicateRemover

dirname = "img"

# Remove Duplicates
dr = DuplicateRemover(dirname)
# dr.find_duplicates()

# Find Similar Images
folder = "/Users/sergey/work/lewagon/spotify-project/data/spectrograms"
dr.find_similar(folder + "/006363.png", 95)
