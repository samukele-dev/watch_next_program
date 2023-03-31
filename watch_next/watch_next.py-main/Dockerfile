# dokcerfile, Image, Container
# https://www.youtube.com/watch?v=0UG2x2iWerk
# https://hub.docker.com/_/python
# I had to do a quick reading with regrads to dockerfile as this is something enew to me

# We selct the ppython version we are using
FROM python:3.10

# We add the files/select the file we want to to run
ADD watch_next.py .

# We add the textfile that we would like to include
ADD movies.txt .

# We pip install space module
RUN pip install spacy

# We again run the english module
# https://stackoverflow.com/questions/63497243/spacy-load-model-in-docker
# I learned how to do it through the link above
RUN python -m spacy download en_core_web_md

# The CMD instruction specifies the program that will execute once
# the image container runs
CMD ["python","./watch_next.py"]