#text = "grogan society officer-5; liaison to the bridge project-5; Colorguard-5; Intramural Tennis-3, Intramural Soccer-2; Tutor at South Bend Center for the homeless children's center-2, eucharistic minister and lector for dorm mass-9, trident Naval Society-5; PFA:  14-1"

# split the block of text up into individual bullets

def breakdown_text(text):

    bullets = []

    split_list = text.split(';')
    for bullet in split_list:
        if ',' in bullet:
            new_bullets = bullet.split(',')
            for bullet in new_bullets:
                bullets.append(bullet)
        else:
            bullets.append(bullet)

    return bullets
            

def capitalize(bullet):
    
    articles = ["the", "is", "and", "with", "for", "to", "at"]  
    
    words = bullet.split()
    capitalized_words = []
    
    for word in words:
        if word not in articles:
            new_word = word.replace(word[0], word[0].upper(), 1)
            capitalized_words.append(new_word)
        else:
            capitalized_words.append(word)
    return capitalized_words
            
def assemble_bullet(words):
	
	size = len(words)
	string = ''
	
    for i in range(size):
	    if i == len(words)-1:
	        string = string + words[i] + ','
	    else:
		    string = string + words[i] + ' '
	return string   

def format_text(text):

    bullets = breakdown_text(text)
    final_bullets = []
    #iterates through the bullets, capitalizes them, and assembles them w/ proper punctuation, appends to a list
    for bullet in bullets:
        final_bullets.append(assemble_bullet(capitalize(bullet)))
    
    #take the assembled bullets and rebuild them into a complete block of text
    output_text = ''
    for final_bullet in final_bullets:
       output_text = output_text + ' ' + final_bullet
    
    return output_text
    


    