---
Title: Predicting Film Trilogy Grosses
Date: 2015-10-01
Author: Dustin Schwenk
Slug: trilogies
Category: personal projects 	
Tags: Films
---
A popular story structure for epic tales is the three-part trilogy, a la Lord of the Rings or Star Wars. 
Sequels are big business for Hollywood, so naturally trilogies are getting made quite often. 
I wanted to know if I could dig into the data and successfully predict the box office gross for the third movie in a 
trilogy; given the box office returns of two films, how accurately can we predict the earnings of the third?
<!-- PELICAN_END_SUMMARY -->
D3:
Scripts: hover.js
Styles: hover.css

This is going to be a blog post about film grosses. 

{% notebook trilogy_exp.ipynb cells[3:12] %}

Now let's look at third film grosses vs. the average gross of the previous films in the trilogy.
We immediately notice that the majority of films fall below the s 1:1 line, meaning that they made less than the previous entries 
in the series. Apparently it's difficult to sustain a franchise through three films. 

<div id="info">
    <div id="point-info">
        Hover over a movie to reveal it's title and box office gross
    </div>
</div>
<div class="plot">
</div>

{% notebook trilogy_analysis.ipynb cells[12:16] %}
