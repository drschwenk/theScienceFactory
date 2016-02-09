---
Title: MixedCompany 
Date:2016-1-14 
Author: Dustin Schwenk 
Slug: comptails 
Category: personal projects 
Tags: cocktails, flavor network 
---
“MixedCompany” is my exploration of the flavor network found in a wide variety of cocktail recipes. 
I wanted to know what kinds of flavors we choose for our mixed drinks; are they harmonious? Discordant? 
And how could that knowledge be used to riff on classic recipes and create something new? I dig into these questions as 
well as build a recommendation engine to suggest novel ingredient pairings.
<!-- PELICAN_END_SUMMARY -->

##Overview
We’re in the midst of a cocktail renaissance. 
Hoping to contribute to this recent resurgence, I’ve created [MixedCompany](recommender "Title")—a tool for recommending novel ingredient pairings and substitutions in cocktails. 
The ingredient-flavor network latent in the world of mixed drinks contains a great deal of information about our preferences for flavor combinations. 
I build and exploit this network to suggest ingredients that should pair well together, but have not appeared together before in existing cocktail recipes. 
Interesting new twists on famous cocktail recipes, backed up by flavor data, are waiting to be explored with [MixedCompany](recommender "Title").

<br><br>


##Dataset

To address the question of why certain ingredients pair well together, two things are needed. The first is a reference 
documenting the chemical compounds found in common cocktail components. For this, I used the 6th edition of Fenaroli’s 
handbook of flavor ingredients. Fenaroli’s handbook is the canonical reference for chemical compounds and their occurrences in 
nature. The second is a source of flavor pairings that human’s enjoy drinking. This is readily found in the form of cocktail 
recipes on the web, from which I’ve collected 2000. This was a straightforward task with Beautiful Soup and some exploration 
of the structure of several popular recipe websites. The bulleted list format of most recipes makes a very easy structure to
pull out of a site's html.

[Burdock, G. A. Fenaroli's handbook of flavor ingredients (CRC Press, 2004), 5th edn.](https://books.google.com/books?id=A8OyTzGGJhYC&printsec=frontcover&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false "Title")

[liquor.com](http://liquor.com/recipes/ "Title")

[NYT drinks](http://topics.nytimes.com/top/features/magazine/columns/drink/index.html "Title")

<br><br>

##Methods

The path I followed was influenced in large part by the work of 
[Ahn, Ahnert, Bagrow and Barabási](http://www.nature.com/articles/srep00196 "Title") on exploring the 
[ingredient-flavor network](https://en.wikipedia.org/wiki/Ingredient-flavor_network 'Title') within world cuisine. 


<br><br>
![method](images/method_overview.jpeg =512x384)
<br><br>

Recipe scraping was straightforward, and the code for my scraping module can be found in this projects github repo. 
Parsing the pdf of Fenaroli’s handbook was considerably more difficult. This first required extracting plaintext from 
the scanned pdf using the tesseract package. Armed with the plain text, I wrote a parser to recover the compound : 
ingredient map that I needed to build the flavor network. This required some tinkering with regex, the result 
of which is realized in the parser module. Sanitizing the flavor and recipe data was a major challenge, 
but one made vastly easier by a fuzzywuzzy, a fuzzy string matching package written in python.

<br><br>

##Results
To test the hypothesis that ingredient pairs sharing many flavor compounds are preferred, I computed every possible 
pairwise ingredient combination possible from the recipe dataset. If shared compounds have no effect on occurrence in 
real-world recipes, we would expect to see that the fraction of pairs occurring in the wild is constant. 
The plot below shows the trend I observed. As the number of shared compounds increases, the fraction of pairs at 
observed at that level of shared flavor compounds increases. This observation is the basis for the ingredient pairings recommended by 
[MixedCompany](recommender "Title").
<br><br>
![coocc](images/plot_light.png =670x344)
<br><b]r>







