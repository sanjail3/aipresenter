import openai


openai.api_key = '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'




# Generate the response using OpenAI API
response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": """
I am making slide presentation on topic Machine learning give me content of 7 slides  each slide should have crisp and clear point up to 5 with   your response should follow this pattern  for any topics 

Slide 1: Title Slide
Title: 

Slide 2: Topics
Topics to be discussed:


Slide 3:
Topic: 
Content:


Slide 4:
Topic: 
Content:


Slide 5:
Topic: 
Content:


Slide 6:
Topic:
Content:


Slide 7:
Topic: 
Content:



Slide 8:
Topic: 
Content:


Slide 9:
Topic: 
Content:

"""


      }
        ]
    )

# Extract the text for each slide
slides = response.choices[0].message.content.split("Slide")
print(slides)


formatted_slides = []
for slide in slides[4:]:
    # Split slide into title and content
    slide_parts = slide.split("Content:")
    if len(slide_parts) > 1:
        val=slide_parts[0].split("Topic:")
        title = val[1]
        content = slide_parts[1].strip()
        formatted_slide = {
            "title": title,
            "content": content
        }
        formatted_slides.append(formatted_slide)

# Print the formatted slides
for index, slide in enumerate(formatted_slides):
    print(f"Slide {index+3}:")
    print(f"Title: {slide['title']}")
    print(f"{slide['content']}")
    print()

slide1_title=slides[2].split("Title:")[1]
slide2_content=slides[3].split("Topics to be discussed:")[1]

print(slide1_title)
print(slide2_content)