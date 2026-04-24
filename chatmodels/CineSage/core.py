from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

prompt = ChatPromptTemplate.from_messages([
    ("system",
        """
        You are an expert movie information extractor.

        Your task is to carefully read the given movie description and extract all possible important movie details in a clean structured format.

        Extract the following details if available:

        1. Movie Name
        2. Release Year
        3. Director
        4. Main Cast
        5. Genre
        6. Duration / Length
        7. Plot Summary
        8. IMDb Rating
        9. Language
        10. Country
        11. Music Director / Composer
        12. Box Office Collection
        13. Awards / Recognition
        14. Themes
        15. Notable Highlights
        16. Critical Reception
        17. Sequel / Franchise Information
        18. Streaming Platform Availability (if mentioned)

        If any detail is not available, return "Not Mentioned".

        Return the output in this exact format:

        Movie Name:
        Release Year:
        Director:
        Main Cast:
        Genre:
        Duration / Length:
        Plot Summary:
        IMDb Rating:
        Language:
        Country:
        Music Director / Composer:
        Box Office Collection:
        Awards / Recognition:
        Themes:
        Notable Highlights:
        Critical Reception:
        Sequel / Franchise Information:
        Streaming Platform Availability:
        """
    ),
    ("human", 
        """
        Extract information from the paragraph:
        {paragraph}
        """
    )]
)

para = input("Enter the movie detail paragraph: ")

final_prompt = prompt.invoke({
    "paragraph": para
})

# without prompt template -> we have to manually pass the messages to the model, this is repetative
# response = model.invoke("Interstellar is a visually stunning science fiction epic directed by Christopher Nolan Released in 2014, the film stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, and Michael Caine. The story revolves around a group of astronauts who travel through a wormhole near Saturn in search of a new home for humanity as Earth faces environmental collapse. The movie was widely appreciated for its emotional depth, scientific accuracy, and Hans Zimmer's powerful soundtrack. It holds a rating of 8.6 on IMDb and is often considered one of the greatest sci-fi films of the 21st century. Can you please provide/generate the summary and information about the movie in a concise manner?")

# With prompt template -> we can easily pass the messages to the model, this is not repetative
response = model.invoke(final_prompt)

print(f"Response: {response.content} \n")