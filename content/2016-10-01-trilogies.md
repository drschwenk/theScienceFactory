Title: Predicting Film Trilogy Grosses
Date: 2015-10-01
Author: Dustin Schwenk
Slug: trilogies
Category: personal projects 	
Tags: Films
Summary: Exploring film trilogy grosses
D3:
Scripts: hover.js
Styles: hover.css

This is going to be a blog post about film grosses. 

{% notebook trilogy_exp.ipynb cells[3:12] %}

Now let's look at third film grosses vs. the average gross of the previous films in the trilogy.
We immediately notice that the majority of films fall below the 1:1 line, meaning that they made less than the previous entries 
in the series. Apparently it's difficult to sustain a franchise through three films. 

<div id="info">
    <div id="point-info">
        Hover over a movie to reveal it's title and box office gross
    </div>
</div>
<div class="plot">
</div>

{% notebook trilogy_analysis.ipynb cells[12:16] %}